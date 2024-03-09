-- Create the 'userbooking' database if it doesn't exist

-- if want to edit the columns of the database, do rmb to change the columns here too and re import
CREATE DATABASE IF NOT EXISTS `userbooking` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `userbooking`;

-- Table structure for table `userbooking`
DROP TABLE IF EXISTS `userbooking`;
CREATE TABLE IF NOT EXISTS `userbooking` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `userid` varchar(64) NOT NULL,
  `class_id` INT NOT NULL,
  `description` text NOT NULL,
  `instructor` varchar(64) NOT NULL,
  `schedule` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
