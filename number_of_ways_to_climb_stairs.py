You are given a positive integer N which represents the number of steps in a staircase. You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.

Solution:
def ways(n):
  if n <= 1:
    return n
  return ways(n-1)+ways(n-2)

def staircase(n):
  return ways(n+1)
  
print(staircase(4))
# 5
print(staircase(5))
# 8 
