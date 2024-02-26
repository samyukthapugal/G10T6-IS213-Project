-- Create the 'userdatabase' database if it doesn't exist
CREATE DATABASE IF NOT EXISTS `userdatabase` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `userdatabase`;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `username` varchar(64) NOT NULL,
  `selected_fitness_classes` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table `users`
-- INSERT INTO `users` (`id`, `username`, `selected_fitness_classes`) VALUES
-- ('1', 'User_1', ''),
-- ('2', 'User_2', '');

-- COMMIT;
