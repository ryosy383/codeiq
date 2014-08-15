# CodeIQ 'prevent overflow' test code
from math import log, exp
from exceptions import OverflowError
def calc_normally(x, y):
    try:
        return log(exp(x) + exp(y))
    except OverflowError:
        return float('inf')
def calc_precisely(x, y):
	"""
	 W(x, y) = log exp(x) (1.0 + exp(y-x))
	 ∴W(x, y) = x + log (1.0 + exp(y-x))
	 （ただし、x > y を仮定する）
	 これにより、指数部の計算がexp(y-x)に収まる
	 logsumexp(x, y)関数は、上記の要領で、W(x, y)を計算する
	 下式のような三項間の和を求める際も、二項間の和 W(x, y)を用いて次のように計算可能
	 W(x, y, z) = log (exp(x) + exp(y) + exp(z))
	 W(x, y, z) = W(W(x, y), z)
	 = W(log(exp(x) + exp(y)), z)
	 = log(exp(log(exp(x) + exp(y))) + exp(z))
	 = log(exp(x) + exp(y) + exp(z))
	"""
	if x == y:
		return Math.log(2)
	vmin = x if x <= y else y
	vmax = x if x >= y else y
	if vmax > vmin + 50:
		return vmax;
	else:
		return vmax + log (exp (vmin - vmax) + 1.0)
if __name__ == '__main__':
    x = 9.0; y = 11.0;
    print("%15.6f %15.6f" % (calc_normally(x, y), calc_precisely(x, y)))
    x = 99.1; y = 100.9;
    print("%15.6f %15.6f" % (calc_normally(x, y), calc_precisely(x, y)))
    x = 999.2; y = 1000.8;
    print("%15.6f %15.6f" % (calc_normally(x, y), calc_precisely(x, y)))
    x = 9999.3; y = 10000.7;
    print("%15.6f %15.6f" % (calc_normally(x, y), calc_precisely(x, y)))
    x = 99999.4; y = 100000.6;
    print("%15.6f %15.6f" % (calc_normally(x, y), calc_precisely(x, y)))
