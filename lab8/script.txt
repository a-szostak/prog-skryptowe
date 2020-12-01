var main = document.getElementsByTagName("main")[0];
var aside = document.getElementsByTagName("aside")[0];
var nav = document.getElementsByTagName("nav")[0];
var footer = document.getElementsByTagName("footer")[0];
var marg = document.getElementsByClassName("marg")
var azure = document.getElementsByClassName("azure");


function set()
{

    main.style.width = "50%";
    main.style.minWidth = "390px";
    main.style.clear = "both";


    aside.style.position = "absolute";
    aside.style.float = "left";
    aside.style.width = "20%";
    aside.style.right = "10px";

    
    nav.style.height = "auto";
    nav.style.width = "12%";
    nav.style.float = "left";


    footer.style.width = "98%";
    footer.style.marginBottom = "10px";


    //Tło
    for (var i=0; i<azure.length; i++)
    {
        azure[i].style.backgroundColor = "#EFF";
        azure[i].style.border = "1px solid #000000";
    }

    //Marginesy
    for (var i=0; i<marg.length; i++)
    {
        marg[i].style.margin = "1%";
        
    }
}


function del()
{
    main.style = "";
    aside.style = "";
    nav.style = "";
    footer.style = "";

    for (var i=0; i<marg.length; i++)
    {
        marg[i].style.margin = "";
        
    }

    for (var i=0; i<azure.length; i++)
    {
        azure[i].style = "";
    }
}
