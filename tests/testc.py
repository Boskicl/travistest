from Calc import Calc

x,y = 1,2
instance = Calc(x,y)
assert instance.add() == x + y, "Add method"
