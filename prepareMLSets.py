import numpy as np
import hashlib

def splitData_basic( inputData, splitRatio):
    #randomly but always the same
    np.random.seed(42)
    shuffledIndice = np.random.permutation( len(inputData) )
    testSetSize = int( len(inputData) * splitRatio )
    testIndices = shuffledIndice[:testSetSize]
    learningIndices = shuffledIndice[testSetSize:]
    return inputData.iloc(learningIndices) , inputData.iloc(testIndices)


def test_set_check( indentifier, splitRatio, hash ):
    return hash( np.int64(indentifier)).digest()[-1] < 256 * splitRatio

def splitData_stable(  inputData, splitRatio, id_column, hash=hashlib.md5 ):
    ids = inputData[ id_column ]
    in_test_set = ids.apply( lambda id_: test_set_check( id_, splitRatio, hash ))
    return inputData.loc[ ~in_test_set], inputData.loc[ in_test_set ]

def splitData_stable_withArtificialIndex( inputData, splitRatio ):
    inputDataWithId = inputData.reset_index()
    traintSet, test_set = splitData_stable( inputDataWithId, splitRatio, "index")

    return traintSet.drop("index", axis=1), test_set.drop("index", axis=1) 