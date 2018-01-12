#conding: utf8

import csv
from datetime import date
#Ouverture du fichier contenant les valeurs de session
date = date.today()
def constructeur():
    
    csvfileX = open("dataX.csv",'r')
    csvFileArrayX = []
    
    csvfileY = open("dataY.csv",'r')
    csvFileArrayY = []
    
    csvfileZ = open("dataZ.csv",'r')
    csvFileArrayZ = []

    for row in csv.reader(csvfileX, delimiter = ';'):
        csvFileArrayX.append(row)
        
            
            
    for row in csv.reader(csvfileY, delimiter = ';'):
        csvFileArrayY.append(row)
        
    for row in csv.reader(csvfileZ, delimiter = ';'):
        csvFileArrayZ.append(row)

    #Valeur contiendra tout les entiers d'acceleration de la session
    valeursX = "["
    heuresX = []
    
    for i in range(0, len(csvFileArrayX)-1):
        valeursX+=str(csvFileArrayX[i][0])+","
        print(len(heuresX))
        
        heuresX.append(str(csvFileArrayX[i][1]))
        i+=1
    valeursX +="]"
    
    
    valeursY = "["
    heuresY = []
    for i in range( 0, len(csvFileArrayY)-1) :
        valeursY+=str(csvFileArrayY[i][0])+","
        heuresY.append(str(csvFileArrayY[i][1]))
        i+=1
    valeursY +="]"
    
    
    
    valeursZ = "["
    heuresZ = []
    for i in range(0, len(csvFileArrayZ)-1):
        valeursZ+=str(csvFileArrayZ[i][0])+","
        heuresZ.append(str(csvFileArrayZ[i][1]))
        i+=1
    valeursZ +="]"

    fichierSession = str(date.day)+"_"+str(date.month)+"_"+str(date.year)+".html"
    
    fichierHTML = open(fichierSession, "a")

    #Ecriture contenu du fichier (en integrant les variables)
    fichier = """<html>
    <head>
        <script src="../JS/Chart.min.js"></script>
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
    <meta charset="UTF-8">
    </head>
    <body>
        <h2>Voici les données de votre session du """+str(date.day)+"/"+str(date.month)+"/"+str(date.year)+""": </h2>

        <div id="chart">
              <canvas id="line-chart" width="800" height="300"></canvas>
        </div>
    </body>


    <script>
    new Chart(document.getElementById("line-chart"), {
  type: 'line',
  data: {
    labels: """+str(heuresX)+""",
    datasets: [{ 
        data: """+str(valeursX)+""",
        label: "Mouvement avant",
        borderColor: "#3e95cd",
        fill: false
      }, { 
        data: """+str(valeursY)+""",
        label: "Mouvement descendant",
        borderColor: "#8e5ea2",
        fill: false
      }, { 
        data: """+str(valeursZ)+""",
        label: "Mouvement lateraux",
        borderColor: "#3cba9f",
        fill: false
      }
    ]
  },
  options: {
    title: {
      display: true,
      text: 'World population per region (in millions)'
    }
  }
});
    </script>

    </html>"""




    fichierHTML.write(fichier)
    fichierHTML.close()
    

constructeur()




