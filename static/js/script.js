// initialise Bootstrap tooltip functionality
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})


/*-----------------------------modals*/

// ensure correct information is displayed on expand modals
// arguments received from onclick function in both profile.html and jokes.html
function displayModal(title, description, teller) {
  // store modal elements in variables
  let modalTitle = document.querySelector(".modal-joke-title");
  let modalDesc = document.querySelector(".modal-joke-description");
  let postedBy = document.querySelector(".modal-joke-teller");

  // store modal elements in variables - for favourites in profile.html
  let favTitle = document.querySelector(".fav-modal-joke-title");
  let favDesc = document.querySelector(".fav-modal-joke-description");
  let favdBy = document.querySelector(".fav-modal-joke-teller");

  // set innerHTML of modal elements to that of card elemets passed into displayModal()
  modalTitle.innerHTML = title;
  modalDesc.innerHTML = description;
  postedBy.innerHTML = `Posted by: ${teller}`;

  // set innerHTML of favourites modal elements to that of card elemets passed into displayModal()
  favTitle.innerHTML = title;
  favDesc.innerHTML = description;
  favdBy.innerHTML = `Posted by: ${teller}`;
}

function deleteModal(id) {
  // store modal anchor link in a variable
  let link = document.querySelector(".delete-modal");
  link.setAttribute("href", `{{ url_for('delete_joke', joke_id=${id}) }}`)
}

//{{ url_for('delete_joke', joke_id=joke._id) }}
/*-----------------------------profile*/

// profile toggle
// set click event listeners on "See Favourites" and "Your Jokes" links, call profileToggle() function
document.querySelector(".see-own")?.addEventListener("mousedown", profileToggle);
document.querySelector(".see-favs")?.addEventListener("mousedown", profileToggle);

// See either user's favourites or user's own jokes at a time. "Your Jokes" is the default
function profileToggle(e) {
  
  // store "Your Jokes" and "Your Favourites" sections in variables
  let favs =  document.querySelector(".user-favourites-container");
  let jokes= document.querySelector(".user-jokes-container");

  // ensure that only the corresponding section of the heading is displayed
  if (e.target.className == "see-favs") {

    // if user's own jokes are showing, their favourite jokes are hidden
    jokes.style.display = "none";
    favs.style.display = "block";

  }  
  else if (e.target.className == "see-own") {

    // if user's own jokes are showing, their favourite jokes are hidden
    favs.style.display = "none";
    jokes.style.display = "block";

  }
}