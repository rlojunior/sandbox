## New requirements for this step 
To test the design of my Issue Tracking Database by using standard queries to add,
update, delete and retrieve information to/from the database.
* INSERT Statments
* DELETE Statements
To test the deleting of records create the following DELETE statements:
	1. Delete a user that has created a ticket
	2. Delete a support staff member that is currently assigned to a ticket
	3. Delete a ticket that has a task and a comment
	4. Delete a hardware that has more than one ticket

* UPDATE Statements
...To test that I can easily modify information stored in my database I will
...develop the following UPDATE statements:
	1. Assign a staff member to a ticket
	2. Change the status of a ticket to completed (or the like)
	3. Change the user id (primary key), for a user that has created tickets, to a new
	value

* SELECT Statements
...To test the retrieval of information from your database, you will develop the
...following SELECT statements:
	1. Retrieve a list of all open tickets
	2. Retrieve a list of tickets reported after Mar. 1, 2020 at 4:30PM and before
	Mar. 4, 2010 at 8:30AM
	3. Retrieve a list of all tickets for three specific categories
	4. Retrieve a list of tickets assigned to a particular staff member and ordered by
	assigned date
	5. Retrieve a list of users’ names and the number of tickets created by each
	user. Display zero (0) for those users that have not created any tickets and
	order the list by the user’s last names.
	6. Retrieve a list of ticket titles that have comments with the phrase “initial
	comment” somewhere in the text
	7. Retrieve a list of the categories for tickets than have more than two (2) active
	tasks that have not been assigned to any staff member


### Files you will find here:

* **SpeedingTickets.sql** - The Structured Query Language (SQL) script necessary to implement my database
design on Microsoft SQL Server 2019.

* **ERD.pdf** - An Entity-Relationship Diagram for your ticket database using Visual
Paradigm. This ERD include some modifications needed to correct my initial
database design (showed in Step_1 folder)

* **Data_Dictionary.md** - A Data Dictionary document that contains enough information to
completely document my database design. With the modifications included.
