// Scroll to Projects
document.getElementById("scrollBtn").addEventListener("click", () => {
  document.querySelector("#projects").scrollIntoView({ behavior: "smooth" });
});

// Typing effect
const typedText = document.getElementById("typed-text");
const texts = ["Cybersecurity Learner.",  "Cloud Enthusiast."];
let index = 0, charIndex = 0;

function type() {
  if (charIndex < texts[index].length) {
    typedText.textContent += texts[index][charIndex];
    charIndex++;
    setTimeout(type, 100);
  } else {
    setTimeout(erase, 1000);
  }
}

function erase() {
  if (charIndex > 0) {
    typedText.textContent = texts[index].substring(0, charIndex - 1);
    charIndex--;
    setTimeout(erase, 50);
  } else {
    index = (index + 1) % texts.length;
    setTimeout(type, 500);
  }
}
type();

// Simple particle background
const canvas = document.getElementById('particle-canvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let particles = [];
for(let i=0;i<100;i++){
  particles.push({
    x: Math.random()*canvas.width,
    y: Math.random()*canvas.height,
    r: Math.random()*2+1,
    dx: (Math.random()-0.5)*0.5,
    dy: (Math.random()-0.5)*0.5
  });
}

function animateParticles(){
  ctx.clearRect(0,0,canvas.width,canvas.height);
  particles.forEach(p=>{
    ctx.beginPath();
    ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
    ctx.fillStyle = 'rgba(59,130,246,0.7)';
    ctx.fill();
    p.x+=p.dx;
    p.y+=p.dy;
    if(p.x<0||p.x>canvas.width) p.dx*=-1;
    if(p.y<0||p.y>canvas.height) p.dy*=-1;
  });
  requestAnimationFrame(animateParticles);
}
animateParticles();

// Animate skill bars
document.querySelectorAll('.skill-bar').forEach(bar => {
  const width = bar.getAttribute('data-width') || '80%';
  bar.style.width = '0%'; // start from 0
  setTimeout(() => {
    bar.style.transition = "width 1.2s ease";
    bar.style.width = width; // animate to correct width
  }, 300); // slight delay to ensure page is rendered
});

