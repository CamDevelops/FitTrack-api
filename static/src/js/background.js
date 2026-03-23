// ─── SHREDLY BACKGROUND ANIMATION ───
// Sweat drops, ember sparks, light rays

const canvas = document.getElementById('bg-canvas');
const ctx = canvas.getContext('2d');
let W, H, particles, rays, sweatDrops;

function resize() {
  W = canvas.width = window.innerWidth;
  H = canvas.height = window.innerHeight;
}

// Floating ember/spark particles rising like heat
class Particle {
  constructor() { this.reset(); }
  reset() {
    this.x = Math.random() * W;
    this.y = H + Math.random() * 100;
    this.size = Math.random() * 2.5 + 0.5;
    this.speedY = -(Math.random() * 1.2 + 0.3);
    this.speedX = (Math.random() - 0.5) * 0.6;
    this.alpha = Math.random() * 0.7 + 0.2;
    this.life = 1;
    this.decay = Math.random() * 0.004 + 0.001;
    const r = Math.random();
    if (r < 0.5) this.color = 'rgba(232,38,10,';
    else if (r < 0.8) this.color = 'rgba(255,120,50,';
    else this.color = 'rgba(255,200,50,';
  }
  update() {
    this.x += this.speedX;
    this.y += this.speedY;
    this.life -= this.decay;
    if (this.life <= 0 || this.y < -20) this.reset();
  }
  draw() {
    ctx.save();
    ctx.globalAlpha = this.life * this.alpha;
    ctx.shadowBlur = 8;
    ctx.shadowColor = this.color + '0.8)';
    ctx.fillStyle = this.color + (this.life * this.alpha) + ')';
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  }
}

// Sweat streaks falling down the screen
class SweatDrop {
  constructor() { this.reset(); }
  reset() {
    this.x = Math.random() * W;
    this.y = -Math.random() * H;
    this.len = Math.random() * 18 + 6;
    this.speed = Math.random() * 3 + 2;
    this.alpha = Math.random() * 0.1 + 0.02;
    this.width = Math.random() * 1.2 + 0.3;
  }
  update() {
    this.y += this.speed;
    if (this.y > H + 30) this.reset();
  }
  draw() {
    ctx.save();
    ctx.globalAlpha = this.alpha;
    ctx.strokeStyle = 'rgba(180,80,50,1)';
    ctx.lineWidth = this.width;
    ctx.beginPath();
    ctx.moveTo(this.x, this.y);
    ctx.lineTo(this.x - 1, this.y + this.len);
    ctx.stroke();
    ctx.restore();
  }
}

// Dramatic spotlight rays pulsing from top right
class Ray {
  constructor(index) {
    this.angle = (index / 7) * Math.PI - Math.PI / 2 + (Math.random() - 0.5) * 0.3;
    this.x = W * 0.65 + (Math.random() - 0.5) * 200;
    this.y = -50;
    this.length = H * 1.8;
    this.width = Math.random() * 80 + 20;
    this.alpha = Math.random() * 0.04 + 0.01;
    this.speed = Math.random() * 0.002 + 0.001;
    this.phase = Math.random() * Math.PI * 2;
    this.currentAlpha = this.alpha;
  }
  update(t) {
    this.currentAlpha = this.alpha * (0.5 + 0.5 * Math.sin(t * this.speed + this.phase));
  }
  draw() {
    ctx.save();
    ctx.globalAlpha = this.currentAlpha;
    const grad = ctx.createLinearGradient(
      this.x, this.y,
      this.x + Math.cos(this.angle) * this.length,
      this.y + Math.sin(this.angle) * this.length
    );
    grad.addColorStop(0, 'rgba(232,38,10,0.9)');
    grad.addColorStop(0.4, 'rgba(200,60,10,0.3)');
    grad.addColorStop(1, 'rgba(0,0,0,0)');
    ctx.strokeStyle = grad;
    ctx.lineWidth = this.width;
    ctx.beginPath();
    ctx.moveTo(this.x, this.y);
    ctx.lineTo(
      this.x + Math.cos(this.angle) * this.length,
      this.y + Math.sin(this.angle) * this.length
    );
    ctx.stroke();
    ctx.restore();
  }
}

function init() {
  resize();
  particles = Array.from({ length: 120 }, () => new Particle());
  sweatDrops = Array.from({ length: 60 }, () => new SweatDrop());
  rays = Array.from({ length: 7 }, (_, i) => new Ray(i));
}

let t = 0;
function animate() {
  requestAnimationFrame(animate);
  t++;

  // Dark base
  ctx.fillStyle = '#0d0d0d';
  ctx.fillRect(0, 0, W, H);

  // Pulsing red atmosphere
  const pulse = 0.5 + 0.5 * Math.sin(t * 0.008);

  const grad1 = ctx.createRadialGradient(W * 0.7, H * 0.15, 0, W * 0.7, H * 0.15, W * 0.7);
  grad1.addColorStop(0, `rgba(180,20,0,${0.18 + pulse * 0.08})`);
  grad1.addColorStop(1, 'rgba(0,0,0,0)');
  ctx.fillStyle = grad1;
  ctx.fillRect(0, 0, W, H);

  const grad2 = ctx.createRadialGradient(W * 0.1, H * 0.85, 0, W * 0.1, H * 0.85, W * 0.5);
  grad2.addColorStop(0, `rgba(100,10,0,${0.12 + pulse * 0.05})`);
  grad2.addColorStop(1, 'rgba(0,0,0,0)');
  ctx.fillStyle = grad2;
  ctx.fillRect(0, 0, W, H);

  // Rays
  rays.forEach(r => { r.update(t); r.draw(); });

  // Sweat drops
  sweatDrops.forEach(s => { s.update(); s.draw(); });

  // Ember sparks
  particles.forEach(p => { p.update(); p.draw(); });

  // Bottom heat glow
  const hazeGrad = ctx.createLinearGradient(0, H * 0.7, 0, H);
  hazeGrad.addColorStop(0, 'rgba(0,0,0,0)');
  hazeGrad.addColorStop(1, `rgba(80,10,0,${0.15 + pulse * 0.1})`);
  ctx.fillStyle = hazeGrad;
  ctx.fillRect(0, 0, W, H);
}

window.addEventListener('resize', () => {
  resize();
  rays.forEach(r => { r.x = W * 0.65 + (Math.random() - 0.5) * 200; });
});

init();
animate();
