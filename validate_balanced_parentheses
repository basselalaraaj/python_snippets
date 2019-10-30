Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:
Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False

Solution:
class Solution:
  def isValid(sel, s):
    isValid = True
    if not s:
      return isValid

    open_list = ['[', '{', '(']
    close_list = [']', '}', ')']
    stack = []
    for i in range(len(s)):
      if s[i] in open_list:
        stack.append(s[i])
      elif s[i] in close_list:
        closeIndex = close_list.index(s[i])
        if open_list[closeIndex] == stack[-1]:
          stack.pop()

    if len(stack) > 0:
      isValid = False
    return isValid

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
