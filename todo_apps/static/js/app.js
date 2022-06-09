// Beginning js from base.html

//Get hamburger menu 
const hamburgerMenuIcon = document.getElementById("hamburgerMenuIcon");
const hambugerMenu = document.getElementById("navbarsExampleDefault");
const closeBtn = document.getElementById("closeBtn");
const formBg = document.querySelector(".formBg");


hamburgerMenuIcon.onclick = function () {
    hamburgerMenuIcon.style.display = 'none';
    hambugerMenu.style.display = "block";
    closeBtn.style.display = 'block';
};

closeBtn.onclick = function () {
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


document.body.addEventListener('htmx:configRequest', (e) => {
    e.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';
});
// End of js from base.html


// Beginning js from tasks / all_tasks / completed_tasks

// Get the modal
var modal = document.getElementById("myModal");

var modalContent = document.getElementById("dialog");

// Get the button that opens the modal
var btn = document.getElementsByClassName("myBtn");


// When the user clicks the button, open the modal 
for (var i = 0; i < btn.length; i++) {
    btn[i].onclick = function () {
        modal.style.display = "block";
    };
};
// End of js from tasks / all_tasks / completed_tasks

//active nav-bar-link
const myTasks = document.getElementById("my_tasks");
const allTasks = document.getElementById("all_tasks");
const completedTasks = document.getElementById("completed_tasks");

window.onload = function () {
    let url = window.location.pathname;
    if (url === "/tasks/") {
        myTasks.style.fontWeight = '700';
        myTasks.style.color = "black";
    } else if (url === "/all_tasks/") {
        allTasks.style.fontWeight = '700';
        allTasks.style.color = "black";
    } else if (url === "/completed_tasks/") {
        completedTasks.style.fontWeight = '700';
        completedTasks.style.color = "black";
    }
};
