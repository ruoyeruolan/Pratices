-- -*- encoding: utf-8 -*-
-- File Name: NthHighestSalary.sql
-- Author: ruoyeruolan
-- Email: ryrl970311@gmail.com
-- Created Date: 2025-01-11
-- Description:

-- Table: Employee

-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | id          | int  |
-- | salary      | int  |
-- +-------------+------+
-- `id` is the primary key (column with unique values) for this table.
-- Each row of this table contains information about the salary of an employee.
 
-- Write a solution to find the `nth` highest salary from the `Employee` table. If there is no `nth` highest salary, return `null`.
-- The result format is in the following example.


-- Input: 
-- Employee table:
-- +----+--------+
-- | id | salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- n = 2
-- Output: 
-- +------------------------+
-- | getNthHighestSalary(2) |
-- +------------------------+
-- | 200                    |
-- +------------------------+
-- Example 2:

-- Input: 
-- Employee table:
-- +----+--------+
-- | id | salary |
-- +----+--------+
-- | 1  | 100    |
-- +----+--------+
-- n = 2
-- Output: 
-- +------------------------+
-- | getNthHighestSalary(2) |
-- +------------------------+
-- | null                   |
-- +------------------------+
-- **************************************


CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET N
  );
END
