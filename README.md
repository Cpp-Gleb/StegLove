# <p><strong> &#128205; Hello ITMO STARS!</strong> 

<strong>Project Description </strong>

An application was developed based on the Qt framework for easy use of basic utilities with a clear interface. Custom widgets are written for uniqueness and beauty. Based on the flask framework, a web application with a built-in api was developed that allows you to analyze the file using various utilities such as exiftool, zsteg and so on. The web application can be accessed by specifying the name of the utility for analyzing the file in the route `https://www.rjomba.com/api/<tool>`. 

I added a database to save the query session, which allows me to go back to analyse the files if the problem was not solved the first time. The Deterministic UUID v4 Generator, which I wrote as a homework assignment for the Discrete Maths course in the Haskell programming language, is used to generate session IDs. Also, a custom trigger is used in the database to conveniently assign an ID for each session. The code includes decorators, working with Flask timeplates, in addition, the application is asynchronous, which improves its performance many times over.

In the future it is planned to add basic utilities to extend the capabilities. Adding a message broker to prevent analyses from being lost. Changing the language for writing the API. Changing the Qt application interface. Scaling of the project, namely breaking the current monolith into a microservice architecture, placing separate servers for message brokers, splitting databases into different servers with current SQLite and in the future added PostgreSQL. 

The web application was packaged in a Docker container for easy scaling and moving between servers. A cloudflare service was connected to protect against bot attacks, allowing the infrastructure to scale without fear of external interference. The app contains guides that teachers can customise to explain different utilities clearly.

&#128202; I realised:
1. Desctop application
2. Web application
3. Api
4. Universally Unique Identifier
5. DB

## &#128242; Web app for all platforms <a href="https://www.rjomba.com">StegLove</a> 
## &#128187; App for win64 <a href="https://github.com/Cpp-Gleb/StegLove/releases/tag/1.2">Download</a> 
## 🌐 Readme translations <a href="https://github.com/Cpp-Gleb/StegLove/tree/main/Translations">Click</a> 

<p><br><br><br><a href="https://github.com/Cpp-Gleb/StegLove/releases/tag/1.2"><img src="https://github.com/user-attachments/assets/e6337c95-a83e-4d61-b220-80b3e8e97288" href="https://rjomba.com" width="140" height="40" /> </a></p>
