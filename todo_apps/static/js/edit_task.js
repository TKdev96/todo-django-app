// Beginning of js from edit_task.html

// Get the success alert  

var alertSuccess = document.getElementById("alertSuccess");

// Get alertTextSuccess

var alertText = document.getElementById("alertText");

// Get the deleted alert  

var alertDelete = document.getElementById("alertDelete");

// Get alertTextDeleted

var alertTextDelete = document.getElementById("alertTextDelete");

// Get Mark as compconsted checkbox

var checkbox = document.getElementById("flexCheckDefault");


// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Get the <span> element that closes the modal
var closeXBtn = document.getElementsByClassName("closeX")[0];

closeXBtn.onclick = function () {
    modal.style.display = "none";
}

// Get the button save
var saveBtn = document.getElementById("save-edit-task")

saveBtn.onclick = function () {
    if (checkbox.checked === true) {
        modalContent.style.display = "none";
        alertSuccess.style.display = "block";
        alertText.innerHTML = "Task has been completed!";
    } else {
        modalContent.style.display = "none";
        alertSuccess.style.display = "block";
        alertText.innerHTML = "Task has been updated!";
    }
    setTimeout(() => { window.location.reload(true) }, 1500);
}

// Get the button cancel
var cancelBtn = document.getElementById("cancel-task")

cancelBtn.onclick = function() {
    modal.style.display = "none";
}

// Get the button save
var deleteBtnPrevent = document.getElementById("delete-task-prevent");
var deleteBtn = document.getElementById("delete-task");

deleteBtnPrevent.onclick = function() {
    let confirmText = "Are you sure delete task?";
    if (confirm(confirmText) == true) {
            deleteBtn.style.display = "block";
            deleteBtnPrevent.style.display = 'none';
            setTimeout(() => {
                deleteBtn.click();
            }, 1000);  
            modalContent.style.display = "none";
            alertDelete.style.display = "block";
            alertTextDelete.innerHTML = "Task has been deleted!"
            setTimeout(() => { window.location.reload(true) }, 1500);
        }
    }



