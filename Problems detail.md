# DSA 20231 Final exam problems detail

## Problem 1: Sum of pair greater than Q

Given n distinct integers a1, a2, ... , an. Given a positive integer Q, Compute the number P of pair of indices i, j such that 1 <= i < j <= n and ai + aj >= Q

Input:

- Line 1: Contains 2 positive Integers n and Q (1 ≤ n ≤ 100000, 1 ≤ Q ≤ 200000)
- Line 2: Contains n distince integers a1, a2, … , an (0 ≤ ai ≤ 200000)

Output:

- Write the value of P

## Problem 2: Count balanced nodes in a Binary search Tree

Given a Binary Search Tree T. Each node is called balanced if:

- It is not a leaf node
- The number of nodes of the left-subtree == the number of nodes of the right subtree

Given a sequence of distinct keys a1, a2, …, an. T is constructed as follows:

- At the beginning, T is empty
- Iteratively insert a1, a2, … an into T

Compute the number of balanced nodes of T

Input:

- Line 1: Contains a positive integer n (1 ≤ n ≤ 2000)
- Line 2: Contains a1, a2, … , an seperated by space (1≤ ai ≤ 100000)

Output:

- Number of balanced nodes of T