<?php

$db_host = 'localhost';
$db_user = 'root';
$db_pass = 'projetfaso';
$db_name = 'Donnees';

$conn = mysqli_connect($db_host, $db_user, $db_pass, $db_name);
if (!$conn) {
        die ('Failed to connect to MySQL: ' . mysqli_connect_error());
}

$sql = 'SELECT *
                FROM donnees ORDER BY Date DESC';

$query = mysqli_query($conn, $sql);

if (!$query) {
        die ('SQL Error: ' . mysqli_error($conn));
}
?>

<html>
<head>
        <title>Tableau de suivi Aquarium</title>
        /* Partie CSS */
        <style type="text/css">
                body {
                        font-size: 15px;
                        color: #343d44;
                        font-family: "segoe-ui", "open-sans", tahoma, arial;
                        padding: 0;
                        margin: 0;
                }
                table {
                        margin: auto;
                        font-family: "Lucida Sans Unicode", "Lucida Grande", "Segoe Ui";
                        font-size: 12px;
                }

                h1 {
                        margin: 25px auto 0;
                        text-align: center;
                        text-transform: uppercase;
                        font-size: 17px;
                }

                table td {
                        transition: all .5s;
                }

                /* Table */
                .data-table {
                        border-collapse: collapse;
                        font-size: 14px;
                        min-width: 537px;
                }

                .data-table th,
                .data-table td {
                        border: 1px solid #e1edff;
                        padding: 7px 17px;
                }
                .data-table caption {
                        margin: 7px;
                }

                /* Table Header */
                .data-table thead th {
                        background-color: #508abb;
                        color: #FFFFFF;
                        border-color: #6ea1cc !important;
                        text-transform: uppercase;
                }

                /* Table Body */
                .data-table tbody td {
                        color: #353535;
                }
                .data-table tbody td:first-child,
                .data-table tbody td:nth-child(4),
                .data-table tbody td:last-child {
                        text-align: right;
                }

                .data-table tbody tr:nth-child(odd) td {
                        background-color: #f4fbff;
                }
                .data-table tbody tr:hover td {
                        background-color: #ffffa2;
                        border-color: #ffff0f;
                }
        </style>
        /* Fin partie CSS */

</head>
<body>
        /* Début partie HTMl, SQL */
        <h1>Suivi de l'Aquarium</h1>
        <table class="data-table">
                <caption class="title">Temperature et PH ordonnes par date</caption>
                <thead>
                        <tr>
                                <th>Temperature</th>
                                <th>PH</th>
                                <th>Date</th>
                        </tr>
                </thead>
                <tbody>
                <?php
                while ($row = mysqli_fetch_array($query))
                {
                        echo '<tr>
                                        <td>'.$row['Temperature'].'</td>
                                        <td>'.$row['PH'].'</td>
                                        <td>'.$row['Date'].'</td>
                                </tr>';
                }?>
                </tbody>
        </table>
<center><p> Pour changer les données, <a href="index.html"> clique ici</a> pour revenir à la page d'accueil</p></center>
<center><form method="post" action="delete_bdd.php" class="delete_form">
    <input type="submit" name="valider" class="delete" value="Cliquez ici pour supprimer les valeurs" />
</form><br><br></center>
</body>
</html>


