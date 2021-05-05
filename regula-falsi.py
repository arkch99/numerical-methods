import sys
import math

e = 0.00001

def f(x):
	return x ** 3 - 2

if len(sys.argv)!= 2:
	print("Usage: python regla-falsi.py <output_file_path.csv>\nMINUS THE ANGULAR BRACES!!\n")
	sys.exit()

x0 = int(input("Enter x0: "))
x1 = int(input("Enter x1: "))
out_path = sys.argv[1]
out = open(out_path, "w")

assert(f(x0) * f(x1) < 0)
n = 1
out.write("n, x0, f(x0), x1, f(x1), x2, f(x2)\n")
while abs(x0 - x1) > e:
	#print("x0:{}, x1:{}".format(x0, x1))
	x2 = x0 - (f(x0) * (x1 - x0)) / (f(x1) - f(x0))
	out.write("{0},{1},{2},{3},{4},{5},{6}\n".format(n, x0, f(x0), x1, f(x1), x2, f(x2)))
	if f(x2) * f(x0) < 0:
		x1 = x2
	elif f(x2) * f(x1) < 0:
		x0 = x2
	n += 1
	if abs(f(x2)) < e:
		break;

print("Root is {0}; calculated in {1} iterations.\nTo view the intermediate values, please open {2} with a spreadsheet viewer.".format(round(x2, 7), n, out_path))

out.close()