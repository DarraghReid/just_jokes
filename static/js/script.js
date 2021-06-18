// initialise Bootstrap tooltip functionality
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})


/*-----------------------------modals*/

// ensure correct information is displayed on modals
// arguments received from onclick function in both profile.html and jokes.html
function displayModal(title, description, teller) {

  // store modal elements in variables
  modalTitle = document.querySelector(".modal-joke-title");
  modalDesc = document.querySelector(".modal-joke-description");
  postedBy = document.querySelector(".modal-joke-teller");

  // store favourites modal elements in variables
  favmodalTitle = document.querySelector(".fav-modal-joke-title");
  favmodalDesc = document.querySelector(".fav-modal-joke-description");
  favpostedBy = document.querySelector(".fav-modal-joke-teller");

  // set innerHTML of modal elements to that of card elemets passed into displayModal()
  modalTitle.innerHTML = title;
  modalDesc.innerHTML = description;
  postedBy.innerHTML = `Posted by: ${teller}`;

  // set innerHTML of favourite modal elements to that of favourite card elemets passed into displayModal()
  favmodalTitle.innerHTML = title;
  favmodalDesc.innerHTML = description;
  favpostedBy.innerHTML = `Posted by: ${teller}`;
}


/*-----------------------------profile*/

// profile toggle
// set click event listeners on "See Favourites" and "Your Jokes" links, call profileToggle() function
document.querySelector(".see-own").addEventListener("mousedown", profileToggle);
document.querySelector(".see-favs").addEventListener("mousedown", profileToggle);

// See either user's favourites or user's own jokes at a time. "Your Jokes" is the default
function profileToggle(e) {
  // store "Your Jokes" and "Your Favourites" headings in variables
  let favsHead =  document.querySelector(".fav-jokes");
  let jokesHead = document.querySelector(".own-jokes");

  // store "Your Jokes" and "Your Favourites" sections in variables
  let favs =  document.querySelector(".user-favourites-container");
  let jokes= document.querySelector(".user-jokes-container");

  // ensure that only one heading at a time is displayed
  if (e.target.className == "see-own") {
    // if "Your Jokes" is showing, "Your Favourites" is hidden
    favsHead.style.display = "none";
    jokesHead.style.display = "block";

    // if "Your Favourites" is showing, "Your Jokes" is hidden
    favs.style.display = "none";
    jokes.style.display = "block";
  }
  // ensure that only the corresponding section of the heading is displayed
  else if (e.target.className == "see-favs") {
    // if user's favourite jokes are showing, their own jokes are hidden
    jokesHead.style.display = "none";
    favsHead.style.display = "block";

    // if user's own jokes are showing, their favourite jokes are hidden
    jokes.style.display = "none";
    favs.style.display = "block";
  }
}