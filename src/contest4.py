def merge_sort(left_arr, right_arr):
    sorted = []
    counter = 0
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            sorted.append(left_arr[i])
            i += 1
        else:
            sorted.append(right_arr[j])
            counter += len(left_arr) - i
            j += 1
    sorted += left_arr[i:]
    sorted += right_arr[j:]
    return sorted, counter

def merge(nums, counter):
    if len(nums) <= 1:
        return nums, counter
    middle_index = len(nums) // 2
    left_arr, l_counter = merge(nums[:middle_index], counter)
    right_arr, r_counter = merge(nums[middle_index:], counter)
    sorted, counter = merge_sort(left_arr, right_arr)
    return sorted, counter + l_counter + r_counter
    
def main():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['1','1']))  # input
    >>> main()
    0 
    >>> sys.stdin = io.StringIO(chr(10).join(['2','3 1']))  # input
    >>> main()
    1 
    >>> sys.stdin = io.StringIO(chr(10).join(['5','5 4 3 2 1']))  # input
    >>> main()
    10
    """
    lenght = int(input())
    nums = list(map(int,input().split(" ")))
    nums, counter = merge(nums, counter)
    print(counter)
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)