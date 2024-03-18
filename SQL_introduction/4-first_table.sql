-- script that creates a table in my database
CREATE TABLE IF NOT EXISTS `hbtn_0c_0`.`first_table` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(256) NOT NULL,
  `score` INT NOT NULL,
  PRIMARY KEY (`id`)
);