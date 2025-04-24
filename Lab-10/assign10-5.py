"""Write a program to make the length of each element 15 of a given Numpy array and the string "
"centred, left-justified, right-justified with paddings of _ (underscore)"""

import numpy as np

arr=np.array(["program"])
centered=np.int64.center(arr,15,'_')
left_justified=np.char.ljust(arr,15,'_')
right_justified=np.char.rjust(arr,15,'_')
print(centered)
print(left_justified)
print(right_justified)

