class MyCounter extends HTMLElement{
  constructor(){
    super();
    this.shadow = this.attachShadow({mode: "open"});
    this.form = document.getElementById("licznik");
  }


  connectedCallback(){
    this.count = this.form.value;
    setInterval(() => {
      if (this.count > 0){
        this.count--;
      }
      this.render();
      if(this.count == 0){
        this.count.value = 0;
      }
    }, 1000);

    this.form.addEventListener("input", i => {
      this.count = licznik.value;
    });
  }

  render(){
    this.shadow.innerHTML = '
    <span> ${this.count} </span>
    <span> ${this.count} </span>
    <span> ${this.count} </span>
    <span> ${this.count} </span>
    <span> ${this.count} </span>
    <span> ${this.count} </span>
    <span> ${this.count} </span>
    <span> ${this.count} </span>
    ';
  }
}

customElements.define("my-counter", MyCounter);
