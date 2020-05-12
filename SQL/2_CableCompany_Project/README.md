# About this folder
Develop a MariaDB database design that will be used by a cable company.

## The purpose of this project is:

A new cable company has cropped up on the west coast. They plan to provide different
channel packages to its customers and each package will consist of different combinations of
the available 800 different channels. Different channel packages might include some of the
same channels.

Each customer can subscribe to one or more of the different packages depending on their
likes and dislikes, but they must have at least the “Basic” cable package.


Along with the channel packages of their choice, customers will also be able to watch Pay-
Per-View events on demand. Each event will be available on a single Pay-Per-View channel
at a given date/time and each channel will show different events as they happen. Customers
will pay for the event after it is shown, and the cable box will enable and disable the channel
automatically for the customer.

## Tasks
- Add three customers: John Buck, Jane Doe and Jack Sprat
- Add three channels: ABC (100), Spike (106) and TSN (110)
- Add three cable packages: Basic, Action and Sports
- Add channel 100 to the Basic package, 106 to the Action package and 110 to
	the Sports package
- Add the Basic package to all the customers’ subscriptions
- Add the Action package to Jane Doe’s subscription
- Add one pay-per-view event (The Prize Fight) to be scheduled on TSN for
	Oct. 31st, 2018 at 8:00PM
- Add John Buck to the list of people who want to watch the big fight
- Update John Buck’s big fight record to complete his payment of $9.95
- Delete Jane Doe’s subscription to the Action package
- Display a list of all customer information alphabetically by last name
- Display all information for the Spike channel
- Display the title and date of all future Pay-Per-View events


## Files in this folder
* **DataBaseCableTV.sql** - A complete database creation script
* **ERD.png** - An Entity-Relationship Diagram



*Fall Term/2019 - Project #4*