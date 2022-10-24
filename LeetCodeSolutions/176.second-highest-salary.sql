#
# [176] Second Highest Salary
#
# https://leetcode.com/problems/second-highest-salary/description/
#
# database
# Easy (23.25%)
# Total Accepted:    72.4K
# Total Submissions: 310.9K
# Testcase Example:  '{"headers": {"Employee": ["Id", "Salary"]}, "rows": {"Employee": [[1, 100], [2, 200], [3, 300]]}}'
#
# Write a SQL query to get the second highest salary from the Employee table.
#
#
# +----+--------+
# | Id | Salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
#
#
# For example, given the above Employee table, the query should return 200 as
# the second highest salary. If there is no second highest salary, then the
# query should return null.
#
#
# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | 200                 |
# +---------------------+
#
#
#
# Write your MySQL query statement below

SELECT (SELECT DISTINCT Employee.Salary  FROM Employee ORDER BY Employee.Salary DESC LIMIT 1 OFFSET 1) AS "SecondHighestSalary";
