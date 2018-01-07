names = ['zhangsan', 'lisi','wangwu', 'zhengba']

message1 = "The names, whose will have diner with me, are as follows, \n"
print(message1+ str(names))

print("I can only invite two of you.")

name_pop = names.pop()
print(name_pop + ", sorry, you cannot join us.")

name_pop = names.pop()
print(name_pop + ", sorry, you cannot join us.")

print(names[0] + ", you are still in the list.")
print(names[1] + ", you are still in the list.")

del names[0]
del names[0]

print("The names is empty? names: " + str(names))
