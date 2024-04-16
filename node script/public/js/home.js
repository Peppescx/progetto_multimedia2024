var socket = io();
reset()
function SubForm (){
  reset();
  $("#list").css("display","block");
  start("timer1");
  var form = new FormData($('#uploadForm')[0]);  
  $.ajax({
      url: '/upload',
      type: 'POST',   
      success: function (res) {
  			
			mandavideo(res);
  	},      
      data: form,                
      cache: false,
      contentType: false,
      processData: false
  }); 
}
let algorithm=0;
function mandavideo(folder){
	algorithm=$("#algoritmo").val();
	socket.emit("elaboravideo",folder,algorithm);
}

var counter1=0;
var counter2=0;
var counter3=0;
var interval1,interval2,interval3;

socket.on("ricevi", (folder) => {
	stop("timer3");
	$(".timer-display-id").css("display","inline-block");
	$("div#c3").css("display","none");
	$("input#c3").css("display","inline-block");
	$("span#c3").text("Codifica completata");
	console.log("Finita elavorazione,chiedo video");
	let img1 = document.getElementById("img1");
	let img2 = document.getElementById("img2");
	let grafi= document.getElementById("grafi");
	img1.src="/trajectory?folder="+folder;
	img2.src="/transforms?folder="+folder;
	grafi.style.display = "inline-flex";
	video_out.src = "/algo?folder="+folder;
	video_out.style.display = "block";
	video_out.play();
});

socket.on("caricato", () => {
	stop("timer1");
	$("div#c1").css("display","none");
	$("input#c1").css("display","inline-block");
	$("span#c1").text("Caricamento completato");
	start("timer2");

});
socket.on("stabilizzato", () => {
	stop("timer2");
	$("div#c2").css("display","none");
	$("input#c2").css("display","inline-block");
	$("span#c2").text("Stabilizzazione completata");
	start("timer3");
});


function reset(){
//prima di cancellare controlla che tutti e 3 siano success
	document.getElementById("video").pause();
	$("div#p-2").css("display","none");
	$("#list").css("display","none");	
	$("span#c1").text("Caricamento in corso");
	$("input#c1").css("display","none");
	$("div#c1").css("display","inline-block");
	$("span#c2").text("Stabilizzazione in corso");
	$("input#c2").css("display","none");
	$("div#c2").css("display","inline-block");
	$("span#c3").text("Encoding in corso");
	$("input#c3").css("display","none");
	$("div#c3").css("display","inline-block");
	$(".timer-display-id").css("display","block");
	stop("timer1");
	stop("timer2");
	stop("timer3");
	 counter1=0;
	 counter2=0;
	 counter3=0;
	document.getElementById("timer").innerHTML = convertSec(counter1);
	document.getElementById("timer2").innerHTML = convertSec(counter1);
	document.getElementById("timer3").innerHTML = convertSec(counter1);
}
     
document.getElementById("video-preview").addEventListener("change", function() {
	 $("#p-2").css("display","block");
	 $("#video").css("border-radius","0.25rem");
	  var media = URL.createObjectURL(this.files[0]);
	  var video = document.getElementById("video");
	  video.src = media;
	  video.style.display = "block";
	  video.play();
});




function stop(timer) {
 switch(timer){
	case "timer1": clearInterval(interval1); break;
	case "timer2": clearInterval(interval2); break;
	case "timer3": clearInterval(interval3); break;
 }
}

function convertSec(cnt) {
	let sec = cnt % 60;
	let min = Math.floor(cnt / 60);
	if (sec < 10) {
	if (min < 10) {
		return "0" + min + ":0" + sec;
	} else {
		return min + ":0" + sec;
	}
	} else if ((min < 10) && (sec >= 10)) {
		return "0" + min + ":" + sec;
	} else {
		return min + ":" + sec;
	}
}



function start(timer) {
ret=document.getElementById(timer);

 switch(timer){
	case "timer1": 
				
				interval1 = setInterval(function() {
				ret.innerHTML = convertSec(counter1++); // timer start counting here...
				}, 1000);
			break;
	case "timer2":  
				
				interval2 = setInterval(function() {
				ret.innerHTML = convertSec(counter2++); // timer start counting here...
				}, 1000); 
			break;
	case "timer3": 
				
				interval3 = setInterval(function() {
				ret.innerHTML = convertSec(counter3++); // timer start counting here...
				}, 1000);
			break;
 }

}


