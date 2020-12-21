var http = require("http");
var url = require("url");




http.createServer(function(request, response) {
    console.log("--------------------------------------")
    console.log("The relative URL of the current request: "+request.url+"\n")
    var url_parts = url.parse(request.url,true); //parsing (relative) URL


    if(url_parts.pathname == '/submit') { //Processing the form content, if the relative URL is '/ submit'
	    var file=url_parts.query['file']; //Read the contents of the field (form) named 'name'
	    console.log("Creating a response header")
	    response.writeHead(200, {"Content-Type": "text/plain; charset=utf-8"});  //Creating an answer header - we inform the browser that the body of the answer will be plain text
        console.log("Creating the body of the response");
        const fs = require('fs');
        fs.access(file, fs.constants.F_OK, function(err) {
            if (!err) {
              fs.stat(file, function (error, stats){
                  if (!error) {
                    if (stats.isFile()){
                      fs.readFile(file, 'utf8', function (error, data) {
                        response.write("File:\n" + data);
                        response.end();
                      });
                    }
                    else{
                      response.write("Directory");
                      response.end();
                    }
                  }
        
              });
            }
            else {
                response.write("Not found");
                response.end();
              }
        });
	     //The end of the response - send it to the browser
	    console.log("Sending a response")
    }
    else { //Generating the form
	    console.log("Creating a response header")
	    response.writeHead(200, {"Content-Type": "text/html; charset=utf-8"});  //Creating a repsonse header - we inform the browser that the body of the response will be HTML text
	    //and now we put an HTML form in the body of the answer
            console.log("Creating a response body")
	    response.write('<form method="GET" action="/submit">');
	    response.write('<label for="file">Give name of a file or directory</label>');
	    response.write('<input name="file">');
	    response.write('<br>');
	    response.write('<input type="submit">');
	    response.write('</form>');
	    response.end();  //The end of the response - send it to the browser
	    console.log("Sending a response")
    }
}).listen(8080);
console.log("The server was started on port 8080");
console.log("To end the server, press 'CTRL + C'");