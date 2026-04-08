
DROP DATABASE IF EXISTS Streampulse;
CREATE DATABASE Streampulse;
USE Streampulse;
CREATE TABLE Production_House (
    StudioID INT PRIMARY KEY,
    Studio_Name VARCHAR(100),
    Headquarters VARCHAR(100),
    Founding_Date DATE
);

CREATE TABLE Advertiser (
    AdCompanyID INT PRIMARY KEY,
    Company_Name VARCHAR(100),
    Industry VARCHAR(50)
);

CREATE TABLE User_Account (
    UserID INT PRIMARY KEY,
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    Email VARCHAR(100)
);

CREATE TABLE Media_Content (
    ContentID INT PRIMARY KEY,
    Title VARCHAR(255),
    StudioID INT,
    FOREIGN KEY (StudioID) REFERENCES Production_House(StudioID)
);

CREATE TABLE Episode (
    ContentID INT,
    Episode_Number INT,
    Episode_Title VARCHAR(255),
    Duration_Minutes INT,
    PRIMARY KEY (ContentID, Episode_Number),
    FOREIGN KEY (ContentID) REFERENCES Media_Content(ContentID)
);

CREATE TABLE User_Review (
    ReviewID INT PRIMARY KEY,
    UserID INT,
    ContentID INT,
    Stars INT,
    FOREIGN KEY (UserID) REFERENCES User_Account(UserID),
    FOREIGN KEY (ContentID) REFERENCES Media_Content(ContentID)
);

CREATE TABLE Ad_Creative (
    AdID INT PRIMARY KEY,
    AdCompanyID INT,
    Ad_URL VARCHAR(255),
    FOREIGN KEY (AdCompanyID) REFERENCES Advertiser(AdCompanyID)
);
INSERT INTO Production_House VALUES
(1, 'Netflix Studios', 'USA', '2000-01-01'),
(2, 'Marvel Studios', 'USA', '1993-01-01');
INSERT INTO Advertiser VALUES
(101, 'Nike', 'Sports'),
(102, 'Coca Cola', 'Beverages');
INSERT INTO User_Account VALUES
(1, 'Utkarsha', 'User', 'user@email.com'),
(2, 'Test', 'User', 'test@email.com');
INSERT INTO Media_Content VALUES
(1, 'Avengers', 1),
(2, 'Thor', 2);
INSERT INTO Episode VALUES
(1, 1, 'Episode 1', 45);
INSERT INTO User_Review VALUES
(1, 1, 1, 5),
(2, 2, 2, 4);
INSERT INTO Ad_Creative VALUES
(1, 101, 'nike_ad.mp4');
SELECT * FROM Production_House;
SELECT * FROM Media_Content;
SELECT * FROM User_Account;
SELECT * FROM User_Review;