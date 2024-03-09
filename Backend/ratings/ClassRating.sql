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
CREATE DATABASE IF NOT EXISTS `classRatings` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `classRatings`;

-- --------------------------------------------------------

--
-- Table structure for table `classRatings`
--

DROP TABLE IF EXISTS `classRatings`;
CREATE TABLE IF NOT EXISTS `classRatings` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `class_id` varchar(64) NOT NULL,
  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

