names = ['zhangsan', 'lisi','wangwu', 'zhengba']

print("I want to have diner with " + names[0].title() + ", " \
   + names[1].title() + ", " + names[2].title()+ ", " \
   + names[3].title()+ ".")

message2 = "However, " + names[0].title() + " cann't come."
print(message2)

names[0] = 'keke'
message3 = "Now, " + names[0].title() + " will replace him."
print(message3)

print(names[0].title() + ", I want to have diner with you.")
print(names[1].title() + ", I want to have diner with you.")
print(names[2].title() + ", I want to have diner with you.")
print(names[3].title() + ", I want to have diner with you.")

message4 = "I have a biger table, and more friends will join us."
print(message4)
names.insert(0,'hongwei')
message5 = "The names, whose will have diner with me, are as follows, \n"
print(message5 + str(names))

names.insert(len(names)/2 + 1, 'jaock')
print(message5 + str(names))

names.append('hahh')
print(message5 + str(names))
