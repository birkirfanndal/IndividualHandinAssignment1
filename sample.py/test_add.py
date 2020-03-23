from add import add

def add_test():
    assert add.Add("") == 0
    assert add.Add("1") == 1
    assert add.Add("1,2") == 3
    assert add.Add("1,2,3,4") == 10