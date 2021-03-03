def main():
    """
    <<< 9
    <<< 12
    <<< 32
    <<< 45
    <<< 67
    <<< 98
    <<< 29
    <<< 61
    <<< 35
    <<< 09
    >>> main()
    Initial array:
    12, 32, 45, 67, 98, 29, 61, 35, 09
    **********
    Phase 1
    Bucket 0: empty
    Bucket 1: 61
    Bucket 2: 12, 32
    Bucket 3: empty
    Bucket 4: empty
    Bucket 5: 45, 35
    Bucket 6: empty
    Bucket 7: 67
    Bucket 8: 98
    Bucket 9: 29, 09
    **********
    Phase 2
    Bucket 0: 09
    Bucket 1: 12
    Bucket 2: 29
    Bucket 3: 32, 35
    Bucket 4: 45
    Bucket 5: empty
    Bucket 6: 61, 67
    Bucket 7: empty
    Bucket 8: empty
    Bucket 9: 98
    **********
    Sorted array:
    09, 12, 29, 32, 35, 45, 61, 67, 98
    """
    Arr = []
    length = int(input())

    for i in range(length):
        Arr.append(input())

    print("Initial array:")

    print(', '.join(Arr))


    Count = len(Arr[0])
    Phase=0
    for i in range(Count-1,-1,-1):
        Phase+=1
        print('**********')
        print("Phase",Phase)
        bucket = [[] for _ in range(10)]
        for j in range(len(Arr)):
            bucket[ord(Arr[j][i]) - ord('0')].append(Arr[j])
        for j in range(10):
            if len(bucket[j])==0:
                print(f'Bucket {j}: empty')
            else:
                print("Bucket "+str(j)+": ", end='')
                for now in range(len(bucket[j])-1):
                    print(bucket[j][now],end=', ')
                print(bucket[j][len(bucket[j])-1])
        p = 0
        for j in range(10):
            for k in range(len(bucket[j])):
                Arr[p] = bucket[j][k]
                p += 1

    print('**********')
    print("Sorted array:")

    print(', '.join(Arr))
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)