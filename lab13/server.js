const https = require("https");
const http = require("http");

var file = 'form.html';
var fs = require("fs");
var url = require("url");

http.createServer(function (request, response) {

var url_parts = url.parse(request.url, true);

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

      const page = "https://journals.agh.edu.pl/csci/oai?verb=GetRecord&metadataPrefix=oai_dc&identifier=" + q.id;




      https.get(page, res => {
          res.setEncoding("utf8");
          let text = "";
          res.on("data", data => {
            text += data;
          });
          res.on("end", () => {
                response.write(text);
                response.end();

          });
        });
      //response.write("eee");


    break;


}




}).listen(8080);
console.log("The server was started on port 8080");
console.log("To end the server, press 'CTRL + C'");
