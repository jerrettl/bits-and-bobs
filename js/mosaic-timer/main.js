document.addEventListener("keydown", function (event) {
  switch (event.key) {
    case "ArrowDown":
      window.offset += 1;
      return;
    case "Down":
      window.offset += 1;
      return;
    case "ArrowUp":
      window.offset -= 1;
      return;
    case "Up":
      window.offset -= 1;
      return;
    case "ArrowLeft":
      window.offset += 5;
      return;
    case "Left":
      window.offset += 5;
      return;
    case "ArrowRight":
      window.offset -= 5;
      return;
    case "Right":
      window.offset -= 5;
      return;
    case "Enter":
      start();
      return;
    case " ":
      start();
      return;
    default:
      return;
  }
});

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function start() {
  if (window.active == true) {
    stop();
    return;
  }

  window.offset = 0;
  var button = document.getElementById("startButton");
  button.setAttribute("onClick", "stop()");
  button.innerHTML = "Stop";

  var time = document.getElementById("time");
  var minutes = document.getElementById("timeMinutes");
  var seconds = document.getElementById("timeSeconds");
  var start = Date.now();
  window.active = true;
  var totalTime = 60 * 20;

  while (window.active == true) {
    window.elapsed = Math.floor((Date.now() - start) / 1000) + window.offset;
    var remaining = totalTime - window.elapsed;

    if ((Math.floor(remaining / 60)) < 10) {
      minutes.innerHTML = "0" + Math.floor(remaining / 60);
    }
    else {
      minutes.innerHTML = Math.floor(remaining / 60);
    }

    if ((remaining % 60) < 10) {
      seconds.innerHTML = "0" + (remaining % 60);
    }
    else {
      seconds.innerHTML = remaining % 60;
    }


    if (remaining <= 0) {
      stop();
    }

    await sleep(50);
  }
}

function stop() {
  var button = document.getElementById("startButton");
  button.setAttribute("onClick", "start()");
  button.innerHTML = "Start";

  window.active = false;

  var minutes = document.getElementById("timeMinutes");
  var seconds = document.getElementById("timeSeconds");
  minutes.innerHTML = "00";
  seconds.innerHTML = "00";
}
