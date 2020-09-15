-- Adminer 4.7.3 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP DATABASE IF EXISTS `mahasiswa`;
CREATE DATABASE `mahasiswa` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `mahasiswa`;

DROP TABLE IF EXISTS `example`;
CREATE TABLE `example` (
  `absen` varchar(2) DEFAULT NULL,
  `npm` varchar(8) NOT NULL,
  `nama` varchar(35) DEFAULT NULL,
  `lama` varchar(5) DEFAULT NULL,
  `baru` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`npm`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- 2020-09-15 14:41:01

