# Django-studies

This is my study repo for Backend dev with Django. I will share what i learn from Corey Schafer's Django Course. Join me on this journey and let's achive the dream of being a backend engineer. 


## Day 1 

- I learnt how to create virtual environments in Windows. i had a little issue because i normally used to do it in bash and i used a mac. 
- Also learnt how to install Django package. initialised a project, see how the project structure looks like and what gets created and how to pull up the default site in a browser. 
- I learnt how create a blog app using `python manage.py startapp blog` and also learnt basic routing by creating url patterns that are handled by the application views

## Day 2 
- I learnt how to create templates for django. the templates directory contains all your HTML files (frontend). Also learnt how to pass variables to our templates. Although not really relevant to backend developement i was a great thing to learn. I even learnt template inheritance where there a base html file containing repeated code in all html files so they can easily adopt them and use them. It helps when you want to make changes. You don't have to make the changes on all the html files.  
- I also learnt how to access the Django ADMIN PAGE. I used   `python manage.py migrate` to initialize the database to create a user since you dont have a default username and password already created and an Operational error (no such table: auth_user) will happen when you don't migrate. I then use `python manage.py createsuperuser` to create an account so you can access the admin page. 

## Day 3 
- I learnt how to create an authentication system for our application so that users can login and logout. We are also going to see how we can restrict certain pages so that users must be logged-in in order to access the page

- I encountered a bug where the logout page was giving an error 403. i fixed it by using. This was an issue because allow GET requests for logout was less secure as previously done in the earlier versions of Django. so now it uses a POST request for security reasoms and it being protected against CSRF attacks. The POST request is to ensure the action was intentional.  i used the code below to fix this issue. 

``<a class="nav-item nav-link" href="{% url 'logout' %}">
                    <form method="post" action="{% url 'logout' %}">
                      {% csrf_token %}
                      <button type="submit">logout</button>
                  </form>
                  </a>``

- I also learnt how to upload user profile and user profile picture 



## Day 4 

- I have learnt to Update user Profile information  and also resizing profile images. so we don't worry the filesystem if images are too large.

## Day 5

- I learnt to add CRUD operations to the blog posts for authorized users to create, update or delete post for themsleves and not other users. also they have to login to make those changes. 
i learnt them by using class-based views. 

- I learnt how to use pagination so we dont have to scroll a lot to see posts. I also created a page for posts created by a specific user

## Day 6 Final day

- i leanrt how we can use email to send a password reset link to a user so that the user can reset their password. Users will be able to fill out a form with their email and have a unique token sent to them, and if their token is verified then they will be able to create a new password

 



