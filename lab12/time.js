
const http = require("http");
const url = "http://worldtimeapi.org/api/timezone/Europe/Moscow";

http.get(url, res => {
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
});
