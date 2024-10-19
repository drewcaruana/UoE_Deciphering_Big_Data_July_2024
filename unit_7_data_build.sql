-- Table for Students
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(100),
    DateOfBirth DATE,
    Support VARCHAR(3),
    ExamScore INT,
    CourseID VARCHAR(10),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) -- Foreign key for CourseID
);

-- Table for Courses
CREATE TABLE Courses (
    CourseID VARCHAR(10) PRIMARY KEY,
    CourseName VARCHAR(100),
    ExamBoardID VARCHAR(10),
    TeacherID VARCHAR(10),
    FOREIGN KEY (ExamBoardID) REFERENCES ExamBoards(ExamBoardID), -- Foreign key for ExamBoardID
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID) -- Foreign key for TeacherID
);

-- Table for Exam Boards
CREATE TABLE ExamBoards (
    ExamBoardID VARCHAR(10) PRIMARY KEY,
    ExamBoardName VARCHAR(100),
    TeacherID VARCHAR(10),
    CourseID VARCHAR(10),
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID), -- Foreign key for TeacherID
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) -- Foreign key for CourseID
);

-- Table for Teachers
CREATE TABLE Teachers (
    TeacherID VARCHAR(10) PRIMARY KEY,
    TeacherName VARCHAR(100),
    CourseID VARCHAR(10),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) -- Foreign key for CourseID
);