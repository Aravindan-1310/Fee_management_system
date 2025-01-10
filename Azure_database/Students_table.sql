CREATE TABLE students_fee_status (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    total DECIMAL(10, 2),
    paid DECIMAL(10, 2),
    email VARCHAR(255),
    due_date DATE
);

INSERT INTO students_fee_status (id, name, total, paid, email, due_date) VALUES
(1, 'aravindan', 10000.00, 5000.00, 'aravindan.1310@outlook.com', '2025-01-01'),
(2, 'arun', 10000.00, 10000.00, 'aravindan.1310@outlook.com', '2025-01-01'),
(3, 'kamal', 10000.00, 6000.00, 'aravindani.aids2021@outlook.com', '2025-01-01'),
(4, 'kiruba', 10000.00, 10000.00, 'aravindani.aids2021@outlook.com', '2025-01-01'),
(5, 'akash', 10000.00, 9000.00, 'tonyaravindan@outlook.com', '2025-01-01'),
(6, 'hemachandar', 10000.00, 10000.00, 'hemachandar@outlook.com', '2025-01-01'),
(7, 'hemadri', 10000.00, 10000.00, 'hemadri@outlook.com', '2025-01-01'),
(8, 'mukesh', 10000.00, 10000.00, 'mukesh@outlook.com', '2025-01-01'),
(9, 'vishal', 10000.00, 10000.00, 'vishal@outlook.com', '2025-01-01'),
(10, 'abi', 10000.00, 10000.00, 'abi@outlook.com', '2025-01-01'),
(11, 'suresh', 10000.00, 10000.00, 'suresh@outlook.com', '2025-01-01'),
(12, 'mani', 10000.00, 10000.00, 'mani@outlook.com', '2025-01-01'),
(13, 'kishore', 10000.00, 10000.00, 'kishore@outlook.com', '2025-01-01'),
(14, 'azfer', 10000.00, 10000.00, 'azfer@outlook.com', '2025-01-01'),
(15, 'arav', 10000.00, 10000.00, 'arav@outlook.com', '2025-01-01'),
(16, 'yogesh', 10000.00, 10000.00, 'yogesh@outlook.com', '2025-01-01'),
(17, 'keerthi', 10000.00, 10000.00, 'keerthi@outlook.com', '2025-01-01'),
(18, 'vasu', 10000.00, 10000.00, 'vasu@outlook.com', '2025-01-01'),
(19, 'ani', 10000.00, 10000.00, 'ani@outlook.com', '2025-01-01'),
(20, 'jagan', 10000.00, 10000.00, 'jagan@outlook.com', '2025-01-01');

