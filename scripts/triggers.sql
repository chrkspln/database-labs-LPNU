USE lab4_auchan;

DROP TRIGGER IF EXISTS prevent_deletion;
DROP TRIGGER IF EXISTS validate_supplier_name;
DROP TRIGGER IF EXISTS prevent_product_update;
DROP TRIGGER IF EXISTS prevent_product_delete;

DELIMITER //

CREATE TRIGGER prevent_product_update
BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Updates are not allowed on the products table';
END //

CREATE TRIGGER prevent_product_delete
BEFORE DELETE ON products
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Deletions are not allowed on the products table';
END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER validate_supplier_name
BEFORE INSERT ON suppliers
FOR EACH ROW
BEGIN
    IF NEW.supplier_name NOT IN ('Svitlana', 'Petro', 'Olha', 'Taras') THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid supplier name. Only "Svitlana", "Petro", "Olha", "Taras" are allowed.';
    END IF;
END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER prevent_deletion
BEFORE DELETE ON deliveries
FOR EACH ROW
BEGIN
    IF OLD.urgency_type_id > 2 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot delete deliveries where urgency_type_id > 2';
    END IF;
END //

DELIMITER ;