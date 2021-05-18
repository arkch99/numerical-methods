import sys
import math

if len(sys.argv)!= 2:
	print("Usage: python bisect.py <output_file_path.csv>\nMINUS THE ANGULAR BRACES!!\n")
	sys.exit()

def f(x): # edit this to correspond to the required function
	return x**3 - 2

a = int(input("Enter a: "))
b = int(input("Enter b: "))
out_path = sys.argv[1]
out = open(out_path, "w")

e = 0.0001

assert(f(a) * f(b) < 0)

out.write("n, a, b, c, f(c)\n")
count = 1
while abs(b - a) > e:
	orig_a = a
	orig_b = b
	c = (a + b) / 2
	if f(a) * f(c) <= 0:
		b = c
	elif f(b) * f(c) <= 0:
		a = c
	out.write("{0},{1},{2},{3},{4}\n".format(count, orig_a, orig_b, c, f(c)))
	count += 1
print("Root is {0}; calculated in {1} iterations.\nTo view the intermediate values, please open {2} with a spreadsheet viewer.".format(round(c, 7), count, out_path))

out.close()

