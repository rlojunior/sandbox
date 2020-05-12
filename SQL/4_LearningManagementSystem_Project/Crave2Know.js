use crave2know;
/* Creating tables */

db.createCollection('Student');
db.createCollection('Enrolment');
db.createCollection('Student_Assignment');
db.createCollection('Specific_Course');
db.createCollection('Assignment');
db.createCollection('Main_Course');

/* Add the following students: Jill Hill (W0111222), Mike Pike (W0222333), Steve Cleve (W0333444)  */

db.Student.insert({
    _id:'W0111222',
    First_name:'Jill',
    Last_name:'Hill',
    Password:'123456',
    Phone_number:'9022212123',
    Address:'35 Leeds St.'
});

db.Student.insert({
    _id:'W0222333',
    First_name:'Mike',
    Last_name:'Pike',
    Password:'111222333',
    Phone_number:'9023321245',
    Address:'3443 Robie St.'
});

db.Student.insert({
    _id:'W0333444',
    First_name:'Steve',
    Last_name:'Cleve',
    Password:'1@1123@@#24',
    Phone_number:'9023346578',
    Address:'43 North St.'
});

/* Add the following courses: Data Fundamentals (DBAS1007), Programming (PROG1700) */

db.Main_Course.insert({
    _id:'DBAS1007',
    Name:'Data Fundamentals',
    Description:'This course offers lecture, laboratory, and online interaction to provide a foundation in data management concepts.'
});

db.Main_Course.insert({
    _id:'PROG1700',
    Name:'Programming',
    Description:'This course offers lecture, laboratory, and online interaction to provide a foundation in data management concepts.'
});

/* Create a new instance of the Data Fundamentals course that starts on Sept.7,2018 and ends on Dec.14, 2018 */

db.Specific_Course.insert({
    _id:'4001',
    Main_course_id:'DBAS1007',
    Teacher:'Brian',
    Start_date:'2018-09-07',
    End_date:'2018-12-14'
});

/* Create a new instance of the Programming course that starts on Jan. 4, 2019 and ends on Apr. 24, 2019 */
db.Specific_Course.insert({
    _id:'5001',
    Main_course_id:'PROG1700',
    Teacher:'Ronan',
    Start_date:'2019-01-04',
    End_date:'2019-04-24'
});

/* Enroll Jill and Mike in the instance of the Data Fundamentals course and Jill and Steve in the instance of the Programming course */
db.Enrolment.insert({
    _id:'111',
    Student_id:'W0111222',
    Specific_course_id:'4001',
    Final_grade:'',
    Feedback:''
});

db.Enrolment.insert({
    _id:'222',
    Student_id:'W0222333',
    Specific_course_id:'4001',
    Final_grade:'',
    Feedback:''
});

db.Enrolment.insert({
    _id:'333',
    Student_id:'W0111222',
    Specific_course_id:'5001',
    Final_grade:'',
    Feedback:''
});

db.Enrolment.insert({
    _id:'444',
    Student_id:'W0333444',
    Specific_course_id:'5001',
    Final_grade:'',
    Feedback:''
});

/* Create two assignments in the database course and one assignment in the programming course */

db.Assignment.insert({
    _id:'41',
    Specific_course_id:'4001'
});

db.Assignment.insert({
    _id:'42',
    Specific_course_id:'4001'
});

db.Assignment.insert({
    _id:'51',
    Specific_course_id:'5001'
});

/* Give the following database assignment grades to Jill  Assignment 1: 95 and Assignment 2: 87 */

db.Student_Assignment.insert({
    _id:'401',
    Student_id:'W0111222',
    Assign_id:'41',
    Grade:'95'
});

db.Student_Assignment.insert({
    _id:'402',
    Student_id:'W0111222',
    Assign_id:'42',
    Grade:'87'
});

/* Remove Steve from the programming course */
db.Enrolment.deleteMany({Student_id:'W0333444'});


/* Update Jill’s total grade for Programming to a 78 */
db.Enrolment.update (
    {
    Student_id:'W0111222',
    Specific_course_id:'5001'

    },
    {
        $set: {
            Final_grade:'78'
            }
    }

);

/* Display a list of all courses */
db.Specific_Course.find().pretty();


/* Display the last name of the student with the student number of W0333444 */
db.Student.find(
{_id:'W0333444'},{Last_name:1}
);

/* Display a list of the assignment grades for student number W0111222 */
db.Student_Assignment.find(
{Student_id:'W0111222'},{Grade:1}
);

/* Display a list of courses that are being delivered after January 1st, 2019 */
db.Specific_Course.find(
{"Start_date":{$gte:'2019-01-01'}}
);

