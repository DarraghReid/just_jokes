# Testing

## Contents
* [Validation](#validation)
    * [W3C Markup Validator](#W3C-Markup-Validator)
    * [W3C CSS Validator Services](#W3C-CSS-Validator-Services)
    * [JSHint](#JSHint)
    * [Lighthouse](#lighthouse)
* [Testing User Stories](#Testing-User-Stories)
    * [First Time User Goals](#First-Time-User-Goals)
    * [Returning User Goals](#Returning-User-Goals)
    * [Site Owner Goals](#Site-Owner-Goals)
* [Testing Features](#Testing-Features)
    * [Navigation](#Navigation)
    * [Home Page Functionality](#Home-Page-Functionality)
    * [Hover Effects](#Hover-Effects)
    * [Click and Appear Functionality](#Click-and-Appear-Functionality)
    * [Removable Functionality](#Removable-Functionality)
    * [Moveable Functionality](#Moveable-Functionality)
    * [Resizable Functionality](#Resizable-Functionality)
* [Site Responsiveness](#Site-Responsiveness)
* [User Testing](#User-Testing)
* [Known Bugs and Issues Section](#known-bugs-and-issues)

## Validation

[W3C Markup Validator](https://validator.w3.org/), [W3C CSS Validator Services](https://jigsaw.w3.org/css-validator/),  [JSHint](https://jshint.com/) and [Pep8 Online](http://pep8online.com/) were used to validate this project's code and to make sure there were no syntax errors in the project.

[Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to test the site's performance.

### W3C Markup Validator
More information about issues that arose when validating my HTML can be found in the Problems section. As of writing, all errors have been resolved, and each HTML page passes throught the validator without any errors. However, they do come with the following warning: 
![W3C Markup Validator](static/images/heading-warning.png)

The W3C Markup Validator warned me that the flash section doesn't have a heading. The flash section extends from the base template. Therefore, all pages came with this warning, when validated. I inserted a heading into the flash section. However, the warning remained.


### W3C CSS Validator Services
CSS code from style.css passed through the [W3C CSS Validator Services](https://jigsaw.w3.org/css-validator/) without issue.
![W3C CSS Validator Services](static/images/css-validation.png)


### JSHint
[JSHint](https://jshint.com/) flagged 10 warnings, which related to use of ES6 syntax:
![JSHint](static/images/jshint-validation.png)

It also noted that the Bootstrap tooltip initialisation code included an undefined variable and an unused variable.

Finally, it marked by displayModal function as unused, perhaps because it is called inside the HTML using an onclick attribute.


### Pep8 Online
Python code from app.py passed through [Pep8 Online](http://pep8online.com/) without issue
![Pep8 Online](static/images/pep8-validation.png)


### Lighthouse
jokes.html, profile.html, users.html, add_joke.html, edit_joke.html, sign_in.html, and sign_up.html were all tested for performance using [Lighthouse](https://developers.google.com/web/tools/lighthouse).
The results were as follows:

#### Home Page
![Home Page](static/images/lighthouse-home.png)

#### Profile Page
![Profile Page](static/images/lighthouse-profile.png)

#### Users Page
![Users Page](static/images/lighthouse-users.png)

#### Add Joke Page
![Add Joke Page](static/images/lighthouse-add-joke.png)

#### Edit Joke Page
![Edit Joke Page](static/images/lighthouse-edit-joke.png)

#### Sign In Page
![Sign In Page](static/images/lighthouse-sign-in.png)

#### Sign Up Page

![Sign Up Page](static/images/lighthouse-sign-up.png)

## Testing User Stories
### First Time User Goals 
1. As a first time user, I want to immediately understand the purpose of the site.
* Upon loading of the site, jokes are immediately visible. Even if the user is logged in, intuitive icons allow to users to understand that they can interact with the jokes by liking and favouriting them. 

    A header informs them that they can sign in to carry out these interections and to see more jokes

2. As a first time user, I want to be able to easily navigate through the site to find what I'm looking for.
* A sticky navbar ensures that any page available to the user is never more than a click away. Pagination minimises scrolling for smartphone users

3. As a first time user, I want to instinctively know what to do in order to get started creating and interacting with jokes.
* Intuitive fontawesome icons ensure users immediately know what to do in order to being liking jokes, adding jokes to their favourites, and adding their own jokes to the site.

4. As a first time user, I want to be able to read jokes.
* All users, including those who have not signed in, immediately have a range of jokes to read upon entering the site.

5. As a first time user, I want to be able upload jokes.
* Jokes can be uploaded easily from the navbar "Add Joke" menu item, which is always visible to signed in users. Users can also click the "Add joke" icon beside the search bar on the Home page to carry out this action.

6. As a first time user, I want to be able to edit my jokes.
* If the user has uploaded a joke, the joke will have an edit icon displayed on its card. Upon clicking, it will lead the user to a form where they can edit the joke's details. All the user's jokes can be found in one place in the "Your Jokes" section of their Profile. 

    Admins can also edit any joke they see fit.

7. As a first time user, I want to be able to delete my jokes.
* If the user has uploaded a joke, the joke will have an delete icon displayed on its card. Upon clicking, it will trigger a modal that will ask the user to confirm the deletion. Upon, confirming, the joke will be removed from the database.. 

8. As a first time user, I want to be able to "like" jokes.
* All jokes, apart from jokes that have been uploaded by the user themselves (unless the user in an admin), will have a like/laughing face icon displayed on their cards. Upon clicking, the colour of the icon will change, indicating that the "like" was successful. 

    The joke will be updated in the database, where the user's name will be added to a MongoDB array that displays the names off all the user's who liked this joke. The "likes" count of the joke will also be incremented by 1 in the database.

    The action can be undone upon clicking the icon a second time.

9. As a first time user, I want to be able to add jokes to a list of my favourites.
All jokes, apart from jokes that have been uploaded by the user themselves (unless the user in an admin), will have an add to favourites/heart icon displayed on their cards. Upon clicking, the colour of the icon will change, indicating that the joke was successfully added to the user's list of favourites.. 

    The joke will be updated in the database, where the user's name will be added to a MongoDB array that displays the names off all the user's who have added this joke to their list of favourites. 
    
    All of the jokes in the user's list of favourites can be found in one place in the "Your Favourites" section of the user's profile.

    The action can be undone upon clicking the icon a second time.

10. As a first time user, I want to be able to search for specific jokes.
* The Home page includes a seach bar that will return jokes that match the input of the user. Only the joke title and joke description are searchable.


### Returning User Goals
1. As a returning user, I want to be immediately familiar with the layout of the site.
* New jokes may be added all the time, but the layout will always have that familiar CRUD functionality. User's should know exactly what to do in order to carry out interactions with the site upon returning.

2. As a returning user, I want to be able to upload new jokes.
* There is currently no limit the the amount of jokes a user can add. User's can add a joke whenever they are logged in.

3. As a returning user, I want to be able to access the jokes I have uploaded.
* All jokes that a user has uploaded can be found in the "Your Jokes" section of their profile.

5. As a returning user, I want to be able to access the jokes in my list of favourites.
* All jokes that a user has added to their list of favourites can be found in the "Your Favourites" section of their profile.

6. As a returning user, I want to be able to remove jokes from my list of favourites.
* If the user has added a joke to their list of favourites, this should be indicated by the "add to favourites" icon being yellow. Upon clicking the yellow icon, the joke is removed from their favourites.

7. As a returning user, I want to be able to "unlike" jokes.
If the user has liked a joke , this should be indicated by the "like" icon being yellow. Upon clicking the yellow icon, the joke is "unliked".


### Site Owner Goals
1. As the site owner/admin, I want to be able to have additional features available to me.
* The site owner, has complete control over the content of the site as well as the users who access it.

2. As the site owner/admin, I want to be able to see all jokes that have been uploaded by users.
* All jokes uploaded to the database are visible from the admin's account. 

3. As the site owner/admin, I want to be able to delete any joke on the platform that I see fit.
* The delete icon will be available to the admin on all jokes.

4. As the site owner/admin, I want to be able to edit any joke on the platform that I see fit.
* The edit icon will be available to the admin on all jokes.

5. As the site owner/admin, I want to be able to access the information of all users of the site.
* The admin can access the Users tab in the navbar where they can see all users that have signed up to the site.

6. As the site owner/admin, I want to be able to remove any user I see fit from the site.
* Each card displaying a user in the Users page will have a delete icon. When clicked, the user will be removed from the database.

7. As the site owner/admin, I want to be able to search for specific users.
* The Users page includes a seach bar that will return users that match the input of the admin. The username and the date of birth of the user are both searchable.

## Testing Features
### Features Available to Adult Users, Underage Users, and Admin Users
#### Base Template Features
The following tests were carried out on features available to all users, bar signed out users:

1. Click the logo and validate that it navigates to the Home page.
2. Click the Home button in the navbar and validate that it navigates to the Home page.
3. Click the Profile button in the navbar and validate that it navigates to the Profile page.
4. Click the Add Joke button in the navbar and validate that it navigates to the Add Joke page.
4. Click the logo in the the footer and validate that it navigates to the Home page.
4. Click the Facebook logo in the the footer and validate that it navigates to Facebook.
4. Click the YouTube logo in the the footer and validate that it navigates to YouTube.
4. Click the Instagram logo in the the footer and validate that it navigates to Instagram.
2. Click the Sign out button in the navbar and validate that it signs the user out navigates to the Sign In page.


#### Home Page Features
The following tests were carried out on features available to all users, bar signed out users:

1. Click the Add Joke icon in beside the search bar and validate that it navigates to the Add Joke page.
3. If the user is an adult or admin, check to see that all jokes are displaying on the page.
4. If the user is under 18 or the user is not signed, validate that only jokes marked suitable for children are displaying.
5. If the user is an adult or is under 18, locate a joke that has not been uploaded by the user and validate that the joke is displaying the "Like" and "Add to favourites" icons.
6. If the user is an adult or is under 18, locate a joke that has been uploaded by the user and validate that the joke is displaying the "Delete joke" and "Edit joke" icons.
7. If the user is under 18, validate that only jokes marked suitable for children are displaying.
8. Validate that each joke is displaying the correct information.
9. If the joke is over 50 characters, validate that the joke is displaying a truncated version of the joke discription.
10. Click the "Expand" button and validate that:
    * A modal is triggered displaying the joke's details in full
    * The modal is canceled by clicking the cancel button in the top right of the modal
    * The modal is canceled by clicking outside of the modal
11. If the user is an admin, locate any joke that has not been liked, or, if the user is not an admin, locate a joke that has not been added by the user and has not been liked. Click the "Like" icon and verify:
    * That the page redirects to back to the Home page.
    * That a flash message displays "You've liked this joke!" at the top of the page.
    * That the joke's "likes" field in MongoDB has been incremented by 1.
    * That the user's name has been added to the joke's "liked_by" array field in MongoDB.
    * That the colour of the "Like" icon has changed to yellow.
12. Choosing the same joke as before, click the "Unlike" icon and verify:
    * That the page redirects back to the Home page.
    * That a flash message display "You've unliked this joke" at the top of the page.
    * That the joke's "likes" field in MongoDB has been decremented by 1.
    * That the user's name has been removed from the joke's "liked_by" array field in MongoDB.
    * That the colour of the "Add to favourites" icon has changed back to black.
13. If the user is an admin, locate any joke that has not been added to the user's favourites, or, If the user is not an admin, locate a joke that has not been added by the user and has not been added to the user's favourites. Click the "Add to favourites" icon and verify:
    * That the page redirects to back to the Home page.
    * That a flash message displays "Joke favourited!" at the top of the page.
    * That the user's name has been added to the joke's "favouriters" array field in MongoDB.
    * That the colour of the "Add to favourites" icon has changed to yellow.
14. Choosing the same joke as before, click the "Remove from favourites" icon  and verify:
    * That the page redirects back to the Home page.
    * That a flash message display "Joke removed from your favourites" at the top of the page.
    * That the user's name has been removed from the joke's "favouriters" array field in MongoDB.
    * That the colour of the "Add to favourites" icon has changed back to black
15. If the user is not an admin, locate a joke that has been uploaded by the user, click the "Delete joke" icon and verify:
    * That a confirmation modal is triggered, asking the user if they are sure they want to delete the joke.
    * That the modal displays the joke details.
    * That the modal provides "Cancel" and "Delete" buttons.
    * That the "Cancel" button closes the modal.
    * That the "Delete" button:
        * Removes the joke from the database
        * Redirects back to the Home Page
        * Displays the flash message "Joke removed" at the top of the page
16. If the user is an admin, locate any joke, or, if the user is not an admin, locate a joke that has been uploaded by the user. Click the "Edit joke" icon and verify:
    * That it redirects to the Edit Joke page.
17. Type a word found in a joke into the search bar and validate that a the corresponding joke is returned below upon clicking "Search".
18. Click "Clear" and verify that it redirects back to the Home page.

#### Profile Page Features
The following tests were carried out on features available to all users, bar signed out users:

1. Validate that the user's username is displayed at the top of the page.
1. Validate that a dropdown menu is displayed beneath the username.
1. Validate that the dropdown menu contains:
* See favourites
* See your Jokes
* Sign out
1. Validate that, upon clicking "See favourites":
    * The jokes in the user's favourites list are displayed below
    * The correct information is displayed on the jokes
    * The "Like" and "Add to favourites" icons are displayed on the joke card
1. Validate that, upon clicking "See your jokes":
    * The jokes the user has uploaded are displayed below
    * The correct information is displayed on the jokes.
    * The "Delete joke" and "Edit joke" icons are displayed on the jokes.
1. Validate that, upon clicking "Sign out":
    * The user is signed out and redirected to the Sign In page.
    * A flash displays the message "Signed out" at the top of the page
9. If the joke is over 50 characters, validate that the joke is displaying a truncated version of the joke discription.
10. Click the "Expand" button and validate that:
    * A modal is triggered displaying the joke's details in full
    * The modal is canceled by clicking the cancel button in the top right of the modal
    * The modal is canceled by clicking outside of the modal
11. Under "Your Favourites", if any jokes are present, locate any joke that has not been liked. Click the "Like" icon and verify:
    * That the page redirects to back to the Home page.
    * That a flash message displays "You've liked this joke!" at the top of the page.
    * That the joke's "likes" field in MongoDB has been incremented by 1.
    * That the user's name has been added to the joke's "liked_by" array field in MongoDB.
    * That the colour of the "Like" icon has changed to yellow.
14. Under "Your Favourites" "Remove from favourites" icon and verify:
    * That the page redirects back to the Home page.
    * That a flash message display "Joke removed from your favourites" at the top of the page
    * That the user's name has been removed from the joke's "favouriters" array field in MongoDB
    * That the colour of the "Add to favourites" icon has changed back to black
    * That the joke no longer appears under "Your Favourites"
15. Under "Your Jokes", if jokes are present, locate any joke. Click the "Delete joke" icon and verify:
    * That a confirmation modal is triggered, asking the user if they are sure they want to delete the joke.
    * That the modal displays the joke details.
    * That the modal provides "Cancel" and "Delete" buttons.
    * That the "Cancel" button closes the modal.
    * That the "Delete" button:
        * Removes the joke from the database
        * Redirects back to the Home Page
        * Displays the flash message "Joke removed" at the top of the page
    * That the joke no longer appears under "Your Jokes"
16. Under "Your Jokes", if jokes are present, locate any joke. Click the "Edit joke" icon and verify:
    * That it redirects to the Edit Joke page.

#### Add Joke Page Features
1. Validate that a form appears upon loading the page.
2. Validate that the form has the following fields:
    * Joke Title
    * Joke
    * Image URL
    * Suitable for children switch
3. Fill in the form with invalid information and validate the form does not submit:
    * Valid information for Joke Title:
        * minlength="3" maxlength="20"
    * Valid information for Joke Description:
        * minlength="4" maxlength="200"
    * Valid information for Image URL:
        * Currently no validation, but must be filled out.
4. Fill out the form with correct information and validate:
    * That the page redirects back to the Add Joke page
    * That a flash message displaying "Joked Added!" appears at the top of the page
    * That the joke appears somewhere in the Home page
    * That the joke appears under "Your Jokes" in the user's profile.
5. Fill out the form and click "Cancel" and verify that the form resets"
6. Upload two jokes, one with the Suitable for children switch "on", and one with the Suitable for children switch "off". Verify that:
    * Both jokes are visible when signed into an adult account.
    * The joke with the Suitable for children switch set to "off" is not visible when signed into an account that belongs to a user under 18 years of age.

#### Edit Joke Page Features
1. Validate that a form appears upon loading the page.
2. Validate that the form has the following fields:
    * Joke Title
    * Joke
    * Image URL
    * Suitable for children switch
1. Validate that the above fields are populated with the details of the joke that was clicked.
1. Click "Cancel" and verify that it redirects to the Home page.
3. Edit the pre populated fields, press "Clear" and validate that the form resets.
3. Edit the pre populated fields, press "Edit" and validate that:
    * It redirects to the Home page.
    * The joke appears somewhere in the Home page with its details changed.
    * The joke appears in "Your Jokes" in the user's profile with its details changed.

#### Sign In Page Features
1. Validate that a form appears upon loading the page.
2. Validate that the form has the following fields:
    * Usersname
    * Password
1. Validate that there is a solitary "Sign in" button below the form.
1. Validate that there is a link that leads to the "Sign up" page below that "Sign in" button.
3. Fill out the form with invalid details and verify that:
    * The page reloads
    * A flash message displaying "Incorrect username and/or password" appears at the top of the page.
4. Fill out the form with valid details and validate that:
    * It redirects to the user's profile
    * A flash message displaying "Welcome, 'username'" appears at the top of the page.

### Features Specific to Admin
The following tests were carried out on features specific to the admin:

1. On the Home page, click the "Users" tab on the navbar and validate that it navigates to the Users Page.
2. On the Home page, validate that all jokes display all options available to the admin; "Like", "Add to favourites", "Delete joke", "Edit joke".
3. On the Users page, check to see that all users are displaying.
4. On the Users page, click the "Delete user" icon and validate that a confirmation modal appears.
5. After the confirmation modal appears, click the cancel button and validate that the action is canceled.
6. Click the "Delete user" icon again, and this time click the delete button. Validate that the user is removed from the database, that the flash message "User removed" appears at the top of the screen and that the user is redirected back to the User's page.
7. On the Users page, type a username into the search bar and validate that a matching user is returned below.
8. On the Users page, type a date into the search bar and validate that users matching that date of birth are returned below.
9. Click "Clear" and verify that it redirects back to the Users page.

### Features Specific to Not-Signed-In Users:
1. Validate that the only options in the navbar are:
    * Home
    * Sign in
    * Sign up

#### Home Page
2. Validate that all jokes displaying have their for_children field in the database set to "on".
3. Locate any joke:
    * Click the "Expand" button and validate that:
        * It triggers a modal
        * The modal displays the message: "Want to see the full joke?"
        * The modal provides a "Sign in" button that leads to the Sign in page
        * The modal provides a "Nah" button that closes the modal
        * The modal closes when the close button at the top right hand corner of the modal is clicked
        * The modal closes when anywhere outside of the modal is clicked
    * Click the "Like" button and validate that:
        * It triggers a modal
        * The modal displays the message: "Sign in the like this joke"
        * The modal provides a "Sign in" button that leads to the Sign in page
        * The modal provides a "Nah" button that closes the modal
        * The modal closes when the close button at the top right hand corner of the modal is clicked
        * The modal closes when anywhere outside of the modal is clicked
    * Click the "Add to favourites" button and validate that:
        * It triggers a modal
        * The modal displays the message: "Sign in to favourite this joke"
        * The modal provides a "Sign in" button that leads to the Sign in page
        * The modal provides a "Nah" button that closes the modal
        * The modal closes when the close button at the top right hand corner of the modal is clicked
        * The modal closes when anywhere outside of the modal is clicked

#### Sign Up Page
1. Validate that a form appears upon loading the page.
2. Validate that the form has the following fields:
    * Username
    * Password
    * Date of birth
3. Fill in the form with invalid information and validate the form does not submit:
    * Valid information is outlined in form labels for Username and Password
    * No specific validation is implemented, this will be addressed in future versions.
4. Fill out the form with correct information and validate:
    * That the page redirects to the Home page
    * That a flash message displaying "You're sign up!" appears at the top of the page

### Features Specific to Smaller Screens
1. Click the burger icon to validate that the navigation links drop down.
2. Validate that the dropdown menu displays the same menu items and the menu on larger screens.
3. Validate that all menu items work correctly

### Other Features
1. Validate that, if there are more than 8 items to be displayed, they will be paginated, with a maximum of 8 items being displayed at a time.

The above tests were carried out on both smaller and larger screens and resulted in a pass.

![Navigation Links](assets/images/testing-imgs/burger.png)

* On the Home Page, click to logo and validate that it navigates to the Home page.
* On the Home Page, click the "Home" button in the menu and validate that it navigates to the Home Page.

* On the Home Page, on smaller screens, click the burger icon to validate that the navigation links drop down.
* On the Home Page, on smaller screens, click the burger icon, then click the "Home" button and validate that it navigates to the Home Page.
* On the Home Page, on smaller screens, click the burger icon, then click the "Design" button and validate that it navigates to the Studio.
* In the footer, click the logo and validate that it navigates to the Home Page.
* In the footer, click the "back to top" button and validate that it navigates to the Home Page.

    Each of the above tests resulted in a pass.

### Home Page Functionality

![Swoop Functionality](assets/images/testing-imgs/swoop-1.png)

* Load the page and validate that the elements of the Home Page are brought onto the screen in stages.

    The above test resulted in a pass.

### Hover Effects

![Logo](assets/images/testing-imgs/feat-logo-1.png)

![Back-to-top ](assets/images/testing-imgs/feat-top-1.png)

![Menu](assets/images/testing-imgs/menu-hover-1.png)
![Item](assets/images/testing-imgs/item-hover-1.png)

* On the Home Page, hover over the logo and validate that it dulls to the expected rgb(201, 197, 197) colour.
* On the Home Page, hover over the "Home" button and validate that it dulls to the expected rgb(201, 197, 197) colour.
* On the Home Page, hover over the "Design" and validate that it dulls to the expected rgb(201, 197, 197) colour.
* On the Home Page, hover over the "Design Your Eden" call-to-action button and validate that it changes its background image to "linear-gradient(to bottom right, rgb(68, 153, 94), rgb(0, 105, 78) 75%)".
* On the Home Page, on smaller screens, tap the burger icon and validate that it dulls to the expected rgb(201, 197, 197) colour.
* On the Home Page, on smaller screens, tap the "Home" button and validate that it dulls to the expected rgb(201, 197, 197) colour.
* On the Home Page, on smaller screens, tap the "Design" button and validate that it dulls to the expected rgb(201, 197, 197) colour.
* On the Home Page, on smaller screens, tap the "Design Your Eden" call-to-action button and validate that it changes its background image to "linear-gradient(to bottom right, rgb(68, 153, 94), rgb(0, 105, 78) 75%)".
* In the Studio, hover over each of the menu items, and validate that the label and image overlay appear.
* In the Studio, hover over an image on the canvas and validate that the border, and ".mover" divs appear.
* In the Studio, hover over the ".tl", ".tr", ".bl" and ".br" divs and validate that the appropriate cursor appears
* In the Studio, on smaller screens, tap an image on the canvas and validate that the border, and ".mover" divs appear.
* In the Studio, on smaller screens, tap each of the menu items, and validate that the label and image overlay appear.
* In the footer, hover over the logo and validate that it dulls to the expected rgb(201, 197, 197) colour.
* In the footer, hover over the "back-to-top" button and validate that it dulls to the expected rgb(201, 197, 197) colour.
* In the footer, on smaller screens, tap the logo and validate that it dulls to the expected rgb(201, 197, 197) colour.
* In the footer, on smaller screens, tap the "back-to-top" button and validate that it dulls to the expected rgb(201, 197, 197) colour.

    Each of the above tests resulted in a pass.

### Click and Appear Functionality

![Click-and-Appear](assets/images/testing-imgs/click-appear.png)

* In the studio, click each of the menu items and validate the the image of the clicked menu item appears on the canvas below.
* In the studio, on smaller screens, tap each of the menu items and validate the the image of the clicked menu item appears on the canvas below.

    Both of the above tests resulted in a pass.

### Removable Functionality 

![Removable](assets/images/testing-imgs/removable.png)

* In the studio, click the cancel/delete icon on an image on the canvas and validate that it is removed from the canvas.
* In the studio, on smaller screens, tap the cancel/delete icon on an image on the canvas and validate that it is removed from the canvas.

    Both of the above tests resulted in a pass.

### Moveable Functionality 

![Moveable](assets/images/testing-imgs/moveable.png)


* In the Studio, click and drag an image on the canvas and validate that it moves along with the cursor.
* In the Studio, on smaller screens, tap and drag an image on the canvas and validate that it moves along with your finger.

    Both of the above tests resulted in a pass.

    NOTE: 
    * The image makes an initial "jump" downwards before it follows the direction of the cursor/finger.
    * When clicking an image that is placed on top of another image, it can happen that the "mouseup"/"touchend" functionality is not registered. In this case, the user must tap or click anywhere on the screen to stop the image from following the cursor/finger.

### Resizable Functionality 

![Resizable](assets/images/testing-imgs/resizable.png)

* In the studio, click and drag each of the ".tl", ".tr", ".bl" and ".br" divs of an image on the canvas and verify that the image resizes along with the movement of the cursor.
* In the studio, on smaller screens, tap and drag each of the ".tl", ".tr", ".bl" and ".br" divs of an image on the canvas and verify that the image resizes along with the movement of your finger.

    Both of the above tests resulted in a pass.

## Site Responsiveness

![Responsive](assets/images/testing-imgs/responsive-1.png)

[Eden](https://darraghreid.github.io/eden/) was tested across a range of devices and internet browsers to assess the responsiveness of the site. The site was also tested on all available devices in Google Dev Tools to ensure it was visually appropriate on all screen sizes.

NOTE:
* Each element in the Home Screen has its own transition period set in [style.css](assets/css/style.css). Please allow a few seconds for each element to transition to its appropriate size and position when inspecting it Dev Tools.

The site was tested on the following devices: 

* MacBook Pro (Retina, 13-inch, Early 2015)
* iPhone 8 Plus
* Samsung Galaxy S10
* Huawei LYO-L01
* Windows 10(desktop)
* iPad Air

And on the following browsers: 

* Google Chrome 
* Safari 
* Opera 
* Samsung Internet

## User Testing

The site was tested by the landscape gardening student who inspired the idea for the site. He appreciated the simplicity of the site, its accessibility, that the software uses coloured elements, and noted that there would be demand for such software.

The site was also tested by members of the Slack community who also expressed appreciation for the project and confirmed some bugs that had been appearing. For more details on bugs, please see the [Known Bugs and Issues Section](#known-bugs-and-issues).

## Known Bugs and Issues

* The biggest and most persistent bug encountered in this project involved some CSS and JS features and functionality not working on Apple Devices (specifically Safari on Mac, all browsers on iPad and iPhone). When the page loaded on one of these devices, the images of the Home Page were already on the screen and did not transition on from outside of the viewport. Also, in the Studio, the images wouldn't appear on the canvas when the menu items were clicked.

    To remedy this, I used [Autoprefixer](http://autoprefixer.github.io/) to add prefixes to my CSS to ensure that my code was as readable on all browsers as possible. I also transpiled my code to ES5 using [babel](https://babeljs.io/) to ensure that my JavaScript code was maximally readable across all browsers. Neither of these fixes worked.

    I consulted my mentor, tutor support, the Slack community and Apple Support multiple times. I also posted in Apple developer forums and consulted other developers. I was unsuccessful in finding an answer. After about a week and a half of failed attempts to address the bug, I finally solved the issue.

    The bug turned out to be two separate issues. The first issue seems to be that the "load" event listener that was put on each of the elements in the home page wasn't being read on Mac browsers. The .swoop class, which is designed to bring the elements onto the page was automatically being added to the elements, before the "load" event listener was read. To address this, I put all of the code associated with the Home Page functionality into a setTimeout() function, with a 500ms timeout. The issue was resolved after this.

    The second issue had to do with how I was targeting elements in my functions. I was using the path property of events to target specific elements (eg: el = e.path[1]). It turns out that events in Safari don't have the path property. Instead, I used properties such as srcElement and offsetParent to target elements. This resolved the issue.

* Another issue involved the resize() function. After initially completing the resize() function, I realised that all of the images on the canvas would be resized along with the image that was being targeted. To remedy this, I specifically set the element to e.target.parentElement.

* While this next bug didn’t affect the function it was located, move(), it prevented the function that followed it. resize(), from running, which is how I discovered it. After writing the resize() function and not being able to make it work, I checked the console for errors. One error that repeatedly popped up was that moveImg and rectVal could not be read. 
    
    Although this didn’t affect the running of the function in which it was located, I tried to remedy it to see if it would help the resize() function to work. I nested my if statements inside the onContact() function (which is inside the move() function). After this, the resize() function began to work.

![mouse touch bug](assets/images/testing-imgs/mouse-touch.png)

* The insertImg() function caused an issue on smaller screens where two images were being inserted onto the canvas at once. This was because the browser was registering both "mousedown" and "touchend" events. I thought it would be possible to simply insert the || operator in the if statement so the browser would choose one or the other. In the end I had to write the following code to erase the bug.

* Another persistent bug arose in the resize() function. The images would not resize on touch screens. I realised that I had to create separate variables for the cursor position and finger position. After much trial and error, the following code succeeded in creating separate variables for both the cursor and finger.

* An early bug that I discovered was the moveable functionality not working on the elements inserted into the canvas. I quickly discovered that this was because the JavaScript code had been read before these new elements had been inserted into the DOM. To remedy this, I called the move() and resize() functions inside the insertImg() function so the JavaScript code would run on the new elements.

![Cursor Finger Bug](assets/images/testing-imgs/cursor-finger.png)

* A bug where the #canvas element moved when trying to resize an image was caused by the user selecting the border of the .img-container, rather than a .mover element. This meant that the moveImg variable in the onContact() function became the canvas. To remedy this. I removed "e.target.className == "img-container" from the "if(e.target.className == "canvas-img" || e.target.className == "img-container")" condition. This issue was resolved.

    See [index.js](assets/js/index.js) for more details on the onContact() function.

![Border bug](assets/images/testing-imgs/border.png)
