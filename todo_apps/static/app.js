 // Get the <span> element that closes the modal
 var span = document.getElementsByClassName("close")[0];
        
 // When the user clicks on <span> (x), close the modal
 span.onclick = function() {
   modal.style.display = "none";
 }
 
 // When the user clicks anywhere outside of the modal, close it
 window.onclick = function(event) {
   if (event.target == modal) {
     modal.style.display = "none";
   }
 }

 // Get the button save
 var saveBtn = document.getElementById("save-edit-task")

 saveBtn.onclick = function() {
     setTimeout(() => {window.location.reload(true)}, 10);
 }

 // Get the button save
 var cancelBtn = document.getElementById("cancel-task")

 cancelBtn.onclick = function() {
     modal.style.display = "none";
 }

// Get the button save
 var deleteBtn = document.getElementById("delete-task")

 deleteBtn.onclick = function() {
     setTimeout(() => {window.location.reload(true)}, 10);
 }
