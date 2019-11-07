Implement a class for a stack that supports all the regular functions (push, pop) and an additional function of max() which returns the maximum element in the stack (return None if the stack is empty). Each method should run in constant time.

Solution:
class MaxStack:
  def __init__(self):
    self.value = []

  def push(self, val):
    return self.value.append(val)

  def pop(self):
    return self.value.pop(1)

  def max(self):
    l = len(self.value)
    return l > 0 and max(self.value) or None

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
