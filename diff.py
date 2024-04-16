from sympy import *
from IPython.display import display

x,y=symbols('x y')
ds = linsolve([Eq(x-y,4),Eq( x + y ,1) ], (x, y))
display(ds)
