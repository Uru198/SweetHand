-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema sweethand
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema sweethand
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sweethand` DEFAULT CHARACTER SET utf8 ;
USE `sweethand` ;

-- -----------------------------------------------------
-- Table `sweethand`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sweethand`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(255) NULL,
  `address` VARCHAR(255) NULL,
  `phone` INT NULL,
  `password` VARCHAR(150) NULL,
  `rol` VARCHAR(45) NULL DEFAULT 'user',
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sweethand`.`shopping`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sweethand`.`shopping` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `date` DATETIME NULL,
  `remarks` TEXT NULL,
  `state` VARCHAR(45) NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_compras_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_compras_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `sweethand`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sweethand`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sweethand`.`products` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `product` VARCHAR(150) NULL,
  `price` INT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sweethand`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sweethand`.`favorites` (
  `user_id` INT NOT NULL,
  `catalog_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `catalog_id`),
  INDEX `fk_users_has_catalogo_catalogo1_idx` (`catalog_id` ASC) VISIBLE,
  INDEX `fk_users_has_catalogo_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_catalogo_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `sweethand`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_catalogo_catalogo1`
    FOREIGN KEY (`catalog_id`)
    REFERENCES `sweethand`.`products` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sweethand`.`detailpurchase`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sweethand`.`detailpurchase` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `product_name` VARCHAR(45) NULL,
  `amount` INT NULL,
  `value` INT NULL,
  `compra_id` INT NOT NULL,
  `producto_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_detallecompra_compras1_idx` (`compra_id` ASC) VISIBLE,
  INDEX `fk_detallecompra_productos1_idx` (`producto_id` ASC) VISIBLE,
  CONSTRAINT `fk_detallecompra_compras1`
    FOREIGN KEY (`compra_id`)
    REFERENCES `sweethand`.`shopping` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_detallecompra_productos1`
    FOREIGN KEY (`producto_id`)
    REFERENCES `sweethand`.`products` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
