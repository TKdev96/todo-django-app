//Get hamburger menu 
const hamburgerMenuIcon = document.getElementById("hamburgerMenuIcon");
const hambugerMenu = document.getElementById("navbarsExampleDefault");
const closeBtn = document.getElementById("closeBtn");
const formBg = document.getElementById('formBg');


hamburgerMenuIcon.onclick = function () {
  hamburgerMenuIcon.style.display = 'none';
  hambugerMenu.style.display = "block";
  closeBtn.style.display = 'block';
};

closeBtn.onclick = function closeBtnFunc() {
  hambugerMenu.style.display = 'none';
  closeBtn.style.display = 'none';
  hamburgerMenuIcon.style.display = 'block';
};


formBg.onclick = function () {
  if (hambugerMenu.style.display === 'block') {
    hambugerMenu.style.display = "none";
    closeBtn.style.display = 'none';
    hamburgerMenuIcon.style.display = 'block';
  };
};

// Get the success alert  
var alertSuccess = document.getElementById("alertSuccess");
// Get alertTextSuccess
var alertText = document.getElementById("alertText");

function reloader() {
  alertSuccess.style.display = "block";
  alertText.innerHTML = "Profile has been updated!";
  setTimeout(() => { window.location.reload(true) }, 3000);
}

document.body.addEventListener('htmx:configRequest', (e) => {
  e.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';
  })