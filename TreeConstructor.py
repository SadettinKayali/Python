# Tree Constructor
# Have the function TreeConstructor(strArr) take the array of strings stored in strArr, which will contain pairs of integers in the following format: 
# (i1,i2), where i1 represents a child node in a tree and the second integer i2 signifies that it is the parent of i1. For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"], 
# then this forms the following tree:

# which you can see forms a proper binary tree. Your program should, in this case, return the string true because a valid binary tree can be formed. 
# If a proper binary tree cannot be formed with the integer pairs, then return the string false. All of the integers within the tree will be unique, 
# which means there can only be one node in the tree with the given integer value.

########################################################################################################
def TreeConstructor(strArr):
  parentList = []
  for node in strArr:
    child,parent = eval(node)
    parentList.append(parent)
    if parentList.count(parent) > 2:
      return "false"
  return "true"
  # code goes here
 

# keep this function call here 
print(TreeConstructor(input()))
########################################################################################################
def TreeConstructor(strArr):
  root = ''
  ptc = {} # parent to child
  ctp = {}  # child to parent
  for s in strArr:
    c = s.split(',')[0][1:]  # find child
    p = s.split(',')[1][:-1]  # find parent
    
    if p not in ptc:
      ptc[p] = [c]
    else:
      if len(ptc[p]) == 2: return 'false'  
      else: ptc[p].append(c)
      # this parent already has 2 children. cannot add one more
    if c in ctp: # c is already a child, cannot be child again
      return 'false'
    ctp[c] = p
  
  # check number of roots
  for r in ptc:
    if r not in ctp: 
      if root == '': root = p  # first and should be the only root
      else: return 'false'
    
  return 'true'

# keep this function call here 
print(TreeConstructor(input()))
########################################################################################################
def TreeConstructor(strArr):
      
  # ndic={}
  listb=[]
  if len(strArr)<1:
    return 'false'
    
  elif len(strArr)<2:
    return 'true'
  
  else:
    for nodes in strArr:
      listb.append(nodes[3])
  
    if any( listb.count(listb[i])>2 for i in range(len(listb))):
      return 'false'
    else:
      return 'true'

print(TreeConstructor(input()))
########################################################################################################
def TreeConstructor(strArr):
    tree = [eval(i) for i in strArr]
    child_nodes = [i[0] for i in tree]
    parent_nodes = [i[1] for i in tree]
    if len(tree) < 2:
        return "true"
    parents = dict()
    for i in parent_nodes:
        parents[i] = parents.get(i, 0)+1
    counter = 0
    for k,v in parents.items():
        if v == 2:
            counter+=1
        if v > 2:
            return "false"
    if counter > 2:
        return "false"
    if len(child_nodes) != len(set(child_nodes)):
        return "false"
    return "true"

# keep this function call here 
print(TreeConstructor(input()))
    ########################################################################################################
def TreeConstructor(strArr):
      pNode = {}
  cNode = {}
  for each in strArr:
    (x,y) = eval(each)
    pNode[y] = pNode.get(y,0)+1
    cNode[x] = cNode.get(x,0)+1
  for c in cNode: 
    if cNode[c] >1: return "false"
  for p in pNode:
    if pNode[p] >2: return "false"
  return "true"
# keep this function call here 
print(TreeConstructor(input()))
########################################################################################################
