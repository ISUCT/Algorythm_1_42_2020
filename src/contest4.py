def merge_sort(left_arr, right_arr, counter):
    sorted = []
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
    return sorted

def merge(nums, counter):
    if len(nums) <= 1:
        return nums
    middle_index = len(nums) // 2
    left_arr = merge(nums[:middle_index])
    right_arr = merge(nums[middle_index:])
    return merge_sort(left_arr, right_arr, counter)
    
def main():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['1','1']))  # input
    >>> main()
    0 
    """
    """
    >>> sys.stdin = io.StringIO(chr(10).join(['2','3 1']))  # input
    >>> main()
    1 
    """
    """
    >>> sys.stdin = io.StringIO(chr(10).join(['52','5 4 3 2 1']))  # input
    >>> main()
    103
    """
    lenght = int(input())
    counter = 0
    # Spasibo, 4to ya potratil mnogo nervov
    # a vse iz-za togo, 4to split(" ")
    nums = list(map(int,input().split()))
    res = merge(nums, counter)
    print(counter)
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)