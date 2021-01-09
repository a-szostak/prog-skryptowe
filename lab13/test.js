

const https = require("https");
const url = "https://journals.agh.edu.pl/csci/oai?verb=GetRecord&metadataPrefix=oai_dc&identifier=oai:ojs.journals.agh.edu.pl:article/2901";

https.get(url, res => {
  res.setEncoding("utf8");
  let body = "";
  res.on("data", data => {
    body += data;
  });
  res.on("end", () => {
    
    console.log(body);
  });
});
