SELECT SUM(Sales) AS Total_Sales FROM sales_data;

SELECT SUM(Profit) AS Total_Profit FROM sales_data;

SELECT MONTH(Order_Date) AS Month, SUM(Sales)
FROM sales_data
GROUP BY MONTH(Order_Date);

SELECT Product_Name, SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 5;
