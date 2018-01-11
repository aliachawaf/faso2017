<?php
mysql_connect("localhost", "root", "projetfaso") or die("Connection Failed");
mysql_select_db("Donnees")or die("Connection Failed");
$query = "truncate table donnees";
 if(mysql_query($query)){
      header("Location: traitement.php");
        exit;

  } else{
      echo "fail";
  }
?>

