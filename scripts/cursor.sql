DELIMITER //

CREATE PROCEDURE create_dynamic_tables()
BEGIN
    DECLARE finished INT DEFAULT 0;
    DECLARE store_id INT;
    DECLARE rating INT;
    DECLARE cur CURSOR FOR SELECT store_id, rating FROM store_feedbacks;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;

    SET @table1 = CONCAT('store_feedback_', UNIX_TIMESTAMP(), '_1');
    SET @table2 = CONCAT('store_feedback_', UNIX_TIMESTAMP(), '_2');

    SET @create_table_sql = CONCAT(
        'CREATE TABLE ', @table1, ' LIKE store_feedbacks;'
    );
    PREPARE stmt FROM @create_table_sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    SET @create_table_sql = CONCAT(
        'CREATE TABLE ', @table2, ' LIKE store_feedbacks;'
    );
    PREPARE stmt FROM @create_table_sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO store_id, rating;
        IF finished THEN
            LEAVE read_loop;
        END IF;

        IF RAND() < 0.5 THEN
            SET @insert_sql = CONCAT(
                'INSERT INTO ', @table1, ' (store_id, rating) ',
                'SELECT store_id, rating FROM store_feedbacks WHERE store_id = ', store_id, ';'
            );
        ELSE
            SET @insert_sql = CONCAT(
                'INSERT INTO ', @table2, ' (store_id, rating) ',
                'SELECT store_id, rating FROM store_feedbacks WHERE store_id = ', store_id, ';'
            );
        END IF;

        PREPARE stmt FROM @insert_sql;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END LOOP;

    CLOSE cur;
END //

DELIMITER ;