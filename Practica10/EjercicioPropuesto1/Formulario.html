<?php
// Conexión a la base de datos
$servername = "localhost:3307";
$username = "root";
$password = "";
$dbname = "DB_Ejercicio1";
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
 die("Error de conexión: " . $conn->connect_error);
}
// Recopilar datos del formulario
$nombre = $_POST['nombre'];
$fecha_nacimiento = $_POST['fecha_nacimiento'];
$tipo_pasajero = $_POST['tipo_pasajero'];
$destino = $_POST['destino'];
// Calcular el precio del pasaje según el tipo de pasajero
if ($tipo_pasajero == 'Adulto') {
 $precio = obtenerPrecioDelPasaje($conn, $destino);
} elseif ($tipo_pasajero == 'Menor') {
 $precio = obtenerPrecioDelPasaje($conn, $destino) * 0.75;
} else { // Infante
 $precio = 0;
}
// Insertar los datos en la base de datos
$sql_pasaje = "INSERT INTO pasajes (destino, precio) VALUES ('$destino', $precio)";
if ($conn->query($sql_pasaje) === TRUE) {
 $id_pasaje = $conn->insert_id;
 $sql_pasajero = "INSERT INTO pasajeros (nombre, fecha_nacimiento, tipo_pasajero,
id_pasaje) VALUES ('$nombre', '$fecha_nacimiento', '$tipo_pasajero', $id_pasaje)";
 if ($conn->query($sql_pasajero) === TRUE) {
 echo "Pasaje comprado exitosamente. Precio: $" . number_format($precio, 2);
 } else {
 echo "Error al insertar los datos del pasajero: " . $conn->error;
 }
} else {
 ec
