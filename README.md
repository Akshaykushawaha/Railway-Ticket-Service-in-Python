# Railway-Ticket-Service-in-Python
This project is based on a python program made by me on train ticket reservation service in class 11, this year I have upgraded the program and implemented many of the things that we have learnt in class 12. In this program there are basically 5 services which we can choose and after getting the desired output, the program will confirm if now we want any other services, satisfying which the program loops back.
I have introduced in the program the concept of functions, file handling and Python-Mysql connector.
<br />The main program being- 
1) Ticket reservation:- 
<br />•Is a big program in which there are many choices that we need to make like train’s name, to enter starting and ending destinations, class of coach etc.
<br />•The program uses tuples to store the names of destinations, trains and coach.
<br />•The no. of seats available and the cost of seats are chosen with random function to get different values each time.
<br />•After entering our choices we are shown the bill of the ticket and also asked if we need to book any other tickets where we can choose to book tickets from same train or a new one.
<br />•While booking tickets and showing bills, there are 2 more things that can be operating as well depending on our choice:-
<br />i) Mysql connector which enters the record of the bill in a table named “tt_bill” in database “class12”. 
<br />ii) And File handling program that enters each bill in a text document named as “tts_bill”, this is saved as a copy of the bill for the ticket.
<br />•At the end of the 1st program we are asked if we want to read the copy of the bill from the text document, if yes then the text document is read and printed.(This we can use to ensure if the text document is created properly or not)
<br />•The whole program is having ‘while loops’ at various steps to check whether the input is correct, if it doesn’t comply with the required parameters then the loop will continue until the correct input is given.
<br />•And at last again we are asked if we need any other service. 
<br />The other minor (simple) services are:-
2) Enquire about ticket’s waiting list- output is a simple statement which displays a number which we can sms our ticket no. to get our ticket status.
3) Get your ticket printed – we are given a site to visit where we can get it printed.
4) Track a Train's live location – we are given a number which we can sms our train number to get the location of the train.
5) To connect to our customer care- A number gets printed to call to connect to customer care.
