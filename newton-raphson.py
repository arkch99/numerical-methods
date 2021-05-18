import sys
import math

e = 0.000001

def f(x): 
	return x**x + 2*x - 6 # replace this with the given function

def df(x):
	return x**x * (math.log(x) + 1) + 2 # replace this with the first derivative of the given function

if len(sys.argv) != 2:
	print("Usage: python newton-raphson.py <output_file_path.csv>\nMINUS THE ANGULAR BRACES!")
	sys.exit()

a = int(input("Enter a: "))
b = int(input("Enter b: "))

out_path = sys.argv[1]
out = open(out_path, "w")

out.write("n, x0, f(x0), f'(x0), x1\n")

assert(f(a) * f(b) < 0)

x0 = (a + b) / 2

n = 1
while abs(f(x0)) > e:
	x1 = x0 - (f(x0)/df(x0))
	out.write("{}, {}, {}, {}, {}\n".format(n, x0, f(x0), df(x0), x1))
	x0 = x1
	n += 1

print("Root is {0}; calculated in {1} iterations.\nTo view the intermediate values, please open {2} with a spreadsheet viewer.".format(round(x1, 7), n, out_path))

out.close()



