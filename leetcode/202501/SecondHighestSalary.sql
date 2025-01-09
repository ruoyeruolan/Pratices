-- -*- encoding: utf-8 -*-
-- File Name: example.sql
-- Author: Your Name
-- Created Date: 2025-01-10
-- Description: Description
-- **************************************


-- Table: Employee

-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | id          | int  |
-- | salary      | int  |
-- +-------------+------+
-- id is the primary key (column with unique values) for this table.
-- Each row of this table contains information about the salary of an employee.
 

-- Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

-- The result format is in the following example.

SELECT IFNULL ((SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET 1), NULL) AS SecondHighestSalary;