let fireworksCanvas = document.getElementById("fireworksCanvas");
let fireworksContext = fireworksCanvas.getContext("2d");
let width = window.innerWidth;
let height = window.innerHeight;
let clicked = false;
let mouseX = 0,
  mouseY = 0;
let particles = [];
let particleSettings = {
  gravity: 0.05,
};

let events = {
  mouse: {
    down: "mousedown",
    move: "mousemove",
    up: "mouseup",
  },
  touch: {
    down: "touchstart",
    move: "touchmove",
    up: "touchend",
  },
};

let deviceType = "";

window.requestAnimationFrame =
  window.requestAnimationFrame ||
  window.webkitRequestAnimationFrame ||
  window.mozRequestAnimationFrame ||
  window.oRequestAnimationFrame ||
  window.msRequestAnimationFrame ||
  function (callback) {
    window.setTimeout(callback, 1000 / 60);
  };

window.onload = () => {
  fireworksCanvas.width = width;
  fireworksCanvas.height = height;
  window.requestAnimationFrame(startFirework);
};

const isTouchDevice = () => {
  try {
    document.createEvent("TouchEvent");
    deviceType = "touch";
    return true;
  } catch (e) {
    deviceType = "mouse";
    return false;
  }
};

isTouchDevice();

fireworksCanvas.addEventListener(events[deviceType].down, function (e) {
  e.preventDefault();
  clicked = true;
  mouseX = isTouchDevice() ? e.touches[0].pageX : e.pageX;
  mouseY = isTouchDevice() ? e.touches[0].pageY : e.pageY;
});

fireworksCanvas.addEventListener(events[deviceType].up, function (e) {
  e.preventDefault();
  clicked = false;
});

function randomNumberGenerator(min, max) {
  return Math.random() * (max - min) + min;
}

function Particle() {
  this.width = randomNumberGenerator(0.1, 0.9) * 5;
  this.height = randomNumberGenerator(0.1, 0.9) * 5;
  this.x = mouseX - this.width / 2;
  this.y = mouseY - this.height / 2;
  this.vx = (Math.random() - 0.5) * 10;
  this.vy = (Math.random() - 0.5) * 10;
}

Particle.prototype = {
  move: function () {
    if (this.x >= fireworksCanvas.width || this.y >= fireworksCanvas.height) {
      return false;
    }
    return true;
  },
  draw: function () {
    this.x += this.vx;
    this.y += this.vy;
    this.vy += particleSettings.gravity;
    fireworksContext.save();
    fireworksContext.beginPath();
    fireworksContext.translate(this.x, this.y);
    fireworksContext.arc(0, 0, this.width, 0, Math.PI * 2);
    fireworksContext.fillStyle = this.color;
    fireworksContext.closePath();
    fireworksContext.fill();
    fireworksContext.restore();
  },
};

function createFirework() {
  var numberOfParticles = randomNumberGenerator(10, 50);
  let color = `rgb(${randomNumberGenerator(0, 255)},${randomNumberGenerator(0, 255)},${randomNumberGenerator(0, 255)})`;

  for (var i = 0; i < numberOfParticles; i++) {
    var particle = new Particle();
    particle.color = color;
    var vy = Math.sqrt(25 - particle.vx * particle.vx);
    if (Math.abs(particle.vy) > vy) {
      particle.vy = particle.vy > 0 ? vy : -vy;
    }
    particles.push(particle);
  }
}

function startFirework() {
  let current = [];
  fireworksContext.fillStyle = "rgba(0,0,0,0.1)";
  fireworksContext.fillRect(0, 0, width, height);
  if (clicked) {
    createFirework();
  }
  for (let i in particles) {
    particles[i].draw();
    if (particles[i].move()) {
      current.push(particles[i]);
    }
  }
  particles = current;
  window.requestAnimationFrame(startFirework);
}