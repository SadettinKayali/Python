# Bracket Matcher
# Have the function BracketMatcher(str) take the str parameter being passed and return 1 if the brackets are correctly matched and each one is accounted for. 
# Otherwise return 0. For example: if str is "(hello (world))", then the output should be 1, but if str is "((hello (world))" the the output should be 0,
# because the brackets do not correctly match up. Only "(" and ")" will be used as brackets. If str contains no brackets return 1.

########################################################################################################
def BracketMatcher(str):

  count = 0
  for c in str:
    if c == '(':
      count += 1
    elif c == ')':
      count -= 1
    if count < 0: return 0

  return 1 if count == 0 else 0

# keep this function call here 
print(BracketMatcher(input()))
########################################################################################################
def BracketMatcher(str):
  lst = []
  try:
    for i in str:
      if i == '(':
        lst.append(i)
      elif i == ')':
        lst.pop()
    return int(lst == [])
  except:
    return 0
# keep this function call here 
print(BracketMatcher(input()))
########################################################################################################
def BracketMatcher(str):
  brackets = []
  for x in str:
    if x == "(":
      brackets.append(x)
    elif x == ")" and "(" in brackets:
      brackets.pop()
    elif x == ")" and "(" not in brackets:
      return 0

  # code goes here
  return 1 if len(brackets) == 0 else 0

# keep this function call here 
print(BracketMatcher(input()))
########################################################################################################
