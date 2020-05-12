##Data Dictionary - Speeding Tickets ERD


###Ticket
|Key|Name       |type    |Size|Default   |Description               |Sample Data     |
|---|-----------|--------|----|----------|--------------------------|----------------|
|PK |TicketID   |INT     |-   |IDENTITY  |Unique sequential Integer.|123456          |
| - |Title      |VARCHAR |-   |-         |Title of the ticket given by the author| I cannot connect to internet|
|FK |CategoryID |INT     |-   |-         |What category ID the ticket is under (__from Category__)|03 |
| - |Author     |VARCHAR |80  |-         |Who create the ticket. Tickets can be created by the user or by the technician|John            |
|FK |UserID     |INT     |-   |-         |The ID of the user - The target of the ticket (__from User_info__)|2212|
|FK |TechnicianID|INT    |-   |-         |The ID of the technician in charge of the ticket (__from Technician_info__)|3343|
|-  |Date        |DATETIME|-  |-         |The date when the ticket was created|2020-01-23 15:30:23|
|-  |IsSolved    |CHAR    |1  |-         |Y if the issue was solved and N if the issue is still open|Y|
|-  |SolvedDate   |DATETIME|- |NULL      |The date when the ticket was closed|2020-01-23 15:30:23|
|- |DetailsOfTheIssue|TEXT|- |-         |Detailed explanation of the issue|Everytime I close a "x" software the Windows shuts down|
|- |HardwareDetails  |TEXT|- |-         |Information about the hardware, so any warranty repairs can be dealt with|Dell - Serial: 121221|
|- |ActionsToDoInFuture|VARCHAR|-       |-    |If it is going to be needed to do any action in future|Buy/order a new keyboard|

 
###Category
|Key|Name       |type    |Size|Default   |Description               |Sample Data     |
|---|-----------|--------|----|----------|--------------------------|----------------|
|PK |CategoryID |INT     |-   |IDENTITY  |Unique sequential Integer.|03              |
|- |Name        |VARCHAR |80  |-         |What category the ticket is under|Hardware issue, Software installation|
###User_info
###Technician_info
###Comments
