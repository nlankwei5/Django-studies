# Django-studies

This is my study repo for Backend dev with Django. I will share what i learn from Corey Schafer's Django Course. Join me on this journey and let's achive the dream of being a backend engineer. 


## Day 1 

- I learnt how to create virtual environments in Windows. i had a little issue because i normally used to do it in bash and i used a mac. 
- Also learnt how to install Django package. initialised a project, see how the project structure looks like and what gets created and how to pull up the default site in a browser. 
- I learnt how create a blog app using `python manage.py startapp blog` and also learnt basic routing by creating url patterns that are handled by the application views

## Day 2 
- I learnt how to create templates for django. the templates directory contains all your HTML files (frontend). Also learnt how to pass variables to our templates. Although not really relevant to backend developement i was a great thing to learn. I even learnt template inheritance where there a base html file containing repeated code in all html files so they can easily adopt them and use them. It helps when you want to make changes. You don't have to make the changes on all the html files.  
- I also learnt how to access the Django ADMIN PAGE. I used   `python manage.py migrate` to initialize the database to create a user since you dont have a default username and password already created and an Operational error (no such table: auth_user) will happen when you don't migrate. I then use `python manage.py createsuperuser` to create an account so you can access the admin page. 