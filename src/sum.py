numbers = input()
def splitToInt(numbers):
    array = [int(item) for item in numbers.split(" ")]
    return array
array = splitToInt(numbers)
def summ(array):
    Sum = 0
    for i in range (len(array)):
        Sum += array[i]
    print(Sum)
summ(array)