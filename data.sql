INSERT INTO product_categories (category_name) VALUES
('Beverages'),
('Dairy'),
('Bakery'),
('Frozen Foods'),
('Meat'),
('Fruits');

INSERT INTO products (product_name, category_id) VALUES
('Coca-Cola', 1),
('Pepsi', 1),
('Milk', 2),
('Cheese', 2),
('Donuts', 3),
('Bread', 3),
('Pizza', 4),
('Varenyky', 4),
('Chicken', 5),
('Pork', 5),
('Apples', 6),
('Bananas', 6);

INSERT INTO stores (store_name, store_address) VALUES
('Auchan Central', '123 Main St'),
('Auchan North', '135 North St'),
('Auchan Mall', '101 Mall Ave'),
('Auchan City Center', '909 City Center Blvd');

INSERT INTO urgency_types (urgency_description) VALUES
('Same Day'),
('Next Day'),
('Standard Delivery (3-5 Days)'),
('Express');

INSERT INTO delivery_costs (urgency_type_id, delivery_cost) VALUES
(1, 200),
(2, 170),
(3, 100),
(4, 140);

INSERT INTO prices (product_id, store_id, price) VALUES
(1, 1, 25.99),  -- Coca-Cola, Auchan Central
(2, 2, 24.50),  -- Pepsi, Auchan North
(3, 3, 35.00),  -- Milk, Auchan Mall
(4, 4, 42.00),  -- Cheese, Auchan City Center
(5, 1, 12.99),  -- Donuts, Auchan Central
(6, 2, 9.99),   -- Bread, Auchan North
(7, 3, 17.99),  -- Pizza, Auchan Mall
(8, 4, 18.50),  -- Varenyky, Auchan City Center
(9, 1, 23.50),  -- Chicken, Auchan Central
(10, 2, 22.00), -- Pork, Auchan North
(11, 3, 14.00), -- Apples, Auchan Mall
(12, 4, 16.00); -- Bananas, Auchan City Center

INSERT INTO product_details (product_id, description, category_id) VALUES
(1, 'Refreshing carbonated beverage', 1),     -- Coca-Cola, Beverages
(2, 'Popular carbonated soda drink', 1),      -- Pepsi, Beverages
(3, 'Fresh milk, sourced locally', 2),        -- Milk, Dairy
(4, 'Aged cheese, mild flavor', 2),           -- Cheese, Dairy
(5, 'Sweet and fluffy fried dough', 3),       -- Donuts, Bakery
(6, 'Soft and fresh bread', 3),               -- Bread, Bakery
(7, 'Classic Italian pizza, various toppings', 4),  -- Pizza, Frozen Foods
(8, 'Traditional Ukrainian dumplings', 4),    -- Varenyky, Frozen Foods
(9, 'Fresh, tender chicken cuts', 5),         -- Chicken, Meat
(10, 'Juicy pork cuts for grilling', 5),      -- Pork, Meat
(11, 'Fresh, crisp apples', 6),               -- Apples, Fruits
(12, 'Sweet, ripe bananas', 6);               -- Bananas, Fruits

INSERT INTO product_expiration (product_id, expiration_date) VALUES
(1, '2025-05-01'),  -- Coca-Cola
(2, '2025-04-15'),  -- Pepsi
(3, '2025-02-20'),  -- Milk
(4, '2025-03-01'),  -- Cheese
(5, '2024-12-25'),  -- Donuts
(6, '2024-12-30'),  -- Bread
(7, '2025-01-15'),  -- Pizza
(8, '2025-02-01'),  -- Varenyky
(9, '2025-06-01'),  -- Chicken
(10, '2025-05-01'), -- Pork
(11, '2025-01-10'), -- Apples
(12, '2025-01-20'); -- Bananas

INSERT INTO suppliers (supplier_name) VALUES
('Supplier A'),
('Supplier B'),
('Supplier C');

INSERT INTO store_supplies (product_id, store_id, supplier_id) VALUES
(1, 1, 1),  -- Coca-Cola, Auchan Central, Supplier A
(2, 2, 2),  -- Pepsi, Auchan North, Supplier B
(3, 3, 3),  -- Milk, Auchan Mall, Supplier C
(4, 4, 1),  -- Cheese, Auchan City Center, Supplier A
(5, 1, 2),  -- Donuts, Auchan Central, Supplier B
(6, 2, 3),  -- Bread, Auchan North, Supplier C
(7, 3, 1),  -- Pizza, Auchan Mall, Supplier A
(8, 4, 2),  -- Varenyky, Auchan City Center, Supplier B
(9, 1, 3),  -- Chicken, Auchan Central, Supplier C
(10, 2, 1), -- Pork, Auchan North, Supplier A
(11, 3, 2), -- Apples, Auchan Mall, Supplier B
(12, 4, 3); -- Bananas, Auchan City Center, Supplier C

INSERT INTO deliveries (delivery_id, store_id, urgency_type_id, delivery_date, quantity) VALUES
(1, 1, 4, '2024-11-27', 50),   -- Coca-Cola, Auchan Central, Same Day
(2, 2, 2, '2024-11-28', 40),   -- Pepsi, Auchan North, Next Day
(3, 3, 3, '2024-11-29', 30),   -- Milk, Auchan Mall, Standard Delivery
(4, 4, 4, '2024-11-30', 20),   -- Cheese, Auchan City Center, Express
(5, 1, 3, '2024-12-01', 100),  -- Donuts, Auchan Central, Standard Delivery
(6, 2, 1, '2024-12-02', 80),   -- Bread, Auchan North, Same Day
(7, 3, 2, '2024-12-03', 60),   -- Pizza, Auchan Mall, Next Day
(8, 4, 4, '2024-12-04', 70),   -- Varenyky, Auchan City Center, Express
(9, 1, 3, '2024-12-05', 50),   -- Chicken, Auchan Central, Standard Delivery
( 10, 2, 1, '2024-12-06', 40),  -- Pork, Auchan North, Same Day
( 11, 3, 2, '2024-12-07', 90),  -- Apples, Auchan Mall, Next Day
( 12, 4, 4, '2024-12-08', 100), -- Bananas, Auchan City Center, Express
(13, 1, 3, '2024-12-09', 50),  -- Coca-Cola, Auchan Central, Standard Delivery
( 14, 2, 1, '2024-12-10', 40),  -- Pepsi, Auchan North, Same Day
( 15, 3, 2, '2024-12-11', 30);  -- Milk, Auchan Mall, Next Day
