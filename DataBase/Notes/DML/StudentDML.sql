USE StudentDemo;
GO

SELECT * FROM Student;
GO

INSERT INTO Student (StudentID, FirstName, LastName, Email, Age, Photo,Child)
VALUES (3,'Jane','Doe', 'jane@nscc.ca',42,NULL,1);

SELECT Email, ClassID FROM Student s
INNER JOIN Class c ON s.StudentID = c.StudentID;
GO

SELECT Email FROM Student s
INNER JOIN Class c ON s.StudentID = c.StudentID;
GO

SELECT DISTINCT Email FROM Student s
INNER JOIN Class c ON s.StudentID = c.StudentID;
GO

SELECT Email FROM Student s
INNER JOIN Class c ON s.StudentID = c.StudentID
GROUP BY Email;
GO
