# Favourite-things
The Project as described in the Test is a web application that allows users list and rank their favourite things based on 
categories.

# Backend
The Backend was written in Flask and it features rest api endpoints that let users create, read and rank their favourite 
things as well as create additional categories. There is an audit log that automatically gets populated with data as users 
perform actions on the website.

The application identifies users by storing cookies on users' browsers and retrieving them when they perform actions on the
web page. 

# Frontend
The Frontend was written in VueJS and as a single page application that communicates with the backend and lets users create
and rank their favourite things (using Vue-draggable), create and view categories and view their audit Logs.

# Deployment
A dockerized version of the backend was deployed using Heroku and the Frontend with Netlify. The frontend and backend contain 
dockerfiles that communicate with each other using a docker-compose file in the root directory (useful for local testing).
