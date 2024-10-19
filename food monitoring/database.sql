-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS food_monitoring;

-- Select the database to use
USE food_monitoring;

-- Create the food_items table
CREATE TABLE IF NOT EXISTS food_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    quantity INT,
    expiry_date DATE
);





