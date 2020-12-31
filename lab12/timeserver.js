const http = require("http");
var url = require("url");
var fs = require("fs");
var file = 'time.html';





http.createServer(function (request, response) {
  var datetime;
  var url_parts = url.parse(request.url, true);  
  console.log(url_parts.pathname);

  switch (url_parts.pathname) {

    
    case '/':
      fs.stat(file, function (err, stats) {
        if (err == null) { 
          fs.readFile(file, function (err, data) { 
            response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
            response.write(data);  
            response.end();
          });
        }
        else { 
          response.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
          response.write('The ' + file + ' file does not exist');
          response.end();
        } 
      }); 

      break;

    
    case '/submit':
      var q = url_parts.query;
      var apiUrl = "http://worldtimeapi.org/api/timezone/" + q.area + "/" + q.location;
      response.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });

      fs.stat(file, function (err, stats) {
        if (err == null) { 
          fs.readFile(file, function (err, data) { 
            response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
            
            response.write(data);  
            response.end();
          });
        }
        else { 
          response.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
          response.write('The ' + file + ' file does not exist');
          response.end();
        } 
      }); 
     
  
      /*http.get(apiUrl, res => {
        res.setEncoding("utf8");
        let body = "";
        res.on("data", data => {
          body += data;
        });
        res.on("end", () => {
          if (body[0] != "<"){
            body = JSON.parse(body);
            var datetime = body.datetime.toString();
            response.write("Local date and time: " + Date() + "\nRemote date and time: " + datetime);
            response.end();

          }
          else{
            response.write("Problem with API connection");
            response.end();
          }
          
          
        });
      });*/
      //response.write("Local date: " + Date()); // Data (response) that we want to send to the web browser
      //response.end();// Sending the answer
      
      

      break;
    }

  /*http.get(apiUrl, res => {
    res.setEncoding("utf8");
    let body = "";
    res.on("data", data => {
      body += data;
    });
    res.on("end", () => {
      body = JSON.parse(body);
      datetime = body.datetime.toString();
      response.write("Date and time: " + datetime);
      response.end();
      
      
    });
  });*/
 
  

}).listen(8080);
console.log("The server was started on port 8080");
console.log("To end the server, press 'CTRL + C'");
