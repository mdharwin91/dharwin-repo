import pandas as pd
from copy import copy, deepcopy

df1 = pd.DataFrame(
    {'Name':['Dharwin', 'Joshwin', 'Meshak'],
    'Village':['Maruthakulam', 'MKM', 'Turunelveli'],
    'Gender':['Male', 'Male', 'Male']
    }
)

df2 = pd.DataFrame(
    {'Name':['Dharwin1', 'Joshwin1', 'Meshak1'],
    'Village':['Maruthakulam', 'MKM', 'Turunelveli'],
    'Gender':['Male', 'Male', 'Male']
    }
)

df3 = pd.DataFrame(
    {
        'Village':['9894140877', '9952395849', '9443508833']
    }
)

dict1 = {'Name': 'Dhawrin', 'Age': 30, 'Gender':'Male'}
# print(df1.append(df2, ignore_index=True))
# print(df1.join(df3))
# print(pd.concat([df1, df3], axis=0, ignore_index=True))

# obj = pd.Series(dict1)
# print(obj)

list1 = [1, 2, 3, [4, 8], 5, 6]
# list2 = [7, 8, 9]
print("list1",list1)
list2 = copy(list1)
# list2.append(7)
list2[3].append(11)
print("list1",list1)
print("list2",list2)
list3= deepcopy(list1)
# list3.append(9)
list3[3].append(10)
print("list1",list1)
print("list3",list3)
