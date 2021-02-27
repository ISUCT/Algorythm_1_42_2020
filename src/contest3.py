def merge_sort(left_arr, right_arr, start_index, end_index):
    sorted = []
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            sorted.append(left_arr[i])
            i += 1
        else:
            sorted.append(right_arr[j])
            j += 1
    sorted += left_arr[i:]
    sorted += right_arr[j:]
    print(f'{start_index + 1} {end_index + 1} {sorted[0]} {sorted[-1]}')
    return sorted

def merge(nums, start_index, end_index):
    if len(nums) <= 1:
        return nums
    middle_index = len(nums) // 2
    left_arr = merge(nums[:middle_index], start_index, start_index + middle_index - 1)
    right_arr = merge(nums[middle_index:],start_index + middle_index, end_index)
    return merge_sort(left_arr, right_arr, start_index, end_index)
    
def main():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['7','707064224 75267074 374155361 539523323 99604066 342179425 342194485']))  # input
    >>> main()
    2 3 75267074 374155361
    1 3 75267074 707064224
    4 5 99604066 539523323
    6 7 342179425 342194485
    4 7 99604066 539523323
    1 7 75267074 707064224
    75267074 99604066 342179425 342194485 374155361 539523323 707064224 
    """
    """
    >>> sys.stdin = io.StringIO(chr(10).join(['5','5 4 3 2 1']))  # input
    >>> main()
    1 2 4 5
    4 5 1 2
    3 5 1 3
    1 5 1 5
    1 2 3 4 5 
    """
    """
    >>> sys.stdin = io.StringIO(chr(10).join(['2','3 1']))  # input
    >>> main()
    1 2 1 3
    1 3
    """
    lenght = int(input())
    nums = list(map(int,input().split(" ")))
    res = merge(nums, 0, lenght - 1)
    print(" ".join(map(str,res)))
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


