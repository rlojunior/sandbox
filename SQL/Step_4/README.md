## New requirements for this step 

My task is to build the following queries, encapsulated as procedures or functions,
and, if necessary, change my database to support them.

1. Display a list of all tickets submitted within a given month of the current year.
...The month will be supplied to the routine as a word (e.g. April)
2. Display a list of the top 10 tickets that have had the most activity in the form
...of comments. A start date and end date will be supplied to the routine in the
...form ‘yyyy-mm-dd’.
3. Display a list of tickets for a particular category, ordered by descending date,
...with the corresponding date displayed in the format (Month dddd, yyyy) e.g.
...November 21st, 2009. A category name will be supplied to the routine.
4. Return the total number of active tasks for a given support staff member. An
...employee number will be supplied to the routine. The routine should also
...return zero (0), if there are no active tasks for that person, and negative one
...(-1), if the support staff member could not be found.
5. Display a “page” of ticket information by passing, to the routine, a page
...number and the number of tickets per page. For example, passing “1,10” will
...return the first ten tickets (ordered by ticket id), but passing “2,10” will
...return next ten tickets (i.e. page 2).


### Files you will find here:

*DDL_Script.sql
...This is the script I have been using for the previous Steps
...to create the database, including any new changes
.

*Test_Data_Script.sql 
...This will include any and all test data that I want inserted into the database before 
...my Speeding Tickets SQL script can be used
.

*SpeedingTickets.sql
...This will include answers to the questions on the requirements (shown above), which will include all the statements 
...to create the necessary functions and procedures, along with the 'exec' 
...statements used to test the procedures
 


*
ERD.JPG
...A final ERD that includes any changes needed.


*Data_Dictionary.md
...A final Data Dictionary that includes everything

