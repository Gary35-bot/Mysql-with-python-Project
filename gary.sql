-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: Lifechoices_sign_in
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Clientle`
--

DROP TABLE IF EXISTS `Clientle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Clientle` (
  `Client_id` int unsigned NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) NOT NULL,
  `Surname` varchar(20) NOT NULL,
  `Phone_number` varchar(10) DEFAULT NULL,
  `Password` varchar(20) NOT NULL,
  `Start_in_date` date DEFAULT NULL,
  `Start_in_time` time DEFAULT NULL,
  `Leave_date` date DEFAULT NULL,
  `Leave_time` time DEFAULT NULL,
  PRIMARY KEY (`Client_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Clientle`
--

LOCK TABLES `Clientle` WRITE;
/*!40000 ALTER TABLE `Clientle` DISABLE KEYS */;
INSERT INTO `Clientle` VALUES (6,'Caron ','Africa','0798022267','boborbob',NULL,NULL,NULL,NULL),(7,'Nasar','Kamish','0659704572','hello','2021-07-10','22:37:55',NULL,NULL),(8,'John','New','0201107485','Goodday',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Clientle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `My_nextkin`
--

DROP TABLE IF EXISTS `My_nextkin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `My_nextkin` (
  `Client_id` int unsigned NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) NOT NULL,
  `Surname` varchar(20) NOT NULL,
  `Phone_number` varchar(10) NOT NULL,
  PRIMARY KEY (`Client_id`),
  CONSTRAINT `My_nextkin_ibfk_1` FOREIGN KEY (`Client_id`) REFERENCES `Register_me` (`Client_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `My_nextkin`
--

LOCK TABLES `My_nextkin` WRITE;
/*!40000 ALTER TABLE `My_nextkin` DISABLE KEYS */;
INSERT INTO `My_nextkin` VALUES (5,'dvbd','soffns','1010101010');
/*!40000 ALTER TABLE `My_nextkin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Register_me`
--

DROP TABLE IF EXISTS `Register_me`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Register_me` (
  `Client_id` int unsigned NOT NULL AUTO_INCREMENT,
  `Id_number` varchar(13) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Surname` varchar(20) NOT NULL,
  `Phone_number` varchar(10) DEFAULT NULL,
  `Password` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Client_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Register_me`
--

LOCK TABLES `Register_me` WRITE;
/*!40000 ALTER TABLE `Register_me` DISABLE KEYS */;
INSERT INTO `Register_me` VALUES (5,'1010101010','ekelkfh','jdsbvbdj','1010101010','dslflisdf');
/*!40000 ALTER TABLE `Register_me` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-12 17:09:41
