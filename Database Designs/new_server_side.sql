-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema IIITSCart
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema IIITSCart
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `IIITSCart` DEFAULT CHARACTER SET utf8 ;
SHOW WARNINGS;
USE `IIITSCart` ;

-- -----------------------------------------------------
-- Table `IIITSCart`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `IIITSCart`.`customer` (
  `c_id` INT(10) NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `phone` INT(10) UNSIGNED NOT NULL,
  `address` VARCHAR(45) NOT NULL,
  `blacklist` TINYINT NOT NULL,
  PRIMARY KEY (`c_id`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `IIITSCart`.`Login`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `IIITSCart`.`Login` (
  `id` INT(10) NOT NULL,
  `username` VARCHAR(30) CHARACTER SET 'utf8' NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  CONSTRAINT `login`
    FOREIGN KEY (`id`)
    REFERENCES `IIITSCart`.`customer` (`c_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `IIITSCart`.`admin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `IIITSCart`.`admin` (
  `a_id` INT(10) NOT NULL,
  `username` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`a_id`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE,
  CONSTRAINT `ids link`
    FOREIGN KEY (`a_id`)
    REFERENCES `IIITSCart`.`Login` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `IIITSCart`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `IIITSCart`.`category` (
  `cat_id` INT(10) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`cat_id`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `IIITSCart`.`product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `IIITSCart`.`product` (
  `id` INT(10) NOT NULL AUTO_INCREMENT,
  `p_id` INT(10) NOT NULL,
  `title` VARCHAR(45) NOT NULL,
  `quantity` INT(5) NOT NULL,
  `category` INT(10) NOT NULL,
  `description` VARCHAR(250) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `p_id_UNIQUE` (`p_id` ASC) VISIBLE,
  INDEX `product-category_idx` (`category` ASC) VISIBLE,
  CONSTRAINT `product-customer`
    FOREIGN KEY (`id`)
    REFERENCES `IIITSCart`.`customer` (`c_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `product-category`
    FOREIGN KEY (`category`)
    REFERENCES `IIITSCart`.`category` (`cat_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `IIITSCart`.`p_reviews`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `IIITSCart`.`p_reviews` (
  `r_id` INT(10) NOT NULL AUTO_INCREMENT,
  `rating` INT(1) NOT NULL,
  `text` VARCHAR(60) NOT NULL,
  PRIMARY KEY (`r_id`),
  CONSTRAINT `customer-reviews`
    FOREIGN KEY (`r_id`)
    REFERENCES `IIITSCart`.`product` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `IIITSCart`.`c_review`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `IIITSCart`.`c_review` (
  `id` INT(10) NOT NULL,
  `rating` INT(1) NULL,
  `text` VARCHAR(60) NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `review-user`
    FOREIGN KEY (`id`)
    REFERENCES `IIITSCart`.`customer` (`c_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
