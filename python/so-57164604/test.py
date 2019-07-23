from sklearn.model_selection import ParameterGrid
from multiprocessing import Pool
from enum import Enum

var1 = 'var1'
var2 = 'var2'
abc = [1, 2]
xyz = list(range(1_00_000))
pg = [{'variant': [var1],
       'abc': abc,
       'xyz': xyz, },
      {'variant': [var2],
       'abc': abc, }]
parameterGrid = ParameterGrid(pg)
myTemp = list(parameterGrid)

print('len(parameterGrid):', len(parameterGrid))


def myFunc(myParam):
    if myParam['abc'] == 1:
        raise ValueError('error thrown')
    print(myParam)


pool = Pool(1)
myList = pool.map(myFunc, parameterGrid)
