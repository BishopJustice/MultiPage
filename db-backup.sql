-- MySQL dump 10.13  Distrib 5.7.14, for osx10.11 (x86_64)
--
-- Host: localhost    Database: multipage
-- ------------------------------------------------------
-- Server version	5.7.14

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `items` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) DEFAULT NULL,
  `description` varchar(500) NOT NULL,
  `label` varchar(50) DEFAULT NULL,
  `priority` varchar(50) DEFAULT NULL,
  `state` varchar(10) NOT NULL,
  `opened_at` varchar(200) NOT NULL,
  `resolved_at` varchar(200) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pid` (`pid`),
  KEY `uid` (`uid`),
  CONSTRAINT `items_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `projects` (`pid`),
  CONSTRAINT `items_ibfk_2` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES (1,3,'Add Multiple Projects inside a project',NULL,NULL,'Open','2016-08-30 14:00:16.743073',NULL,1),(2,3,'Add priority or starts to projects',NULL,NULL,'Deleted','2016-08-30 14:00:29.383128','2016-08-30 18:36:28.339661',1),(3,3,'Show starred projects on main page',NULL,NULL,'Open','2016-08-30 14:00:38.646153',NULL,1),(4,3,'Fix link display',NULL,NULL,'Resolved','2016-08-30 14:00:45.471237','2016-08-30 16:46:50.677865',1),(5,3,'Add colors',NULL,NULL,'Resolved','2016-08-30 14:00:48.601099','2016/08/31 11:25:59',1),(6,3,'Make items on top draggable',NULL,NULL,'Open','2016-08-30 14:00:53.913260',NULL,1),(7,1,'Review UX findings',NULL,NULL,'Resolved','2016-08-30 16:44:59.764447','2016/08/31 11:08:09',1),(8,3,'Fix Date Added Display',NULL,NULL,'Resolved','2016-08-30 16:47:04.708636','2016/08/30 16:50:15',1),(9,3,'Test Datetime Change',NULL,NULL,'Resolved','2016/08/30 16:50:07','2016/08/30 16:50:14',1),(10,3,'Test it out',NULL,NULL,'Resolved','2016/08/30 16:51:34','2016/08/30 16:51:43',1),(11,3,'1',NULL,NULL,'Deleted','2016/08/30 16:51:49','2016-08-30 16:52:07.163795',1),(12,1,'asd',NULL,NULL,'Deleted','2016/08/30 18:14:29','2016-08-31 11:12:01.829364',1),(13,3,'Check buttons',NULL,NULL,'Deleted','2016/08/30 18:16:10','2016-08-30 18:21:53.022813',1),(14,3,'Test it',NULL,NULL,'Deleted','2016/08/30 18:21:57','2016-08-30 18:22:09.173995',1),(15,3,'Test again',NULL,NULL,'Deleted','2016/08/30 18:22:12','2016-08-30 18:22:16.153904',1),(16,3,'Add starring ability',NULL,NULL,'Open','2016/08/30 18:36:32',NULL,1),(17,8,'Work on Ajax, get client talking to server',NULL,NULL,'Open','2016/08/30 18:56:05',NULL,1),(18,8,'Start using Json',NULL,NULL,'Open','2016/08/30 18:56:11',NULL,1),(19,2,'Follow up with David',NULL,NULL,'Resolved','2016/08/31 09:26:04','2016/08/31 09:26:06',1),(20,4,'Calrify shipping process with Brannan',NULL,NULL,'Open','2016/08/31 11:10:23',NULL,1),(21,1,'sddddddfsdfjsdfjsklfjlskdfjklsdjflksdjflksdfjslfjldsjflsdkfjsdlkfjdslkfjsdlfdsjflksdjflkdsjflsdfjsdlkfjdsklfjdsklfjdslkfjsldkfjsklfjdslfjsdklfjdslkfjsdlfjdslkfjsdlkfjdslkfjsdlfjdslkfjsdlfdsjflsdjkfldksjfdlksjfslkfj',NULL,NULL,'Deleted','2016/08/31 12:50:10','2016-08-31 12:50:32.677058',1),(22,1,'asjakjkjksjkdjlasjkdslajdlasjkdaklsjdaklsdjaskldjaslkdjaslkdjsalkdjaskldjasldjlasdjaslkdjasldjasldjaslkdjalskjdlksajkldjaskljweekajlkfjwef',NULL,NULL,'Deleted','2016/08/31 12:50:57','2016-08-31 13:12:35.887422',1),(23,1,'Hello',NULL,NULL,'Open','2016/08/31 13:12:32',NULL,1),(24,3,'adsjadshjkashdkjasyhdaskjdh ajkd hdkj ahdjkas hdjksa hdjkas hdjka shdkjas dhkjas dhjkas dhjkas dhajsk dhsakj dhasjkd hsakjd hakd hakd ahsjkd ashkd ajkd ahjdkas hdjkas djksa hjkas hk jk hjk hfskjf hz',NULL,NULL,'Deleted','2016/08/31 13:12:54','2016-08-31 13:16:02.436451',1),(25,2,'asd',NULL,NULL,'Open','2016/08/31 13:28:04',NULL,1);
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `links`
--

DROP TABLE IF EXISTS `links`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `links` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) DEFAULT NULL,
  `url` varchar(600) DEFAULT NULL,
  `link_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pid` (`pid`),
  CONSTRAINT `links_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `projects` (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `links`
--

LOCK TABLES `links` WRITE;
/*!40000 ALTER TABLE `links` DISABLE KEYS */;
INSERT INTO `links` VALUES (5,1,'https://docs.google.com/spreadsheets/d/1c83aVvuOEqizLDW96VWVfIz4axyBTpTxnnJexwJz2ck/edit?ts=5787fcb7#gid=1033026756','Master Workback'),(6,1,'https://docs.google.com/document/d/1jinemArPiKi5BBSK5tuuMTfrLUpcY910lIQX8GSZzks/edit#','Distro Requirements'),(7,1,'https://docs.google.com/spreadsheets/d/1mj5k7YIIDwQfF2T3RhBYyK-FcjnxNk5mNRlbl42Dhnw/edit#gid=0','UX Notes'),(8,1,'https://docs.google.com/document/d/11JO-L_5qdurj-PGE2DjMuHJAKySXDphfOtNA2c_mscI/edit#','Functionality'),(9,3,'https://www.pythonanywhere.com/user/BishopJustice/consoles/bash/3274473/','Bash Shell'),(10,3,'http://bishopjustice.pythonanywhere.com/','Website'),(11,3,'https://github.com/BishopJustice/MultiPage','Github'),(12,3,'https://www.pythonanywhere.com/user/BishopJustice/consoles/mysql/3368758/','MySql Console'),(13,3,'https://www.pythonanywhere.com/user/BishopJustice/files/var/log/bishopjustice.pythonanywhere.com.error.log','Error Log'),(14,8,'https://www.codecademy.com/courses/javascript-beginner-en-g7vdk/0/1','Jquery Ajax'),(15,8,'https://www.codecademy.com/tracks/projects','Coding Projects'),(16,1,'https://docs.google.com/a/lyft.com/document/d/11D9u-bVjycbNAeBLRrmo-BpnCTqbeEifCMAVKkiyDc8/edit?usp=sharing','Product Scope');
/*!40000 ALTER TABLE `links` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `migrate_version`
--

DROP TABLE IF EXISTS `migrate_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `migrate_version` (
  `repository_id` varchar(250) NOT NULL,
  `repository_path` text,
  `version` int(11) DEFAULT NULL,
  PRIMARY KEY (`repository_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `migrate_version`
--

LOCK TABLES `migrate_version` WRITE;
/*!40000 ALTER TABLE `migrate_version` DISABLE KEYS */;
INSERT INTO `migrate_version` VALUES ('database repository','/Users/lukegreenwood/Sites/MultiPage/db_repository',22);
/*!40000 ALTER TABLE `migrate_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projects` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`pid`),
  KEY `uid` (`uid`),
  CONSTRAINT `projects_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects`
--

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
INSERT INTO `projects` VALUES (1,1,'AMP'),(2,1,'STB'),(3,1,'MultiPage'),(4,1,'Project Oval'),(5,2,'Yay!'),(6,2,'Ho'),(7,2,'Hey!'),(8,1,'Learn Code');
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `email` varchar(120) DEFAULT NULL,
  `pwdhash` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Luke','Greenwood','luke@lyft.com','pbkdf2:sha1:1000$yhwKum3h$0cac73e443ffc33b4af22952a1f1432e63d9cc2c'),(2,'Bacon','George','bacon@lyft.com','pbkdf2:sha1:1000$JDU1IF5S$fd46eae154f98cfe70e031b0d498bd68482c34ac');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-08-31 14:07:53
