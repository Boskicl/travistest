from Calc import Calc

def test_add():
    x,y = 1,2
    instance = Calc(x,y)
    if instance.add() == x+y:
        print('True')

test_add()
