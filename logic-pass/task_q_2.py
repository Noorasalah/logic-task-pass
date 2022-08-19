def find_prime_numbers(begin, stop):
    nums = []
    factors = 0
    while begin <= stop:
        temp = 1
        while temp <= begin:
            if begin == 0:
                break
            if begin % temp == 0:
                factors += 1
            temp += 1
        if factors == 2:
            nums.append(begin)
        begin += 1
        factors = 0
    return nums


start = input("Enter start : ")
end = input("Enter end: ")
numbers = find_prime_numbers(int(start), int(end))
print(numbers)

