
""" Setting the Data Type
In Python, the data type is set when you assign a value to a variable: """
x= "hello"
int = 10
float = 10.5
bool = True
complex = 10+5j
print(type(x))
print(type(int))
print(type(float))
print(type(bool))
print(type(complex))
for i in range(0,10):
    product = i*i*i
    print(product)
table = [[1,2,3],[4,5,6],[7,8,9]]
print(*[i for row in table for i in row])
