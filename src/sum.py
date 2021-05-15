def summary(int_str):
    array = [int(item) for item in int_str.split()]
    sum = 0
    for item in array:
        sum += item
    return(sum)
int_str = input()
print(summary(int_str))
