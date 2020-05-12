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
    PRIMARY KEY (CommentID)
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
    Action                VARCHAR(255) NOT NULL ,
    AssignTechnicianID     INT NOT NULL
    PRIMARY KEY (ActionsToDoInFutureID)
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
ALTER TABLE ActionsToDoInFuture
    ADD CONSTRAINT FK__ActionsToDoInFuture__TechnicianInfo__TechnicianInfoID FOREIGN KEY (AssignTechnicianID) REFERENCES TechnicianInfo (TechnicianInfoID) ON DELETE CASCADE ;

GO







