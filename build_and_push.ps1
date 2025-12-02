# powershell
# Define variables
$IMAGE_NAME = "flask-app"
$TAG = "latest"
$ECR_URI = "810278669249.dkr.ecr.eu-north-1.amazonaws.com/lpnu-clouds-lab"

Write-Host "=== Checking Docker status... ==="

# Check if Docker is running
$dockerStatus = Get-Process -Name "Docker Desktop" -ErrorAction SilentlyContinue

if (-not $dockerStatus) {
    Write-Host "Docker Desktop is not running. Starting it..."
    Start-Process "C:\Program Files\Docker\Docker\Docker Desktop.exe"
    Write-Host "Waiting for Docker to start..."
    Start-Sleep -Seconds 15
} else {
    Write-Host "Docker is already running."
}

# Wait until Docker Engine actually responds
$maxAttempts = 10
for ($i = 1; $i -le $maxAttempts; $i++) {
    try {
        docker info > $null 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Docker Engine is up."
            break
        }
    } catch {
        Write-Host "Docker not ready yet... attempt $i/$maxAttempts"
        Start-Sleep -Seconds 5
    }
    if ($i -eq $maxAttempts) {
        Write-Host "Docker failed to start. Exiting."
        exit 1
    }
}

# Build the Docker image
Write-Host "=== Building image '${IMAGE_NAME}' ==="
docker build -t $IMAGE_NAME .

if ($LASTEXITCODE -ne 0) {
    Write-Host "Docker build failed. Exiting."
    exit 1
}

# Tag the image for ECR
Write-Host "=== Tagging image ==="
docker tag "${IMAGE_NAME}:${TAG}" "${ECR_URI}:${TAG}"

# Authenticate to ECR
Write-Host "=== Logging in to AWS ECR ==="
aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin $ECR_URI

if ($LASTEXITCODE -ne 0) {
    Write-Host "ECR login failed. Exiting."
    exit 1
}

# Push image to ECR
Write-Host "=== Pushing image to ECR ==="
docker push "${ECR_URI}:${TAG}"

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Successfully pushed ${ECR_URI}:${TAG}"
} else {
    Write-Host "❌ Push failed."
    exit 1
}
