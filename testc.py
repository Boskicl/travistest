from Calc import Calc

def test_add():
    x,y = 1,2
    instance = Calc(x,y)
    assert instance.add() == x + y, "Add method"