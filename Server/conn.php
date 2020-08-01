<?php
/// Datos de conexión de a la Base de datos mysql 
/* 

La Base de datos esta creada con la siguiente estructura:

TSG       ┐ 
          ├ Users ┐
          │       ├ ID_user (int, Primary. A.I)
          │       ├ Name (Varchar64)
          │       ├ Password (Varchar128)
          │       ├ Proyect (Varchar64)
          │       ├ Enable (Varchar6) *
          │       └ DatelastAccess (timestamp) *
          └ B2_key ┐
                   ├ ID_key (int, Primary. A.I)
                   ├ ID_key_user (int)
                   ├ KeyName (Varchar128)
                   ├ KeyPassword (Varchar128)
                   └ Enable (Varchar6) *

                   *No implementado 31/07/20

El codigo SQL utilizado para crear esta estructura es:

CREATE TABLE `TSG`.`Users` ( `ID_user` INT NOT NULL AUTO_INCREMENT , `Name` VARCHAR(64) NOT NULL , 
                                  `Password` VARCHAR(128) NOT NULL , `Proyect` VARCHAR(64) NOT NULL , 
                                  `Enable` VARCHAR(6) NOT NULL , `DatelastAccess` VARCHAR(128) NOT NULL , 
                                   `key_bucket` INT NOT , PRIMARY KEY (`ID_user`)) ENGINE = InnoDB;

CREATE TABLE `TSG`.`B2_key` ( `ID_key` INT NOT NULL AUTO_INCREMENT , `ID_key_user` INT NOT NULL , 
                                   `KeyName` VARCHAR(128) NOT NULL , `KeyPassword` VARCHAR(128) NOT NULL , 
                                   `Enable` VARCHAR(6) NOT NULL , `Bucket` VARCHAR(64) NOT NULL ,
                                   PRIMARY KEY (`ID_key`)) ENGINE = InnoDB;


*/




/// Datos de Conexión
$dbhost	= "localhost";      // Remplace con la Direción de su db mysql
$dbuser	= "userName";		// Remplace con el nombre de usuario de su base de datos
$dbpass	= "Password1234";	// Remplace con la contraseña de acceso de su baase de datos
$dbname	= "TSG";   // Remplace con la con el nombre de la base de datos

/// Conexión a la base de datos

$conn = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname);

// Verificación de conexión exitosa
if (!$conn) {
    die("Connection: " . mysqli_connect_error());
}