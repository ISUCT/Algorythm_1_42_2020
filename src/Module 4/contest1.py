"""
>>> import io, sys 
>>> sys.stdin = io.StringIO('))(((')  # input
>>> brackets()
5
>>> sys.stdin = io.StringIO('())(()')  # input
>>> brackets()
2 
"""
def brackets():
    patenthis = input()
    counter = 0
    list_patenthis = []
    for item in patenthis:
        if item == '(':
            list_patenthis.append(item)
        if item == ')':
            if len(list_patenthis) > 0:
                list_patenthis.pop(-1)
            else:
                counter += 1
    counter += len(list_patenthis)
    print(counter)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


