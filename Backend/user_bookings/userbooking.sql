-- Create the 'userbooking' database if it doesn't exist
CREATE DATABASE IF NOT EXISTS `userbooking` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `userbooking`;

-- Table structure for table `userbooking`
DROP TABLE IF EXISTS `userbooking`;
CREATE TABLE IF NOT EXISTS `userbooking` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `userid` VARCHAR(64) NOT NULL,
  `class_id` INT NOT NULL,
  `rate_status` VARCHAR(64) NOT NULL,
  `unique_id` VARCHAR(64) NOT NULL,
  `email` VARCHAR(64) NOT NULL,
  `payment_intent_id` VARCHAR(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
