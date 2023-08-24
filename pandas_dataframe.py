import pandas as pd
#simple df from a list
lst = [1,2,3,6,4,5]
df = pd.DataFrame(lst)
print(df)
#df from list of list
list2 = [2,2,5,8,3,],[22,55,787,66,66]
df2 = pd.DataFrame(list2)
print(df2)
#df using list of list
list3 = [['aj',70] ,['bj',55],['cj',98]]
df3 = pd.DataFrame(list3,columns=['Name','Marks'])
print(df3)
#using dict
data = {'name': ['raj','aman','rahul'],
        'marks' : [89,55,72]
        }
df4 =pd.DataFrame(data,index=['student1','student2','student3'])
print(df4)
#df using list of dictionaries
lst=[{'a':1, 'b':33, 'c': 22},
     {'a':22,'b':55,'c':45}]
df5 = pd.DataFrame(lst)
print(df5)
#creating df using zip function
names = ['raj','rahul','ajay']
marks = [55,65,98]
list_of_students = list(zip(names,marks))
df6 = pd.DataFrame(list_of_students,columns = ['name','marks'])
print(df6)
#df using list of dict
data1 = {'subjects': pd.Series(['Hindi','English','Mathematics','Science']),
    'ajay' : pd.Series([22,44,55,66]),
    'amrit' : pd.Series([33,22,54,96])}
df7 = pd.DataFrame(data1)
print(df7)