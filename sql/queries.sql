-- Total Revenue
SELECT SUM(TotalPrice) AS total_revenue
FROM retail;

-- Top 5 Countries
SELECT Country,
SUM(TotalPrice) AS revenue
FROM retail
GROUP BY Country
ORDER BY revenue DESC
LIMIT 5;

-- Top 5 Products
SELECT Description,
SUM(Quantity) AS total_qty
FROM retail
GROUP BY Description
ORDER BY total_qty DESC
LIMIT 5;