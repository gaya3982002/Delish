/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - recipe
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`recipe` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `recipe`;

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `Comp_id` int(80) NOT NULL AUTO_INCREMENT,
  `User_lid` int(80) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Complaint` varchar(80) DEFAULT NULL,
  `Reply` varchar(80) DEFAULT NULL,
  `Status` varchar(80) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Comp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`Comp_id`,`User_lid`,`Date`,`Complaint`,`Reply`,`Status`,`type`) values 
(1,5,'2022-10-12','no net','okkk','replied',NULL),
(2,4,'2022-12-02','tydsyi.','pending','pending','shop'),
(3,4,'2022-12-02','not good','pending','pending','shop'),
(4,4,'2022-12-03','mmm','pending','pending','shop'),
(5,0,'0000-00-00','\"++\"',NULL,NULL,NULL),
(6,7,'2022-12-29','fg','pending','pending','user'),
(7,7,'2022-12-29','fg','pending','pending','user'),
(8,7,'2022-12-29','fg','pending','pending','user'),
(9,7,'2022-12-29','very bad','we will make it better','pending','user'),
(10,7,'2022-12-29','good','pending','pending','user'),
(11,7,'2022-12-29','good','pending','pending','user'),
(12,7,'2022-12-29','good','pending','pending','user'),
(13,7,'2022-12-29','bad service ','get lost','pending','user'),
(14,3,'2023-01-14','not worth','pending','pending','shop'),
(15,3,'2023-01-14','bad','pending','pending','shop'),
(16,7,'2023-01-21','bh\n','pending','pending','user'),
(17,7,'2023-01-28','bad','pending','pending','user'),
(18,3,'2023-01-29','ok','pending','pending','shop'),
(19,3,'2023-01-29','','pending','pending','shop'),
(20,3,'2023-01-29','kljhb','pending','pending','shop'),
(21,7,'2023-01-29','gg','pending','pending','user'),
(22,7,'2023-01-29','gg','pending','pending','user'),
(23,7,'2023-02-04','hg','pending','pending','user'),
(24,4,'2023-02-04','bad','pending','pending','shop'),
(25,7,'2023-03-06','good','pending','pending','user');

/*Table structure for table `item` */

DROP TABLE IF EXISTS `item`;

CREATE TABLE `item` (
  `Item_id` int(80) NOT NULL AUTO_INCREMENT,
  `Store_lid` int(80) DEFAULT NULL,
  `Veg_id` int(80) DEFAULT NULL,
  `Quantity` int(80) DEFAULT NULL,
  PRIMARY KEY (`Item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `item` */

insert  into `item`(`Item_id`,`Store_lid`,`Veg_id`,`Quantity`) values 
(8,5,13,6),
(9,4,14,12),
(10,3,15,2),
(11,8,16,1),
(12,3,17,1),
(13,3,18,1),
(14,3,25,5),
(15,3,24,5),
(16,3,16,12),
(17,3,23,12),
(18,4,33,3),
(19,4,21,2),
(20,4,18,32);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(80) NOT NULL AUTO_INCREMENT,
  `Username` varchar(80) NOT NULL,
  `Password` varchar(80) NOT NULL,
  `Type` varchar(80) NOT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`Username`,`Password`,`Type`) values 
(1,'admin@gmail.com','admin','admin'),
(3,'gayu123@gmail.com','123','shop'),
(4,'aswa@gmail.com','123','shop'),
(5,'\"+email+\"','\"+str(cnfpswd)+\"','user'),
(6,'abc','123','user'),
(7,'hdhd','1111','user'),
(8,'abhi@gmail.com','abhi','shop'),
(9,'sd','112233','shop'),
(10,'sd','1122','shop'),
(11,'abhi@gmail.com','1122','shop'),
(12,'aswa@gmail.com','123','shop');

/*Table structure for table `recipe` */

DROP TABLE IF EXISTS `recipe`;

CREATE TABLE `recipe` (
  `Recipe_id` int(80) NOT NULL AUTO_INCREMENT,
  `Recipe_name` varchar(80) NOT NULL,
  `Image` varchar(80) NOT NULL,
  `Description` varchar(80) NOT NULL,
  PRIMARY KEY (`Recipe_id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=latin1;

/*Data for the table `recipe` */

insert  into `recipe`(`Recipe_id`,`Recipe_name`,`Image`,`Description`) values 
(18,'sambar','/static/Recipe/IMG20230121171201jpg','take some vegetables cut it in to small pieces.'),
(31,'Paneer Curry','/static/Recipe/IMG20230131124740jpg','fghyut'),
(32,'resam','/static/Recipe/IMG20230227150655jpg','iohhvfdfmnm'),
(38,'bittergourd fry','/static/Recipe/IMG20230306124016jpg','very tasty'),
(40,'beetroot pachadi','/static/Recipe/IMG20230306145930jpg','fgg'),
(41,'cucumber salad','/static/Recipe/IMG20230306150928jpg','ryude');

/*Table structure for table `recipe_item` */

DROP TABLE IF EXISTS `recipe_item`;

CREATE TABLE `recipe_item` (
  `Rec_item_id` int(80) NOT NULL AUTO_INCREMENT,
  `Rec_id` int(80) DEFAULT NULL,
  `Veg_id` int(80) DEFAULT NULL,
  PRIMARY KEY (`Rec_item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=120 DEFAULT CHARSET=latin1;

/*Data for the table `recipe_item` */

insert  into `recipe_item`(`Rec_item_id`,`Rec_id`,`Veg_id`) values 
(1,19,13),
(2,19,14),
(6,17,14),
(7,17,15),
(12,23,22),
(17,29,32),
(18,17,14),
(27,23,26),
(28,22,13),
(33,30,32),
(35,29,32),
(41,25,13),
(48,20,30),
(58,18,24),
(65,24,24),
(67,24,26),
(74,31,26),
(81,37,15),
(95,38,33),
(96,32,19),
(97,32,20),
(98,32,23),
(99,31,17),
(100,31,19),
(101,31,20),
(102,31,25),
(103,20,17),
(104,20,19),
(105,20,20),
(106,20,23),
(107,20,25),
(108,39,13),
(109,39,16),
(110,39,17),
(111,39,18),
(112,39,20),
(113,39,23),
(114,39,25),
(115,20,34),
(116,20,34),
(117,40,14),
(118,40,20),
(119,41,34);

/*Table structure for table `review` */

DROP TABLE IF EXISTS `review`;

CREATE TABLE `review` (
  `Rev_id` int(80) NOT NULL AUTO_INCREMENT,
  `Shop_lid` int(80) DEFAULT NULL,
  `User_lid` int(80) DEFAULT NULL,
  `Review` varchar(80) DEFAULT NULL,
  `Rating` varchar(80) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`Rev_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `review` */

insert  into `review`(`Rev_id`,`Shop_lid`,`User_lid`,`Review`,`Rating`,`Date`) values 
(1,4,5,'good','5','2022-10-30'),
(2,0,7,'g','1.5','2022-12-29'),
(3,0,7,'f','1.0','2022-12-29'),
(4,0,7,'good','5.0','2022-12-29'),
(5,5,7,'good','2.5','2023-01-14'),
(6,3,7,'4','3.5','2023-01-14'),
(7,5,7,'good','2.5','2023-01-28'),
(8,5,7,'bad','2.0','2023-01-29');

/*Table structure for table `store` */

DROP TABLE IF EXISTS `store`;

CREATE TABLE `store` (
  `Store_id` int(80) NOT NULL AUTO_INCREMENT,
  `Store_lid` int(80) DEFAULT NULL,
  `Store_name` varchar(80) NOT NULL,
  `Place` varchar(80) NOT NULL,
  `Post` varchar(80) NOT NULL,
  `Pin` varchar(80) NOT NULL,
  `Phone` varchar(80) NOT NULL,
  `Photo` varchar(800) NOT NULL,
  `Email` varchar(80) NOT NULL,
  `Latitude` varchar(80) NOT NULL,
  `Longitude` varchar(80) NOT NULL,
  `Status` varchar(90) NOT NULL,
  `Licencse_no` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`Store_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `store` */

insert  into `store`(`Store_id`,`Store_lid`,`Store_name`,`Place`,`Post`,`Pin`,`Phone`,`Photo`,`Email`,`Latitude`,`Longitude`,`Status`,`Licencse_no`) values 
(1,5,'Reliance','Karapparamb','kottooli','8765','9946294806','/static/store/a.jpg','123@gmail.com','10.026617','76.308411','rejected','657412'),
(4,6,'Anona','kk','','54','54','/static/store/b.jpg','554','11','1','approved','45'),
(5,3,'gayu','clt','Post','Post','66772299','/static/store/a.jpg','gayu123@gmail.com','12','21','approved','123654789'),
(6,4,'adysh p','tvm','Post','Post','33216544789','/static/store/c.jpg','aswa@gmail.com','12','21','approved','7894'),
(7,8,'store','calicut','125478','252212','5544887755','/static/store/IMG20230114133419jpg','abhi@gmail.com','15','21','rejected','221154785'),
(8,9,'hh','ss','ss','ss','12451214','/static/store/IMG20230129165727jpg','sd','15','21','approved','1245221'),
(9,10,'store','calicut','125478','252212','12451214','/static/store/IMG20230129170044jpg','sd','15','21','pending','1245221'),
(10,11,'hh','calicut','ss','545544','1245121444','/static/store/IMG20230129170533jpg','abhi@gmail.com','15','21','pending','1245221'),
(11,12,'hh','calicut','125478','252212','5544887755','/static/store/IMG20230219005759jpg','aswa@gmail.com','15','21','pending','1245221');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `UserId` int(80) NOT NULL AUTO_INCREMENT,
  `User_lid` int(80) DEFAULT NULL,
  `User_name` varchar(80) NOT NULL,
  `Place` varchar(80) NOT NULL,
  `Post` varchar(80) NOT NULL,
  `Pin` varchar(80) NOT NULL,
  `City` varchar(80) NOT NULL,
  `Phone` varchar(80) NOT NULL,
  `Email` varchar(90) NOT NULL,
  `Photo` varchar(80) NOT NULL,
  PRIMARY KEY (`UserId`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`UserId`,`User_lid`,`User_name`,`Place`,`Post`,`Pin`,`City`,`Phone`,`Email`,`Photo`) values 
(1,5,'Rakesh','Kannur','Puthiyangadi','673021','Kannur','9995494806','123@gmail.com','static/user/20221226-164634.jpg'),
(2,6,'krishna','clt','clt','468242','clt','8855449966','pon@gmail.com','static/user/20221226-164634.jpg'),
(3,7,'thejuu','puthiyappa','Calicut','987878','Kozhikodee','9846729177','theju@gmail.com','/static/user/20230218-115427.jpg'),
(4,6,'sam','Calicut ','676767','Calicut ','Calicut ','9876543210','sam@gmail.com','static/user/20221226-164634.jpg'),
(5,7,'thejuu','puthiyappa','Calicut','987878','Kozhikodee','9846729177','theju@gmail.com','/static/user/20230218-115427.jpg');

/*Table structure for table `vegetables` */

DROP TABLE IF EXISTS `vegetables`;

CREATE TABLE `vegetables` (
  `Veg_id` int(15) NOT NULL AUTO_INCREMENT,
  `Veg_name` varchar(80) NOT NULL,
  `Image` varchar(800) NOT NULL,
  PRIMARY KEY (`Veg_id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;

/*Data for the table `vegetables` */

insert  into `vegetables`(`Veg_id`,`Veg_name`,`Image`) values 
(13,'beans','/static/Vegetable/IMG20230121165039jpg'),
(14,'beetroot','/static/Vegetable/IMG20230129120710jpg'),
(15,'brinjal','/static/Vegetable/IMG20230129120817jpg'),
(16,'carrot','/static/Vegetable/IMG20230129120840jpg'),
(17,'onion','/static/Vegetable/IMG20230129120910jpg'),
(18,'potato','/static/Vegetable/IMG20230129120941jpg'),
(19,'tomato','/static/Vegetable/IMG20230129121007jpg'),
(20,'garlic','/static/Vegetable/IMG20230129121100jpg'),
(21,'wintermelon','/static/Vegetable/IMG20230122143312jpg'),
(22,'cauliflower','/static/Vegetable/IMG20230128122012jpg'),
(23,'green chilli','/static/Vegetable/IMG20230128122102jpg'),
(24,'red chilli','/static/Vegetable/IMG20230128122143jpg'),
(25,'ginger','/static/Vegetable/IMG20230128122218jpg'),
(26,'capsicum','/static/Vegetable/IMG20230128122243jpg'),
(27,'cabbage','/static/Vegetable/IMG20230128122307jpg'),
(28,'corn','/static/Vegetable/IMG20230128122357jpg'),
(29,'lettuce','/static/Vegetable/IMG20230128122426jpg'),
(30,'lemon','/static/Vegetable/IMG20230128122457jpg'),
(31,'raddish','/static/Vegetable/IMG20230128122536jpg'),
(32,'spinach','/static/Vegetable/IMG20230128122626jpg'),
(33,'bitter guard','/static/Vegetable/IMG20230204162644jpg'),
(34,'cucumber','/static/Vegetable/IMG20230306151042jpg');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
