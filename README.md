## Contents
* [Introduction](#Eden)
* [UX](#UX)
    * [User Stories](#User-Stories)
        * [First Time User Goals](#First-Time-User-Goals)
        * [Returning User Goals](#Returning-User-Goals)
        * [Site Owner Goals](#Site-Owner-Goals)
* [Structure](#Structure)
* [Design](#Design)
* [Wireframes](#Wireframes)
    * [Differences Between Wireframes and Final Product](#Differences-Between-Wireframes-and-Final-Product)
* [Features](#Features)
    * [Home Page](#Home-Page)
    * [Studio Section](#Studio-Section)
    * [Footer](#Footer)
    * [Potential Future Features](#Potential-Future-Features)
* [Technologies Used](#Technologies-Used)
    * [Languages Used](#Languages-Used)
    * [Frameworks, Libraries & Programs Used](#Frameworks-,-Libraries-&-Programs-Used)
* [Testing](#Testing)
* [Deployment](#Deployment)
    * [Project Creation](#Project-Creation)
    * [GitHub Pages](#GitHub-Pages)
    * [Forking the GitHub Repository](#Forking-the-GitHub-Repository)
    * [Run Locally](#Run-Locally)
* [Credits](#Credits)
    * [Code](#Code)
    * [Content](#Content)
    * [Media](#Media)
    * [Acknowledgements](#Acknowledgements)

# Eden

![Eden Wbsite](static/images/amiresponsive.png)

View the live project [here](http://just-jokes.herokuapp.com/get_jokes)

This website was created for Code Institute's Milestone 3 Project as part of the Diploma in Full Stack Web Development. The purpose of this project is to demonstrate the student's knowledge and skills acquired thus far in the course. This includes skills in HTML, CSS, JavaScript, Python, Flask as well as other technologies as outlined in the [Technologies Used](#Technologies-Used) section. The focus of this project is to demonstrate the student's ability to carry out CRUD functionality
This project marks the developer's first time writing Python and working with databases.

The purpose of this site is to provide users with a platform on which they create, read, update, and delete jokes. These features, as well as other features. such as liking jokes and adding jokes to favourites will be discussed in the [Features](#Features) section of this README.md. I decided that using jokes was fun way to explore CRUD functionality. With myself in mind as the site owner/admin, I began creating user stories.

## UX
### User Stories

#### First Time User Goals 
1. As a first time user, I want to immediately understand the purpose of the site.
2. As a first time user, I want to be able to easily navigate through the site to find what I'm looking for.
3. As a first time user, I want to instinctively know what to do in order to get started creating and interacting with jokes
4. As a first time user, I want to be able to read jokes.
5. As a first time user, I want to be able upload jokes.
6. As a first time user, I want to be able to edit my jokes.
7. As a first time user, I want to be able to delete my jokes.
8. As a first time user, I want to be able to "like" jokes.
9. As a first time user, I want to be able to add jokes to a list of my favourites.

#### Returning User Goals
1. As a returning user, I want to be immediately familiar with the layout of the site.
2. As a returning user, I want to be able to upload new jokes.
3. As a returning user, I want to be able to access the jokes I have uploaded.
5. As a returning user, I want to be able to access the jokes in my list of favourites.
6. As a returning user, I want to be able to remove jokes from my list of favourites.
7. As a returning user, I want to be able to "unlike" jokes.

#### Site Owner Goals
1. As the site owner, I want to be able to design gardens in real time for potential customers.
2. As the site owner, I want to be able to carry out all of the operations available to users.
3. As the site owner, I want to be able to carry additional operations than other users.
4. As the site owner, I want to be able to carry out all operations on all jokes, even if they are not my own.
5. As the site owner, I want to be able to be able to access information on all users.
6. As the site owner, I want to be able to be able to remove users from the platform, at my own discretion.
7. As the site owner, I want to be able to be able to restrict access to users who are under 18 years of age.
8. As the site owner, I want to be able to be able to restrict access to users who are not signed in or registered.

## Structure
JustJokes includes 10 web pages, with some pages being more versatile and able to show a variety of information depending on the user's age, account type, and preferences. All web pages inhered html, head, and body elements from a base.html template using jinja. They also inherit the navbar and footer from base.html.

    A fixed navbar ensures that all pages available to the specific user are never more than a click away. It also assits users on smaller devices to avoid exessive scrolling when navigating the site. Pagination has also been implemented to reduce scrolling for users. More on what each page does and how it functions will be discussed in the [Features](#Features) of the README.md.

## Design
* Colour Scheme
    * The colourscheme of the site was kept relatively simple. Because most pages were going to be data-focused, I didn't want the colourscheme to distract the user or cause further clutter.

        The colours used in the site were black, white, and variables of rgb(245, 180, 60), rgb(245, 188, 31), and rgb(245, 180, 60). 
        
        I found this orang/yellow colour suited the fun concept of JustJokes The background of each web page of this site in a linear gradient of these three RGB colours. I felt the linear gradient gave the site a bit more depth, making it slightly easier on the eye.

        Black is the main contrasting colour throughout the site. It tames the vibrancy of the orange/yellow and makes a good colour for headings and navigations elements.

        A slightly dulled white was used for the card elements, inut elements and in buttons.

        I used [coolers.co](https://coolors.co/) as a starting off point for choosing the colours

    ![colour palette](static/images/coolers.png)

* Typography
    * The dominant font I chose for JustJokes was Noto Sans. I feel it gave the typography of the site a distinctive, but not distracting, look.

        The font was sourced from [Google Fonts](https://fonts.google.com/)

* Imagery
    * the only images displayed on the site are uploaded by users themselves and are displayed alongside the uploaded joke in a card format.

    * Images are uploaded to the site via url, using the image url input in the "Add Joke" form. Having users add images to their jokes adds an extra fun element. It makes the user experience more enjoyable and makes the site more interesting. Memes are also very popular in other social media websites.

        The images are chosen at the discretion of the user. The user is, however, instructed to ensure that the image is somewhat related to the joke. This can be moderated by the admin, who can remove jokes at their discretion.

## Wireframes
* Wireframe of Home Page
![Wireframe of Home Page](static/images/jj-wireframes.png)

* Wireframe of Studio
![Wireframe of Studio](assets/images/readme-imgs/wireframe-studio.png)

* Wireframe of Tutorial Section (Not included in final product)
![Wireframe of Studio](assets/images/readme-imgs/wireframe-tutorial.png)

### Differences Between Wireframes and Final Product
* On the home screen, I decided to omit the sort by dropdown as I didn't feel it would contribute to the project according to the guidelines set out in the Assessment Handbook. Also, I had already included a dropdown in the Profile page where users are presented with a range of options.

* Having dropped the dropdown, I decided I would include the number of user's who had liked a particular joke in the card display. This feature adds to the UX of the site.

* I had orginally planned on manipulating the card to show the full joke, if the joke's characters exeeded the characters able to be displayed on the card. I felt a modal displaying the full joke would be a better design a lead to a better user experience. Bootstrap modals are a prominant feature throughout the site.

* As discussed above, the links to toggle between the user's uploaded jokes and the user's favourite jokes, were replaced with a dropdown menu with the additional option to sign out. I felt this was more of an intuitive layout that users would be used to from social media platforms.

* Icons were omitted from the forms. I had intentionally left them to do if I had time, as I didn't think they were very important. In the end, time didn't allow to include them.

* In sign in form, instead of a switch indicating whether the user was an adult or not, I opted for a calandar input. I sliced the information I needed from the user's DOB string and calculated their ages. Different features are available to users based on their age, as will be discussed in the [Features](#Features) section.

## Features
    Different features are available to users based on their age and the type of account they have, ie; a general user, or an admin. I will discuss these features in relation to these criteria.

#### Admin

* All features are available to the admin. The Home, Profile, Users, Add Jokes, and Sign Out pages are visible on the admin's navbar.

* On the Home page, the admin can see all jokes that are stored in the jokes collection in mongo db. The jokes are displayed on Bootstrap cards that display detail of the joke including the image, title, description, who posted the joke, and the number of likes it has.

    They can like, unlike, add to favourites, remove from favourites, edit, and delete any joke they choose, without restriction. Liking the joke will add 1 to the "likes" field of the joke and add the user's name to the list of other users who liked the array, which is the joke's "liked_by" array field in the database. Unliking the joke will reverse this action

    Adding a joke to the user's favourites will result in the user's name being added to a list of other users who added the joke to their favourites, which is the joke's "liked_by" array field in the database. The joke will then be displayed in the "Your Favourites" section of their profile. Removing the joke from their favourites will reverse this action.

    A user can tell if they have liked or removed a joke from their favourites by the colour change in their respective icon. Yellow means the joked has been liked or favourited, while black means it has not be liked or favourited.

    The admin can also click the "Expand" button on the joke card, which will trigger a modal that will display the full joke. The joke on the card is capped at 50 characters.

    The admin can also search all jokes from the Home page using the search bar at the top of the page.

* Beside the search bar, there is an "add" icon which will lead them to the Add Joke page, where they can upload a joke to the site. This page can also be accessed from the sticky navbar at any time.

    As seen in the [Wireframes](#Wireframes) section, the Add Joke page is comprised of a form that takes information about the joke. This information includes the jokes, title, description, an images, related to the joke, and whether or not it is suitable for under 18s. 
    
    This information, along with additional information is then inserted into the jokes collection in MongoDB. The additional fields include the user who uploaded the joke, and the "likes", "liked_by", and "favouriter" fields discussed above.

* In their profile, the admin can access the jokes that they have uploaded themselves, as well as the jokes that they have added to their favourites via a dropdown menu. The dropdown menu also allows users to sign out.

* The Admin user also has access to a Users page, where they can view all users who have signed up to the site. They can see all available information about the user, including their ID, username, and date of birth. Here, the admin can also chose to delete a user at their own discretion.

#### General User

* The general user has a more restricted version of the site available to them. They can access all the pages available to the admin user, except for the Users page

* All other pages are identical to the admin's version, except for the actions available to them. They can only edit or deleted a joke that they have uploaded themselves. 

    If the joke as been uploaded by another user, the only options available to them is the ability to like a joke or add a joke to their favourites.

    If they have uploaded the joke themselves, the only available options are to edit or delete the joke

#### Under 18 User

* Users under 18 years of age have an almost identical account as a general user. The only difference between the accounts is that users that are under 18 years of age may only see jokes that were marked "Suitable for children" in the Add Joke form.

#### Signed Out User
* A user who has not signed up or has not signed in, can access the most restricted version of the site. They have the Home, Sign up and Sign in pages available to them.

* Their access to the Home page is similar to the Under 18 user's. Like users under 18 years of age, they may only see jokes suitable for children. However, unlike other users, if they try to take any action, such as trying to see the full joke, liking, or adding the joke to their favourites, the will be presented with a modal providing them with the option of signing in. They can agree or decline.

* If the agree, they are led to the Sign Up page, where they enter their username, password and date of birth. Upon completing this action, they are uploaded to the users collection in the database. They are then considered a general user and redirected to their Profile page. Thanks to [Werkzeug](https://palletsprojects.com/p/werkzeug/), their password are securely stored and checked upon signing in.

## Potential Future Features
#### Categories
* There are many types of categories that jokes could be grouped into. This features would allow users to search for their favourite jokes based on a category. Possible categories might include: Dad Jokes, One-liners, Blonde jokes, and even memes!

#### Sort By
* I had originally planned to include this features, but chose to omit it, as discussed above. Users could use this feature to filter jokes based on their popularity, length, upload date, etc. It would allow users more control over what they see.

#### Shuffle
* An interesting future feature would allow users to shuffle through jokes. The users would press the shuffle button and one random joke would appear on their screen at a time.

#### Originals
* Another option would be to be allow users specify whether the joke they are uploading is original or not. They could possibly gain a following of users who enjoy their jokes.

#### Possibly Offensive Content
* Some jokes may be tagged with a warning that it might include contense that some may find offesive.


## Technologies Used 

### Languages Used 
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    * [Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine))

### Frameworks, Libraries & Programs Used
* [Balsamiq](https://balsamiq.com/)
    * Balsamiq was used to make the wireframes for the project

* [Bootstrap 5.0.0](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    * Bootstrap was used in conjunction with [jQuery](https://jquery.com/) extensively throughout the site.
    
        It was used on the Navbar to make it responsive and to collapse the menu items into a single button at smaller screen sizes.

        Initialized with [jQuery](https://jquery.com/), the tooltips on all icons throughout the site are Bootstrap features 

        More prominantly it was used to create the card elements that the jokes were displayed on. Bootstrap is also responsible for all modals seen throughout the site. Bootstrap classes were often used instead of CSS on other elements to assist with centering and positioning.

        Of course, extensive editing had to be carried out on all Bootstrap elements throughout the site to get it functioning a looking the way it currently is. 

* [Fontawesome](https://fontawesome.com/)
    * All icons seen throughout the site were sourced from Fontawesome, including the dropdown menu button in the navbar.
    
* [Git](https://git-scm.com/)
    * The Gitpod terminal was used to commit to Git and push to Github.

* [GitHub](https://github.com/)
    * Github was used to store the code from the project.

* [Google Dev Tools](https://developer.chrome.com/docs/devtools/)
    * Google Dev Tools was extensively used throughout the project, especially for testing code, and addressing bugs.

* [Google Fonts](https://fonts.google.com/)
    * Noto Sans, the font used throughout the site, was sourced from Google Fonts.

* [jQuery](https://jquery.com/)
    * jQuery was used in conjunction with Bootstrap on various elements througout the site.

* [MongoDB](https://www.mongodb.com/)
    * MongoDB was used to creates collections within a database to store data about the sites registered users and jokes uploaded by them.

* [Flask Paginate](https://pythonhosted.org/Flask-paginate/)
    * Flask paginate was used for pagination in the Home and Profile pages.

* [Coolers.co](https://coolors.co/)
    * Coolers was used to help choose the colour palette seen throughout the site.

* [Am I Responsive](http://ami.responsivedesign.is/)
    * Am I Responsive was used to produce the image displaying the website on different screen sizes at the beginning of this document.

* [Autoprefixer](http://autoprefixer.github.io/) was used for the same reason as babel. I used Autoprefixer to add vendor prefixes to make it more compatible with various browsers and devices. It was also unsuccessful in addressing the bug. As well as this, as you will see in the Known Bugs section of [TESTING.md](/TESTING.md), it caused errors when put through the W3C CSS Validator. For these reasons, the prefixes were removed.

## Testing
Information on testing can be found in a separate [TESTING.md](/TESTING.md) file

## Deployment

### Project Creation
This project was created by using the following steps:

1. Log in to GitHub.
2. In the Repositories section, click the green "New" button.
3. Under "Repository template", select "Code-Institute-Org/gitpod-full-template".
4. Enter repository name (eden).
5. Click "Create repository".
6. When re-directed, select the green "Gitpod" button. 

### GitHub Pages
This project was deployed to GitHub Pages using the following steps:

1. Log in to GitHub.
2. Select repository.
3. Navigate to and click the "Settings" button.
4. When re-directed, scroll down to the "GitHub Pages" section.
5. Under "Source", click the dropdown named "None" and select "Master Branch".
6. Click the "Save" button.
7. Upon page refresh, scroll down and locate the link to the live deployed page.

### Forking the GitHub Repository

Forking the GitHub repository allows us to make a copy of our original repository where changes can be made without affect the original copy.
To do this, follow these steps:

1. Log in to GitHub.
2. Select your repository.
3. Locate and click the "Fork" in the top right corner, under the nav bar.
4. A copy of the original repository should have been created in your GitHub account.

### Run Locally

1. Log in to GitHub.
2. Locate repository.
3. Locate and click the "Code" dropdown menu.
4. Under HTTPS, copy the URL.
5. Open your development editor and a terminal window in your chosen directory.
6. In the terminal, type "git clone " followed by the URL you copied in step 4 and press enter.
7. A clone of the project should have been created.

## Credits

### Code 
* [Ed Bradley's](https://github.com/Edb83) pagination code was a great template for learning how to implement my own. His code can be found [here](https://github.com/Edb83/self-isolution/blob/master/app.py).

* I learned how to make the 404 and 500 error pages from [this resource](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/).

* [This](https://www.youtube.com/watch?v=RjMbCUpvIgw) video from [Socratica](https://www.youtube.com/user/SocraticaStudios) and [this](https://www.youtube.com/watch?v=NWDQDLzqMt8) video from [Irfan Khan](https://www.youtube.com/channel/UCK5QUBOwyE9cAaO0SV1etyQ) were very helpful in understanding how to calculate the user's age.

Of course, all functions, variables, classes and ids have been changed. However, much more needed to be done to implement moveable and resizable functionality into my project, as well as to include the removable functionality. Added layers of complexity included the functionality being written for elements that don't yet exist in the DOM and also that the moveable and resizable elements were nested inside other elements.

Further details of the bugs encountered in the project can be found in the Known Bugs Section of the [TESTING.md](/TESTING.md).

### Content 
* The site was created solely by the developer. All jokes are uploaded by different users.

### Media
* All images seen on the site are uploaded by users as urls as part of the process of adding a joke. The site does not own the copyright to these images.

### Acknowledgements

I would like to thank the slack community for their assistance, particularly Daisy Mc Girr who is always willing to share her wisdom and advice. Igor Busaga's hands-off assistance and patience was also very much appreciated.