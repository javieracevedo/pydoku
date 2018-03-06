# Just a module containing utility functions


# Utils

def nonblank_lines(f):
  for l in f:
    line = l.rstrip()
    if line:
      yield line

# check if a value appears more than on
# on a list or a string
def appearsTwice(l, value, ignore=None):
  # Counter to keep track of how much a value appears
  appearance = 0
  if is2dArray(l):
    for array in l:
      for i in array:
        if i == value:
          appearance += 1
  else:
    for item in l:
      if item == value and item != ignore:
        appearance += 1
    
  if appearance > 1:
    return True
  else:
    return False

# Check if a given array is a 2D array
def is2dArray(array):
  for l in array:
    if type(l) is not list:
      return False
  return True

# Checks if a value appears inside a 2d array
def in2dArray(array, value):
  for outer_v in outer_arr:
    for inner_v in inner_arr:
      if inner_v == value:
        return True
  return False
