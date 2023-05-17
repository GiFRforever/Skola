"""# refactor
def add(a, list=None):
    list = list or []
    list.append(a)
    return list


list1 = add(1)
list2 = add(2)
list3 = add(3, [])
list4 = add(4)
print(list1)
print(list2)
print(list3)
print(list4)
"""
a = [[0, 0] * 10] * 10
a[0][0] = 1
print(a)
