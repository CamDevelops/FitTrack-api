// ─── SHREDLY API CONFIG ───
const API = 'http://127.0.0.1:5000';

// ─── PAGE ROUTING ───
function showPage(name) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.getElementById(name).classList.add('active');
  window.scrollTo(0, 0);
}

// ─── UTILS ───
function togglePass(id) {
  const input = document.getElementById(id);
  input.type = input.type === 'password' ? 'text' : 'password';
}

function showError(id, msg) {
  const el = document.getElementById(id);
  el.textContent = msg;
  el.classList.add('show');
  const successId = id.replace('error', 'success');
  const successEl = document.getElementById(successId);
  if (successEl) successEl.classList.remove('show');
}

function showSuccess(id, msg) {
  const el = document.getElementById(id);
  el.textContent = msg;
  el.classList.add('show');
  const errorId = id.replace('success', 'error');
  const errorEl = document.getElementById(errorId);
  if (errorEl) errorEl.classList.remove('show');
}

// ─── LOGIN ───
async function handleLogin() {
  const email = document.getElementById('login-email').value.trim();
  const password = document.getElementById('login-password').value;
  const btn = document.getElementById('login-btn');

  if (!email || !password) {
    showError('login-error', 'Please fill in all fields.');
    return;
  }

  btn.disabled = true;
  btn.textContent = 'Logging in...';

  try {
    const res = await fetch(`${API}/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    if (data.access_token) {
      localStorage.setItem('token', data.access_token);
      showSuccess('login-success', '🔥 Welcome back! Redirecting...');
      setTimeout(() => alert('Logged in! Token stored. Dashboard coming soon.'), 1200);
    } else {
      showError('login-error', data.error || 'Login failed. Check your credentials.');
    }
  } catch (e) {
    showError('login-error', 'Could not connect to server. Make sure Flask is running.');
  }

  btn.disabled = false;
  btn.textContent = "Let's Get It";
}

// ─── SIGNUP ───
async function handleSignup() {
  const name = document.getElementById('signup-name').value.trim();
  const username = document.getElementById('signup-username').value.trim();
  const email = document.getElementById('signup-email').value.trim();
  const ph_number = document.getElementById('signup-phone').value.trim();
  const age = parseInt(document.getElementById('signup-age').value);
  const password = document.getElementById('signup-password').value;
  const btn = document.getElementById('signup-btn');

  if (!name || !username || !email || !password || !age) {
    showError('signup-error', 'Please fill in all required fields.');
    return;
  }

  btn.disabled = true;
  btn.textContent = 'Creating account...';

  try {
    const res = await fetch(`${API}/signup`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, username, email, ph_number, age, password })
    });

    const data = await res.json();

    if (data.message) {
      showSuccess('signup-success', '🔥 Account created! Redirecting to login...');
      setTimeout(() => showPage('login'), 1500);
    } else {
      showError('signup-error', data.error || 'Signup failed. Please try again.');
    }
  } catch (e) {
    showError('signup-error', 'Could not connect to server. Make sure Flask is running.');
  }

  btn.disabled = false;
  btn.textContent = 'Start For Free';
}
