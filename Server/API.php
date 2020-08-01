<?php
/// API para obtener acceso a la key de b2

///Se incluye conn.php que ofrece la conexión con la base de datos

include 'conn.php';

$user = $_POST["user"];
$pass = $_POST["password"];

$request_user = mysqli_query($conn, "SELECT key_bucket,  Password FROM Users WHERE Name='$user'");
$row_rUser = mysqli_fetch_assoc($request_user);
$hash = $row_rUser['Password'];
$key_bucket = $row_rUser['key_bucket'];

/* 

***ALERTA***
El HASH de la password aun no se encuentra implementado
***ALERTA***

 */

if($hash == $pass){
    $request_key = mysqli_query($conn, "SELECT KeyName, KeyPassword, Bucket FROM B2_key WHERE ID_key='$key_bucket'");
    $row_rKey= mysqli_fetch_assoc($request_key);
    $key=$row_rKey['KeyPassword'];
    $userkey=$row_rKey['KeyName'];
    $bucket = $row_rKey['Bucket'];
    echo $userkey.",".$key.",".$bucket;

}else{echo "E:062";}
