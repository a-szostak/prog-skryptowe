var azure = document.getElementsByClassName("azure");
var left = document.getElementsByClassName("onLeft");
var blockquote = document.querySelector("blockquote");
var headh1 = document.querySelector("header h1");
var aside = document.querySelector("aside");
var footer = document.querySelector("footer");
var header = document.querySelector("header");
var main = document.querySelector("main");
var nav = document.querySelector("nav");
var form = document.querySelector("form");

document.getElementById("ustaw").onclick = ustaw;
document.getElementById("skasuj").onclick = skasuj;



function ustaw(){

  for (var i=0; i<azure.length; i++){
    azure[i].style.backgroundColor = "#EFF";
    azure[i].style.borderStyle = "solid";
    azure[i].style.borderColor = "black";
    azure[i].style.borderWidth = "1px";
    azure[i].style.boxShadow = "0 0 5px black";
    azure[i].style.fontSize = "20px";
  }
  for (var i=0; i<left.length; i++){
    left[i].style.float = "left";
    left[i].style.marginLeft = "25px";
  }
  blockquote.style.fontFamily = '"Lucida Console", Courier, monospace';
  blockquote.style.marginLeft = "10px";
  blockquote.style.paddingBottom = "5%";

  headh1.style.marginBottom = "6px";
  headh1.style.marginTop = "6px";

  document.querySelector("main h1").style.paddingLeft = "10px";
  document.querySelector("aside h1").style.marginBottom = "-25px";

  aside.style.width = "30%";
  aside.style.float = "right";
  aside.style.marginRight = "25px";
  aside.style.paddingLeft = "15px";
  aside.style.paddingRight = "400px";

  footer.style.width = "95%";
  footer.style.marginTop = "1%";
  footer.style.padding = "13px";

  header.style.paddingLeft = "10px";
  header.style.margin = "0px 25px 25px 25px";

  main.style.width = "40%";
  main.style.paddingRight = "20px";
  main.style.marginTop = "1%";

  nav.style.paddingRight = "15px";
  nav.style.paddingLeft = "17px";

  form.style.float = "left";
  form.style.margin = "20px";

}

function skasuj(){
  for (var i=0; i<azure.length; i++){
    azure[i].style = "";
  }
  for (var i=0; i<left.length; i++){
    left[i].style = "";
 }
  blockquote.style = "";
  aside.style = "";
  footer.style = "";
  header.style = "";
  document.querySelector("main h1").style = "";
  main.style = "";
  document.querySelector("aside h1").style = "";
  nav.style = "";
  headh1.style =  "";
  form.style = "";

}
