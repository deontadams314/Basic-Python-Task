#Towers of Hanoi
def move(beg, end):
	print("Move " + str(beg) + " to " + str(end))


def tower(n, beg, aux, end):
	if n == 1:
		move(beg, end)
	else:
		tower(n-1, beg, end, aux)
		tower(1, beg, aux, end)
		tower(n-1, aux, beg, end)
