// Get the success alert  
var alertSuccess = document.getElementById("alertSuccess");

// Get alertText
var alertText = document.getElementById("alertText");

// Get the <span> element that closes the modal
var closeXBtn = document.getElementsByClassName("closeX")[0];

closeXBtn.onclick = function () {
    modal.style.display = "none";
}


// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Get the button save
var confirmBtn = document.getElementById("confirm-task")

confirmBtn.onclick = function () {
    modalContent.style.display = "none";
    alertSuccess.style.display = "block";
    alertText.innerHTML = "Task has been added!"
    setTimeout(() => { window.location.reload(true) }, 1500);
}

// Get the button cancel
var cancelBtn = document.getElementById("cancel-task")

cancelBtn.onclick = function () {
    modal.style.display = "none";
}
