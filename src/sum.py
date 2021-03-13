def split_to_int(numbers):
    array = [int(item) for item in numbers.split(" ")]
    return array
def summ(array):
    sum = 0
    for i in range (len(array)):
        sum += array[i]
    print(sum)
numbers = input()
array = split_to_int(numbers)
summ(array)