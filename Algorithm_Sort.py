


def bubble_sort(datas):
    count = 0
    is_ok = True

    for i in range(1, len(datas)):

        for j in range(0, len(datas) - i):
            count +=1
            if datas[j] > datas[j + 1]:
                datas[j], datas[j + 1] = datas[j + 1], datas[j]
                is_ok = False

        if is_ok == True:
            break

    print('count =',count)
    return list_data

def select_sort(datas):
    for i in range(len(datas) - 1):

        for j in range(i + 1, len(datas)):
            if datas[i] > datas[j]:
                datas[i], datas[j] = datas[j], datas[i]

    return list_data

def insert_sort(datas):
    for i in range(1, len(datas)):
        for j in range(i, 0, -1):
            if datas[j] < datas[j - 1]:
                datas[j], datas[j - 1] = datas[j - 1], datas[j]

    return datas

list_data = [5, 4, 3, 2, 1]
print('bubble_sort = ',bubble_sort(list_data))

list_data = [5, 4, 3, 2, 1]
print('select_sort = ',select_sort(list_data))

list_data = [5, 4, 3, 2, 1]
print('insert_sort = ', insert_sort(list_data))


