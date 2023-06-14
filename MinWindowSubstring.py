# Min Window Substring
# Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr, which will contain only two strings, the first parameter being the string N and 
# the second parameter being a string K of some characters, and your goal is to determine the smallest substring of N that contains all the characters in K. 
# For example: if strArr is ["aaabaaddae", "aed"] then the smallest substring of N that contains the characters a, e, and d is "dae" located at the end of the string. 
# So for this example your program should return the string dae.

# Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that contains all of the characters in K is "aabd" which is located at the beginning of the string. 
# Both parameters will be strings ranging in length from 1 to 50 characters and all of K's characters will exist somewhere in the string N. 
# Both strings will only contains lowercase alphabetic characters.
########################################################################################################
def MinWindowSubstring(strArr):

  n = strArr[0]
  k = list(strArr[1])

  windowSize = len(k)
  
  while windowSize <= len(n):
    for i in range(len(n) - windowSize + 1):
      substring = n[i : i + windowSize]
      isInSubstring = True
      substringCopy = substring
      for character in k:
        if character in substringCopy:
          characterIndex = substringCopy.find(character)
          substringCopy = substringCopy[:characterIndex] + substringCopy[characterIndex + 1:]
        else:
          isInSubstring = False
          break
      if isInSubstring:
        return substring
    windowSize += 1
      
# keep this function call here 
print(MinWindowSubstring(input()))
########################################################################################################
def MinWindowSubstring(a):

  x = len(a[1])
  while True:
    for i in range(x, len(a[0]) + 1):
      y = a[0][i-x:i]
      met = True
      for z in set(list(a[1])):
        if z not in y or y.count(z) < a[1].count(z):
          met = False
          break
      if met == True:
        return y
    x += 1

# keep this function call here 
print(MinWindowSubstring(input()))
########################################################################################################
def MinWindowSubstring(inp):
      length = len(inp[1])
  check = inp[1]
  contains = 0
  

  while length <= len(inp[0]):
    for i in range(0, len(inp[0]) - length+1):
      sub = inp[0][i:i+length]
      temp = list(sub)
      for i in check:
        if i not in temp:
          contains = 0
          break
        temp.remove(i)
        contains += 1
      if contains:
       return sub

    length += 1


print(MinWindowSubstring(input()))
########################################################################################################

