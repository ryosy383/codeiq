# CodeIQ 'fast exp' test code
#Language: Python (ideone.com)
#Output:
#Success	 time: 0.01 memory: 7896 signal:0
#              x             exp        fast_exp       rel.error
#      -2.000000        0.135335        0.135335        0.000000
#      -1.000000        0.367879        0.367879        0.000000
#       0.000000        1.000000        1.000000        0.000000
#       1.000000        2.718282        2.718282        0.000000
#       2.000000        7.389056        7.389056        0.000000
#       3.000000       20.085537       20.085537        0.000000
#       4.000000       54.598150       54.598150        0.000000
#       5.000000      148.413159      148.413159        0.000000

import sys
from math import exp
def fast_exp(x):
	"""
	Please implement fast exp(x) without using power/logarithmic function
	"""
	eps = sys.float_info.min;
	elementary = 1
	summary = 0
	positive = True
	if x < 0:
		positive = False
		x = -x

	i = 1
	while elementary >= eps:
		summary += elementary
		elementary *= x / i
		i += 1
		if summary > sys.float_info.max:
			break
	
	if not positive:
		return 1 / summary
	else:
		return summary
		
	return 0.0

if __name__ == '__main__':
    print("%15s %15s %15s %15s" % ("x", "exp", "fast_exp", "rel.error"))
    t = -2
    while t <= 5:
        x = float(t)
        ev = exp(x)
        approx = fast_exp(x)
        abserr = abs(approx - ev)
        relerr = abs(approx - ev) / ev
        print("%15.6f %15.6f %15.6f %15.6f" % (x, ev, approx, relerr))
        
        #assert relerr < 0.1
        t += 1

        
        

