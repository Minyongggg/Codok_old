//////////////////////bbModal/////////////////////////////////

// Get the modal
var bbmodal = document.getElementById("bbModal");

// Get the button that opens the modal
var bbbtn = document.getElementById("bbBtn");

// Get the <span> element that closes the modal
var bbspan = document.getElementsByClassName("cancle")[0];

// When the user clicks on the button, open the modal
bbbtn.onclick = function() {
  bbmodal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
bbspan.onclick = function() {
  bbmodal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == bbmodal) {
    bbmodal.style.display = "none";
  }
}
///////////////////////////////////////////////////////////////

////////////////////////myModal/////////////////////////////
// Get the modal
var mymodal = document.getElementById("myModal");

// Get the button that opens the modal
var mybtn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var myspan = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
mybtn.onclick = function() {
  mymodal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
myspan.onclick = function() {
  mymodal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == mymodal) {
    mymodal.style.display = "none";
  }
}