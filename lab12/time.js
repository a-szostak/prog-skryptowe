
const http = require("http");
var url = "http://worldtimeapi.org/api/timezone/";//Europe/Moscow";


http.createServer(function (request, response) {

var q = "Europe"+"/" +"Moscow";
url = url + q;
http.get(url, res => {
  res.setEncoding("utf8");
  let body = "";
  res.on("data", data => {
    body += data;
  });
  res.on("end", () => {
    //body = JSON.parse(body);
    var datetime = body;//.datetime.toString();
    response.write("Local date and time: " + Date() + "\nRemote date and time: " + datetime[0]);
    response.end();
  });
});

}).listen(8080);