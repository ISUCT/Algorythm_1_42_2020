def summ(a, b):
    return a + b 


    n = int(input())
   
    arr = input()
    str_lst = arr.split(" ")
    res = []
    for item in str_lst:
        res.append (int(item))
    #print(res)
    n = len(res)
    for i in range(0, n-1):
        #print(f"i={i}")
        for j in range(0, n-1-i):
          #print (f"j={i}")
          if res[j] > res[j+1]:
             res[j] , res[j+1] = res[j+1], res[j]
             print(" ".join(map(str,res)))
     print (res)


