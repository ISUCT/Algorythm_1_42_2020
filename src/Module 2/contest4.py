def merge_sort(left_arr, right_arr):
    sorted = []
    i = j = 0
    counter = 0
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

def merge(nums, start_index, end_index):
    if len(nums) <= 1:
        return nums, 0
    middle_index = (start_index + end_index) // 2
    left_arr, l_counter = merge(nums[:middle_index], start_index, start_index + middle_index-1)
    right_arr, r_counter = merge(nums[middle_index:], start_index + middle_index, end_index)
    result, counter = merge_sort(left_arr, right_arr)
    return result, counter + r_counter + l_counter

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
    nums = list(map(int,input().split()))
    sorted_list, total_counter = merge(nums, 0, len(nums)-1)
    print(total_counter)
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)