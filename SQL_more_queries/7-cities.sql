-- Creating a database usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Using the database usa
USE hbtn_0d_usa;

-- Creating the table cities
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
)