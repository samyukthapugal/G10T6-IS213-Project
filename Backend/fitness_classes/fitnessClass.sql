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
('1', 'High-Intensity Interval Training (HIIT)', 'Unleash your full potential with our HIIT class! Experience a heart-pounding, high-energy workout that combines intense bursts of exercise with short recovery periods. Torch calories, boost metabolism, and sculpt your body in this dynamic and efficient session. Get ready for a challenging and rewarding fitness experience that will leave you energized and empowered', 'John Doe', 'Mon 10:00 AM - 11:00 AM', '30', 70),
('2', 'Yoga', "Embark on a journey of self-discovery and wellness in our Yoga class. Immerse yourself in a harmonious blend of physical postures, breath work, and mindfulness. Whether you're a beginner or a seasoned yogi, our classes offer a serene environment to enhance flexibility, reduce stress, and promote overall well-being. Join us for a transformative experience that nurtures both body and mind", 'Jane Smith', 'Tue 3:00 PM - 4:30 PM', '50', 25),
('3', 'Spinning/Cycling', "Pedal your way to fitness with our exhilarating Cycling class! Jump on a stationary bike and embark on a journey of cardiovascular exhilaration set to invigorating music. With varying intensities and motivating instructors, our spinning classes promise a fun and challenging ride. Boost your endurance, burn calories, and enjoy the camaraderie of a high-energy cycling community", 'James Bond', 'Fri 5:30 PM - 6:30 PM', '25', 30),
('4', 'Strength Training', "Elevate your strength and reshape your physique in our Strength Training class. Guided by expert trainers, you'll engage in a mix of resistance exercises using weights and bodyweight. Whether you're a fitness novice or a seasoned lifter, our classes are designed to build muscle, enhance endurance, and sculpt your body. Unleash your inner strength in a supportive and motivating environment", 'ALAN', 'Wed 8:00 AM - 9:00 AM', '40', 20),
('5', 'Dance Fitness', "Dance your way to fitness with our vibrant Dance Fitness class! Experience the joy of movement as you follow dynamic and fun dance routines set to energetic music. This full-body workout is perfect for all fitness levels and is a fantastic way to improve coordination, burn calories, and boost your mood. Join our lively community and let the rhythm inspire your fitness journey.", 'Alan Walker', 'Thu 6:00 PM - 7:00 PM', '35', 30),
('6', 'Pilates', "Transform your body and mind with our Pilates class. Focus on building core strength, improving flexibility, and enhancing overall body awareness in a low-impact environment. Led by skilled instructors, our classes offer a balance of controlled movements and mindful exercises. Experience the benefits of Pilates as you tone and sculpt your body, promoting strength and agility for a healthier you", 'Amelia', 'Fri 7:30 PM - 8:30 PM', '25', 50);


COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
