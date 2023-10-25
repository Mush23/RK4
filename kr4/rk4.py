import math as m
import sympy as sp
from sympy.abc import x, y
import traceback

# RK-4 method
def rk4(f, x0, y0, xn, n):
	try:
		l_data = []
		f = sp.lambdify([x, y], sp.sympify(f))
		# Calculating step size
		h = (xn - x0) / n
		# l.append(['x0','y0','yn'])
		print('-------------------------')
		#x0 += xn #change here
		#x0 = x0 + h
		for _ in range(n+1):
			k1 = h * (f(x0, y0))
			k2 = h * (f((x0 + h / 2), (y0 + k1 / 2)))
			k3 = h * (f((x0 + h / 2), (y0 + k2 / 2)))
			k4 = h * (f((x0 + h), (y0 + k3)))
			k = (k1 + 2 * k2 + 2 * k3 + k4) / 6
			yn = y0 + k


			l_data.append(['%.4f' % (x0), '%.4f' % (y0), '%.4f' % (yn), '%.4f' % (k),
						   '%.4f' % (k1), '%.4f' % (k2), '%.4f' % (k3), '%.4f' % (k4)]) #pass actual value

			y0 = yn
			x0 = x0 + h
	except:
		print(traceback.format_exc())
		pass
	return l_data

# Analysis method
def rk4Analyse(f, x0, y0, xn, n, origEq):
	try:
		l_data = []
		f = sp.lambdify([x, y], sp.sympify(f))
		fOrig = sp.lambdify([x, y], sp.sympify(origEq))
		# Calculating step size
		h = (xn - x0) / n
		# l.append(['x0','y0','yn'])
		print('-------------------------')
		#x0 = x0 + h #change here
		for _ in range(n+1):
			k1 = h * (f(x0, y0))
			k2 = h * (f((x0 + h / 2), (y0 + k1 / 2)))
			k3 = h * (f((x0 + h / 2), (y0 + k2 / 2)))
			k4 = h * (f((x0 + h), (y0 + k3)))
			k = (k1 + 2 * k2 + 2 * k3 + k4) / 6
			yn = y0 + k

			#k1_ = h * (fOrig(x0, y0))
			#k2_ = h * (fOrig((x0 + h / 2), (y0 + k1_ / 2)))
			#k3_ = h * (fOrig((x0 + h / 2), (y0 + k2_ / 2)))
			#k4_ = h * (fOrig((x0 + h), (y0 + k3_)))
			#kVal_ = (k1_ + 2 * k2_ + 2 * k3_ + k4_) / 6
			y_analytic = fOrig(x0,y0)

			l_data.append(['%.4f' % (x0), '%.4f' % (y0), '%.4f' % (yn), '%.4f' % (k),
						   '%.4f' % (k1), '%.4f' % (k2), '%.4f' % (k3), '%.4f' % (k4), '%.4f' % (y_analytic),'%.4e' % (y_analytic-y0)]) #pass actual value

			y0 = yn
			x0 = x0 + h
	except Exception:
		print(traceback.format_exc())
		pass
	return l_data


