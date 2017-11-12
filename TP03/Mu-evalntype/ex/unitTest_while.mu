var n:int;
var note:int;
var compilation:bool;
n=0;
note=20;
compilation=true;

while(n<3){
	log(n);
	n=n+1;
}

while(compilation == true){
	if(note > 1){
		note = note - 1;
	}else{
		compilation=false;
	}
}

log("Ai-je une bonne note en compilation ?");

if(note > 11){
	log("OUI");
}else{
	log("NON");
}

log("Ai-je une note dans la moyenne en compilation ?");

if(note == 10){
	log("OUI");
}else{
	log("NON");
}

log("Suis-je nul ?");
if(note < 5){
	log("OUI");
}

# EXPECTED
# 0
# 1
# 2
# Ai-je une bonne note en compilation ?
# NON
# Ai-je une note dans la moyenne en compilation ?
# NON
# Suis-je nul ?
# OUI