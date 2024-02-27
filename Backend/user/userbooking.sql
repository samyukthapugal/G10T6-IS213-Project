-- Create the 'userbooking' database if it doesn't exist
CREATE DATABASE IF NOT EXISTS `userbooking` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `userbooking`;

-- Table structure for table `users`
DROP TABLE IF EXISTS `userbooking`;
CREATE TABLE IF NOT EXISTS `userbooking` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `userid` varchar(64) NOT NULL,
  `description` text NOT NULL,
  `instructor` varchar(64) NOT NULL,
  `schedule` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


