from sklearn.model_selection import ParameterGrid
from multiprocessing import Pool
from enum import Enum

var1 = 'var1'
var2 = 'var2'
abc = [1, 2]
xyz = list(range(1000))  # reduce numbers for debug
pg = [{'variant': [var1],
       'abc': abc,
       'xyz': xyz, },
      {'variant': [var2],
       'abc': abc, }]
parameterGrid = ParameterGrid(pg)
myTemp = list(parameterGrid)

print('len(parameterGrid):', len(parameterGrid))


def myFunc(myParam):
    print("Start working")
    if myParam['abc'] == 1:
        raise ValueError('error thrown')
    print(myParam)


pool = Pool(1)
myList = pool.map(myFunc, parameterGrid)
