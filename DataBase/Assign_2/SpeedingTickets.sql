USE master;
GO

DROP DATABASE IF EXISTS SpeedingTickets;
CREATE DATABASE SpeedingTickets;
GO

USE SpeedingTickets;
GO

DROP TABLE IF EXISTS Category;
CREATE TABLE Category (
  CategoryID int IDENTITY NOT NULL,
  Name       varchar(80) NOT NULL,
  PRIMARY KEY (CategoryID));

DROP TABLE IF EXISTS Comments;
CREATE TABLE Comments (
  CommentID     int NOT NULL,
  TicketID      int NOT NULL,
  Technician_ID int NULL,
  UserID        int NULL,
  Comment       varchar(255) NOT NULL,
  PRIMARY KEY (CommentID,
  TicketID));



--ALTER TABLE Comments DROP CONSTRAINT FK__Ticket__TicketID;
--ALTER TABLE Comments DROP CONSTRAINT FK__Technician_info__ID;
--ALTER TABLE Comments DROP CONSTRAINT FK__User_info__ID;


DROP TABLE IF EXISTS Hardware_info;
CREATE TABLE Hardware_info (
  ID              int IDENTITY NOT NULL,
  HardwareDetails varchar(255) NULL,
  PRIMARY KEY (ID));

DROP TABLE IF EXISTS Technician_info;
CREATE TABLE Technician_info (
  ID      int IDENTITY NOT NULL,
  Name    varchar(80) NOT NULL,
  Contact varchar(32) NOT NULL,
  PRIMARY KEY (ID),
  CONSTRAINT CK__Technician_info__Contact CHECK (Contact LIKE '%_@__%.__%'));

GO

-- ALTER TABLE Technician_info DROP CONSTRAINT AK__Technician_info__Contact;
ALTER TABLE Technician_info
    ADD CONSTRAINT AK__Technician_info__Contact UNIQUE (Contact);

CREATE INDEX IX__Technician_info__Contact
    ON Technician_info (Contact);



DROP TABLE IF EXISTS Ticket;
CREATE TABLE Ticket (
  TicketID            int IDENTITY NOT NULL,
  Title               varchar(255) NOT NULL,
  CategoryID          int NOT NULL,
  UserID              int NULL,
  AssignTechnicianID  int NULL,
  Date              datetime NOT NULL,
  IsSolved            char(1) NOT NULL,
  SolvedDate          datetime NULL,
  DetailsOfTheIssue   varchar(255) NOT NULL,
  ActionsToDoInFuture varchar(255) NULL,
  AuthorTechnicianID  int NULL,
  PRIMARY KEY (TicketID),

  CONSTRAINT CK__Ticket__IsSolved CHECK (IsSolved = 'Y'OR IsSolved = 'N' ));
GO

ALTER TABLE Ticket
    ADD CONSTRAINT DF__Ticket__Date DEFAULT GETDATE() FOR Date;

--ALTER TABLE Ticket DROP CONSTRAINT FK__User_info__ID;
--ALTER TABLE Ticket DROP CONSTRAINT FK__Technician_info__ID;
--ALTER TABLE Ticket DROP CONSTRAINT FK__Category__CategoryID;
--ALTER TABLE Ticket DROP CONSTRAINT FK__Technician_info__ID;


GO

DROP TABLE IF EXISTS Ticket_Hardware_info;
CREATE TABLE Ticket_Hardware_info (
  TicketID   int NOT NULL,
  HardwareID int NOT NULL,
  PRIMARY KEY (TicketID,
  HardwareID));
--ALTER TABLE Ticket_Hardware_info DROP CONSTRAINT FK__Ticket__TicketID;
--ALTER TABLE Ticket_Hardware_info DROP CONSTRAINT FK__Hardware_info__ID;


DROP TABLE IF EXISTS User_info;
CREATE TABLE User_info (
  ID         int IDENTITY NOT NULL,
  Name       varchar(80) NOT NULL,
  Department varchar(32) NOT NULL,
  Contact    varchar(32) NOT NULL,
  PRIMARY KEY (ID),
  CONSTRAINT CK__User_info__Contact CHECK (Contact LIKE '%_@__%.__%'));

ALTER TABLE User_info
    ADD CONSTRAINT AK__User_info__Contact UNIQUE (Contact);

CREATE INDEX IX__User_info__Contact
    ON User_info (Contact);

GO


ALTER TABLE Comments
    ADD CONSTRAINT FK__Comment_Ticket__TicketID FOREIGN KEY (TicketID) REFERENCES Ticket (TicketID);
ALTER TABLE Comments
    ADD CONSTRAINT FK__Technician_info__ID FOREIGN KEY (Technician_ID) REFERENCES Technician_info (ID);
ALTER TABLE Comments
    ADD CONSTRAINT FK__User_info__ID FOREIGN KEY (UserID) REFERENCES User_info (ID);

GO


ALTER TABLE Ticket
    ADD CONSTRAINT FK__Ticket_User_info__ID FOREIGN KEY (UserID) REFERENCES User_info (ID);
ALTER TABLE Ticket
    ADD CONSTRAINT FK__Ticket_Technician_info__ID FOREIGN KEY (AssignTechnicianID) REFERENCES Technician_info (ID);
ALTER TABLE Ticket
    ADD CONSTRAINT FK__Category__CategoryID FOREIGN KEY (CategoryID) REFERENCES Category (CategoryID);
--ALTER TABLE Ticket
    --ADD CONSTRAINT FK__Ticket_Technician_info__ID FOREIGN KEY (AuthorTechnicianID) REFERENCES Technician_info (ID);

GO


ALTER TABLE Ticket_Hardware_info
    ADD CONSTRAINT FK__Ticket__TicketID FOREIGN KEY (TicketID) REFERENCES Ticket (TicketID);
ALTER TABLE Ticket_Hardware_info
    ADD CONSTRAINT FK__Hardware_info__ID FOREIGN KEY (HardwareID) REFERENCES Hardware_info (ID);


GO
