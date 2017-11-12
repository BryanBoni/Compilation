var n:int;
n=8;

if (n>7){
	log("n est superieur à 7");
}

if (n>8){
	log("n est superieur à 8");
}else if (n==8){
	log("n est égale à 8");
}else{
	log("n est inférieur à 8");
}

if (n>=9){
	log("n est superieur à 9");
}else{
	log("n est inférieur à 9");
}

if(n!=10){
	log("n est différent de 10");
}

if((n+2) == 10){
	log("n + 2 est égale à 10");
}

if(n>5){
	if(n>10){
		log("n est superieur à 10");
	}else{
		log("n est compris entre 5 et 10");
	}
}

# EXPECTED
# n est superieur à 7
# n est égale à 8
# n est inférieur à 9
# n est différent de 10
# n + 2 est égale à 10
# n est compris entre 5 et 10