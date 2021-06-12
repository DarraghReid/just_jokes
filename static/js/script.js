// initialise Bootstrap tooltip functionality
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

// add click event listener on card expand buttons, call display modal function
let expandBtns = document.querySelectorAll(".expand");
expandBtns.forEach(expandBtn => expandBtn.addEventListener("click", displayModal));

// add click event listener on modal exit button & background, call hide modal function
document.querySelector(".exit").addEventListener("click", hideModal);
document.querySelector(".modal-bg").addEventListener("click", hideModal);

// display modal to user, display info specific to clicked card
function displayModal() {
  let display = document.querySelector(".modal-bg");
  display.style.display = "flex";

  // elements displayed on card
  //cardImg = document.querySelector(".card-img-top");
  cardTitle = document.querySelector(".card-title");
  cardDesc = document.querySelector(".alt-desc");
  cardUser = document.querySelector(".teller");

  // corresponding elements displayed on modal
  modalTitle = document.querySelector(".modal-title");
  modalDesc = document.querySelector(".modal-text");
  modalUser = document.querySelector(".modal-user");

  // insert card info into modal elements
  modalDesc.innerHTML = cardDesc.innerHTML;
  modalTitle.innerHTML = cardTitle.innerHTML;
  modalUser.innerHTML = cardUser.innerHTML;
}

// hide modal
function hideModal() {
  let hide = document.querySelector(".modal-bg");
  hide.style.display = "none";
}