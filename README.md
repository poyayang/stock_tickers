# stock_tickers
 Automation for stock tickers
The project is to create an automation for users get to know latest stock prices.

In this project, Render is the Python Host to deploy the project automation.

Preparation
1.	Make sure that Flask is imported to the main file
 from flask import Flask, request
app=Flask(__name__)

2.	Install requirement.txt, and save it in the same folder, "pip3 install -r requirements.txt"

  	NOTE. Render may not support some of the latest versions of libraries, this will have to refer to the instruction in the building process.

Connect Github to Render

3.	Register on Render and click “New+” to create a Web Service
4.	Choose “Build and deploy from a Git repository”, to connect Github to Render
5.	Select the repository, make sure the repository is set as ‘Public’ on Github
6.	Go to Render – Settings, fill in the information 
Repository – The URL of the repository on Github
Branch – The project is in the “Main” Branch
Build Command - pip install -r requirements.txt
Start Command - python app.py (the main file of the project)
7.	Hit ‘Create Web Service”


https://github.com/poyayang/stock_tickers/assets/136909810/a4215440-e25e-4684-ade8-769b42f540c5





