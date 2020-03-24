import pytest
from add import add

def add_test():
    assert add.Add("") == 0
    assert add.Add("1") == 1
    assert add.Add("1,2") == 3
    assert add.Add("1,2,3,4") == 10
    assert add.Add("21,5\n4,7") == 37
    assert add.Add("2,59\n1004") == 61