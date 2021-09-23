-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: ozon
-- ------------------------------------------------------
-- Server version	8.0.25

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
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(55) NOT NULL,
  `sub_category` decimal(10,1) unsigned DEFAULT NULL,
  `sub_category_name` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq` (`id`,`name`) /*!80000 INVISIBLE */,
  UNIQUE KEY `uniq2` (`name`,`sub_category`) /*!80000 INVISIBLE */,
  UNIQUE KEY `uniq4` (`sub_category_name`,`sub_category`),
  UNIQUE KEY `uniq6` (`name`,`sub_category_name`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Электроника',1.0,'Нотбуки'),(2,'Электроника',2.0,'Мониторы'),(4,'Обувь',1.0,'Кроссовки'),(7,'Электроника',3.0,'Видеокарты'),(8,'Одежда',1.0,'Детская одежда'),(9,'Электроника',4.0,'ОЗУ'),(10,'Еда',1.0,'Шоколадки'),(12,'Электроника',5.0,'Мышки'),(15,'Товары для животных',1.0,'Корм для кошек'),(16,'Бытовая техника',1.0,'Холодильники'),(17,'Бытовая техника',2.0,'Телевизоры'),(18,'Автотовары',1.0,'Шины и диски'),(19,'Одежда',1.1,'Одежда для новорожденных'),(20,'Одежда',1.2,'Пеленки текстильные'),(21,'Дом и сад',1.0,'Шторы и карнизы'),(29,'Дом и сад',1.1,'Посуда');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category_links`
--

DROP TABLE IF EXISTS `category_links`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category_links` (
  `id_path` int unsigned NOT NULL AUTO_INCREMENT,
  `category_id` int unsigned NOT NULL,
  `path` varchar(150) NOT NULL,
  PRIMARY KEY (`id_path`),
  UNIQUE KEY `path_UNIQUE` (`path`),
  KEY `fk_categories_idx` (`category_id`),
  CONSTRAINT `fk_categories` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category_links`
--

LOCK TABLES `category_links` WRITE;
/*!40000 ALTER TABLE `category_links` DISABLE KEYS */;
INSERT INTO `category_links` VALUES (1,1,'/electronics/notebooks'),(2,2,'/electronics/monitors'),(3,10,'/food/chocolates'),(4,4,'/shoes/snickers'),(5,7,'/electronics/videocards'),(6,29,'/dom-i-sad/dishes'),(7,18,'/auto/shiny-i-diski'),(8,12,'/electronics/mouses'),(9,16,'/bytovaya-tehnika/holodilniki'),(10,17,'/bytovaya-tehnika/tv'),(11,21,'/dom-i-sad/shtory-i-zhalyuzi'),(12,8,'/odezhda/detskaya-odezhda'),(13,19,'/odezhda/odezhda-dlya-novorozhdennyh'),(14,20,'/odezhda/pelenki-tekstilnye'),(15,9,'/electronics/operativnaya-pamyat');
/*!40000 ALTER TABLE `category_links` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_in_cart`
--

DROP TABLE IF EXISTS `goods_in_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `goods_in_cart` (
  `id` int NOT NULL AUTO_INCREMENT,
  `products_id` int unsigned NOT NULL,
  `users_id` int unsigned NOT NULL,
  `quantity` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_goods_in_cart_products1_idx` (`products_id`),
  KEY `fk_goods_in_cart_users1_idx` (`users_id`),
  CONSTRAINT `fk_goods_in_cart_products1` FOREIGN KEY (`products_id`) REFERENCES `products` (`id_product`),
  CONSTRAINT `fk_goods_in_cart_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_in_cart`
--

LOCK TABLES `goods_in_cart` WRITE;
/*!40000 ALTER TABLE `goods_in_cart` DISABLE KEYS */;
INSERT INTO `goods_in_cart` VALUES (1,2,159,3),(2,4,189,1);
/*!40000 ALTER TABLE `goods_in_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_likes`
--

DROP TABLE IF EXISTS `goods_likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `goods_likes` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `products_id` int unsigned NOT NULL,
  `users_id` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `in_unique2` (`id`,`users_id`),
  UNIQUE KEY `in_inuque` (`products_id`,`users_id`),
  KEY `fk_goods_likes_products1_idx` (`products_id`),
  KEY `fk_goods_likes_users1_idx` (`users_id`),
  CONSTRAINT `fk_goods_likes_products1` FOREIGN KEY (`products_id`) REFERENCES `products` (`id_product`),
  CONSTRAINT `fk_goods_likes_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_likes`
--

LOCK TABLES `goods_likes` WRITE;
/*!40000 ALTER TABLE `goods_likes` DISABLE KEYS */;
INSERT INTO `goods_likes` VALUES (4,3,136),(2,3,177),(1,4,136),(3,4,177);
/*!40000 ALTER TABLE `goods_likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `goodsrateusers`
--

DROP TABLE IF EXISTS `goodsrateusers`;
/*!50001 DROP VIEW IF EXISTS `goodsrateusers`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `goodsrateusers` AS SELECT 
 1 AS `Name_of_Product`,
 1 AS `description`,
 1 AS `rate`,
 1 AS `feedback`,
 1 AS `lastname`,
 1 AS `email`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int unsigned NOT NULL,
  `status_delivery` int unsigned NOT NULL,
  `product_id` int unsigned NOT NULL,
  `quantity` int NOT NULL,
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `comments` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `status_delivery_UNIQUE` (`status_delivery`),
  KEY `users_key_idx` (`user_id`),
  KEY `order_fk_idx` (`status_delivery`),
  KEY `fk_product_orders_idx` (`product_id`),
  CONSTRAINT `order_fk` FOREIGN KEY (`status_delivery`) REFERENCES `status delivery` (`id`),
  CONSTRAINT `prod` FOREIGN KEY (`product_id`) REFERENCES `products` (`id_product`),
  CONSTRAINT `users_key` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (5,108,1,1,12,'2021-08-29 18:01:56','2021-08-29 18:13:13',NULL),(6,97,2,4,23,'2021-08-29 18:02:14','2021-08-29 18:26:55',NULL),(7,115,3,3,10,'2021-08-29 18:17:07','2021-08-29 18:26:55',NULL),(8,126,4,2,20,'2021-08-29 18:21:21','2021-08-29 18:26:55',NULL),(9,166,5,1,100,'2021-08-29 18:22:14','2021-08-29 18:26:55',NULL),(24,116,6,8,500,'2021-08-30 13:20:08','2021-08-30 13:20:08',NULL);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `orders_AFTER_INSERT` AFTER INSERT ON `orders` FOR EACH ROW BEGIN
 update `storage`
    set quantity = quantity - new.quantity 
    where product = new.product_id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `pics_goods`
--

DROP TABLE IF EXISTS `pics_goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pics_goods` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `path` varchar(200) NOT NULL,
  `products_id` int unsigned NOT NULL,
  `pic_name` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `path_UNIQUE` (`path`),
  KEY `fk_pics_products1_idx` (`products_id`),
  CONSTRAINT `fk_pics_products1` FOREIGN KEY (`products_id`) REFERENCES `products` (`id_product`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pics_goods`
--

LOCK TABLES `pics_goods` WRITE;
/*!40000 ALTER TABLE `pics_goods` DISABLE KEYS */;
INSERT INTO `pics_goods` VALUES (4,'oprativka243223423',8,'operativka-na-komp'),(5,'modul-operativnoy-pamyati-hyperx-fury-hx426',7,'fury-hx426');
/*!40000 ALTER TABLE `pics_goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id_product` int unsigned NOT NULL AUTO_INCREMENT,
  `category_path_id` int unsigned NOT NULL,
  `product_path` varchar(265) CHARACTER SET ascii COLLATE ascii_general_ci NOT NULL,
  `name` varchar(100) NOT NULL,
  `weight` decimal(10,1) DEFAULT NULL,
  `price` int unsigned NOT NULL,
  `color` varchar(45) DEFAULT NULL,
  `description` varchar(600) DEFAULT NULL,
  PRIMARY KEY (`id_product`),
  UNIQUE KEY `product_path_UNIQUE` (`product_path`),
  UNIQUE KEY `name_UNIQUE` (`name`),
  KEY `fk_products_category_links1_idx` (`category_path_id`),
  CONSTRAINT `chain` FOREIGN KEY (`category_path_id`) REFERENCES `category_links` (`id_path`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,1,'15-6-igrovoy-noutbuk-asus-90nb0p51-m25720-amd-ryzen-5-pro-3500u-2-1-ggts-ram-12-gb-ssd-512-gb-amd-245389655/','Игровой ноутбук ASUS 90NB0P51-M25720, AMD Ryzen 5 3500U (2.1 ГГц)',1.9,23914,'Серебристый','Ноутбук на базе четырехядерного процессора AMD Ryzen 5 3500U с частотой 2.1 ГГц, с оперативной памятью DDR4 объемом 12288 Мб, SSD 512 Гб для супербыстрой работы операционной системы будет Вашим надежным помощником в бизнесе и дома. Матовый дисплей ноутбука 15.6\" по технологии IPS с разрешением Full HD 1920x1080 прекрасно передает изображение благодаря видеокарте от AMD на базе графического чипсета Radeon Vega 8.'),(2,4,'krossovki-adidas-coreracer-212828821/','Кроссовки adidas Coreracer',0.3,2999,'Черный',NULL),(3,2,'23-8-monitor-acer-sa240yabi-chernyy-155320594/','23.8\" Монитор Acer SA240YABI, черный',2.8,9921,'Черный','Монитор ACER SA240YAbi идеален для создания рабочего стационарного компьютера. Ведь он обеспечит вам хорошие характеристики качества картинки на широком экране в 23.8 дюймов. Классическое соотношение сторон 16:9, умеренные яркость (250 кд/м2) и контрастность (1000:1) в сочетании с малым временем отклика в 4 м/с делают Acer удачным решением для плодотворной повседневной работы. '),(4,1,'15-6-igrovoy-noutbuk-asus-90nb0p51-m25720-amd-ryzen-5-pro-3500u-2-1-ggts-ram-12-gb-ssd-512-gb-amd/','Игровой ноутбук ASUS 90NB0P51-M25720, AMD Ryzen 7 3500U (2.1 ГГц)',1.9,48600,'Серебристый','Ноутбук на базе четырехядерного процессора AMD Ryzen 5 3500U с частотой 2.1 ГГц, с оперативной памятью DDR4 объемом 12288 Мб, SSD 512 Гб для супербыстрой работы операционной системы будет Вашим надежным помощником в бизнесе и дома. Матовый дисплей ноутбука 15.6\" по технологии IPS с разрешением Full HD 1920x1080 прекрасно передает изображение благодаря видеокарте от AMD на базе графического чипсета Radeon Vega 8'),(5,5,'product/videokarta-asus-rog-strix-radeon-rx-570-oc-8gb-rog-strix-rx570-o8g-gaming-166323310/','Видеокарта ASUS Radeon RX 570 8 ГБ (ROG-STRIX-RX570-O8G-GAMING)',0.5,51352,'','ROG Strix Radeon RX570 OC edition, 8 ГБ GDDR5'),(6,3,'product/pobeda-vkusa-shokolad-gorkiy-72-kakao-bez-sahara-100-g-171473627/','Победа вкуса \"Шоколад горький\" 72 ',0.1,171,NULL,'Эксклюзивная серия некалорийного шоколада без сахара с \"медовой травой\" стевией прос'),(7,15,'modul-operativnoy-pamyati-hyperx-fury-hx426c16fb3k2-16-16gb-162563073/','Оперативная память HyperX HX432C16FB4K4',NULL,7824,'Черный','HyperX® FURY DDR4 поможет повысить производительность во время игр, редактирования видео и визуализации, обеспечивая частоту до 3733 МГц. '),(8,15,'operativnaya-pamyat-fujitsu-1x128-gb-ddr4-s26361-f3844-l517-302023636/','Оперативная память Fujitsu 1x128 ГБ DDR4 (S26361-F3844-L517)',NULL,204531,NULL,'Суммарный объем памяти 1920 ГБ');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `products_and_paths`
--

DROP TABLE IF EXISTS `products_and_paths`;
/*!50001 DROP VIEW IF EXISTS `products_and_paths`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `products_and_paths` AS SELECT 
 1 AS `id_product`,
 1 AS `ProdNames`,
 1 AS `Path_link`,
 1 AS `ProdPath`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `products_rating`
--

DROP TABLE IF EXISTS `products_rating`;
/*!50001 DROP VIEW IF EXISTS `products_rating`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `products_rating` AS SELECT 
 1 AS `Name_of_Product`,
 1 AS `description`,
 1 AS `rate`,
 1 AS `feedback`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `rating_goods`
--

DROP TABLE IF EXISTS `rating_goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rating_goods` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `products_id` int unsigned NOT NULL,
  `users_id` int unsigned NOT NULL,
  `rating_goods` smallint NOT NULL DEFAULT '0' COMMENT ' 5 - отлично, 4 - хорошо, 3 - нормальный, 2 - плохой, 1 - ужасный товар',
  `feedback` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `in_unique` (`products_id`,`users_id`) /*!80000 INVISIBLE */,
  UNIQUE KEY `in_unique2` (`id`,`products_id`),
  KEY `fk_rating_goods_products1_idx` (`products_id`),
  KEY `fk_rating_goods_users1_idx` (`users_id`),
  CONSTRAINT `fk_rating_goods_products1` FOREIGN KEY (`products_id`) REFERENCES `products` (`id_product`),
  CONSTRAINT `fk_rating_goods_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rating_goods`
--

LOCK TABLES `rating_goods` WRITE;
/*!40000 ALTER TABLE `rating_goods` DISABLE KEYS */;
INSERT INTO `rating_goods` VALUES (1,1,105,5,'Цена. Всё заявленные характеристики в нем. Видяха справляется с большенством популярных игр на средних и высоких настройках. Экран матовый. Звук отличный.  '),(2,3,104,5,'ips, маленькие рамки, настройка для игрового режима, считаю лучшим монитором за такие деньги '),(3,3,115,1,'Засветы на весь экран  '),(4,2,136,1,'Прошёл в этих кроссовках 15 километров пешком. Получил травму стопы из-за искажения подошвы. На ней образовался \"волдырь\" в результате нога уже три месяца болит.  '),(7,3,105,4,'Экран матовый. Звук отличный.  '),(8,6,181,5,'Вкусный шоколад и главное без сахара. Очень нравится. ');
/*!40000 ALTER TABLE `rating_goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status delivery`
--

DROP TABLE IF EXISTS `status delivery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `status delivery` (
  `id` int unsigned NOT NULL,
  `status` varchar(45) NOT NULL COMMENT '5 статусов (Оплачен, Доставляется, Доставлен, Забрали, Возврат)',
  `type_payment` varchar(45) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cancelled_at` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status delivery`
--

LOCK TABLES `status delivery` WRITE;
/*!40000 ALTER TABLE `status delivery` DISABLE KEYS */;
INSERT INTO `status delivery` VALUES (1,'Оплачен','Сбер Онлайн','2021-08-28 23:37:24','2021-08-29 18:00:39','2021-08-29 18:00:39'),(2,'Оплачен','Сбер Онлайн','2021-08-28 23:38:10','2021-08-29 18:00:39','2021-08-29 18:00:39'),(3,'Доставлен в пункт выдачи','Тинькофф','2021-08-28 23:38:59','2021-08-29 18:01:08','2021-08-29 18:01:08'),(4,'Получена','Озон кард','2021-08-28 23:39:48','2021-08-29 18:01:08','2021-08-29 18:01:08'),(5,'Отменен','СКБ ','2021-08-29 18:26:23','2021-08-29 18:26:23',NULL),(6,'Возврат','Наличными','2021-08-29 18:26:41','2021-08-29 18:26:41',NULL);
/*!40000 ALTER TABLE `status delivery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storage`
--

DROP TABLE IF EXISTS `storage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `storage` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `product` int unsigned NOT NULL,
  `quantity` int unsigned NOT NULL,
  `adress_storage` varchar(65) DEFAULT NULL,
  `updated_info` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `prod_fk_idx` (`product`),
  CONSTRAINT `prod_fk` FOREIGN KEY (`product`) REFERENCES `products` (`id_product`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storage`
--

LOCK TABLES `storage` WRITE;
/*!40000 ALTER TABLE `storage` DISABLE KEYS */;
INSERT INTO `storage` VALUES (1,1,300,'Екатеринбург, Щкрбаковаб 20','2021-08-30 12:46:08'),(2,2,1000,'Екатеринбург, Щкрбаковаб 26','2021-08-30 12:46:08'),(6,3,1000,'Ростов-на-Дону, Ленина 13','2021-08-30 12:46:08'),(7,8,450,'Ростов-на-Дону, Ленина 18','2021-08-30 13:20:08');
/*!40000 ALTER TABLE `storage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `lastname` varchar(45) NOT NULL,
  `birthday` date NOT NULL,
  `email` varchar(50) NOT NULL,
  `sex` tinyint unsigned NOT NULL COMMENT '0 - мужской , 1 - женский',
  `tel` mediumint NOT NULL COMMENT '+7',
  `adress` varchar(90) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `deleted_at` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tel_UNIQUE` (`tel`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=193 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (97,'Brennon','Crooks','1978-05-23','gloria.orn@jacobson.com',0,8388607,NULL,'1993-09-30 01:15:15',NULL),(99,'Dylan','Reinger','1974-08-18','langworth.breana@kihn.net',1,8279447,NULL,'2016-09-01 23:57:42',NULL),(101,'Dillan','Kozey','1981-05-27','lucile32@wehner.biz',0,8348009,NULL,'1993-01-17 17:24:33',NULL),(104,'Hettie','Koch','1996-09-20','haley.malachi@gmail.com',1,8249953,NULL,'1985-11-14 21:20:46',NULL),(105,'Gracie','Jenkins','1973-04-26','aracely70@lemke.info',0,8279850,NULL,'1989-10-03 16:25:16',NULL),(106,'Art','Nitzsche','1980-01-22','mcclure.dahlia@feeneywalker.biz',1,8259811,NULL,'1988-05-04 12:12:38',NULL),(107,'Vilma','Osinski','1991-06-27','metz.camylle@gmail.com',1,8236595,NULL,'2021-02-22 23:21:16',NULL),(108,'Liana','Donnelly','1989-12-08','eladio07@stehr.info',1,8344752,NULL,'2012-11-26 22:02:19',NULL),(109,'Eino','Wilderman','2009-07-02','auer.crystal@funk.com',1,8235272,NULL,'1982-11-21 20:03:54',NULL),(110,'Eugenia','Gottlieb','1995-10-25','tia86@gmail.com',0,8362600,NULL,'2006-09-15 02:28:34',NULL),(115,'Chaz','Cruickshank','1997-12-08','bruen.macie@willms.info',0,8216650,NULL,'2005-12-10 11:51:11',NULL),(116,'Maxie','Weber','1978-05-04','dayana.dickens@hansengottlieb.com',0,8227241,NULL,'2016-05-11 08:59:57',NULL),(118,'Colten','Blanda','2006-04-13','fern73@quigleyveum.info',1,8315951,NULL,'1993-01-08 15:42:55',NULL),(125,'Koby','Mohr','1979-12-01','gabrielle33@kubpfeffer.net',1,8115094,NULL,'1979-05-16 12:12:59',NULL),(126,'Phoebe','Schamberger','2016-08-26','selmer85@yahoo.com',1,8315353,NULL,'2004-05-03 19:53:21',NULL),(136,'Maybell','Quitzon','2015-02-19','jerrell69@hotmail.com',1,8068640,NULL,'2003-01-27 06:05:36',NULL),(137,'Maximillian','Wintheiser','1984-04-21','kevon35@gmail.com',1,8067044,NULL,'2018-10-06 21:46:58',NULL),(142,'Janet','Kreiger','1977-09-13','timmy24@mayercrist.com',1,8276032,NULL,'2000-10-11 00:49:02',NULL),(143,'Jayda','Lebsack','2006-04-19','jaclyn.renner@connpagac.com',0,8019753,NULL,'1995-01-11 22:39:34',NULL),(145,'Shyann','Cronin','1979-04-13','jaleel52@gmail.com',1,8110677,NULL,'2010-05-10 08:54:45',NULL),(149,'Joshuah','Leuschke','1982-04-24','sigurd71@cronin.info',0,8151649,NULL,'1972-11-18 09:06:52',NULL),(157,'Sofia','Schroeder','2019-09-12','jcrist@lubowitzhartmann.com',1,8099505,NULL,'2013-10-20 20:17:52',NULL),(159,'Rozella','Sanford','1990-09-25','jbernhard@morarmraz.info',1,8322273,NULL,'2014-04-28 23:35:13',NULL),(160,'Jaeden','Jaskolski','2017-06-09','kshlerin.maxime@gmail.com',1,8142751,NULL,'2015-01-14 00:15:54',NULL),(161,'Viva','Trantow','2015-06-06','adell.pollich@hotmail.com',0,8368569,NULL,'1976-04-07 20:55:22',NULL),(164,'Tito','Green','1994-04-16','fnader@heathcotefeest.com',1,8170225,NULL,'1976-08-05 14:01:13',NULL),(166,'Savannah','Skiles','1981-01-13','hoeger.derick@yahoo.com',1,8169761,NULL,'1985-04-09 13:09:03',NULL),(167,'Summer','Turner','1971-08-09','sawayn.gisselle@mertzcronin.com',1,8334884,NULL,'1998-09-26 21:06:04',NULL),(169,'Adrianna','Bogisich','2009-06-09','batz.danika@ratke.com',0,8026276,NULL,'1999-04-26 11:07:21',NULL),(170,'Lue','Douglas','2005-07-07','hirthe.howard@jakubowski.com',0,8366788,NULL,'1975-06-04 10:52:24',NULL),(171,'Geraldine','Prosacco','2002-04-25','bcummings@terry.com',0,8185600,NULL,'1980-01-01 19:21:18',NULL),(173,'Kaylah','Herzog','1991-11-08','madaline.tromp@hotmail.com',0,8304775,NULL,'1990-01-26 00:44:51',NULL),(177,'Stephon','Ullrich','2013-01-12','meaghan54@hotmail.com',0,8248361,NULL,'2018-03-28 03:06:47',NULL),(180,'Lennie','Fay','2016-06-07','morissette.cierra@hotmail.com',0,8031788,NULL,'1997-01-15 21:53:17',NULL),(181,'Leann','Lemke','1989-12-26','gjacobs@dooley.biz',1,8296695,NULL,'2002-07-12 03:29:53',NULL),(185,'Wyatt','Mohr','1973-08-09','flittel@jast.com',0,8252654,NULL,'1992-08-25 18:41:29',NULL),(189,'Emmy','Anderson','1973-05-04','maurine.sauer@swift.com',1,8275319,NULL,'2011-08-14 09:23:50',NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'ozon'
--
/*!50003 DROP PROCEDURE IF EXISTS `SPRING SALE!` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `SPRING SALE!`()
BEGIN
UPDATE `products` SET price = price*0.9
where category_path_id = 1;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `goodsrateusers`
--

/*!50001 DROP VIEW IF EXISTS `goodsrateusers`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `goodsrateusers` AS select `products`.`name` AS `Name_of_Product`,`products`.`description` AS `description`,`rating_goods`.`rating_goods` AS `rate`,`rating_goods`.`feedback` AS `feedback`,`users`.`lastname` AS `lastname`,`users`.`email` AS `email` from ((`products` left join `rating_goods` on((`products`.`id_product` = `rating_goods`.`products_id`))) join `users` on((`rating_goods`.`users_id` = `users`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `products_and_paths`
--

/*!50001 DROP VIEW IF EXISTS `products_and_paths`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `products_and_paths` AS select `products`.`id_product` AS `id_product`,`products`.`name` AS `ProdNames`,`category_links`.`path` AS `Path_link`,`products`.`product_path` AS `ProdPath` from (`products` left join `category_links` on((`products`.`category_path_id` = `category_links`.`id_path`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `products_rating`
--

/*!50001 DROP VIEW IF EXISTS `products_rating`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `products_rating` AS select `products`.`name` AS `Name_of_Product`,`products`.`description` AS `description`,`rating_goods`.`rating_goods` AS `rate`,`rating_goods`.`feedback` AS `feedback` from (`products` left join `rating_goods` on((`products`.`id_product` = `rating_goods`.`products_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-30 17:26:17
