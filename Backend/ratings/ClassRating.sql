-- Drop the existing database if it exists
DROP DATABASE IF EXISTS `classRatings`;

-- Create the database with the correct character set and collation
CREATE DATABASE `classRatings` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- Use the created database
USE `classRatings`;

-- Create the table structure for classRatings
DROP TABLE IF EXISTS `classRatings`;
CREATE TABLE IF NOT EXISTS `classRatings` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `class_id` VARCHAR(64) NOT NULL,
  `rating` INT NOT NULL CHECK (rating >= 1 AND rating <= 5)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Insert sample data into classRatings table with specified IDs
INSERT INTO `classRatings` (`id`, `class_id`, `rating`) VALUES
(1, '1', 4),
(2, '2', 5),
(3, '3', 3),
(4, '4', 2),
(5, '5', 5),
(6, '6', 4);
