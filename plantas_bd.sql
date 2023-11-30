-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: plantas_bd
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `características`
--

DROP TABLE IF EXISTS `características`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `características` (
  `id_características` int NOT NULL,
  `iluminacion` varchar(45) NOT NULL,
  `riego` varchar(45) NOT NULL,
  `ubicación` char(20) NOT NULL,
  `suelo` varchar(45) NOT NULL,
  `plaga` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_características`,`iluminacion`),
  KEY `fk_características_plantas_idx` (`id_características`),
  CONSTRAINT `fk_características_plantas` FOREIGN KEY (`id_características`) REFERENCES `plantas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `características`
--

LOCK TABLES `características` WRITE;
/*!40000 ALTER TABLE `características` DISABLE KEYS */;
INSERT INTO `características` VALUES (1,'sin luz directa','mucha','suelo/roca/troncos','superficies porosas','-'),(2,'luz indirecta','en verano todos los días','interior y exterior','ambas','cochinillas'),(3,'mucha','media','exterior','tierra húmeda','la enfermedad nematodo'),(4,'mucha','poco riego','exterior','Tierra','Resiste las plagas'),(5,'mucha','frecuentes, poco abundantes','exterior','tierra húmeda','-'),(6,'mucha','mantenerlo húmedo sin encharcar','exterior','maceta o suelo con tierra húmeda','chancro del cipres (hongo)'),(7,'media','poco riego','exterior','suelo húmedo y profundo','longicornios'),(8,'mucha luz solar','media','exterior','maceta y tierra','Pulgón'),(9,'luz solar indirecta','abundante, sin encharcar','interior','maceta','cochinillas y pulgón'),(10,'media','riego abundante','exterior','suelo arcilloso bien drenado','insectos, roedores, aves'),(11,'mucha luz solar','frecuente, poco abundante','interior y exterior','maceta y tierra','Pulgón, caracoles y babosas'),(12,'alta','poco riego','interior y exterior','maceta con drenaje','Hongos'),(13,'mucha luz solar','riego frecuente en verano','exterior','maceta y tierra','Hongos'),(14,'media','abundante, sin encharcar','exterior','suelos húmedos','Moho y hongos'),(15,'alta','riego medio a la sombra','exterior','suelo arcilloso bien drenado','araña roja, chinches'),(16,'mucha luz, indirecta','poco riego','interior','maceta con drenaje','Cochinillas, hongos, ácaro'),(17,'mucha luz solar','riego moderado','interior','Maceta grande','Cochinillas y arañas rojas'),(18,'mucha luz solar indirecta','riego moderado','interior','macetas de suelo o colgantes','Pulgón verde'),(19,'mucha luz','poco riego, sin mojar ramas','Exterior','suelo o maceta c/ buen drenaje','Cochinillas, larvas'),(20,'mucha luz solar','poco riego','exterior','Maceta','Pulgón y cochinillas'),(21,'mucha luz','riego abundante','exterior','suelos húmedos c/ buen drenaje','Hongos'),(22,'poca luz, indirecta','riego abundante','interior','maceta','Araña roja y cochinilla'),(23,'mucha luz, indirecta','moderado, sin encharcar','Exterior','suelo o maceta c/ buen drenaje','Pulgón y hongos'),(24,'luz solar indirecta','riego moderado, sin encharcar','interior','Maceta - sustrato húmedo','mosca blanca, cochinillas'),(25,'mucha luz','riego abundante, sin encharcar','exterior','suelos húmedos c/ buen drenaje','Pulgón, mosca blanca'),(26,'luz moderada, indirecta','poco riego','interior','maceta','Hongos'),(27,'luz abundante, indirecta','poco riego','interior','maceta','Cochinillas'),(28,'luz abundante, indirecta','riego moderado','interior y exterior','maceta o suelo c/ sustrato húmedo','Araña roja, mosca blanca'),(29,'mucha luz directa','riego moderado','exterior','suelo arenoso y húmedo','Araña roja, mosca blanca'),(30,'luz moderada, indirecta','riego moderado','interior','maceta','Araña roja, pulgón, hongos'),(31,'luz moderada, indirecta','riego moderado','interior','maceta','Pulgón, ácaros, trips'),(32,'luz abundante, indirecta','riego moderado, sin encharcar','interior y exterior','maceta','Hongos'),(33,'luz directa abundante','riego abundante','exterior','suelo c/ buen drenaje','Cochinilla, ácaro, pulgón'),(34,'luz directa abundante','riego escaso','exterior','suelos poco húmedos','Prays, mosca, cochinilla'),(35,'luz solar directa','riego moderado','exterior','maceta o suelo','Pulgón, cochinilla'),(36,'luz abundante, indirecta','riego frecuente','exterior','maceta o suelo húmedo','Pulgón, trip, ácaros'),(37,'luz moderada, indirecta','riego moderado','interior','maceta','Cochinilla'),(38,'luz abundante, directa','poco riego','exterior','maceta o tierra','Thrips, pulgón, minador'),(39,'luz moderada, indirecta','riego moderado','exterior','suelo c/ buen drenaje','Cochinillas'),(40,'luz abundante, indirecta','riego moderado','interior','maceta o suelo húmedo','Ácaros y cochinillas'),(41,'luz moderada, indirecta','riego moderado','interior','maceta','Araña roja, pulgón, cochinilla');
/*!40000 ALTER TABLE `características` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plantas`
--

DROP TABLE IF EXISTS `plantas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plantas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre_comun` varchar(45) NOT NULL,
  `nombre_científico` varchar(30) NOT NULL,
  `foto` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plantas`
--

LOCK TABLES `plantas` WRITE;
/*!40000 ALTER TABLE `plantas` DISABLE KEYS */;
INSERT INTO `plantas` VALUES (1,'musgo común','Bryum',NULL),(2,'Helecho','Filicopsida',NULL),(3,'pino','pinus',NULL),(4,'Ginkgo','Ginkgo Biloba',NULL),(5,'Abeto','Abies',NULL),(6,'Cipres','Cupressus',NULL),(7,'Secuoya','Sequoioideae',NULL),(8,'Trigo','Triticum',NULL),(9,'Orquídea','Orchidaceae',NULL),(10,'Arroz','Oryza Sativa',NULL),(11,'Lirio','Lilium',NULL),(12,'Suculenta','Echeveria',NULL),(13,'Rosa','Roseae',NULL),(14,'Roble','Quercus',NULL),(15,'Manzano','Malus',NULL),(16,'Potus','Epipremnun aureum',NULL),(17,'Gomero','Ficus elástica',NULL),(18,'Tradescantia','Tradescantia',NULL),(19,'Lavanda','Lavandula',NULL),(20,'Geranio','Geranium',NULL),(21,'Ciruelo','Prunnus domestica',NULL),(22,'Alocasia','Alocasia G. Don',NULL),(23,'Crisantemo','Chrysanthemum',NULL),(24,'Fitonia','Fittonia',NULL),(25,'Jazmin','Jazminum',NULL),(26,'Calathea','Calathea',NULL),(27,'Rubra','Cordyline rubra',NULL),(28,'Cóleos','Solenostemon',NULL),(29,'Tomate','Solanum lycopersicum',NULL),(30,'Palo de agua','Dracaena fragrans',NULL),(31,'Violeta de los Alpes','Ciclamen',NULL),(32,'Begonia','Begonia',NULL),(33,'Limonero','Citrus limón',NULL),(34,'Olivo','Olea europaea',NULL),(35,'Romero','Salvia rosmarinus',NULL),(36,'Menta','Mentha',NULL),(37,'Clivia','Clivia',NULL),(38,'Gazania','Gazania',NULL),(39,'Santa Rita','Boungainvillea',NULL),(40,'Punta de flecha','Singonio',NULL),(41,'Monstera','Monstera',NULL);
/*!40000 ALTER TABLE `plantas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-27 20:18:01