<?php 
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "kupferpreis.ch";
//$servername = "efarinit.mysql.db.internal";
//$dbname = "efarinit_kupferpreis";
//$username = "efarinit_ilija";
//$password = "21j10i95K21+";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sqlPrice = "SELECT * FROM `preise`";
$resultPrice = $conn->query($sqlPrice);
$rowPrice = $resultPrice->fetch_assoc();
$index = $rowPrice['index'] / 100;
$usdchf = $rowPrice['usdchf'];
$kupferpreis = $rowPrice['kupferpreis'];
$alupreis = $rowPrice['alupreis'];
$bleipreis = $rowPrice['bleipreis'];
$edelstahl = $rowPrice['nickelpreis'];
$zinnpreis = $rowPrice['zinnpreis'];
$datum = $rowPrice['datum'];
function getProdDetail($id,$conn)
{
/*$sqlPrice = "SELECT * FROM `preise` WHERE id='2'";
$resultPrice = $conn->query($sqlPrice);
$rowPrice = $resultPrice->fetch_assoc();
$index = $rowPrice['index'] / 100;
//$alu = $rowPrice['kupferpreis'];
//$usdchf = $rowPrice['usdchf'];
$blei = $rowPrice['kupferpreis'];
//$edelstahl = $rowPrice['chni'];
$datum = $rowPrice['datum'];
function getProdDetail($id,$conn)
{*/

	$sql = "SELECT * FROM `metall` WHERE id=$id";
	$totalCount = $conn->query($sql);
	$result = $conn->query($sql);
	// echo $result->num_rows;
	if ($result->num_rows > 0) {
	    return  $result->fetch_assoc();
	} 
	else
	{
		return "";
	}
}
?>