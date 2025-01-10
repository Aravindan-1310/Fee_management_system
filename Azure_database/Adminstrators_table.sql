CREATE TABLE Administrators (
    AdminID INT PRIMARY KEY,
    Name VARCHAR(255),
    Role VARCHAR(255)
);

INSERT INTO Administrators (AdminID, Name, Role) VALUES
(1, 'Alice', 'System Administrator'),
(2, 'Bob', 'Database Administrator'),
(3, 'Charlie', 'Network Administrator'),
(4, 'David', 'Security Administrator'),
(5, 'Eve Green', 'Application Administrator');

