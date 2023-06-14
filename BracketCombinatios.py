## Bracket Combinations
# Have the function BracketCombinations(num) read num which will be an integer greater than or equal to zero, and return the number of valid combinations that can be formed with num pairs of parentheses. 
# For example, if the input is 3, then the possible combinations of 3 pairs of parenthesis, namely: ()()(), are ()()(), ()(()), (())(), ((())), and (()()). 
# There are 5 total combinations when the input is 3, so your program should return 5.

"""
from math import factorial

def BracketCombinations(num):
  return int(factorial(2 * num) / (factorial(num + 1) * factorial(num)))
  # code goes here
  # return num

# keep this function call here 
print(BracketCombinations(input()))
"""
"""
def BracketCombinations(num):
  return int(Fact(2 * num) / (Fact(num + 1) * Fact(num)))

def Fact(n):  
  if (n == 1):
    return 1
  else:
    return n * Fact(n-1)   
# keep this function call here 
print(BracketCombinations(input()))
"""
"""
def BracketCombinations(num):
    
  # code goes here
  return bracket(num,num)

def bracket(l,r):
  if r>0:
    if l>r:
      return bracket(l-1,r) +  bracket(l,r-1)
    else:
      return bracket(l,r-1)
  else:
    return 1

# keep this function call here 
print(BracketCombinations(input()))
"""
"""
from math import factorial

def BracketCombinations(num):

  # https://en.wikipedia.org/wiki/Catalan_number

  return int(factorial(2 * num) / (factorial(num + 1) * factorial(num)))

# keep this function call here 
print(BracketCombinations(input()))
"""
"""
def BracketCombinations(num):
      
  return int(Fact(2 *num) / (Fact(num + 1)*  Fact(num)))

def Fact(num):
  fact = 1
  while (num!=0):
    fact=fact*num
    num=num-1
  return fact
# keep this function call here 
print(BracketCombinations(input()))
"""
"""
def BracketCombinations(num):
      num=int(num)
  return fact(num*2)//(fact(num+1)*fact(num))

def fact(n):
  if n==1:
    return 1
  else:
    return n*fact(n-1)

# keep this function call here 
print(BracketCombinations(input()))
"""
"""
def BracketCombinations(num):
      answer=int(factorial(2*num) /(factorial(num+1)*factorial(num)))
  # code goes here
  return answer

def factorial(num):
  n_fat = 1
    # calcule n!
  for i in range(2,num+1):
    n_fat = n_fat * i 
  return n_fat
# keep this function call here 
print(BracketCombinations(input()))
"""
"""
def BracketCombinations(num):
      num = (factorial(2*num)) / (factorial(num)*factorial(num+1))
  # code goes here
  return int(num)

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
# keep this function call here 
print(BracketCombinations(input()))
"""