var affiche = 0;
var nbAffiche = 3;


function recupTouche(e){
	
	if (e.charCode == "104") {
    }
	
	// G
    else if (e.charCode == "103") {
		affiche--;
		
    }
    else if (e.charCode == "98") {
        
    }
	// D
    else if (e.charCode == "100") {
		affiche++;
        
    }
	
	if (affiche == -1) {
		affiche = nbAffiche -1;
	}
	
	
	if (affiche%nbAffiche == 0) {
		   document.getElementById('affichage_1').style.display = "block";
		   document.getElementById('affichage_2').style.display = "none";
		   document.getElementById('affichage_3').style.display = "none";
		   
	}
		
	if (affiche%nbAffiche == 1) {
		   document.getElementById('affichage_1').style.display = "none";
		   document.getElementById('affichage_2').style.display = "block";
		   document.getElementById('affichage_3').style.display = "none";
	}
	
	if (affiche%nbAffiche == 2) {
		   document.getElementById('affichage_1').style.display = "none";
		   document.getElementById('affichage_2').style.display = "none";
		   document.getElementById('affichage_3').style.display = "block";
	}
}



document.addEventListener("keypress", recupTouche);