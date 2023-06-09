def buble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
a = [5,3,2,6,7,8,9,1,4]
print(buble_sort(a))
