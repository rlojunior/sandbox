USE SpeedingTickets;
GO


INSERT INTO Category (Name) VALUES
    ('Hardware'),
    ('Software'),
    ('Internet'),
    ('Phone'),
    ('Other');
GO

INSERT INTO UserInfo(UserInfoID, Name, LastName, Department, Contact) VALUES
    (1,'Reynaldo','Junior','HR','rey@company.com'),
    (2,'Carlos','Ramos','Accountability','carlos@company.com'),
    (3,'Maria','Soledad','HR','maria@company.com'),
    (4,'John','Smith','Sales','john@company.com'),
    (5,'Sarah','Burns','Customer Service','sarah@company.com'),
    (6,'Tom','Soyer','Clerck','tom@company.com');
GO

INSERT INTO TechnicianInfo (Name, Contact) VALUES
    ('Beatriz','bia@company.com'),
    ('Martinez','matin@company.com'),
    ('Bob','bob@company.com'),
    ('Bill','bill@company.com'),
    ('Mona','mona@company.com');
GO

INSERT INTO Ticket (Title, CategoryID, UserID, AssignTechnicianID,IsSolved, SolvedDate, DetailsOfTheIssue, AuthorTechnicianID) VALUES
    ('The mouse is not working',1,3,1,'N',NULL,'When I try to click on mouse it doesnt respond',NULL),
    ('The computer is not connecting to the internet',3,1,2,'N',NULL,'I cannot use internet when i`m logged',NULL),
    ('I forgot my password',5,2,2,'N',NULL,'I would like to reset my password. I cannot remenber it',NULL),
    ('The screen is not working properly',1,3,3,'N',NULL,'The screen turns on but display nothing',NULL),
    ('My computer is too slow',5,1,4,'N',NULL,'It takes a long time to open a software',NULL),
    ('I cannot make a call',4,5,5,'N',NULL,'I can call to other departments but I cannot make a call to a number outside the company',NULL),
    ('The user cannot access his email',3,2,4,'Y','2020-03-13 10:05:00.000','The webserver was not connecting',4),
    ('I cannot access a specific website',3,2,NULL,'N',NULL,'I can access the internet but the local newspaper website is not opening',NULL);
GO


INSERT INTO Ticket (title, CategoryID, UserID, AssignTechnicianID, Date, IsSolved, SolvedDate, DetailsOfTheIssue, AuthorTechnicianID) VALUES
    ('**TEST**', 1,1,1,'2020-02-13 09:05:00.000','N',NULL,'**TEST**',NULL), -- Ticket before Mar. 1, 2020
    ('**TEST**', 1,1,1,'2020-02-10 08:03:00.000','N',NULL,'**TEST**',NULL), -- Ticket before Mar. 1, 2020
    ('**TEST**', 1,1,1,'2020-03-01 09:05:00.000','N',NULL,'**TEST**',NULL), -- Ticket on Mar. 1, 2020 before 4:30PM
    ('**TEST**', 1,1,1,'2020-03-01 17:10:00.000','N',NULL,'**TEST**',NULL), -- In range
    ('**TEST**', 1,1,1,'2020-03-02 09:10:00.000','N',NULL,'**TEST**',NULL), -- In range
    ('**TEST**', 1,1,1,'2020-03-05 17:10:00.000','N',NULL,'**TEST**',NULL), -- Ticket after Mar. 4, 2010
    ('** TEST initial comment **', 1,4,1,'2020-04-08 09:05:00.000','N',NULL,'**TEST**',NULL),
    ('** initial comment TEST TEST **', 1,3,1,'2020-04-09 09:05:00.000','N',NULL,'**TEST**',NULL),
    ('initial comment **', 1,6,1,'2020-04-10 09:05:00.000','N',NULL,'**TEST**',NULL),
    ('** PROBLEM WITH MY PHONE  **', 4,6,NULL,'2020-04-08 10:00:00.000','N',NULL,'** I CANNOT RECEIVE AND MAKE CALLS **',NULL);
GO



INSERT INTO Comment (TicketID, TechnicianID, UserID, Comment) VALUES
    (1,1,3,'From technician: can you tell me the name of the mouse manufacturer?'),
    (1,1,3,'From user: It is a Dell mouse'),
    (2,2,1,'From technician: When was the last time you have connected to the internet?'),
    (2,2,1,'From user: Yesterday worked fine, but today when I turned on my computer it didnt connected'),
    (3,2,2,'From technician: I will create a defaut password then you can change it later'),
    (3,2,2,'From user:Ok. Thanks'),
    (4,3,3,'From technician: When exactly this problem happened? '),
    (4,3,3,'From user: This problem started when I moved the computer to a new desk'),
    (5,4,1,'From technician: Did you install any software recently?'),
    (5,4,1,'From user: Yes. I did. I installed Autocad on my machine'),
    (6,5,5,'From technician: Is your department coleagues having the same problem?'),
    (6,5,5,'From user: No, Just me'),
    (4,2,4,'Comment 1'), (4,2,4,'Comment 2'),  (4,2,4,'Comment 3'),  (6,4,6,'Comment 1'), (6,4,6,'Comment 2'), (6,4,6,'Comment 3'),
    (6,4,6,'Comment 4'), (7,5,3,'Comment 1'),  (7,5,3,'Comment 2'),  (8,5,3,'Comment 1'), (8,5,3,'Comment 2'),(8,5,3,'Comment 3'),
    (9,2,4,'Comment 1'), (9,2,4,'Comment 2'), (9,2,4,'Comment 3'), (9,2,4,'Comment 4'), (10,1,1,'Comment 1'), (10,1,1,'Comment 2'),
    (10,1,1,'Comment 3'),  (11,2,3,'Comment 1'),   (11,2,3,'Comment 2'), (11,2,3,'Comment 3'), (11,2,3,'Comment 4'), (11,2,3,'Comment 5'),
    (11,2,3,'Comment 6'),  (17,4,6,'Comment 1'),  (17,4,6,'Comment 2');
GO


INSERT INTO HardwareInfo (HardwareDetails) VALUES
    ('Dell Wireless Mouse-WM126'),
    ('Dell - XPS 15 Laptop - 8GB DDR4-2666MHz, 2x4G'),
    ('Dell - Inspiron 15 3000 Laptop'),
    ('Dell - Inspiron Desktop - 12GB, DDR4, 2666MHz'),
    ('Dell - Inspiron 22 3000 Touch All-in-One Desktop'),
    ('Dell - ooma DP1-O - Wireless digital phone - DECT 6.0');
GO

INSERT INTO TicketHardwareInfo (TicketID, HardwareID) VALUES
    (1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,4);
GO


INSERT INTO ActionsToDoInFuture (TicketID, Action,AssignTechnicianID) VALUES
    (1,'Buy a new mouse',1),
    (5,'Need to clean temporary files',1),
    (5,'Need to defrag the HD',2),
    (3,'CONFIGURE THE PHONE`S IP ADDRESS',2),
    (3,'CHANGE THE DEVICE TO A NEW ONE',2),
    (2,'Task 1',4),(2,'Task 2',4), (2,'Task 3',4),(2,'Task 4',4),(4,'Task 1',5),(4,'Task 2',5),(4,'Task 3',5),(3,'Task 1',2), (3,'Task 2',2),
    (5,'Task 1',2),(5,'Task 2',2), (12,'Task 1',4),(12,'Task 2',4),(12,'Task 3',4),(12,'Task 4',4),(6,'Task 1',1),(6,'Task 2',1), (6,'Task 3',1),
    (17,'Task 1',1),(17,'Task 2',2), (18,'Task 1',2),(18,'Task 2',2),(7,'Task 1',4),(7,'Task 2',4),(7,'Task 3',4),(3,'Task 1',4), (3,'Task 2',4);
GO

