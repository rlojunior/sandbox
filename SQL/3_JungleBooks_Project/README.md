# About this folder
Develop a database for an online book retailer, Jungle.com. The application will be the online ordering system for Jungle.com
which will allow clients to view information about different books, add them to their
“shopping cart” and when they are done selecting their books, proceed to checkout and
pay for their books.

## Requirements:
1. The database must hold information about the products the company is selling
(i.e. books). Each book consists of a title, a brief summary, an author (or authors),
an ISBN, a price and any additional information you deem necessary.

2. The database must hold information about book categories (e.g. Science Fiction,
Non-Fiction, etc). A particular book can have multiple categories (e.g. Children’s
Books and Fiction).

3. The database must hold information about the customers who are purchasing the
books. The customers must submit their full names, billing address, shipping
address, phone number, and email address. When they register, they will provide
a username and password in order to login to their account.

4. The database must hold information about the customers’ orders. Each order is
given a unique order number, the date ordered, the date shipped, the status of the
order (e.g. pending confirmation, in progress, completed, etc), the subtotal of the
order, the taxes, the total cost and, of course, each order consists of one or more
products that are being purchased.

5. The database must hold information about each item on the order. The item’s
information will contain the product being purchased, the quantity being
purchased and the subtotal of each line item.

6. A completed Entity-Relationship diagram is needed before the database can be
constructed. The ERD should have all information required to complete the
database design and should be carefully and professionally laid out using Visual
Paradigm.

7. A SQL script is required with all the SQL statements necessary to create the
database, the tables and the foreign keys.

8. Since you are not working on the web portion of the database, you must test all
the database functionality using standard SQL statements. These statements
would then be given to the web developers to complete the front-end.

9. The database will require the following tests:
	* Add three books of your choice, their information and their categories to
	the database.
	* Create customer information for four fictitious people and add their
	information to the database.
	* Create three new orders
		* Customer 1 buys one copy of all three books
		* Customer 2 buys just one of the books
		* Customer 3 buys five copies of one book, two copies of the second
		and ten copies of the third
	* Delete the second order
	* Change the status of the first order to complete.
	* Change the third order to add another copy of the second book.
	* Display all customer information for customers that have no orders. (i.e.
	the count of their order ids is zero)
	* Display the title, author, ISBN and price of all books related to databases.
	(i.e. contain the word “database” or are in the “database” category)
	* Display the email addresses of customers who have outstanding orders.
	(i.e. orders that have no ship date yet)
	* Display just the order information (i.e. not the order details) on all orders
	that have purchased more than one copy of any of the books. (e.g. two
	copies of book one, three copies of book three, etc)
	* Display the order number and the total number of books in each order.
	This will be used to calculate shipping costs.
	* Display each order number, customer name and the total cost of their
	order by adding the cost of all the items. (Determine each cost by using
	the quantity and price and adding 15% tax).


## Files in this folder
* **JungleBooks.sql** - A complete database creation script
* **ERD.png** - An Entity-Relationship Diagram



*Fall Term/2019 - Project #5*