function sleep(ms){
	return new Promise(resolve => setTimeout(resolve, ms));
}

async function sleepPlz(){
	while(true){
		await sleep(30000);
		var iframe = document.getElementById('graph');
		iframe.src = iframe.src;
	}
}

sleepPlz();
