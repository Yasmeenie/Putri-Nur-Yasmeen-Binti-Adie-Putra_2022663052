-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 06:15 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `special_class_ticket`
--

-- --------------------------------------------------------

--
-- Table structure for table `order_ticket`
--

CREATE TABLE `order_ticket` (
  `User_Name` text NOT NULL,
  `User_Phone_Number` int(10) NOT NULL,
  `User_Address` text NOT NULL,
  `User_Age` int(3) NOT NULL,
  `Special_Class_Type` varchar(30) NOT NULL,
  `Ticket` int(100) NOT NULL,
  `Total_Price` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `order_ticket`
--

INSERT INTO `order_ticket` (`User_Name`, `User_Phone_Number`, `User_Address`, `User_Age`, `Special_Class_Type`, `Ticket`, `Total_Price`) VALUES
('Lily Nisa Binti Latip', 19889120, 'No 320b, Jalan Bujang Saujana 3/6, Taman Lembah Bujang, Bedong, 08100, Kedah', 21, 'Special Class A', 1, 200),
('Adam Qusaiqeem Bin Aton Nim', 1723230055, '142/4 Jalan 11 Selayang Baru, 68100, Batu Caves, Selangor Darul Ehsan', 21, 'Special Class C', 2, 200),
('Lee Syu Ying', 147725634, 'No 23, Jalan Timah 8, Taman Sri Putri, 081300 Skudai, Johor', 7, 'Special Class A', 3, 600),
('Sofia Binti Kamarulzaman', 1345453322, 'No 26, Lorong 5, Taman Gurun Jaya, 08300 Gurun, Kedah', 0, 'Special Class C', 1, 100),
('Jackson Wang', 132656478, 'No 26, Lorong 5, Taman Gurun Jaya, 08300 Gurun, Kedah', 41, 'Special Class M', 1, 150);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
