-- -*- encoding: utf-8 -*-
-- File Name: EmployeesEarningMoreThanTheirManagers.sql
-- Author: ruoyeruolan
-- Email: ryrl970311@gmail.com
-- Created Date: 2025-01-14
-- Description: leetcode 181
-- **************************************

-- Table: `Employee`
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- | salary      | int     |
-- | managerId   | int     |
-- +-------------+---------+
-- `id` is the primary key (column with unique values) for this table.
-- Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
 
-- Write a solution to find the employees who earn more than their managers.
-- Return the result table in any order.
-- The result format is in the following example.

-- Example 1:
-- Input: 
-- Employee table:
-- +----+-------+--------+-----------+
-- | id | name  | salary | managerId |
-- +----+-------+--------+-----------+
-- | 1  | Joe   | 70000  | 3         |
-- | 2  | Henry | 80000  | 4         |
-- | 3  | Sam   | 60000  | Null      |
-- | 4  | Max   | 90000  | Null      |
-- +----+-------+--------+-----------+
-- Output: 
-- +----------+
-- | Employee |
-- +----------+
-- | Joe      |
-- +----------+
-- Explanation: Joe is the only employee who earns more than his manager.

SELECT e1.name AS Employee FROM Employee e1 JOIN Employee e2 ON e1.managerId = e2.id WHERE e1.salary > e2.salary

SELECT e1.name AS Employee FROM Employee e1, Employee e2 WHERE e1.managerId = e2.id and e1.salary > e2.salary