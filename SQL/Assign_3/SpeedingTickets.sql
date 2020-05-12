USE master;
GO

ALTER DATABASE SpeedingTickets SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
GO

DROP DATABASE IF EXISTS SpeedingTickets;
CREATE DATABASE SpeedingTickets;
GO

USE SpeedingTickets;
GO

DROP TABLE IF EXISTS Category;
CREATE TABLE Category
(
    CategoryID INT IDENTITY NOT NULL,
    Name       VARCHAR(80)  NOT NULL,
    PRIMARY KEY (CategoryID)
);

DROP TABLE IF EXISTS Comment;
CREATE TABLE Comment
(
    CommentID    INT  IDENTITY NOT NULL,
    TicketID     INT          NOT NULL,
    TechnicianID INT          NULL,
    UserID       INT          NULL,
    Comment      VARCHAR(255) NOT NULL,
    PRIMARY KEY (CommentID,
                 TicketID)
);


DROP TABLE IF EXISTS HardwareInfo;
CREATE TABLE HardwareInfo
(
    HardwareInfoID  INT IDENTITY NOT NULL,
    HardwareDetails VARCHAR(255) NOT NULL,
    PRIMARY KEY (HardwareInfoID)
);

DROP TABLE IF EXISTS TechnicianInfo;
CREATE TABLE TechnicianInfo
(
    TechnicianInfoID INT IDENTITY NOT NULL,
    Name             VARCHAR(80)  NOT NULL,
    Contact          VARCHAR(32)  NOT NULL,
    PRIMARY KEY (TechnicianInfoID),
    CONSTRAINT CK__TechnicianInfo__Contact CHECK (Contact LIKE '%_@__%.__%')
);

GO


-- ALTER TABLE TechnicianInfo DROP CONSTRAINT AK__TechnicianInfo__Contact;
ALTER TABLE TechnicianInfo
    ADD CONSTRAINT AK__TechnicianInfo__Contact UNIQUE (Contact);

CREATE INDEX IX__TechnicianInfo__Contact
    ON TechnicianInfo (Contact);


DROP TABLE IF EXISTS Ticket;
CREATE TABLE Ticket
(
    TicketID            INT IDENTITY NOT NULL,
    Title               VARCHAR(255) NOT NULL,
    CategoryID          INT          NOT NULL,
    UserID              INT          NULL,
    AssignTechnicianID  INT          NULL,
    Date                DATETIME     NOT NULL,
    IsSolved            CHAR(1)      NOT NULL,
    SolvedDate          DATETIME     NULL,
    DetailsOfTheIssue   VARCHAR(255) NOT NULL,
    AuthorTechnicianID  INT          NULL,
    PRIMARY KEY (TicketID),

    CONSTRAINT CK__Ticket__IsSolved CHECK (IsSolved = 'Y' OR IsSolved = 'N' )
);
GO

--ALTER TABLE Ticket DROP CONSTRAINT DF__Ticket__Date;
ALTER TABLE Ticket
    ADD CONSTRAINT DF__Ticket__Date DEFAULT GETDATE() FOR Date;



DROP TABLE IF EXISTS ActionsToDoInFuture;
CREATE TABLE ActionsToDoInFuture
(
    ActionsToDoInFutureID INT IDENTITY NOT NULL,
    TicketID                INT NOT NULL,
    Action                VARCHAR(255) NULL,
    PRIMARY KEY (ActionsToDoInFutureID,
                 TicketID)
);

GO

DROP TABLE IF EXISTS TicketHardwareInfo;
CREATE TABLE TicketHardwareInfo
(
    TicketID   INT NOT NULL,
    HardwareID INT NOT NULL,
    PRIMARY KEY (TicketID,
                 HardwareID)
);



DROP TABLE IF EXISTS UserInfo;
CREATE TABLE UserInfo
(
    UserInfoID INT NOT NULL,
    Name       VARCHAR(80)  NOT NULL,
    LastName VARCHAR(80)  NOT NULL,
    Department VARCHAR(32)  NOT NULL,
    Contact    VARCHAR(32)  NOT NULL,
    PRIMARY KEY (UserInfoID),
    CONSTRAINT CK__Userinfo__Contact CHECK (Contact LIKE '%_@__%.__%')
);

--ALTER TABLE UserInfo DROP CONSTRAINT AK__UserInfo__Contact;


ALTER TABLE UserInfo
    ADD CONSTRAINT AK__UserInfo__Contact UNIQUE (Contact);

CREATE INDEX IX__UserInfo__Contact
    ON UserInfo (Contact);

GO

--ALTER TABLE Comment DROP CONSTRAINT FK__Comment_Ticket__TicketID;
--ALTER TABLE Comment DROP CONSTRAINT FK__TechnicianInfo__ID;
--ALTER TABLE Comment DROP CONSTRAINT FK__UserInfo__ID;
ALTER TABLE Comment
    ADD CONSTRAINT FK__Comment_Ticket__TicketID FOREIGN KEY (TicketID) REFERENCES Ticket (TicketID) ON DELETE CASCADE;
ALTER TABLE Comment
    ADD CONSTRAINT FK__TechnicianInfo__ID FOREIGN KEY (TechnicianID) REFERENCES TechnicianInfo (TechnicianInfoID) ON DELETE CASCADE;

ALTER TABLE Comment
    ADD CONSTRAINT FK__UserInfo__ID FOREIGN KEY (UserID) REFERENCES UserInfo (UserInfoID) ON DELETE CASCADE ON UPDATE CASCADE ;
GO



--ALTER TABLE Ticket DROP CONSTRAINT FK__UserInfo__UserInfoID;
--ALTER TABLE Ticket DROP CONSTRAINT FK__Category__CategoryID;
--ALTER TABLE Ticket DROP CONSTRAINT FK__TechnicianInfo__TechnicianInfoID;
ALTER TABLE Ticket
    ADD CONSTRAINT FK__Ticket_UserInfo__UserInfoID FOREIGN KEY (UserID) REFERENCES UserInfo (UserInfoID) ON DELETE SET NULL ON UPDATE CASCADE ;
ALTER TABLE Ticket
    ADD CONSTRAINT FK__Ticket_TechnicianInfo__TechnicianInfoID FOREIGN KEY (AssignTechnicianID) REFERENCES TechnicianInfo (TechnicianInfoID) ON DELETE SET NULL ;
ALTER TABLE Ticket
    ADD CONSTRAINT FK__Category__CategoryID FOREIGN KEY (CategoryID) REFERENCES Category (CategoryID) ON DELETE CASCADE;


GO

--ALTER TABLE TicketHardwareInfo DROP CONSTRAINT FK__Ticket__TicketID;
--ALTER TABLE TicketHardwareInfo DROP CONSTRAINT FK__HardwareInfo__ID;
ALTER TABLE TicketHardwareInfo
    ADD CONSTRAINT FK__Ticket__TicketID FOREIGN KEY (TicketID) REFERENCES Ticket (TicketID) ON DELETE CASCADE;
ALTER TABLE TicketHardwareInfo
    ADD CONSTRAINT FK__HardwareInfo__ID FOREIGN KEY (HardwareID) REFERENCES HardwareInfo (HardwareInfoID) ON DELETE CASCADE;


GO

--ALTER TABLE ActionsToDoInFuture DROP CONSTRAINT FK__ActionsToDoInFuture__TicketID;
ALTER TABLE ActionsToDoInFuture
    ADD CONSTRAINT FK__ActionsToDoInFuture__TicketID FOREIGN KEY (TicketID) REFERENCES Ticket (TicketID) ON DELETE CASCADE ;

GO

-- Inserting
INSERT INTO Category (Name) VALUES
    ('Hardware'),
    ('Software'),
    ('Internet'),
    ('Phone'),
    ('Other');


INSERT INTO UserInfo(UserInfoID, Name, LastName, Department, Contact) VALUES
    (1,'Reynaldo','Junior','HR','rey@company.com'),
    (2,'Carlos','Ramos','Accountability','carlos@company.com'),
    (3,'Maria','Soledad','HR','maria@company.com'),
    (4,'John','Smith','Sales','john@company.com'),
    (5,'Sarah','Burns','Customer Service','sarah@company.com'),
    (6,'Tom','Soyer','Clerck','tom@company.com');

INSERT INTO TechnicianInfo (Name, Contact) VALUES
    ('Beatriz','bia@company.com'),
    ('Martinez','matin@company.com'),
    ('Bob','bob@company.com'),
    ('Bill','bill@company.com'),
    ('Mona','mona@company.com');

INSERT INTO Ticket (Title, CategoryID, UserID, AssignTechnicianID,IsSolved, DetailsOfTheIssue) VALUES
    ('The mouse is not working',1,3,1,'N','When I try to click on mouse it doesnt respond' ),
    ('The computer is not connecting to the internet',3,1,2,'N','I cannot use internet when i`m logged'),
    ('I forgot my password',5,2,2,'N','I would like to reset my password. I cannot remenber it'),
    ('The screen is not working properly',1,3,3,'N','The screen turns on but display nothing'),
    ('My computer is too slow',5,1,4,'N','It takes a long time to open a software'),
    ('I cannot make a call',4,5,5,'N','I can call to other departments but I cannot make a call to a number outside the company');

INSERT INTO Ticket(title, categoryid, userid, assigntechnicianid, issolved, solveddate, detailsoftheissue, authortechnicianid) VALUES
    ('The user cannot access his email',3,2,4,'Y','2020-03-13 10:05:00.000','The webserver was not connecting',4);


INSERT INTO Ticket(title, categoryid, userid, assigntechnicianid, issolved, detailsoftheissue) VALUES
    ('I cannot access a specific website',3,2,NULL,'N','I can access the internet but the local newspaper website is not opening');


INSERT INTO Comment (TicketID, TechnicianID, UserID, Comment) VALUES
    (1,1,3,'From technician: can you tell me the name of the mouse manufacturer?'),
    (1,1,3,'From user: It is a Dell mouse');

INSERT INTO Comment (TicketID, TechnicianID, UserID, Comment) VALUES
    (2,2,1,'From technician: When was the last time you have connected to the internet?'),
    (2,2,1,'From user: Yesterday worked fine, but today when I turned on my computer it didnt connected');

INSERT INTO Comment (TicketID, TechnicianID, UserID, Comment) VALUES
    (3,2,2,'From technician: I will create a defaut password then you can change it later'),
    (3,2,2,'From user:Ok. Thanks');

INSERT INTO Comment (TicketID, TechnicianID, UserID, Comment) VALUES
    (4,3,3,'From technician: When exactly this problem happened? '),
    (4,3,3,'From user: This problem started when I moved the computer to a new desk');

INSERT INTO Comment (TicketID, TechnicianID, UserID, Comment) VALUES
    (5,4,1,'From technician: Did you install any software recently?'),
    (5,4,1,'From user: Yes. I did. I installed Autocad on my machine');

INSERT INTO Comment (TicketID, TechnicianID, UserID, Comment) VALUES
    (6,5,5,'From technician: Is your department coleagues having the same problem?'),
    (6,5,5,'From user: No, Just me');

INSERT INTO HardwareInfo (HardwareDetails) VALUES
    ('Dell Wireless Mouse-WM126'),
    ('Dell - XPS 15 Laptop - 8GB DDR4-2666MHz, 2x4G'),
    ('Dell - Inspiron 15 3000 Laptop'),
    ('Dell - Inspiron Desktop - 12GB, DDR4, 2666MHz'),
    ('Dell - Inspiron 22 3000 Touch All-in-One Desktop'),
    ('Dell - ooma DP1-O - Wireless digital phone - DECT 6.0');

INSERT INTO TicketHardwareInfo (TicketID, HardwareID) VALUES
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,4);

INSERT INTO ActionsToDoInFuture (TicketID, Action) VALUES
    (1,'Buy a new mouse'),
    (5,'Need to clean temporary files'),
    (5,'Need to defrag the HD');

-- DELETE Statements
--A. Delete a user that has created a ticket
    --Checking the users that has a ticket
    SELECT DISTINCT UserID, count(UserID) FROM Ticket GROUP BY UserID;
    --Deleting the user
    DELETE FROM UserInfo WHERE UserInfoID = 5;

--B. Delete a support staff member that is currently assigned to a ticket
    --Checking the technician that has been assigned
    SELECT DISTINCT AssignTechnicianID, count(AssignTechnicianID) FROM Ticket GROUP BY AssignTechnicianID;
    --Deleting the technician
    DELETE FROM TechnicianInfo WHERE TechnicianInfoID = 3;

--C. Delete a ticket that has a task and a comment
    --Checking which tickets have a comment AND a task (In my case I named task as ActionsToDoInFuture)
    SELECT C.TicketID FROM Comment C
    INNER JOIN ActionsToDoInFuture A
    ON C.TicketID = A.TicketID;
    --Deleting ticket
    DELETE FROM Ticket WHERE TicketID=1;

--D. Delete a hardware that has more than one ticket
    --Checking which hardware has more than one ticket
     DELETE FROM HardwareInfo WHERE HardwareInfoID = (SELECT DISTINCT HardwareID
            FROM TicketHardwareInfo GROUP BY HardwareID HAVING count(HardwareID) >1);


-- UPDATE Statements
--A. Assign a staff member to a ticket
    -- Checking which ticket doesn`t have an assign technician
    SELECT TicketID, AssignTechnicianID FROM Ticket;
    UPDATE Ticket
        SET AssignTechnicianID = 5
        WHERE TicketID = 4;

--B. Change the status of a ticket to completed (or the like)
    SELECT TicketID, IsSolved,SolvedDate FROM Ticket;
    UPDATE Ticket
        SET IsSolved = 'Y', SolvedDate = '2020-03-13 10:05:00.000'
        WHERE TicketID = 5;

--C. Change the user id (primary key), for a user that has created tickets, to a new value
SELECT * FROM UserInfo;

UPDATE UserInfo
    SET UserInfoID = 20
    WHERE  Name = 'Carlos';


-- SELECT Statements
--A. Retrieve a list of all open tickets
SELECT * FROM Ticket WHERE IsSolved = 'N';
-- Or
SELECT * FROM Ticket WHERE SolvedDate IS NULL;

--B. Retrieve a list of tickets reported after Mar. 1, 2020 at 4:30PM and before
--Mar. 4, 2010 at 8:30AM
SELECT * FROM Ticket;

-- Because my ticket dates is out of the required date range, I'm going to insert some test data:

INSERT INTO Ticket (title, CategoryID, UserID, AssignTechnicianID, Date, IsSolved, SolvedDate, DetailsOfTheIssue, AuthorTechnicianID) VALUES
('**TEST**', 1,1,1,'2020-02-13 09:05:00.000','N',NULL,'**TEST**',NULL), -- Ticket before Mar. 1, 2020
('**TEST**', 1,1,1,'2020-02-10 08:03:00.000','N',NULL,'**TEST**',NULL), -- Ticket before Mar. 1, 2020
('**TEST**', 1,1,1,'2020-03-01 09:05:00.000','N',NULL,'**TEST**',NULL), -- Ticket on Mar. 1, 2020 before 4:30PM
('**TEST**', 1,1,1,'2020-03-01 17:10:00.000','N',NULL,'**TEST**',NULL), -- In range
('**TEST**', 1,1,1,'2020-03-02 09:10:00.000','N',NULL,'**TEST**',NULL), -- In range
('**TEST**', 1,1,1,'2020-03-05 17:10:00.000','N',NULL,'**TEST**',NULL); -- Ticket after Mar. 4, 2010

SELECT * FROM Ticket WHERE Date BETWEEN '2020-03-01 16:30:00.000' AND '2020-03-04 08:30:00.000';


--C. Retrieve a list of all tickets for three specific categories
SELECT * FROM Ticket WHERE CategoryID = '1' OR CategoryID = '2' OR CategoryID = '3';

--D. Retrieve a list of tickets assigned to a particular staff member and ordered by
--assigned date
SELECT * FROM Ticket WHERE AssignTechnicianID = '1' AND Date = '2020-03-02 09:10:00.000';


--E. Retrieve a list of users’ names and the number of tickets created by each
--user. Display zero (0) for those users that have not created any tickets and
--order the list by the user’s last names.

SELECT U.Name, U.LastName, count(T.UserID) AS NumberOfTickets
FROM Ticket AS T
RIGHT JOIN UserInfo AS U ON T.UserID = U.UserInfoID
GROUP BY  U.Name, U.LastName
ORDER BY U.LastName;

--F. Retrieve a list of ticket titles that have comments with the phrase “initial
--comment” somewhere in the text

-- I`m going to add some test data because I don`t have any comment with “initial comment”

INSERT INTO Ticket (title, CategoryID, UserID, AssignTechnicianID, Date, IsSolved, SolvedDate, DetailsOfTheIssue, AuthorTechnicianID) VALUES
('** TEST initial comment **', 1,4,1,'2020-04-08 09:05:00.000','N',NULL,'**TEST**',NULL),
('** initial comment TEST TEST **', 1,3,1,'2020-04-09 09:05:00.000','N',NULL,'**TEST**',NULL),
('initial comment **', 1,6,1,'2020-04-10 09:05:00.000','N',NULL,'**TEST**',NULL);

SELECT Title FROM Ticket WHERE Title LIKE '%initial comment%';


--G. Retrieve a list of the categories for tickets than have more than two (2) active
--tasks that have not been assigned to any staff member

-- I don't have any ticket with more than two tasks that have not been assigned to any staff member.
-- first I'll create a ticket with no assign technician:
INSERT INTO Ticket (title, CategoryID, UserID, AssignTechnicianID, Date, IsSolved, SolvedDate, DetailsOfTheIssue, AuthorTechnicianID) VALUES
('** PROBLEM WITH MY PHONE  **', 4,6,NULL,'2020-04-08 10:00:00.000','N',NULL,'** I CANNOT RECEIVE AND MAKE CALLS **',NULL);


-- now I'm going to create two tasks for the ticket created above:
INSERT INTO ActionsToDoInFuture (TicketID, Action) VALUES
    (19,'CONFIGURE THE PHONE`S IP ADDRESS'),
    (19,'CHANGE THE DEVICE TO A NEW ONE');


    -- the table (SELECT DISTINCT TicketID  FROM ActionsToDoInFuture GROUP BY TicketID HAVING count(TicketID)>1)
    -- selects all the tickets that has 2 or more tasks (in my case I'm calling task as action)

    -- the table (SELECT * FROM Ticket WHERE AssignTechnicianID IS NULL)
    -- selects all the tickets that has no assign technician

    -- Then I made a inner join between those two tables. Bellow follow the retrieving command

SELECT B.CategoryID FROM (SELECT DISTINCT TicketID  FROM ActionsToDoInFuture GROUP BY TicketID HAVING count(TicketID)>1) AS A
INNER JOIN (SELECT * FROM Ticket WHERE AssignTechnicianID IS NULL) AS B
ON A.TicketID = B.TicketID;






