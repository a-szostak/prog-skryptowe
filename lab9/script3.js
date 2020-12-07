spans = document.querySelectorAll('span');

form = document.getElementById('licznik');

counter = form.value;
window.setInterval(decrement, 1000);


function decrement(){
  spans.forEach(function (i){
    i.textContent = counter;
  })
  if (counter > 0){
    counter--;
  }
  else if (counter==0){
    spans[0].textContent = 0;
  }
}




form.addEventListener("input", function(){
   counter = form.value;
   //window.setInterval(decrement, 1000);
});
