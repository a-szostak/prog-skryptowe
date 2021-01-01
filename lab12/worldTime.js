
const http = require("http");
var url = "http://worldtimeapi.org/api/timezone/Europe/Moscow";


http.createServer(function (request, response) {


http.get(url, res => {
  res.setEncoding("utf8");
  let body = "";
  res.on("data", data => {
    body += data;
  });
  res.on("end", () => {
    if (body[0] != "<"){
      body = JSON.parse(body);
      var datetime = body.datetime.toString();
      response.write("Date and time: " + datetime);
      response.end();
    }
    else{
      response.write("API doesn't response");
      response.end();
    }
  });
});

}).listen(8080);
console.log("The server was started on port 8080");
console.log("To end the server, press 'CTRL + C'");