class MyCounter extends HTMLElement{
    constructor() {
        super();
        this.shadow = this.attachShadow({ mode: "open" });
        this.licznik = document.getElementById("licznik");
    }


   connectedCallback(){
      this.count = this.licznik.value;


      setInterval(() => {
          this.render();

          if(this.count > 0)
              this.count--;
          if(this.count == 0)
              this.count.value = 0;

      }, 1000);

      this.licznik.onchange = () => {
        this.count = licznik.value;
      }

  }
  render(){
        this.shadow.innerHTML = `
          ${this.count}
          ${this.count}
          ${this.count}
          ${this.count}
          ${this.count}
          ${this.count}
          ${this.count}
          ${this.count}
          ${this.count}
          ${this.count}
          `;
  }}
customElements.define("my-counter", MyCounter);
