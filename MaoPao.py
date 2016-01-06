def bubble(list):
    for i in range(len(list)):
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list
l1 = [20, 40, 60, 80, 30, 70, 90, 10, 50, 0]
bubble(l1)
print(l1)
