window.addEventListener("load", function(event) {

cacher(); 

  });

window.addEventListener('error', function(e) { cacher(); }, true);

function cacher(){
		let div = document.getElementById("image");
    		div.style.display = "none";
    	let div1 = document.getElementById("animation");
    		div1.style.display = "none";
}

function simulations(arg) {
	
	let filtreDepartement = document.getElementById('departement');
	let filtreCirconscription = document.getElementById('circonscription');

	filtreDepartement = filtreDepartement.value;
	filtreCirconscription = filtreCirconscription.value;


	if (filtreDepartement == "" || filtreCirconscription == ""){
		cacher();
		alert("Attention! Il manque un paramètre.")    		
    	
    }

    else{
	
		let div = document.getElementById("image");
			div.src="Plots/"+filtreDepartement+"-"+filtreCirconscription+".png";
			div.style.display = "inline";
		let div1 = document.getElementById("animation");
			div1.src="Animations/"+filtreDepartement+"-"+filtreCirconscription+".mp4";
			div1.style.display = "inline";
    	}


}