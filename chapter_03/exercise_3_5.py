names = ['zhangsan', 'lisi','wangwu', 'zhengba']

#~ message1 = "I want to have diner with " + names[0].title() + ", " /
   #~ + names[1].title() + ", " + names[2].title()+ ", " /
   #~ + names[3].title()+ "."

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


