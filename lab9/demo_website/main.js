const iterations = 100;
const multiplier = 1000000000;

var worker = new Worker("calculate.js");

/**
 * Doing the pointless computations.
 */
var pointlessComputationsButton = document.getElementById("pointless-computations");
pointlessComputationsButton.disabled = false;
pointlessComputationsButton.addEventListener("click", doPointlessComputations, false);

var blocking;
var anframe;
var worker;
var setint;
var settime;

function doPointlessComputations() {
  pointlessComputationsButton.disabled = true;

  var useWorkerButton = document.getElementById("use-worker");
  var useBlockingJsButton = document.getElementById("use-blocking-js");
  var useRequestAnimationFrame = document.getElementById("use-request-animation-frame");
  var useSetInterval =  document.getElementById("use-si");
  var useSetTimeout =  document.getElementById("use-st");

  if (useBlockingJsButton.checked) {
    var t11 = performance.now();
    doPointlessComputationsWithBlocking();
    var t12 = performance.now();
    blocking = t12-t11;

  }
  else if (useRequestAnimationFrame.checked) {
    var t21 = performance.now();
    doPointlessComputationsWithRequestAnimationFrame();
    var t22 = performance.now();
    anframe = t22-t21;
  }
  else if (useWorkerButton.checked) {
    var t31 = performance.now();
    doPointlessComputationsInWorker();
    var t32 = performance.now();
    worker = t32-t31;
  }
  else if (useSetInterval.checked){
    var t41 = performance.now();
    doPointlessComputationsWithSetInterval();
    var t42 = performance.now();
    setint = t42-t41;
  }
  else if (useSetTimeout.checked){
    var t51 = performance.now();
    doPointlessComputationsWithSetTimeot();
    var t52 = performance.now();
    settime = t52-t51;
  }

  var chart = new CanvasJS.Chart("chartContainer", {
    	theme: "light1", // "light2", "dark1", "dark2"
    	animationEnabled: false, // change to true
    	title:{
    		text: "Czasy wykonania funkcji"
    	},
    	data: [
    	{
    		// Change type to "bar", "area", "spline", "pie",etc.
    		type: "column",
    		dataPoints: [
    			{ label: "WithBlocking();",  y: blocking },
    			{ label: "WithRequestAnimationFrame", y:  anframe  },
    			{ label: "InWorker", y: worker  },
    			{ label: "WithSetInterval",  y: setint  },
    			{ label: "WithSetTimeot",  y: settime  }
    		]
    	}
    	]
    });
    chart.render();
}

/**
 * Start/stop animation
 */
var started = false;
var startStopButton = document.getElementById("start-stop");

startStopButton.addEventListener("click", startStop, false);

function startStop() {
  started = !started;
  if (started) {
    container.classList.add("started");
    startStopButton.value = "Stop animations";
  }
  else {
   container.classList.remove("started");
   startStopButton.value = "Start animations";
  }
}
