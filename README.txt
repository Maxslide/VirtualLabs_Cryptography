ItSS Assignment 4
Cryptographic Hashing - Cryptography lab

Manas Kabre - 2018111014
Shivam Mangale - 2018101008

Prerequisites :
1) Python 3.0 or later
2) pip3
3) import libraries for flask implementation :
	from flask import Flask, render_template, jsonify, json
	from flask_sqlalchemy import SQLAlchemy
	from random import shuffle
4) minimum requirements for pip3 : 
    Click==7.0
    cycler==0.10.0
    Flask==1.0.2
    Flask-SQLAlchemy==2.3.2
    itsdangerous==1.1.0
    Jinja2==2.10
    kiwisolver==1.0.1
    MarkupSafe==1.1.1
    matplotlib==3.0.3
    numpy==1.16.2
    pyparsing==2.3.1
    python-dateutil==2.8.0
    scikit-learn==0.20.3
    scipy==1.2.1
    six==1.12.0
    sklearn==0.0
    SQLAlchemy==1.3.1
    virtualenv==16.4.3
    Werkzeug==0.15.1

Files included in the repository : 
1 ] experiment.py - The control flask. On execution creates a server for navigation.
2 ] static - Includes the js,css and images required for the functioning of the file.
	1] bootstrap.min.css - to render the page quicker.
	2] images - includes all the images used in this repo.
	3] style.css - the main css file.
	4] js - includes all the js used in this repo. 
		1] jquery.js - ????
		2] jsreqexp - Includes all the js required for the functioning of the experiment.
			1]  base64.js   - used for converting between integer representations
    		2]  hmac.js     - main (controller) js file 
    		3]  jsbn.js     - required for rsa encryptions
    		4]  jsbn2.js    - required for rsa private operations
    		5]  prng4.js    - to implement OOP with the random number 
    		6]  rng.js      - random number generator
    		7]  rsa-dss.js  - to encrypt 
    		8]  rsa.js      - for utf-8 encoding
    		9]  rsa2.js     - support utf-8 encoding
    		10] sha1.js     - implementation of the Secure Hash Algorithm
3] templates - has all the html files
		1] Experiment.html
        2] Further_Reading.html
        3] Introduction.html
        4] Manual.html
        5] Objective.html
        6] Procedure.html
        7] Quizzes.html
        8] Theory.html
        9] index.html