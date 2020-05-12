# About this folder
Design a database using MongoDB.

## Context
The local community college has decided to update their aging learning management
system (LMS) to give their students better access to course content, grades and feedback.
They are currently calling this new system Crave2Know.


## Requirements:
1. The database will need to hold information about the students, including their
names, student numbers, passwords and personal details (e.g. phone numbers,
address, etc.).

2. The database will also hold information about the courses, including their names,
descriptions and course code.

3. Each course can be delivered multiple times and each instance of a course will
need to be stored in the database with its start and end dates, and the list of
students enrolled in the course.

4. Each delivered course will have its own list of assignments that will be used to
evaluate the enrolled students.

5. Each student enrolled in each course will be able to view their individual
assignment marks and text feedback for each assignment, as well as the total
grade for the course.

6. A completed Entity-Relationship diagram is needed before the database can be
constructed. The ERD should have all information required to complete the
database design and should be carefully and professionally laid out using Visual
Paradigm.

7. A MongoDB script is required with all the NoSQL statements necessary to create
the database, the collections, and perform the following actions:
	* Add the following students:
		* Jill Hill (W0111222), Mike Pike (W0222333), Steve Cleve (W0333444)
	* Add the following courses:
		* Data Fundamentals (DBAS1007), Programming (PROG1700)
	* Create a new instance of the Data Fundamentals course that starts on Sept.7,
	2018 and ends on Dec.14, 2018
	* Create a new instance of the Programming course that starts on Jan. 4, 2019
	and ends on Apr. 24, 2019
	* Enroll Jill and Mike in the instance of the Data Fundamentals course and Jill
	and Steve in the instance of the Programming course
	* Create two assignments in the database course and one assignment in the
	programming course
	* Give the following database assignment grades to Jill
		* Assignment 1: 95 and Assignment 2: 87
	* Remove Steve from the programming course
	* Update Jill’s total grade for Programming to a 78
	* Display a list of all courses
	* Display the last name of the student with the student number of W0333444
	* Display a list of the assignment grades for student number W0111222
	* Display a list of courses that are being delivered after January 1st, 2019


## Files in this folder

* **Crave2Know.js** - A complete database creation script
* **ERD.png** - An Entity-Relationship Diagram



*Fall Term/2019 - Project #6*