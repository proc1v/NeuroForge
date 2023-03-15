import sys
from count import count_sequences

try:
	args = sys.argv[1:]
	N, S = -1, -1
	print(args)

	for index, arg in enumerate(args):
		if arg == 'N':
			N = int(args[index+1])
		elif arg == 'S':
			S = int(args[index+1])
	if N == -1 or S == -1:
		print('The arguments are not correct!!!')
		print('Example: "python horse_on_the_phonepad.py N 4 S 1"')

	else:
		print(f'You can dial {count_sequences(S, N)} distinct numbers in {N} hops from a starting position of {S}.')

except Exception as e:
	print(e)
	print('The arguments are not correct!!!')
	print('Example: "python horse_on_the_phonepad.py N 4 S 1"')