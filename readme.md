# Charity Fund #

Fourth Milestone Project - Full Stack Frameworks with Django 

This project has bought together all the knowledge learnt in the Python and Data Centric Modules that have been covered previously as well as the Full Stack Frameworks with Django Module.  

I have created a crowd funcing website utilising the services of Heroku and Postgres DB. 
This site facilitates small charities and local community groups to access funding streams that they may not normally be able to access. 

Anyone using the site can go view the available appeals that are on the site.  
The users, if registered, can add donate to any appeal and contact any appeal via email, registered users also have the option to register one charity or a community group and from that point register as many appeals on behalf of the charity/community group, which will be stored in their 'My Organisation' page for review. They can edit the organisation and appeals but not delete as we for transaprency, given the nature of donating for charitiable and community group causes it is best to leave them up so that donors can view the progress in the future. The user only has permission to carry out any maintenance on their profile, own organisation and appeals, but dont have the facility to carry out these tasks on anyone elses.

The deployed website is [CharityFund](https://charityfunding.herokuapp.com/).

## UX ##

I have considered the different user experiences as they would move through the site, from whether they are registered users to organisation owners.
New comers who do not wish to register are unable to have access the full benefits of the site such as a registered user would, such as viewing the full appeal information, donating to an appeal or adding one. This is to ensure that there are levels of authentication effectively and collect more data about the users and given projects and organisations, as well as geolocation data as to the where abouts of these appeals.

#### User Stories ####
1. A user wishes to make a donation after finding a particular type of appeal that they are interested in supporting.
2. A user wishes to make a donation after finding a particular type of appeal that they are interested in but remain anonymous.
3. A user has a charity/community group and wishes to set up an appeal to receive donations from the public.
4. A user wishes to see the appeals that are in there immediate area and contact the one that they are interested in to offer volunteering help.
5. A user wishes to use the site to keep a track of all there appeals that they have running concurrently, able to see exactly what is being donated and in what amounts.

See the [wireframes](https://github.com/michael-leese/charityfund/tree/master/wireframes) I used as a basis for my construction process.

### Features ###

The site has been created offering benefits to the user's who register and login with the ability to donate, contact and view the appeals. The users passwords are stored in an encrypted format that cannot even be seen by the DBA(database analyst). The user can search through all appeals in order to chose where or to whom they would like to donate, if logged in they can actually make a donation, they must be logged in so as to track customers and prevent fraud/money laundering.
Users are able to add and edit their own appeals as long as the register a Registered Charity or Community Group with CharityFund first, once an organisation and/or appeal is created the owner may edit those details.
Other users are unable to access the edit funcitonality of organisations or appeals.

#### Features for future Implementation ####

In the future, I would like to add the ability of searching your own Appeals and having the ability of providing appeals with ways that they could hire volunteers.

## Technologies Used ##

In this project I have used the following technologies in order to create the website.

[Python 3.6.8](https://www.python.org/downloads/release/python-368/) was the base language used in order to create the app, provide navigation, logic to the buttons/links, forms and models as well as connection to [Postgres](https://www.heroku.com/postgres) and [Heroku](https://www.heroku.com/home), all within the Django Framework. For staorgae of static files and images uploaded by users I have created [S3 Buckets](https://aws.amazon.com/s3/) on AWS services to provide the dynamic storage required.

I utilised [Django](https://www.djangoproject.com/), [Django Bootstrap Forms](https://pypi.org/project/django-forms-bootstrap/), [Django Mathfilters](https://pypi.org/project/django-mathfilters/), [Django Taggit](https://pypi.org/project/django-taggit/), [Django Rest Framework](https://pypi.org/project/djangorestframework/), [Gunicorn](https://gunicorn.org/), [Django Storages](https://django-storages.readthedocs.io/en/latest/), [Pillow](https://pypi.org/project/Pillow/) and [AWS Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) for the majority of the functionality, however more were used and these have been recorded in the [requirements.txt](https://github.com/michael-leese/charityfund/blob/master/requirements.txt) file with a full list of depenedencies that were utilised. Heroku utilises this file in order to install them locally on the server after an automatic push triggers a new build of the project.

[Jinja Template](https://jinja.palletsprojects.com/en/2.10.x/) was used in conjunction with HTML5 to provide the dynamically populated structure of the website and was styled using CSS3.
[Bootstrap4](https://getbootstrap.com/docs/4.0/getting-started/introduction/) was used in order to style and make responsive the front end of the site, as well as the use of Bootstrap's [Tempus Dominus](https://tempusdominus.github.io/bootstrap-4/).

JQuery and Javascript were used in order to create API calls and style some of the dynamic elements on the  such as the filter functionality I created for the all appeals pages, they were more extensively used to integrate some of the pluggins, such as [Google Maps](https://developers.google.com/maps/documentation), [Stripe](https://stripe.com/gb) and [EmailJs](https://www.emailjs.com/). 

In Ubuntu I used Bash Script in order to carry out tasks and perform installs and connections in the terminal.

GIT and GitHub were used in order to version my code and store it in a repository. GitHub's automatic integration with Heroku enabled automatic pushing of the repository upto Heroku for deployment.

[VS Code](https://code.visualstudio.com/) was the environment in which I created my app, I had to install extensions for it in order to provide it with the capability of running and editing my code. These included WSL, Python, HTML, CSS, Javascript, Django HTML and some formatting versions for these languages so that i could beautify my code.

MarkDown was used to create the Readme.md file you are reading now, as well as the [testing.md](https://github.com/michael-leese/charityfund/blob/master/testing.md) file.

## Deployment ##

I have hosted the site on Heroku, and git committed to a repository of the code on [GitHub pages](https://github.com/michael-leese/charityfund), which has been linked and automatically deploys directly from the Master Branch, Heroku uses my [Procfile](https://github.com/michael-leese/charityfund/blob/master/Procfile) to ensure it knows what type of application it is building and gets all its access details from the os.environ variables that are stored locally on the heroku server in the config vars, this provides all the access to all access to MongoDB database is handled in this file as well as connection to the app and templates.

Initially a super user was created for access to the database, however upon the site reaching the point that data could be added through the front end all other DB data was added through the relevant forms on the site.

If the site is to be updated or added to then further commits will automatically add to this branch and update any file changed/moved/deleted.
After first signing up for Heroku and creating a Postgres DB I then went about setting up my VS Code environment with all the extensions that it required and then connected my environment to Heroku using the Ubuntu terminal with Bash Script.

A list of the commands that I had used in the Ubuntu terminal are as follows:
* VS Code
    * wsl
    * code .
* Python 3.6
    * python3
    * python3 --version
* Django
    * sudo pip3 install django
    * sudo pip3 install <-name of dependency->
    * django-admin startproject <-name of project->
    * django-admin startapp <-name of app-> (then update the settings.py file with the new app)
    * python3 manage.py createsuperuser
    * pip3 freeze --local
    * pip3 freeze --local > requirements.txt
    * python3 manage.py runserver (to run the code locally in virtual environment)
* Create Procfile
    * echo web: python manage.py > Procfile

As well as the various GIT commands that we use regularily in order to commit our code. 

The environment variables on Heroku were used to store the IP, PORT, AWS_ACCESS_KEY_ID, AWS_SECRET_KEY_ID, DATABASE_URL, DISABLE_COLLECTSTATIC, RUN_PRODUCTION, SECRET_KEY, STRIPE_PUB_KEY and STRIPE_SECRET_KEY so that they are not visible or accessable to the public or stored in any repositroy. These are imported locally via a file that was gitignored called env.py, with some logic in settings.py that distinguished as to whether the env.py existed and/or the RUN_PRODUCTION variable was available, these were accessed and used by importing OS for production purposes.

## Testing ##

I have carried out some automated testing on the accounts app, testing forms, models and views using the [Django Test Framework](https://docs.djangoproject.com/en/3.0/topics/testing/), as well as a structured manual [regression testing process](https://github.com/michael-leese/charityfund/blob/master/testing.md) was completed and undertaken manually, going through the user stories as well as testing all functionality and logic through the front end. This involved testing while not logged in and paying particular attention to the authorised access and the logic the links and buttons would play given the level of access granted to the site.

Further testing was carried out on the responsivity of the site across different browsers and platforms in order to ensure that the site maintained its stylings. The items that have been tested with are listed below:

Tested On | <span style="color:white"></span>       
---------- | ----------
Chrome | web-server-for-chrome
FireFox | Microsoft Edge
Safari | Android Device
IoS Device | Windows LapTop
Chrome devTools inc Remote Device Debug | mybrowseraddon.com useragent-switcher 

## Credits ##

I have utilised some of the code that was on the Full Stack Frameworks with Django Course in order to get some of the functionality working and off the ground, and have built my own logic and functionality into the site using some of the sources that have been mentioned in this section.
* ### CodeSnippets ###                                             
    * https://simpleisbetterthancomplex.com/
    * https://simpleisbetterthancomplex.com/tips/2016/08/04/django-tip-9-password-change-form.html
    * https://docs.djangoproject.com/en/3.0/topics/auth/passwords/#included-validators
    * https://pypi.org/project/django-tempus-dominus/
    * https://stackoverflow.com/questions/57595553/django-tempus-dominus-timepicker-format
    * https://pypi.org/project/django-mathfilters/
    * https://dev.to/coderasha/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704
    * https://django-taggit.readthedocs.io/en/latest/api.html
    * https://stackoverflow.com/questions/1644455/django-form-not-saving-default-image-name
    * https://www.django-rest-framework.org/
    * https://stackoverflow.com/questions/16476357/django-ajax-get-request
    * https://remysharp.com/2016/12/23/beginners-guide-to-stripe-integration
    * https://stackoverflow.com/questions/5448545/how-to-retrieve-get-parameters-from-javascript
    * https://getbootstrap.com/docs/4.0/components/pagination/
    * https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html

#### Media ####

All the appeals are made up and do not reference any actual organisations or appeals, images were foudn using Google Image search and ensuring that the settings for usage rights had been changed to free to use or share, even commercially.
Further images were incorporated to help style the site.
* Images and Fonts    
    * https://www.wallpaperflare.com/human-hands-digital-wallpaper-volunteers-voluntary-wrap-protect-wallpaper-ukhgk
    * https://pixabay.com/illustrations/donate-charity-giving-give-aid-654328/
    * https://simple.wikipedia.org/wiki/Mask
    * https://pixabay.com/photos/the-old-lady-grandma-garden-3503684/
    * https://www.needpix.com/
    * https://fonts.google.com/

#### Acknowledgements ####

I am thankful for the lessons and miniproject that is in the Full Stack Frameworks with Django Module of the course by [The Code Institute](https://codeinstitute.net/), my mentor for getting me to this my final project and all the staff who have assisted me over the time while I have been studying. It has been a real honour to study at [The Code Institute](https://codeinstitute.net/) and a real pleasure to do the work, I look forward to the future and putting all my skills to use.

###### This project has been created for educational use ######