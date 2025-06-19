

fruits=["apple","mango","banana"]
print("first fruits:", fruits[0])
print("first fruit:",fruits[-1])
print("Total number of fruits:",len(fruits))
fruits[1]="pineapple"
print("updated fruits list:",fruits)
x=["harish","naresh","suresh","mahesh"]
print("id before change:",id(x))
x[2]="kiran"
print("update list:",x)
print("id after changes:",id(x))
data=[1,2,[4,5],[6,7],8,["something"]]
print("value 4 :",data[2][0])
print("value 7:",data[3][1])
print("Letter 'm':",data[5][0][3])
mixed=[1,2,"hi",12.3,True]
for item in mixed:
    print(f"value:{item}, Type:{type(item)}")


