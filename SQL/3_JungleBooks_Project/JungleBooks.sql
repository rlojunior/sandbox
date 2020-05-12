DROP DATABASE IF EXISTS JungleBooks;
CREATE DATABASE JungleBooks;
USE JungleBooks;


-- Create Tables
CREATE TABLE Author (
  ID        INT(10) NOT NULL,
  FirstName VARCHAR(32) NOT NULL,
  LastName  VARCHAR(32) NOT NULL,
  PRIMARY KEY (ID));
CREATE TABLE Author_written_books (
  Book_descriptionISBN VARCHAR(17) NOT NULL,
  AuthorID             INT(10) NOT NULL,
  PRIMARY KEY (Book_descriptionISBN,
  AuthorID));
CREATE TABLE Book_category (
  ID   INT(10) NOT NULL,
  Name VARCHAR(32) NOT NULL,
  PRIMARY KEY (ID));
CREATE TABLE Book_description (
  ISBN    VARCHAR(17) NOT NULL,
  Title   VARCHAR(32) NOT NULL,
  Summary VARCHAR(500) NOT NULL,
  Price   FLOAT NOT NULL,
  PRIMARY KEY (ISBN));
CREATE TABLE Book_description_Book_category (
  Book_descriptionISBN VARCHAR(17) NOT NULL,
  Book_categotyID      INT(10) NOT NULL,
  PRIMARY KEY (Book_descriptionISBN,
  Book_categotyID));
CREATE TABLE Customer (
  Username        VARCHAR(32) NOT NULL,
  Password        VARCHAR(80) NOT NULL,
  FirstName       VARCHAR(32) NOT NULL,
  LastName        VARCHAR(32) NOT NULL,
  BillingAddress  VARCHAR(80) NOT NULL,
  ShippingAddress VARCHAR(80) NOT NULL,
  Phone           VARCHAR(13) NOT NULL,
  email           VARCHAR(32) NOT NULL,
  PRIMARY KEY (Username));
CREATE TABLE `Order` (
  OrderNumber         INT(11) NOT NULL,
  Book_descriptionISBN VARCHAR(17) NOT NULL,
  CustomerUsername     VARCHAR(32) NOT NULL,
  DateOrder            DATETIME NOT NULL,
  DateShpiped          DATETIME,
  Satus                VARCHAR(32) NOT NULL,
  Subtotal             FLOAT NOT NULL,
  Taxes                FLOAT NOT NULL,
  Quantity             INT(3) NOT NULL,
  PRIMARY KEY (Book_descriptionISBN, CustomerUsername));
ALTER TABLE Book_description_Book_categoty ADD CONSTRAINT FKBook_descr962506 FOREIGN KEY (Book_descriptionISBN) REFERENCES Book_description (ISBN);
ALTER TABLE Book_description_Book_categoty ADD CONSTRAINT FKBook_descr973372 FOREIGN KEY (Book_categotyID) REFERENCES Book_categoty (ID);
ALTER TABLE Author_written_books ADD CONSTRAINT FKAuthor_wri762314 FOREIGN KEY (Book_descriptionISBN) REFERENCES Book_description (ISBN);
ALTER TABLE Author_written_books ADD CONSTRAINT FKAuthor_wri437428 FOREIGN KEY (AuthorID) REFERENCES Author (ID);
ALTER TABLE `Order` ADD CONSTRAINT FKOrder988679 FOREIGN KEY (CustomerUsername) REFERENCES Customer (Username);
ALTER TABLE `Order` ADD CONSTRAINT FKOrder614152 FOREIGN KEY (Book_descriptionISBN) REFERENCES Book_description (ISBN);

-- DML commands

-- Add three books
INSERT INTO AUTHOR (ID, FIRSTNAME, LASTNAME)
    VALUES (1, "Dan", "Brown"),
           (2, "Ramez", "Elmasri"),
           (3, "Shamkant", "Navathe");

INSERT INTO BOOK_DESCRIPTION (ISBN, TITLE, SUMMARY, PRICE)
    VALUES ("9780385514231","Origin: A Novel","In keeping with his trademark style, Dan Brown, author of The Da Vinci Code and Inferno, interweaves codes, science, religion, history, art, and architecture into this new novel. Origin thrusts Harvard symbologist Robert Langdon into the dangerous intersection of humankind’s two most enduring questions, and the earthshaking discovery that will answer them.", 27.00),
       ("9781400079148","The Lost Symbol","In this stunning follow-up to the global phenomenon The Da Vinci Code, Dan Brown demonstrates once again why he is the world’s most popular thriller writer. The Lost Symbol is a masterstroke of storytelling that finds famed symbologist Robert Langdon in a deadly race through a real-world labyrinth of codes, secrets, and unseen truths . . . all under the watchful eye of Brown’s most terrifying villain to date.",12.80),
       ("9780133970777","Fundamentals of Database Systems","This book introduces the fundamental concepts necessary for designing, using, and implementing database systems and database applications. Our presentation stresses the fundamentals of database modeling and design, the languages and models provided by the database management systems, and database system implementation techniques.",185.60);

INSERT INTO AUTHOR_WRITTEN_BOOKS (BOOK_DESCRIPTIONISBN, AUTHORID)
    VALUES ("9780385514231", 1),
           ("9781400079148", 1),
           ("9780133970777", 2),
           ("9780133970777", 3);

INSERT INTO BOOK_CATEGOTY (ID, NAME)
    VALUES (1,"Fiction"),
           (2, "Textbook");

INSERT INTO BOOK_DESCRIPTION_BOOK_CATEGOTY (BOOK_DESCRIPTIONISBN, BOOK_CATEGOTYID)
    VALUES ("9780385514231",1),
           ("9781400079148",1),
           ("9780133970777",2);



-- Create customer information for four fictitious people and add their
-- information to the database.

INSERT INTO Customer (Username, Password, FirstName, LastName, BillingAddress, ShippingAddress, Phone, email)
    VALUES ("mdbmysql", "aasasdes", "Maria", "Dibiase","221 Washmill Lake Dr.", "221 Washmill Lake Dr.", "902-222-3323","mdb@mysql.com");

INSERT INTO Customer (Username, Password, FirstName, LastName, BillingAddress, ShippingAddress, Phone, email)
    VALUES ("coolbill", "12345", "William", "Miller","325 Leeds St.", "221 Rosemeade Av.", "902-233-5544","bill@mysql.com"),
    ("marybeauty", "Acs$$212", "Mary", "Filomena","777 Robie St.", "777 Robie St.", "902-555-7763","mfilomena@mysql.com"),
    ("mrsmith", "abcdef$", "John", "Smith","2212 Robie St.", "2212 Robie St.", "902-111-3232","mrsmith@mysql.com");


-- Create three new orders
    -- § Customer 1 buys one copy of all three books
        -- obs.: I'm not going to add the shipping date in this query
INSERT INTO `Order` (OrderNumber ,Book_descriptionISBN, CustomerUsername, DateOrder, Satus, Subtotal, Taxes, Quantity)
    VALUES (1,"9780385514231","mdbmysql","2019-11-20 20:50:40.999999","pending confirmation",27,0.13,1),
           (1,"9781400079148","mdbmysql","2019-11-20 20:55:59.999999","pending confirmation",12.8,0.13,1),
            (1,"9780133970777","mdbmysql","2019-11-20 21:00:50.999999","pending confirmation",185.60,0.13,1);


    -- § Customer 2 buys just one of the books
INSERT INTO `Order` (OrderNumber, Book_descriptionISBN, CustomerUsername, DateOrder, Satus, Subtotal, Taxes, Quantity)
    VALUES (2,"9780385514231","coolbill","2019-11-22 17:50:40.999999","pending confirmation",27,0.13,1);

    -- § Customer 3 buys five copies of one book, two copies of the second
INSERT INTO `Order` (OrderNumber,Book_descriptionISBN, CustomerUsername, DateOrder, Satus, Subtotal, Taxes, Quantity)
    VALUES (3,"9781400079148","marybeauty","2019-11-22 15:30:40.999999","pending confirmation", 5*12.8,0.13,5),
        (3,"9780133970777","marybeauty","2019-11-22 15:50:40.999999","pending confirmation", 2*185.60,0.13,2);

    --  and ten copies of the third
INSERT INTO `Order` (OrderNumber,Book_descriptionISBN, CustomerUsername, DateOrder, Satus, Subtotal, Taxes, Quantity)
    VALUES (3,"9780385514231","marybeauty","2019-11-22 15:30:40.999999","pending confirmation", 10*27,0.13,10);


-- Delete the second order
DELETE FROM `Order` WHERE Book_descriptionISBN = "9780385514231" AND CustomerUsername = "coolbill";

-- Change the status of the first order to complete.
UPDATE `Order`
    SET Satus = "complete"
    WHERE CustomerUsername = "mdbmysql";

-- Change the third order to add another copy of the second book.
UPDATE `Order`
   SET Quantity = 3, Subtotal = 3*185.60, DateOrder = now()
    WHERE Book_descriptionISBN = "9780133970777" AND CustomerUsername = "marybeauty";


-- Display all customer information for customers that have no orders.
SELECT * FROM Customer C
LEFT OUTER JOIN `Order` O
ON C.Username = O.CustomerUsername
WHERE O.Quantity IS NULL;

-- Display the title, author, ISBN and price of all books related to databases.
SELECT TITLE, B.ISBN,A.FIRSTNAME AS Author_Fist_Name, A.LASTNAME AS Author_Last_Name, B.Price
    FROM BOOK_DESCRIPTION B
    INNER JOIN AUTHOR_WRITTEN_BOOKS W ON W.BOOK_DESCRIPTIONISBN = B.ISBN
    INNER JOIN AUTHOR A ON A.ID = W.AUTHORID
    INNER JOIN BOOK_DESCRIPTION_BOOK_CATEGOTY BB ON B.ISBN = BB.BOOK_DESCRIPTIONISBN
    INNER JOIN BOOK_CATEGOTY BC ON BC.ID = BB.BOOK_CATEGOTYID
    WHERE Title LIKE "%database%";

-- Display the email addresses of customers who have outstanding orders.
SELECT C.email FROM Customer C
    INNER JOIN `Order` O on O.CustomerUsername = C.Username
    WHERE O.DateShpiped IS NULL;

-- Display just the order information (i.e. not the order details) on all orders
-- that have purchased more than one copy of any of the books.
SELECT Title, Quantity FROM `Order` O
    INNER JOIN Book_description B ON B.ISBN = O.Book_descriptionISBN
    WHERE O.Quantity >1;


-- Display the order number and the total number of books in each order.
-- This will be used to calculate shipping costs.
SELECT OrderNumber, Title,Quantity FROM `Order` O
    INNER JOIN Book_description B ON B.ISBN = O.Book_descriptionISBN
    ORDER BY OrderNumber;


-- Display each order number, customer name and the total cost of their
-- order by adding the cost of all the items.

-- Cost of each book purchase
SELECT OrderNumber, Title,Quantity,ROUND(Quantity*Price,2) AS Cost,ROUND(Quantity*Price*1.15,2) AS 'Cost + 15% Tax' FROM `Order` O
    INNER JOIN Book_description B ON B.ISBN = O.Book_descriptionISBN
    ORDER BY OrderNumber;

-- Total Cost
SELECT OrderNumber,FirstName AS Customer_First_Name,LastName AS Customer_Last_Name, SUM (ROUND(Quantity*Price*1.15,2)) AS Order_Total_Cost FROM `Order` O
    INNER JOIN Book_description B ON B.ISBN = O.Book_descriptionISBN
    INNER JOIN Customer C ON CustomerUsername = Username
    GROUP BY OrderNumber;