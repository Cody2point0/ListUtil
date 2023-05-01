import math
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
list3 = ['alpha', 'beta', 'gamma', 'delta']
list4 = [10, 11, 12, 13]
def avg(list):
  '''
  Returns the avarage of a list
  '''
  return avg(list)


def combine(lists, other, separator='', removeEmptyValues=True):
  '''
  Takes imput from 2 lists and combines the 2 into 1 returned list. Lists must be equal in lenght or function will return type None
  '''
  combine = []
  if len(lists) != len(other):
    return None
  for i in range(len(lists)):
    combine.append(lists[i])
    combine.append(separator)
    combine.append(other[i])
    combine.append(separator)
  if removeEmptyValues == True:
    combine = list(filter(None, combine))
  return combine

def matrix4x4(row1, row2, row3, row4):
  '''
  Generates a nested list matrix with an input of 4 lists. can be read with the matrix value reader
  '''
  if len(row1) == 4:
    if len(row2) == 4:
      if len(row3) == 4:
        if len(row4) == 4:
          matrix = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
          for i in range(4):
            matrix[i][0] = row1[i]
          for i in range(4):
            matrix[i][1] = row2[i]
          for i in range(4):
            matrix[i][2] = row3[i]
          for i in range(4):
            matrix[i][3] = row4[i]
          return matrix
        else:
          return None
        pass
      else:
        return None
      pass
    else:
      return None
    pass
  else:
    return None
def matrixValueReader(matrix, listedCoordinate):
  '''
  Returns the wanted value in a given matrix. top left corner of matrix is 0,0 and bottom right is 3,3
  '''
  return matrix[listedCoordinate[0]][listedCoordinate[1]]
def doubleList(list):
  temp = []
  for i in range(len(list)):
    for j in range(2):
      temp.append(list[i])
  return temp
