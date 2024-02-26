-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: feb 25, 2024 at 21:49pm
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fitness classes`
--
CREATE DATABASE IF NOT EXISTS `fitnessclass` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `fitnessclass`;

-- --------------------------------------------------------

--
-- Table structure for table `fitnessclass`
--

DROP TABLE IF EXISTS `fitnessclass`;
CREATE TABLE IF NOT EXISTS `fitnessclass` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `name` varchar(64) NOT NULL,
  `description` text NOT NULL,
  `instructor` varchar(64) NOT NULL,
  `schedule` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `availability` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Dumping data for table `fitnessclass`
--

INSERT INTO `fitnessclass` (`id`, `name`, `description`, `instructor`, `schedule`, `price`, `availability`) VALUES
('1', 'Running', '5km run', 'John Doe', 'Mon, Wed, Fri 10:00 AM - 11:00 AM', '21.50', 2),
('2', 'weight training', 'a set of different weight exercises', 'Jane Smith', 'Tue, Thu 3:00 PM - 4:30 PM', '99.40', 25),
('3', 'Yoga Basics', 'Description for Yoga Basics', 'Yoga Instructor', 'Mon, Fri 5:30 PM - 6:30 PM', '15.00', 10),
('4', 'HIIT Training', 'Description for HIIT Training', 'Fitness Trainer', 'Mon, Wed 8:00 AM - 9:00 AM', '25.00', 15),
('5', 'Pilates for Beginners', 'Description for Pilates', 'Pilates Instructor', 'Tue, Thu 6:00 PM - 7:00 PM', '18.50', 12),
('6', 'Zumba Dance Fitness', 'Description for Zumba Dance', 'Zumba Instructor', 'Wed, Fri 7:30 PM - 8:30 PM', '12.00', 20);


COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
