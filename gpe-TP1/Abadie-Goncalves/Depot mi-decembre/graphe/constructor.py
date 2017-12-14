#conding: utf8

import csv
from datetime import date
#Ouverture du fichier contenant les valeurs de session
date = date.today()
def constructeur(fichierSession):


    csvfile = open(fichierSession,'r')
    csvFileArray = []

    for row in csv.reader(csvfile, delimiter = ';',):
        csvFileArray.append(row)

    i=1
    #Valeur contiendra tout les entiers d'acceleration de la session
    valeurs = "["
    heures = []
    
    while i < len(csvFileArray)-1:
        valeurs+=str(csvFileArray[i][0])+","
        heures.append(str(csvFileArray[i][1]))
        i+=1
    valeurs +="]"

    fichierSession = str(date.day)+"_"+str(date.month)+"_"+str(date.year)+".html"
    
    fichierHTML = open(fichierSession, "a")

    #Ecriture contenu du fichier (en integrant les variables)
    fichier = """<html>
    <head>
        <script src="Chart.min.js"></script>
        <style type="text/css">
        h2{
            font-family: 'Roboto';
            font-weight: 500;
        }
        canvas{
            box-shadow: 3px 1px 10px #efefef;
            margin:auto;
            padding:50px 0px 50px 0px
        }
    </style>
    </head>
    <body>
        <h2>Voici les données de votre session du """+str(date.day)+"/"+str(date.month)+"/"+str(date.year)+""": </h2>

        <div id="chart">
              <canvas id="myChart" width="800" height="300"></canvas>
        </div>
    </body>


    <script>
    var ctx = document.getElementById("myChart").getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: """+str(heures)+""",
            datasets: [{
                label: 'Acceleration',
                data:"""+str(valeurs)+""",
                backgroundColor: [
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
    </script>

    </html>"""




    fichierHTML.write(fichier)
    fichierHTML.close()
