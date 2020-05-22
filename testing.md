## Automated Testing ##

I have used the Django Test Framework to carry out my automated testing and have used [coverage](https://coverage.readthedocs.io/en/coverage-5.1/) to run my tests and produce reports, including the htmlcov folder with indepthe reports. The commands used in the termial were:

* py manage.py test
* coverage run manage.py test
* coverage report
* coverage run --source=accounts manage.py test
* coverage html

As I was running locally on [Vistual Studio Code](https://code.visualstudio.com/) I had to use [Web Server for Chrome](https://chrome.google.com/webstore/detail/web-server-for-chrome/ofhbbkphhbklhfoeikjpcbhemlocgigb?hl=en) to locally run up the testing report suite, however i couldnt view it from any where, which would be valuable for remomte monitoring, although static at poresent in the future could have more options added to the area.  
Including the htmlcov in settings.py in the templates dictionary of directories, I then was able to store the js, css and images in the S3 bucket via a 'collectstatic' command, adapt the index.html page to have Django Template, static tags and added some custom Javascript to disable all the links as they arent all added to the urls currently but in the future a more meaningful dive into the testing reports would be available to build on.

You can access the report page via my admin login only and view the report page from the about section, at the bottom of the page in 'Site Test Framework Reports' link. No other user can see this, as obviously this is sensitive to the developer only and not other users, and could serve in the future as an an additional admin area for testers.
As I could of spent a very long time completeing lots of automated tests across the full package which would be done in the future. I carried out automated testing on the Account App only, for which I completed testing on forms, models, views and apps.py getting 66% completion.
A screenshot of the testing can be found [here](https://github.com/michael-leese/charityfund/blob/master/static/img/Screenshot-admin-test-information.png).


## Manual Testing ##

This section outlines the manual regression tests that were carried out in order to prove the functionality of the website.

1. Home Page(not logged in):
    * The website says Welcome and the Links are Home, View Appeals, Login, Register, About.
    * You can search using the search bar and on pressing search are directed to the View Appeals page with the results.
    * On pressing the Logo you are directed to same page.
    * On pressing the CharityFund name in footer you are taken to About page.
    * On pressing any of the social media icons in the footer you are directed to the corresponding site for the icon.
    * Home Nav Link is highlighted.
2. Home Page(logged in):
    * The webiste says welcome and in the navbar it says 'Hi, (nickname)' next to your userprofile image, if one has been uploaded and the navbar is populated with Links to Home, View Appeals, Logout, Register Org, About.
    * The Navbar now says "Hi," followed by the nickname you chose in your registration form, with your profile pic if you chose one, this serves as navigation to your edit profile page. 
    * You can search using the search bar and on pressing search are directed to the View Appeals page with the results.
    * On pressing the Logo you are directed to same page.
    * On pressing the CharityFund name in footer you are taken to About page.
    * On pressing any of the social media icons in the footer you are directed to the corresponding site for the icon.
    * Home Nav Link is highlighted.
3. Register:
    * If you do not enter information in the fields you are instructed to do so.
    * If you enter a username that already exists you are given a message explaining the error.
    * If you enter a password that does not meet the regex you are instructed to do so and provided the criteria.
    * If you enter a password that does not match the confirm password you are instructed to correct this.
    * When you click on register with valid information in the fields you are registered and taken to the Home page.
    * Register Nav Link is highlighted.
4. Login:
    * If you do not fill out the fields you are instructed to do so.
    * If you enter a password that does not meet the criteria you are instructed.
    * If you enter a valid user name and password you are taken back to Home Page(logged in).
    * If you enter an incorrect username/password you are given a message explaining the error.
    * Login Nav Link is highlighted.
5. Logout:
    * Logs the user out and returns them back to the Home Page(not logged in).
6. View Appeals(not logged in):
    * Display a list of all appeals added to the site.
    * Shows a Google Map Api that is centered over the middle of the UK, showing all the UK.
    * If you click on a map marker or press view on any appeal, you are directed to the Login page, with an option to register if necessary.
    * If you want to click on the filters button, you are only given an option to register first and directed there on clicking it.
    * Donor message are displayed.
    * View Appeals Nav Link is highlighted.
7. View Appeals(logged in):
    * Display a list of all appeals added to the site.
    * Shows a Google Map Api that is centered over the middle of the UK, if you do not have geolocation active, otherwise it zooms into your current location to show you nearby appeals.
    * If you click on a map marker or press view on any appeal, you are taken to that appeal to view it in full and carry out actions such as Donate, Contact and if owner Edit.
    * If you click on the filters button, you are given options to filter the appeals and on clicking one the appeals are filtered how you have asked and the filter is highlighted in the dropdown when you click back on the filter button.
    * Donor message are displayed.
    * View Appeals Nav Link is highlighted.
8. Edit Profile(must be logged in):
    * Navigation via the profile image in navbarwith Hi message.
    * Give you the options to update your user profile and save. 
    * There is a button to direct you to change password page if required.
    * Go back button takes you to Home page(logged in).
9. Change Password(must be logged in):
    * Provides a clear set of instructions of how to construct new password. If you do not fill out the fields correctly you are instructed to do so.
    * If you populate the form with valid information and save then you are directed back to the Edit Profile page with a success message, cancel redirects you back to Edit Profile page also, without a message.
10. About:
    * The image takes users to the Home page.
    * If you are an admin user and logged in with an admin account you can view the Site Test Framework remotely, if not then you are redirected back to the index page with a message, depending on if logged in or if logged in and not an admin.
    * About Nav Link is highlighted.
11. Register Org(must be logged in):
    * You are provided with a form to create an organisation.
    * Organisation and Bio field must be completed for validation.
    * Register takes you to Home Page with a success message.
    * Cancel takes you to Home Page(logged in and Org Registered).
    * Register Org Nav Link is highlighted.
12. Home Page(logged in and Org Registered):
    * The webiste says welcome and in the navbar it says 'Hi, (nickname)' next to your userprofile image, if one has been uploaded and the navbar is populated with Links to Home, View Appeals, Logout, Create Appeal, My Organisation, About. 
    * The Navbar says "Hi," followed by the nickname you chose in your registration form, with your profile pic if you chose one, this serves as navigation to your edit profile page. 
    * You can search using the search bar and on pressing search are directed to the View Appeals page with the results.
    * On pressing the Logo you are directed to same page.
    * On pressing the CharityFund name in footer you are taken to About page.
    * On pressing any of the social media icons in the footer you are directed to the corresponding site for the icon.
    * The form must be populated with valid information.
    * Home Nav Link is highlighted.
13. Create Appeal(must be logged in and have Registered an Org):
    * The form must be populated with valid  for all fields, only image field may be left blank.
    * The this site link opens in a new window at https://www.latlong.net/ which allows user to get the lat/long of their location.
    * On successful submition of the form you are taken to the All Appeals Page with a success message.
    * Create Appeal Nav Link is highlighted.
14. My Organisation(must be logged in and have Registered an Org):
    * Shows the users organisation at the top of the page with a button to edit organisation.
    * Display a list of all  users organisations appeals added to the site.
    * Shows a Google Map Api that is centered over the middle of the UK, if you do not have geolocation active, otherwise it zooms into your current location to show only your appeals.
    * If you click on a map marker or press view on any appeal, you are taken to that appeal to view it in full and carry out actions such as Donate, Contact and Edit.
    * If you click on the filters button, you are given options to filter the appeals and on clicking one the appeals are filtered how you have asked and the filter is highlighted in the dropdown when you click back on the filter button.
    * Donor message are displayed.
    * My Organisation Nav Link is highlighted.
15. View Appeal(must be logged in):
    * The appeal info is displayed in full and a dynamic bar displaying the percentage of money raised is displayed.
    * The buttons Donate, Contact and Go Back are present, if you are the owner you have an additional button Edit.
    * Donor message are displayed.
    * No Nav Link is highlighted.
16. Donate(must be logged in):
    * Present you with a donation/payment form, you must fill out all the information for the form to be valid, you can select to be anonymous under your message which means that your donation message will not have you information in it when displayed.
    * No Nav Link is highlighted.
17. Contact(must be logged in):
    * You enter a message which will be emailed to the user who owns the appeal you have chosen, this contains the senders information for the recievers to respond.
    * If you are the owner of the appeal you cannot send an email to yourself and a message is displayed stating this and the Send button is hidden.
    * No Nav Link is highlighted.
18. Edit Appeal(must be logged in and have Registered an Org and Appeal):
    * The form must be populated with valid  for all fields, only image field may be left blank.
    * The this site link opens in a new window at https://www.latlong.net/ which allows user to get the lat/long of their location.
    * On successful submition of the form you are taken back to the View Appeal page.
    * No Nav Link is highlighted.