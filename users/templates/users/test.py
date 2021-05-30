def rec_dig_sum(n):
	lst = [int(x) for x in str(n)]
	z = sum(lst)
	return z

input = int(input("please enter you number: "))
container = rec_dig_sum(input)
print("the result is ", container)