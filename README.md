# G10T6-IS213-Project
The ESD web application is a Fitness Web Application that allows user to book different fitness classes. 

# vue-project Main Setup Instructions
This ESD project contains a few parts to setup before you are able to run the website. Please Setup both FRONTEND and BACKEND code before running the website on your local machine. Please refer to the instructions below for the setup guide.

## Project Setup (FRONTEND)
##Below are the steps to setup the Frontend Vue
1. Unzip the folder and store the folder in the path best suited for opening the files.
2. Open the files and open a new terminal, cd Frontend and type in the following command: npm install
3. Once the npm install is done, to run the frontend, type in the following command: npm run dev
4. You will not be able to see some of the UI display if you have not done Project Setup (BACKEND), refer to the instructions below.


## Project Setup (BACKEND)
There are 4 parts to the docker setup, 
Part 1:
Load the 3 sql scripts from the following folders:
folder Name: fitness_classes, file name: fitnessClass.sql
folder Name: ratings, file name: ClassRating.sql
folder Name: user_bookings, file name: user_bookings.sql

add in the setup for one of the lab sql is213 thing

Part 2:
Setup the Rabbit MQ container using the lab 5 class lab notes which the instructions are provided below:

1. Open CMD window and run:
docker run -d --hostname esd-rabbit --name rabbitmq-mgmt -p 5672:5672 -p 15672:15672 rabbitmq:3-management
2. Open the docker container clicking rabbit mq UI
    Login: guest
    Password: guest

3. Import the "rabbit_esd-rabbit_2024-3-15" file that is within the zip folder to load the rabbit mq configurations.

4. Lastly, run the Rabbit MQ Container before moving to the next step.

Part 3:
There is a Stripe folder file that require you to change the domain_url to the file path of your localhost wamp/mamp.
1. Firstly, you will need to test open success.html file on your web browser localhost by navigating to Backend -> html -> success.html
2. If you are able to see the content of this success.html file, move on to step 3.
3. Open stripe folder and open server then open server.py file within. 
4. Go to Line 205 and you should see the current code: "domain_url = "http://localhost/ESD_Project/G10T6_Project/G10T6-IS213-Project/Backend/html"" 
5. Based on the file path that you previously open in step 1, copy that file path and replace domain_url with the file path on your localhost machine and DO NOT include "/success.html" in the domain_url.
6. Which the file path should something like step 4 code provided.
7. Once all above step is done, move on to part 4.


Part 4:
This part is the setup of the whole backend microservices. 
1. Open a new terminal, cd Backend and run the following command: docker-compose up --build (Make sure the Rabbit MQ container is running before doing a docker-compose up -build command so that it allows for amqp connection that is needed)

2. Wait for everything to build and once its done, you can test the code at the frontend


