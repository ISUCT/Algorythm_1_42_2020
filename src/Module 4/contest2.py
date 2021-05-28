def check_sort(train):
    dead_lock = []
    train_b = []
    sorted_train = sorted(train)

    while len(train) != 0:
        if dead_lock == []:
            dead_lock.append(train[0])
            train.pop(0)
        else:
            if train[0] < dead_lock[-1]:
                dead_lock.append(train[0])
                train.pop(0)
            else:
                train_b.append(dead_lock[-1])
                dead_lock.pop(-1)
    if dead_lock != []:
        dead_lock.reverse()
        train_b += dead_lock

    return train_b == sorted_train

def main():
    """
    >>> import io, sys 
    >>> sys.stdin = io.StringIO(chr(10).join(['3','3 2 1']))  # input
    >>> main()
    YES
    >>> sys.stdin = io.StringIO(chr(10).join(['4','4 1 3 2']))  # input
    >>> main()
    YES
    >>> sys.stdin = io.StringIO(chr(10).join(['3','2 3 1']))  # input
    >>> main()
    NO
    """
    lenght = int(input())
    train = list(map(int, input().split()))
    train_b = check_sort(train)

    if train_b:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
   import doctest
   doctest.testmod(verbose=True)
