#method1
name = "Sudhanshu"
age = 24
print("My namw is {0} and I am {1} years old".format(name,age))
#method2
name = "Ramy"
age = 23
print("My name is {} and I am {} years old".format(name,age))
#method3
name = "aditya"
age = 25
txt = "My name is {name} and I am {age} years old"
print(txt.format(name=name, age=age))
#method4
name = "Enrique"
names = "Ramy"
age = 26
txt = "My name is {1} and I am {2} years old".format(name,names,age)
print(txt)