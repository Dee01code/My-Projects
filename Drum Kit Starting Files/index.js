var allbtn = document.querySelectorAll("button");
for(var i = 0; i<allbtn.length; i++){
    allbtn[i].addEventListener("click", function(){
        var text = this.innerHTML;
        makesound(text);
        clickChange(text);
    });
}

document.addEventListener("keypress", function(event){
    var text = event.key;
    makesound(text);
    clickChange(text);
})

function makesound(text){
    switch(text){
        case "u":
            var aud1 = new Audio('sounds/crash.mp3');
            aud1.play();
            break;
        case "i":
            var aud1 = new Audio('sounds/kick-bass.mp3');
            aud1.play();
            break;
        case "n":
            var aud1 = new Audio('sounds/snare.mp3');
            aud1.play();
            break; 
        case "m":
            var aud1 = new Audio('sounds/tom-1.mp3');
            aud1.play();
            break;
        case "j":
            var aud1 = new Audio('sounds/tom-2.mp3');
            aud1.play();
            break;
        case "k":
            var aud1 = new Audio('sounds/tom-3.mp3');
            aud1.play();
            break; 
        case "h":
            var aud1 = new Audio('sounds/tom-4.mp3');
            aud1.play();
            break;       
        default : null;
    }
}

function clickChange(key){
    document.querySelector("."+key).classList.add("pressed");
    setTimeout(function(){
        document.querySelector("."+key).classList.remove("pressed");
    },100);
}