-- -*- encoding: utf-8 -*-
-- File Name: solution.sql
-- Author: ruoyeruolan
-- Email: ryrl970311@gmail.com
-- Created Date: 2025-02-13
-- Description:
-- **************************************

SELECT name as Customers FROM Customers WHERE id not in (SELECT customerId FROM Orders);

SELECT Customers.name as Customers FROM Customers LEFT JOIN Orders ON Customers.id = Orders.cutomerId WHERE Orders.customerId IS NULL;