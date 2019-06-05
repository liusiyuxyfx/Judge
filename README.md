# Study on the Auto-evaluation of Students’ Solutions in the Education Big Data of MOOC Platform

### Description
My graduation design for HRBUC  

### Introduction
With the gradual popularization of network teaching technology, teachers need  more comprehensive student feedback from the network. In order to solve the problem that teachers hard to get and evaluate the the advantages and disadvantages of student solutions in the discussion area for school students in the MOOC platform, the system mainly uses the web crawler technology and the similarity calculation algorithm based on tf-idf algorithm and cosine similarity to realize auto-evaluation of students’ solutions.The system can crawl the website data in the discussion area, and get the detail of problems and all the students’ solution by Data Cleaning technology.Then, the system can calculate the similarity between the standard answer and students’ solution and give a score, it can also make a summary graph and save all the result to the database.The system can display processed results intuitively and allow teachers to modify information of students and questions within the database,it can also output the result as an Excel document. The system can effectively help teachers make intuitive judgment on students' questions and answers, optimizing the teaching process thusly.  

### Develop Environment
System: Macos 10.14  
Language: Python 3.7  
IDE: Jetbrains Pycharm Professional   
Related libraries:  
* Webcrawler   
selenium, chromedriver, requests, urllib3
* NLP  
scikit-learn
* Data-clean  
re
* Painting  
wordcloud(only for Mac and Linux), matplotlib
* UI  
pyqt
* Database  
pymysql
Database: Mysql 8.0  
