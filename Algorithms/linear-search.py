#linear search algorithm

def linearSearch(values: list[int], target: int):
	counter = 0

	for v in values:
		counter += 1
		if v == target:
			return counter


def main():
	values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
	target = int(input("Enter a number between 1 and 20: "))
	count = linearSearch(values, target)
	print(f"{target} was found in {count} iterations. This is a linear search because the worst case scenario O(n), will have more iterations when it has more inputs to work with.")


if __name__ == '__main__':
	main()