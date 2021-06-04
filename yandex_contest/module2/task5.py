def merge(l_list, r_list):
    s_list = []
    l_idx = 0
    r_idx = 0
    for i in range(len(l_list)+len(r_list)):
        if l_idx < len(l_list) and r_idx < len(r_list):
            if l_list[l_idx] <= r_list[r_idx]:
                s_list.append(l_list[l_idx])
                l_idx += 1               
            else:
                s_list.append(r_list[r_idx])
                r_idx += 1                
    s_list += l_list[l_idx:]
    s_list += r_list[r_idx:]
    return s_list


def merge_sort(uns_list):
    if len(uns_list) == 1:
        return uns_list
    mid = len(uns_list) // 2
    l_list = merge_sort(uns_list[:mid])
    r_list = merge_sort(uns_list[mid:])
    return merge(l_list, r_list)


n = int(input())
stroka = list(map(int, input().split()))
stroka = merge_sort(stroka)
for i in range(1, len(stroka)):
    if stroka[i]==stroka[i-1]:
        n-=1
print(n)