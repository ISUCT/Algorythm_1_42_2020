def merge(l_list, r_list, str_idx, end_idx):
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
    print(str(str_idx)+" "+str(end_idx)+" "+str(s_list[0])+" "+str(s_list[-1]))
    return s_list


def merge_sort(uns_list, str_idx, end_idx):
    if len(uns_list) == 1:
        return uns_list
    mid = len(uns_list) // 2
    l_list = merge_sort(uns_list[:mid], str_idx, str_idx + mid-1)
    r_list = merge_sort(uns_list[mid:], str_idx + mid, end_idx)
    return merge(l_list, r_list, str_idx, end_idx)


n = int(input())
stroka = list(map(int, input().split()))
stroka = merge_sort(stroka, 1, len(stroka))
print(" ".join(map(str, stroka)))