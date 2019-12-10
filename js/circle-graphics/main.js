function main() {
  document.getElementById("button").innerHTML = "Bam";
  const canvas = document.getElementById("canvas");
  const context = canvas.getContext("2d");

  let x = 30;
  let y = 30;
  let accelX = 0;
  let velX = 0.7;
  let accelY = 0.05;
  let velY = 0;

  function update() {
    context.beginPath();
    context.arc(x, y, 30, 0, 2 * Math.PI);
    context.fillStyle = "#99FF99";
    context.fill();
    context.stroke();

    velX += accelX;
    x += velX;
    velY += accelY;
    y += velY;

    if (y > 200) {
      accelY = -0.05;
    }

    if (y < 200) {
      accelY = 0.05;
    }

    if (y > 470) {
      velY *= -0.9;
    }

    if (y < 30) {
      velY *= -0.9;
    }

    if (x > 470) {
      velX *= -1;
    }

    if (x < 30) {
      velX *= -1;
    }
  }

  setInterval(function() {
    update();
  }, 1);
}
