A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.

Example:
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"

Input: "tracecars"
Output: "racecar"

Solution:
class Solution: 
    def longestPalindrome(self, s):
      n = len(s)
      table = [[0 for x in range(n)] for y in range(n)]

      i = 0
      while i < n:
        table[i][i] = 1
        i = i + 1
      
      start = 0
      i = 0
      while i < n-1:
        if s[i] == s[i+1]:
          table[i][i+1] = 1
          start = i
          end = i+1
        i = i + 1
      
      maxlength = 0
      end = 0
      y = 0
      while y < n:
        x = y
        last = 0
        while x < n :
          if s[y] == s[x]:
            table[y][x] = 1
            if x > y and x > end:
              last = x
            length = last-y
            if length > maxlength:
              maxlength = length
              start = y
              end = last+1
          x = x + 1
        y = y + 1
      return s[start:end]
        
# Test program
print(str(Solution().longestPalindrome("banana")))
print(str(Solution().longestPalindrome("million")))
print(str(Solution().longestPalindrome("tracecars")))
# racecar
