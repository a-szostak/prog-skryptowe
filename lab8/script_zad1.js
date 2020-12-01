window.prompt("Tekst1","Tekst2");


var body = document.querySelector('body');
body.onload = function(){
          console.log('Tekst 1');
          window.alert('Tekst 2');
        }



var button = document.getElementById('wypisz');

button.onclick = function() {
    var txt = document.forms[0].elements['pole_tekstowe'].value;
    var num =  document.forms[0].elements['pole_liczbowe'].value;

    document.getElementById('formElements').innerText = txt;
    document.getElementById('formElements').innerText += "\n" + num;

  }
