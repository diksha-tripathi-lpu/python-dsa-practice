-- Table 1

CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    UserName VARCHAR(50),
    City VARCHAR(50),
    AccountType VARCHAR(20)
);
INSERT INTO Users VALUES
(1, 'Aman Verma', 'Delhi', 'Premium'),
(2, 'Riya Sen', 'Mumbai', 'Regular'),
(3, 'Rahul Sharma', 'Bengaluru', 'Premium'),
(4, 'Priya Gupta', 'Kolkata', 'Regular'),
(5, 'Arjun Mehta', 'Chennai', 'Premium'),
(6, 'Neha Singh', 'Lucknow', 'Regular'),
(7, 'Karan Patel', 'Ahmedabad', 'Premium'),
(8, 'Sneha Nair', 'Hyderabad', 'Regular'),
(9, 'Vikram Joshi', 'Pune', 'Premium'),
(10, 'Anjali Roy', 'Jaipur', 'Regular');


-- Table 2

CREATE TABLE Restaurants (
    RestaurantID INT PRIMARY KEY,
    RestaurantName VARCHAR(100),
    Cuisine VARCHAR(50),
    Rating DECIMAL(2,1)
);
INSERT INTO Restaurants VALUES
(101, 'Spice Symphony', 'North Indian', 4.5),
(102, 'Pizza Express', 'Italian', 3.9),
(103, 'Biryani House', 'Mughlai', 4.6),
(104, 'Dragon Wok', 'Chinese', 4.2),
(105, 'South Spice', 'South Indian', 4.4),
(106, 'Burger Hub', 'Fast Food', 3.8),
(107, 'Taco Fiesta', 'Mexican', 4.1),
(108, 'Sushi World', 'Japanese', 4.7),
(109, 'Cafe Delight', 'Cafe', 4.3),
(110, 'Royal Thali', 'Gujarati', 4.5);


-- Table 3

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    UserID INT,
    RestaurantID INT,
    BillAmount DECIMAL(10,2),
    OrderDate DATE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (RestaurantID) REFERENCES Restaurants(RestaurantID)
);
INSERT INTO Orders VALUES
(501, 1, 101, 1200.00, '2026-07-15'),
(502, 2, 102, 450.00, '2026-07-16'),
(503, 3, 103, 850.00, '2026-07-16'),
(504, 4, 104, 650.00, '2026-07-17'),
(505, 5, 105, 980.00, '2026-07-17'),
(506, 6, 106, 320.00, '2026-07-18'),
(507, 7, 107, 720.00, '2026-07-18'),
(508, 8, 108, 1450.00, '2026-07-19'),
(509, 9, 109, 560.00, '2026-07-19'),
(510, 10, 110, 890.00, '2026-07-20');


-- Table 4
CREATE TABLE Deliveries (
    DeliveryID INT PRIMARY KEY,
    OrderID INT,
    DeliveryStatus VARCHAR(20),
    DeliveryTimeMinutes INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);
INSERT INTO Deliveries VALUES
(901, 501, 'Delivered', 25),
(902, 502, 'Delivered', 42),
(903, 503, 'Delivered', 30),
(904, 504, 'Cancelled', 0),
(905, 505, 'Delivered', 35),
(906, 506, 'In-Transit', 20),
(907, 507, 'Delivered', 28),
(908, 508, 'Delivered', 40),
(909, 509, 'Cancelled', 0),
(910, 510, 'Delivered', 33);


-- Section A

-- Question 1

SELECT
    U.UserName,
    R.RestaurantName,
    O.BillAmount
FROM Orders O
JOIN Users U
ON O.UserID = U.UserID
JOIN Restaurants R
ON O.RestaurantID = R.RestaurantID;


-- Question 2

SELECT DISTINCT
    R.RestaurantName
FROM Restaurants R
JOIN Orders O
ON R.RestaurantID = O.RestaurantID
JOIN Deliveries D
ON O.OrderID = D.OrderID;


-- Question 3

SELECT
    O.OrderID,
    U.UserName,
    D.DeliveryTimeMinutes
FROM Orders O
JOIN Users U
ON O.UserID = U.UserID
JOIN Deliveries D
ON O.OrderID = D.OrderID
WHERE D.DeliveryTimeMinutes > 35;


-- Question 4

SELECT
    U.UserName,
    SUM(O.BillAmount) AS TotalSpent
FROM Users U
JOIN Orders O
ON U.UserID = O.UserID
GROUP BY U.UserName;


-- Section B

-- Question 5

SELECT
    U.UserName,
    COUNT(O.OrderID) AS TotalOrders
FROM Users U
LEFT JOIN Orders O
ON U.UserID = O.UserID
GROUP BY U.UserID, U.UserName;

-- Question 6

SELECT
    R.RestaurantName,
    SUM(O.BillAmount) AS TotalRevenue
FROM Restaurants R
JOIN Orders O
ON R.RestaurantID = O.RestaurantID
JOIN Users U
ON O.UserID = U.UserID
WHERE U.City = 'Delhi'
GROUP BY R.RestaurantID, R.RestaurantName
HAVING SUM(O.BillAmount) > 5000;

-- Question 7

SELECT
    R.RestaurantName,
    COUNT(*) AS CancelledOrders
FROM Restaurants R
JOIN Orders O
ON R.RestaurantID = O.RestaurantID
JOIN Deliveries D
ON O.OrderID = D.OrderID
WHERE D.DeliveryStatus = 'Cancelled'
GROUP BY R.RestaurantID, R.RestaurantName;


-- Section C

-- Question 8

SELECT
    U.UserName,
    U.City,
    O.BillAmount
FROM Users U
JOIN Orders O
ON U.UserID = O.UserID
WHERE O.BillAmount >
(
    SELECT AVG(BillAmount)
    FROM Orders
);

-- Question 9

SELECT
    R.Cuisine,
    AVG(D.DeliveryTimeMinutes) AS AverageDeliveryTime
FROM Restaurants R
JOIN Orders O
ON R.RestaurantID = O.RestaurantID
JOIN Deliveries D
ON O.OrderID = D.OrderID
GROUP BY R.Cuisine
HAVING AVG(R.Rating) > 4.0;

-- Question 10

SELECT
    R.Cuisine,
    R.RestaurantName,
    COUNT(O.OrderID) AS OrderCount,
    RANK() OVER (
        PARTITION BY R.Cuisine
        ORDER BY COUNT(O.OrderID) DESC
    ) AS RestaurantRank
FROM Restaurants R
LEFT JOIN Orders O
ON R.RestaurantID = O.RestaurantID
GROUP BY
    R.RestaurantID,
    R.RestaurantName,
    R.Cuisine;


