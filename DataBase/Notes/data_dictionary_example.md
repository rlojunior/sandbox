# Top Level Headings
## Sub Level Headings
### Sub-Sub Level Headings
This should be **bold** text

This can be __bold__ also

This should be in _italics_

```
-- get all customer information
SELECT * FROM Customer;
```

|CustomerID|FirstName|LastName|
|----------|---------|--------|
|1         | John    |Smith   |
|2         | Jane    |Doe     |
|3         | Jack    |Sprat   |
|4         |Jill     |Hill    |

# Data Dictionary Example

###Student
|Key|Name       |type    |Size|Default   |Description              |Sample Data     |
|---|-----------|--------|----|----------|-------------------------|----------------|
|PK |StudentID  |INT     |11  |IDENTITY  |Unique sequencial Integer.|123456         |
| - |FirstName  |NVARCHAR|32  |-         |Student's first name.     |Jane           |
| - |LastName   |NVARCHAR|32  |-         |Student's lasst name.     |Smith          |
| - |Age        |SMALLINT|3   |-         |Student's age.(0-150)     |32             |
| - |Photo      |IMAGE   |-   |NULL      |Student ID photo.         |_image.jpg_    |

 
 ###Class
 |Key|Name       |type    |Size|Default   |Description              |Sample Data     |
|---|-----------|--------|----|----------|-------------------------|-----------------|
|PK|ClassID|INT|11|IDENTITY|Unique sequencial integer.|123456|
|-|Code|NCHAR|8|-|Course code. (AAAA1234)|DBAS4002|
|-|Name|NVARCHAR|32|-|Course name.|Database|
|FK|StudentID|INT|11|-|StudentID(__from Student__)|123456|


