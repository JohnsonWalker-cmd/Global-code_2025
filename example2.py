#total = fold(lambda item, running_total: item + running_total, [1, 2, 3, 4, 5])
from functools import fold

total = fold(lambda x , running_total : x + running_total , [1,3,4])
print(total)

