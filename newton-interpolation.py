import sys
import math

def getDiffTable(x, y):
	n = len(x)
	diffs = [[] for i in range(n)]
	diffs[0] = y[:]
	rowNo = 0
	for row in diffs[1:]:
		for i in range(1, n):
			row.append(diffs[rowNo][i] - diffs[rowNo][i - 1])
		rowNo += 1
		n -= 1	
	for row in diffs:
		for i, val in enumerate(row):			
			row[i] = round(val, 8)
	print(diffs)
	return diffs

def forwardInterpolation(s, diffs):
	val = 0
	# Δ ∇
	for i, row in enumerate(diffs):
		sProd = 1
		for nS in range(i): # calculate the product of the s-terms
			sProd *= s - nS
		val += (sProd * row[0]) / math.factorial(i)
	return val

def backwardInterpolation(s, diffs):
	val = 0
	# Δ ∇
	for i, row in enumerate(diffs):
		sProd = 1
		for nS in range(i): # calculate the product of the s-terms
			sProd *= s + nS
		val += (sProd * row[-1]) / math.factorial(i)
	return val

def writeDiff(diffs, out, method): # TODO: inspect this
	symbols = ['Δ', '∇']
	usedSym = symbols[method]
	n = len(diffs)
	#out.write(('{},' * n).format(list(range(n))))
	out.write(',' + ','.join(map(str, range(n)))  + '\n')
	rowHeads = ['y']
	for i in range(1, n):
		rowHeads.append('{}{}y'.format(usedSym, i))
	#out.write('x,' + ','.join(map(str, x)) + '\n')
	for i, row in enumerate(diffs):
		out.write("{},".format(rowHeads[i]) + ','.join(map(str, row)) + '\n')
	out.close()


if len(sys.argv) != 2:
	print("Usage: python newton-interpolation.py <output_file_path.csv>\nMINUS THE ANGULAR BRACES!")
	sys.exit()

out_path = sys.argv[1]
out = open(out_path, "w")

nVals = int(input("Enter number of given values: "))

x = []
fx = []

for i in range(nVals):
	x.append(float(input("Enter x{}: ".format(i))))
	fx.append(float(input("Enter f(x{}): ".format(i))))

h = x[1] - x[0]

xReq = float(input("Enter x at which to calculate the function: "))
ans = 0

diffs = getDiffTable(x, fx)
FWD = 0
BWD = 1
method = -1
if abs(xReq - x[0]) < abs(xReq - x[-1]):
	s = (xReq - x[0]) / h
	ans = forwardInterpolation(s, diffs)
	method = FWD
else:
	s = (xReq - x[-1]) / h
	ans = backwardInterpolation(s, diffs)
	method = BWD
writeDiff(diffs, out, method)
print(round(ans, 8))