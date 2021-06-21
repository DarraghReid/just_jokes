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

// display correct information on the confirm joke deletion modal - insert python url to carry out deletion
// arguments received from onclick function in both profile.html and jokes.html
function deleteModal(title, description, teller, id) {
  // store modal elements in variables
  let deleteTitle = document.querySelector(".delete-joke-title");
  let deleteDesc = document.querySelector(".delete-joke-description");
  let deleteTeller = document.querySelector(".delete-joke-teller");
  let link = document.querySelector(".delete-modal");

  // insert argument variables into modal
  deleteTitle.innerHTML = title;
  deleteDesc.innerHTML = description;
  deleteTeller.innerHTML = `Posted by: ${teller}`;
  link.setAttribute("href", `{{ url_for('delete_joke', joke_id=${id}) }}`)
}

// display correct information on the confirm user deletion modal - insert python url to carry out deletion
// arguments received from onclick function in users.html
function deleteUser(username, id, dob) {
  // store modal elements in variables
  let usernName = document.querySelector(".modal-username");
  let userId = document.querySelector(".modal-id");
  let dateOfBirth = document.querySelector(".modal-dob");
  let deleteLink = document.querySelector(".delete-user");

  // insert argument variables into modal
  usernName.innerHTML = `Username: ${username}`;
  userId.innerHTML = `ID: ${id}`;
  dateOfBirth.innerHTML = `DOB: ${dob}`;
  deleteLink.setAttribute("href", `{{ url_for('delete_user', user_id=${id}) }}`)
  
}

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