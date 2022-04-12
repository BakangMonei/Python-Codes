# author; MoneiBK
# Finding second derivative
# of exp with respect to x

import symbol;


derivative2_x = sym.diff(exp, x, 2)
print('second derivative w.r.t. x: ',
      derivative2_x)

# Finding second derivative
# of exp with respect to y
derivative2_y = sym.diff(exp, y, 2)
print('second derivative w.r.t. y: ',
      derivative2_y)
