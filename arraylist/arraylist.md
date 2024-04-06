### Does array list holds data of different type?  
In Python list can hold elements of different type. 

```python
a_list = list()
a_list.append(1)
a_list.append("Sam")
a_list.append(1.0232)

print(a_list)
print(type(a_list[0]))
print((type(a_list[1])))
print(type(a_list[2]))
```

### What is finally block in Python?


In Python, the finally block is used in exception handling along with try and except blocks. The code inside the finally block is always executed whether an exception occurs or not. It is typically used to perform cleanup actions such as closing files or releasing resources, ensuring that these actions are taken regardless of whether an exception is raised.