def largestRectangleArea(heights):
  # initialize a stack to store the indices
  stack = []
  # initialize the maximum area to 0
  max_area = 0
  # loop through the list of heights
  for i in range(len(heights)):
    # while the stack is not empty and the current height is smaller than the top of the stack
    while stack and heights[i] < heights[stack[-1]]:
      # pop the top of the stack and store it as the height of the rectangle
      h = heights[stack.pop()]
      # if the stack is empty, the left boundary is 0, otherwise it is the previous element in the stack
      l = 0 if not stack else stack[-1] + 1
      # the right boundary is the current index
      r = i
      # calculate the area of the rectangle and update the maximum area if it is larger
      area = h * (r - l)
      max_area = max(max_area, area)
    # push the current index to the stack
    stack.append(i)
  # after the loop, there might be some elements left in the stack
  # we need to pop them and calculate the area of the rectangle formed by them
  while stack:
    # pop the top of the stack and store it as the height of the rectangle
    h = heights[stack.pop()]
    # if the stack is empty, the left boundary is 0, otherwise it is the previous element in the stack
    l = 0 if not stack else stack[-1] + 1
    # the right boundary is the length of the list
    r = len(heights)
    # calculate the area of the rectangle and update the maximum area if it is larger
    area = h * (r - l)
    max_area = max(max_area, area)
  # return the maximum area
  return max_area

# test the code with the given list
l = []
n=int(input("Enter the number of elements you want ot append : "))
for i in range (n):
    l.append(int(input("Enter the number at l({i}): ")))
    if l[i]<0:
      print ("Invalid input , please try again ")
      exit(0)
    else:
      continue
print(largestRectangleArea(l))
