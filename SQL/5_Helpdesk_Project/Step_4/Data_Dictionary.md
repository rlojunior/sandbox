####  _Reynaldo Junior - April 2020_
## Data Dictionary - Speeding Tickets ERD


### Ticket
|Key|Name       |type    |Size|Default   |Description               |Sample Data     |
|---|-----------|--------|----|----------|--------------------------|----------------|
|PK |TicketID   |INT     |-   |IDENTITY  |Unique sequential Integer.|123456          |
| - |Title      |VARCHAR |-   |-         |Title of the ticket given by the author| I cannot connect to internet|
|FK |CategoryID |INT     |-   |-         |What category ID the ticket is under (__from Category__)|03 |
|FK |UserID     |INT     |-   |-         |The ID of the user - The target of the ticket (__from User_info__)|2212|
|FK |AssignTechnicianID|INT    |-   |-         |The ID of the technician in charge of the ticket (__from Technician_info__)|3343|
|DF  |Date        |DATETIME|-  |GETDATE()         |The date when the ticket was created|2020-01-23 15:30:23|
|CK  |IsSolved    |CHAR    |1  |-         |Y if the issue was solved and N if the issue is still open|Y|
|-  |SolvedDate   |DATETIME|- |NULL      |The date when the ticket was closed|2020-01-23 15:30:23|
|- |DetailsOfTheIssue|VARCHAR|255 |-         |Detailed explanation of the issue|Everytime I close a "x" software the Windows shuts down|
|FK |AuthorTechnicianID| INT|-|-|The name of the technician who generate/created the ticket (__from Technician_info__)| 2321|
 
### Category
|Key|Name       |type    |Size|Default   |Description               |Sample Data     |
|---|-----------|--------|----|----------|--------------------------|----------------|
|PK |CategoryID |INT     |-   |IDENTITY  |Unique sequential Integer.|03              |
|- |Name        |VARCHAR |80  |-         |What category the ticket is under|Hardware issue, Software installation|

### UserInfo
|Key|Name       |type    |Size|Default   |Description               |Sample Data     |
|---|-----------|--------|----|----------|--------------------------|----------------|
PK |UserInfoID |INT     |-   |-  |Unique sequential Integer.|03
|-|Name|VARCHAR|80|-|The name of the user|Erica|
|-|LastName|VARCHAR|80|-|The name of the user|Silva|
|-|Department|VARCHAR|32|-|Which dept the user works| Human Resources|
|-|Contact|VARCHAR|32|-|The user contact/email|erica@hr.ca|


### TechnicianInfo
|Key|Name       |type    |Size|Default   |Description               |Sample Data     |
|---|-----------|--------|----|----------|--------------------------|----------------|
PK |TechnicianInfoID |INT     |-   |IDENTITY  |Unique sequential Integer.|03
|-|Name|VARCHAR|80|-|The name of the technician|Bob|
|CK/AK/IX|Contact|VARCHAR|32|-|The technician contact/email|bob@info.ca|


### Comment
|Key|Name       |type    |Size|Default   |Description               |Sample Data     |
|---|-----------|--------|----|----------|--------------------------|----------------|
PK |CommentID |INT     |-   |IDENTITY  |Unique sequential Integer.|11213
|FK |TicketID |INT     |-   |-         | The ID of the ticket(__from Ticket__)|03 |
|FK |Technician_ID |INT     |-   |-         | The ID of the technician(__from Technician_info__)|03 |
|FK |UserID |INT     |-   |NULL         | The ID of the user(__from User_info__)|03 |
|-|Comment|VARCHAR|255|-|A chat/comment between the user and the technician|"When exactly the issue started?"|

### HardwareInfo 
|Key|Name       |type    |Size|Default   |Description               |Sample Data     |
|---|-----------|--------|----|----------|--------------------------|----------------|
|PK  |    HardwareInfoID     |INT     |-   |IDENTITY  |Unique sequential Integer.|11213|
|- |HardwareDetails  |VARCHAR|255 |-         |Information about the hardware, so any warranty repairs can be dealt with|Dell - Serial: 121221|


### TicketHardwareInfo
|Key|Name       |type    |Size|Default   |Description               |Sample Data     |
|---|-----------|--------|----|----------|--------------------------|----------------|
|PK/FK |TicketID |INT     |-   |-         | The ID of the ticket(__from Ticket__)|03 |
|PK/FK |HardwareID |INT     |-   |-         | The ID of the hardware info (__from Hardware_info__)|03 |

### ActionsToDoInFuture (New Table)
|Key|Name       |type    |Size|Default   |Description               |Sample Data     |