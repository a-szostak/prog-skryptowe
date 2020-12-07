txt = document.getElementById('txt');
checkbox = document.getElementById('checkbox');
add = document.getElementById('add');
write = document.getElementById('write');


  function addStudent(){

  }

  var subjects = new Map();
  index = 0;

  function addSub(sub, grade){
    subjects.set(sub, grade);
    console.log(subjects);
  }


  add.onclick = function(){
    text = txt.value
    if(text[0] == 's'){
      sub = text.substr(1, text.length-2);
      grade = text.substr(text.length-1, text.length-2);
      addSub(sub, grade);
    }

  }
