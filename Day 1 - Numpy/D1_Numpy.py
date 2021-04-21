# Day 1 Journey Log - Numpy Lesson / Revision
import numpy as np

# Creating an array of zeros
arr = np.zeros(10)
print(arr)

# Create an array of 10 ones
arr = np.ones(10)
print(arr)

# Create an array of 10 (fives)
arr = np.ones(10)*5
print(arr)

# Array of integers from 10 to 50
arr = np.arange(10,51)
print(arr)

# Create an array of all the even integers from 10 to 50
arr = np.arange(10,51,2)
print(arr)

# Create a 3x3 matrix with value ranging from 0 to 8
arr = np.arange(0,9).reshape(3,3)
print(arr)

# Generate a random number between 0 and 1
print(np.random.rand(1))

#Generate 25 random numbers that are sampled from a standard distribution
print(np.random.randn(25))

# Create a matrix that starts from 0.01 to 1. with 0.01 increments
print(np.linspace(0.01,1,100).reshape(10,10))
print(np.arange(1,101).reshape(10,10)/100)

# Create an array of 20 linearly spaced points between 0 and 1
print(np.linspace(0,1,20))

# Indexing
# Use this matrix for the following examples

mat = np.arange(1,26).reshape(5,5)
print(mat)

# get this array
# [12,13,14,15]
# [17,18,19,20]
# [22,23,24,25]

print(mat[2:,1:])

# 20
print(mat[3,4])

# [2]
# [7]
# [12]
print(mat[0:3,1:2])

# [12,22,23,24,25]
print(mat[4,:])

# [16,17,18,19,20]
# [21,22,23,24,25]
print(mat[3:,:])

# summation
print(mat.sum())

# standard deviation
print(mat.std())

# summation of columns
print(mat.sum(axis=0))

