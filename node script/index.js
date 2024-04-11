/**
 * Module dependencies.
 */

var bodyParser = require("body-parser")
var path = require('path');
const fs = require("fs");
const os = require('os');

const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = require('socket.io')(server, {
  maxHttpBufferSize: 1e8, pingTimeout: 25000
});
const fileUpload = require('express-fileupload');

const { exec } = require("child_process");


app.use(fileUpload());

app.use(express.static(path.join(__dirname, 'public')));

app.use(bodyParser.urlencoded({ extended: false }));



io.on('connection', (socket) => {
  console.log('a user connected '+socket.id);
  
  	socket.on('elaboravideo', (folder,algorithm) => {
  		console.log("sono qua algoritmo="+algorithm);
  		elabora(folder+"/input.mp4",folder,socket,algorithm);
  		
	});


});




app.get('/algo',function(req, res) {

 folder= req.query.folder;
 video=folder+"/output.mp4";
 res.sendFile(video);

});

app.get('/trajectory',function(req, res) {

 folder= req.query.folder;
 img=folder+"/trajectory.png";
 res.sendFile(img);

});

app.get('/transforms',function(req, res) {

 folder= req.query.folder;
 img=folder+"/transforms.png";
 res.sendFile(img);

});

app.post('/upload', function(req, res) {
  let sampleFile;
  let uploadPath;
  if (!req.files || Object.keys(req.files).length === 0) {
    return res.status(400).send('No files were uploaded.');
  }
  // The name of the input field (i.e. "sampleFile") is used to retrieve the uploaded file
  sampleFile = req.files.sampleFile;
       fs.mkdtemp(path.join(__dirname+"/video/", 'foo-'), (err, folder) => {
			if (err) throw err;
			uploadPath = folder+"/input.mp4";
			// Use the mv() method to place the file somewhere on your server
			sampleFile.mv(uploadPath, function(err) {
				if (err)
				return res.status(500).send(err);
				res.send(folder);
  			});
  			
		});
});




function elabora(str,folder,socket,algorithm){
	socket.emit("caricato");
	a="";
	switch(algorithm){
	 case "1":{ 
	 	console.log("Elaboro video con il primo algoritmo da "+socket.id);
	 	a="./video/videostab "+"'"+str+"'";
	 	break;
	 	}
	 case "2": {
		console.log("Elaboro video con il secondo algoritmo da "+socket.id);
		a="./video/videostabKalman "+"'"+str+"'";
		break;
		}
	 case "3":{console.log("Elaboro video con il terzo algoritmo da "+socket.id);
	 	a="python3 'video/main.py' '"+str+"'";
	 	break;
	 	}
	default:{console.log("Elaboro video con il primo algoritmo da "+socket.id);
	 	a="./video/videostab "+"'"+str+"'";
	 	break;}
	}
	
	var comando1= exec(a, (error, stdout, stderr) =>{
		if (error) {
		console.log(`stderr: ${stderr}`); 
		return;
		}else{ 
			socket.emit("stabilizzato");
			a="ffmpeg -i '"+folder+"/input.mp4' -i '"+folder+"/outcpp.avi' -vsync 2  -filter_complex hstack '"+folder+"/output.mp4'";		
			var comando2= exec(a, (error, stdout, stderr) =>{
				if (error) {
				console.log(`stderr: ${stderr}`); 
					
				}else{
					socket.emit("ricevi",folder);
				}
				
				return;
			});
				//console.log(`stdout: ${stdout}`); 	
			
		    }
		});		
}



server.listen(3000);
console.log('listening on port 3000');

