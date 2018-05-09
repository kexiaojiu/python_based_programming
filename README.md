[toc]
---

## 01 第1章 起步
搭建环境，推荐编辑器geany.

---

## 02 第2章 变量和简单数据类型
* title() --- 首字母大写
* upper() --- 所有字母大写
* lower() --- 所有字母小写
* rstrip() --- 删除字符串末尾空白
* lstrip() --- 删除字符串开头空白
* strip() --- 删除字符串两端空白
* str() --- 将非字符串值表示为字符串

---

## 03 第3章 列表简介
### 3.1 列表定义
**列表**由一系列按照特定顺序排列的元素组成。索引从0而不是1开始。

### 3.2 修改、添加和删除列表
假设list是列表，i是其索引坐标，value是对应的值
* list[i] = value --- 直接修改列表的值
* list.append(value) --- 将value添加到列表list末尾
* list.instert(i, value) --- 将value插入索引坐标i对于的位置
* del list[i] --- 删除list[i]对应的值
* list_pop = list.pop(i) --- 删除list[i]对应的值，并赋值给list_pop,list.pop()默认删除列表最后一个值
* list.remove(value) --- 删除与value相同值的列表值，只删除第一个指定值，如果需要全部删除，使用循环来处理。

### 3.2 组织列表
list.sort() --- 对列表进行永久性排序，list.sort(reverse=True)反向排序
* **sorted(list)** --- 对列表临时性排序
* list.reverse() --- 倒着排序，对列表修改具有永久性
* len(list) --- 确定列表长度

---

## 04 第4章 操作列表
### 4.1 遍历整个列表
* 使用单数和复数命令，便于判断处理对象是单个列表元素还是整个列表

### 4.2 避免缩进错误
缩进错误会打印
>IndentationError:unxpected indent

### 4.3 创建数值列表
* range(m, n) --- 生成从m到n-1的数字
* list(range(m,n)) --- 创建数字列表
* 列表介绍将for循环的创建新元素的代码合并成一行，并自动附加新元素

### 4.4 使用列表的一部分
* 使用list_copy = list[:]复制整个列表
* list_copy = list表示使用了列表赋值，两者指向同一个列表

### 4.5 元组
不可变的列表成为元组，使用圆括号标识，与列表一样使用索引访问元素。

### 4.6 设置代码格式
* 每级缩进四个空格
* 每行不能超过80字符

---

## 05 第5章 if语句
### 5.1 一个示例
...

### 5.2 条件测试
* == 检查是否相等
* =! 检查是否不想等
* and 检查多个条件
* or 检查多个条件
* in 检查特定的值是否已经包含在列表中
* not in 检查特定的值是否不包含在列表中

### 5.3 if语句
* if
* if - else
* if - elif - else

### 5.4 使用if语句处理列表
在if语句中将列表名用在条件表达式中，Python将在列表至少包含一个元素时返回True，否则返回False.

---

## 06 第6章 字典
### 6.1 一个简单字典
字典是一系列键值对

### 6.2 使用字典
字典是动态结构，可以随时在其中添加键-值对。添加键-值对，可依次指定字典名、用方括号括起的键和相关联的值。
del语句删除键-值对，必须指定字典名和要删除的键。

## 6.3 遍历字典
### 6.3.1 遍历所有的键-值对
字典方法items()
```
for key, value in dircionary.items():
```
### 6.3.2 遍历字典中所有键
字典方法keys()
```
for key in dictionary.keys():
```
### 6.3.3 按顺序遍历字典中的所有键
要以特定的顺序返回元素，一种方法在for循环中对返回的键进行排序，如：
```
for key in sorted(dictionary.keys()):
```
### 6.3.4 遍历字典中的所有值
字典方法values()
```
for value in dictionary.values():
```
为了剔除重复，可以使用集合(set)，集合类似一个列表，但是每个元素都是独一无二的。
```
for value in set(dictionary.values()):
```

## 6.4 嵌套
### 6.4.1 字典列表
在列表中嵌套字典
```
list = [dictionary1, dictionary2,dictionary3, dictionary n]
```
### 6.4.2 在字典中存储列表
每当字典中需要将一个键关联到多个值时，都可以在字典中嵌套一个列表。
### 6.4.3 在字典中存储字典
```
dictionary = {
    key1: dictionary1,
    key2: dictionary2,
    key3: dictionary3,
    }
```

---

# 7  用户输入和while循环
## 7.1 函数input()
函数input()让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中，以方便你使用。
## 7.2 while循环介绍
* while()循环不断地运行，直到指定条件不满足为止
* 在要求很多条件都满足才继续运行的程序中，可以定义一个变量，用于判断整个程序是否处于活动状态，这个变量被称为标志，充当了程序的交通信号灯
## 7.3 使用while循环来处理列表和字典
for循环可以变量列表，但是不应修改列表，否则姜导致python难以跟踪其中元素。要在遍历列表的同事对其进行修改，可以使用while循环。
主要用于
* 在列表之间移动元素
```
#!/usr/bin/env python3

# Firstly, build a list for unconfirmed users and a list for confirmed users
unconfirmed_users = ['alice0', 'brian', 'candace']
confirmed_usres = []

# Secondly, confirm every user in the list until there is no unconfirmed user
# then move confirmed users to the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("verifying user: " + current_user.title())
    confirmed_usres.append(current_user)

# At last, print all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_usres:
    print(confirmed_user.title())
    

```
* 删除包含特定值的所有列表元素
```
#!/usr/bin/env python3

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    
print(pets) 
```
* 使用用户输入来填充字典

```
#!/usr/bin/env python3

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Whick mountain would you like to climb someday? ")
    
    responses[name] = response
    
    repeat = input("Would you like to let another person respond?(yes or no)")
    if repeat == 'no':
        polling_active = False
        
        
print("\n --- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response + ".")
```

---

# 8 函数
## 8.1 定义函数
函数后面所有的缩进构成了函数体。两个'''被用作文档字符串。

## 8.2 传递实参
### 8.2.1 位置实参
调用函数时候，Python将函数调用中每个实参都关联到函数定义中的一个形参。因而，最简单的关联方式是基于实参的顺序。
### 8.2.2 关键字实参
关键字实参是传递给函数的名称-值对，调用顺序无关紧要。
```
#!/usr/bin/env python3

def describe_pet(animal_type, pet_name):
    '''show the information of animal'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name)

#~ describe_pet('hamster', 'harry')
describe_pet(animal_type = 'hamster', pet_name ='harry')
```
### 8.2.3 默认值
编写函数时，可以给每个形参指定默认值。
在使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的形参。
### 8.2.4 等效的函数调用
可以混合使用位置实参、关键字实参和默认值。
## 8.3 返回值
* 在函数中，可以使用return语句将值返回到调用函数的代码行。
* 为实参提供一个空字符串，这样让实参变为可选
```
#!/usr/bin/env python3

def get_formatted_name(first_name, last_name, middle_name=''):
    '''return formatted name'''
    if middle_name:
        full_name = first_name + ' ' + middle_name + '' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
    
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```
## 8.4  传递列表
 * 将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的
* 将列表副本传递给函数，可以使用切片[:]
```
function_name(list_name[:])
```
