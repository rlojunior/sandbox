####  _Reynaldo Junior - February 2020_
## Data Dictionary - Speeding Tickets ERD


### Ticket
|Key|Name       |type    |Size|Default   |Description               |Sample Data     |
|---|-----------|--------|----|----------|--------------------------|----------------|
|PK |TicketID   |INT     |-   |IDENTITY  |Unique sequential Integer.|123456          |
| - |Title      |VARCHAR |-   |-         |Title of the ticket given by the author| I cannot connect to internet|
|FK |CategoryID |INT     |-   |-         |What category ID the ticket is under (__from Category__)|03 |
|FK |UserID     |INT     |-   |-         |The ID of the user - The target of the ticket (__from User_info__)|2212|
|FK |**AssignTechnicianID**|INT    |-   |-         |The ID of the technician in charge of the ticket (__from Technician_info__)|3343|
|DF  |Date        |DATETIME|-  |-         |The date when the ticket was created|2020-01-23 15:30:23|
|CK  |IsSolved    |CHAR    |1  |-         |Y if the issue was solved and N if the issue is still open|Y|
|-  |SolvedDate   |DATETIME|- |NULL      |The date when the ticket was closed|2020-01-23 15:30:23|
|- |DetailsOfTheIssue|TEXT|- |-         |Detailed explanation of the issue|Everytime I close a "x" software the Windows shuts down|
|- |ActionsToDoInFuture|VARCHAR|-       |NULL    |If it is going to be needed to do any action in future|Buy/order a new keyboard|
|FK |**AuthorTechnicianID**| INT|-|-|The name of the technician who generate/created the ticket (__from Technician_info__)| 2321|
 
### Category
|Key|Name       |type    |Size|Default   |Description               |Sample Data     |
|---|-----------|--------|----|----------|--------------------------|----------------|
|PK |CategoryID |INT     |-   |IDENTITY  |Unique sequential Integer.|03              |
|- |Name        |VARCHAR |80  |-         |What category the ticket is under|Hardware issue, Software installation|

### User_info
|Key|Name       |type    |Size|Default   |Description               |Sample Data     |
|---|-----------|--------|----|----------|--------------------------|----------------|
PK |ID |INT     |-   |IDENTITY  |Unique sequential Integer.|03
|-|Name|VARCHAR|80|-|The name of the user|Erica|
|-|Department|VARCHAR|32|-|Which dept the user works| Human Resources|
|CK/AK/IX|Contact|VARCHAR|32|-|The user contact/email|erica@hr.ca|


### Technician_info
|Key|Name       |type    |Size|Default   |Description               |Sample Data     |
|---|-----------|--------|----|----------|--------------------------|----------------|
PK |ID |INT     |-   |IDENTITY  |Unique sequential Integer.|03
|-|Name|VARCHAR|80|-|The name of the technician|Bob|
|CK/AK/IX|Contact|VARCHAR|32|-|The technician contact/email|bob@info.ca|


### Comments
|Key|Name       |type    |Size|Default   |Description               |Sample Data     |
|---|-----------|--------|----|----------|--------------------------|----------------|
PK |CommentID |INT     |-   |IDENTITY  |Unique sequential Integer.|11213
|PK/FK |TicketID |INT     |-   |-         | The ID of the ticket(__from Ticket__)|03 |
|FK |Technician_ID |INT     |-   |-         | The ID of the technician(__from Technician_info__)|03 |
|FK |UserID |INT     |-   |-         | The ID of the user(__from User_info__)|03 |
|-|Comment|TEXT|-|-|A chat/comment between the user and the technician|"When exactly the issue started?"|

### Hardware_info _(New table)_
|Key|Name       |type    |Size|Default   |Description               |Sample Data     |
|---|-----------|--------|----|----------|--------------------------|----------------|
|PK  |    ID     |INT     |-   |IDENTITY  |Unique sequential Integer.|11213|
|- |HardwareDetails  |VARCHAR|255 |NULL         |Information about the hardware, so any warranty repairs can be dealt with|Dell - Serial: 121221|


### Ticket_Hardware_info _(New table)_
|Key|Name       |type    |Size|Default   |Description               |Sample Data     |
|---|-----------|--------|----|----------|--------------------------|----------------|
|PK/FK |TicketID |INT     |-   |-         | The ID of the ticket(__from Ticket__)|03 |
|PK/FK |HardwareID |INT     |-   |-         | The ID of the hardware info (__from Hardware_info__)|03 |