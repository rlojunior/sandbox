-- DDL commands (Create)
DROP DATABASE IF EXISTS CableCompany;
CREATE DATABASE CableCompany;

USE CableCompany;

DROP TABLE IF EXISTS Channel;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Customer_Package;
DROP TABLE IF EXISTS `Customer_Pay-Per-View`;
DROP TABLE IF EXISTS Package;
DROP TABLE IF EXISTS Package_Channel;
DROP TABLE IF EXISTS `Pay-Per-View`;


CREATE TABLE Channel (
  ChannelID int(11) NOT NULL AUTO_INCREMENT,
  Name      varchar(32) NOT NULL,
  PRIMARY KEY (ChannelID));

CREATE TABLE Customer (
  CustomerID int(11) NOT NULL AUTO_INCREMENT,
  Name       varchar(32) NOT NULL,
  Adress     varchar(32) NOT NULL,
  Phone      varchar(13) NOT NULL,
  PRIMARY KEY (CustomerID));

CREATE TABLE Customer_Package (
  CustomerCustomerID int(11) NOT NULL,
  PackagePackageID   int(11) NOT NULL,
  PRIMARY KEY (CustomerCustomerID,
  PackagePackageID));

CREATE TABLE `Customer_Pay-Per-View` (
  CustomerCustomerID       int(11) NOT NULL,
  `Pay-Per-ViewPPVeventID` int(11) NOT NULL,
  IsPaymentOk TINYINT(1) NOT NULL,   -- 1 for Yes or 0 for Not
  PRIMARY KEY (CustomerCustomerID,
  `Pay-Per-ViewPPVeventID`));

CREATE TABLE Package (
  PackageID int(11) NOT NULL AUTO_INCREMENT,
  Name      varchar(32) NOT NULL,
  Price     float NOT NULL,
  PRIMARY KEY (PackageID));

CREATE TABLE Package_Channel (
  PackagePackageID int(11) NOT NULL,
  ChannelChannelID int(11) NOT NULL,
  PRIMARY KEY (PackagePackageID,
  ChannelChannelID));

CREATE TABLE `Pay-Per-View` (
  PPVeventID  int(11) NOT NULL AUTO_INCREMENT,
  ChannelID   int(11) NOT NULL,
  EventName  varchar(32) NOT NULL,
  ChannelName varchar(32) NOT NULL,
  `Date`      datetime NOT NULL,
  Price       float NOT NULL,
  PRIMARY KEY (PPVeventID));

ALTER TABLE Customer_Package ADD CONSTRAINT FKCustomer_P480667 FOREIGN KEY (CustomerCustomerID) REFERENCES Customer (CustomerID);
ALTER TABLE Customer_Package ADD CONSTRAINT FKCustomer_P667843 FOREIGN KEY (PackagePackageID) REFERENCES Package (PackageID);
ALTER TABLE Package_Channel ADD CONSTRAINT FKPackage_Ch220333 FOREIGN KEY (PackagePackageID) REFERENCES Package (PackageID);
ALTER TABLE Package_Channel ADD CONSTRAINT FKPackage_Ch846054 FOREIGN KEY (ChannelChannelID) REFERENCES Channel (ChannelID);
ALTER TABLE `Pay-Per-View` ADD CONSTRAINT `FKPay-Per-Vi789494` FOREIGN KEY (ChannelID) REFERENCES Channel (ChannelID);
ALTER TABLE `Customer_Pay-Per-View` ADD CONSTRAINT FKCustomer_P570512 FOREIGN KEY (CustomerCustomerID) REFERENCES Customer (CustomerID);
ALTER TABLE `Customer_Pay-Per-View` ADD CONSTRAINT FKCustomer_P667527 FOREIGN KEY (`Pay-Per-ViewPPVeventID`) REFERENCES `Pay-Per-View` (PPVeventID);

ALTER TABLE Customer_Package DROP FOREIGN KEY FKCustomer_P480667;
ALTER TABLE Customer_Package DROP FOREIGN KEY FKCustomer_P667843;
ALTER TABLE Package_Channel DROP FOREIGN KEY FKPackage_Ch220333;
ALTER TABLE Package_Channel DROP FOREIGN KEY FKPackage_Ch846054;
ALTER TABLE `Pay-Per-View` DROP FOREIGN KEY `FKPay-Per-Vi789494`;
ALTER TABLE `Customer_Pay-Per-View` DROP FOREIGN KEY FKCustomer_P570512;
ALTER TABLE `Customer_Pay-Per-View` DROP FOREIGN KEY FKCustomer_P667527;

-- Add three customers: John Buck, Jane Doe and Jack Sprat
INSERT INTO Customer (name, adress, phone)
VALUES  ('John Buck', '2212 Robie St.','(902)221-3211'),('Jane Doe','4434 Rosemeade Av.','(902)332-3324'),('Jack Sprat','5545 Leeds St.','(221)223-3323');

-- Add three channels: ABC (100), Spike (106) and TSN (110)
INSERT INTO Channel (Name)
VALUES ('ABC(100)'), ('Spike(106)'), ('TSN(110)');

-- Add three cable packages: Basic, Action and Sports
INSERT INTO Package (NAME, PRICE)
VALUES ('Basic', 55),('Action',73),('Sports',82), ('Fammily',50);

-- Add channel 100 to the Basic package, 106 to the Action package and 110 to
-- the Sports package
INSERT INTO PACKAGE_CHANNEL (PACKAGEPACKAGEID,CHANNELCHANNELID )
    VALUES ((SELECT PACKAGEID  FROM PACKAGE WHERE NAME = 'Basic'),(SELECT ChannelID FROM Channel WHERE Name = 'ABC(100)')),
       ((SELECT PACKAGEID  FROM PACKAGE WHERE NAME = 'Action'),(SELECT ChannelID FROM Channel WHERE Name = 'Spike(106)')),
       ((SELECT PACKAGEID  FROM PACKAGE WHERE NAME = 'Sports'),(SELECT ChannelID FROM Channel WHERE Name = 'TSN(110)')),
       ((SELECT PACKAGEID  FROM PACKAGE WHERE NAME = 'Fammily'),(SELECT ChannelID FROM Channel WHERE Name = 'Spike(106)'));

-- Add the Basic package to all the customers’ subscriptions
INSERT INTO CUSTOMER_PACKAGE (CUSTOMERCUSTOMERID, PACKAGEPACKAGEID)
    VALUES ((SELECT CUSTOMERID  FROM CUSTOMER WHERE NAME = 'John Buck'),(SELECT PACKAGEID FROM PACKAGE WHERE Name = 'Basic')),
           ((SELECT CUSTOMERID  FROM CUSTOMER WHERE NAME = 'Jane Doe'),(SELECT PACKAGEID FROM PACKAGE WHERE Name = 'Basic')),
           ((SELECT CUSTOMERID  FROM CUSTOMER WHERE NAME = 'Jack Sprat'),(SELECT PACKAGEID FROM PACKAGE WHERE Name = 'Basic'));

-- Add the Action package to Jane Doe’s subscription
INSERT INTO CUSTOMER_PACKAGE (CUSTOMERCUSTOMERID, PACKAGEPACKAGEID)
    VALUES ((SELECT CUSTOMERID  FROM CUSTOMER WHERE NAME = 'Jane Doe'),(SELECT PACKAGEID FROM PACKAGE WHERE Name = 'Action'));

-- Add one pay-per-view event (The Prize Fight) to be scheduled on TSN for
-- Oct. 31st, 2018 at 8:00PM

INSERT INTO `Pay-Per-View` (CHANNELID, EVENTNAME, CHANNELNAME, Date, PRICE)
    VALUES ((SELECT ChannelID FROM Channel WHERE Name = 'TSN(110)'),'The Prize Fight','TSN(110)','2018-10-31 20:00:00',9.95);


-- Add John Buck to the list of people who want to watch the big fight
INSERT INTO `Customer_Pay-Per-View` (CUSTOMERCUSTOMERID, `Pay-Per-ViewPPVeventID`, ISPAYMENTOK)
    VALUES ((SELECT CUSTOMERID  FROM CUSTOMER WHERE NAME = 'John Buck'),(SELECT PPVEVENTID  FROM `Pay-Per-View` WHERE EVENTNAME = 'The Prize Fight'),0)



-- Update John Buck’s big fight record to complete his payment of $9.95
UPDATE `Customer_Pay-Per-View`
    SET ISPAYMENTOK = 1
    WHERE  CUSTOMERCUSTOMERID = (SELECT CUSTOMERID  FROM CUSTOMER WHERE NAME = 'John Buck');



-- Delete Jane Doe’s subscription to the Action package
DELETE FROM CUSTOMER_PACKAGE WHERE CUSTOMERCUSTOMERID = (SELECT CUSTOMERID  FROM CUSTOMER WHERE NAME = 'Jane Doe') AND PACKAGEPACKAGEID = (SELECT PACKAGEID  FROM PACKAGE WHERE NAME = 'Action');


-- Display a list of all customer information alphabetically by last name

        -- Adding a new customer.
        INSERT INTO Customer (name, adress, phone)
        VALUES  ('Jeovah Cox','556 North St.','(902)665-4534');


        -- SELECT INSTR('Reynaldo Junior',' '); -- Just for understanding how INSTR works
        -- SELECT SUBSTR('Reynaldo Junior',9);  -- Just for understanding how SUBSTR works

SELECT * FROM CUSTOMER ORDER BY SUBSTR(Name, INSTR(Name, ' '));


-- Display all information for the Spike channel

    -- Display the information about Spike channel
    SELECT * FROM Channel WHERE Name = 'Spike(106)'; -- in this case, I only have in the table channel the information about the channel ID
                                                     -- but, if I add more information about the channel it will be displayed by the same command.
    -- Display which package has the Spike channel
    SELECT Name FROM Package WHERE PackageID IN (SELECT PackagePackageID FROM Package_Channel WHERE ChannelChannelID = (SELECT ChannelID FROM Channel WHERE Name = 'Spike(106)'));


-- Display the title and date of all future Pay-Per-View events

    -- Creating a future event on pay-per-view table
    INSERT INTO `Pay-Per-View` (CHANNELID, EVENTNAME, CHANNELNAME, Date, PRICE)
        VALUES ((SELECT ChannelID FROM Channel WHERE Name = 'ABC(100)'),'Total Soccer','ABC(100)','2019-12-10 20:00:00',9.95);

SELECT * FROM `Pay-Per-View` WHERE Date > now();



