[toc]
---

# 01 第1章 起步
搭建环境，推荐编辑器geany.

---

# 02 第2章 变量和简单数据类型
* title() --- 首字母大写
* upper() --- 所有字母大写
* lower() --- 所有字母小写
* rstrip() --- 删除字符串末尾空白
* lstrip() --- 删除字符串开头空白
* strip() --- 删除字符串两端空白
* str() --- 将非字符串值表示为字符串

---

# 03 第3章 列表简介
## 3.1 列表定义
**列表**由一系列按照特定顺序排列的元素组成。索引从0而不是1开始。

## 3.2 修改、添加和删除列表
假设list是列表，i是其索引坐标，value是对应的值
* list[i] = value --- 直接修改列表的值
* list.append(value) --- 将value添加到列表list末尾
* list.instert(i, value) --- 将value插入索引坐标i对于的位置
* del list[i] --- 删除list[i]对应的值
* list_pop = list.pop(i) --- 删除list[i]对应的值，并赋值给list_pop,list.pop()默认删除列表最后一个值
* list.remove(value) --- 删除与value相同值的列表值，只删除第一个指定值，如果需要全部删除，使用循环来处理。

## 3.2 组织列表
list.sort() --- 对列表进行永久性排序，list.sort(reverse=True)反向排序
* **sorted(list)** --- 对列表临时性排序
* list.reverse() --- 倒着排序，对列表修改具有永久性
* len(list) --- 确定列表长度

---

# 04 第4章 操作列表
## 4.1 遍历整个列表
* 使用单数和复数命令，便于判断处理对象是单个列表元素还是整个列表

## 4.2 避免缩进错误
缩进错误会打印
>IndentationError:unxpected indent

## 4.3 创建数值列表
* range(m, n) --- 生成从m到n-1的数字
* list(range(m,n)) --- 创建数字列表
* 列表介绍将for循环的创建新元素的代码合并成一行，并自动附加新元素

## 4.4 使用列表的一部分
* 使用list_copy = list[:]复制整个列表
* list_copy = list表示使用了列表赋值，两者指向同一个列表

## 4.5 元组
不可变的列表成为元组，使用圆括号标识，与列表一样使用索引访问元素。

## 4.6 设置代码格式
* 每级缩进四个空格
* 每行不能超过80字符

---

# 05 第5章 if语句
## 5.1 一个示例
...

## 5.2 条件测试
* == 检查是否相等
* =! 检查是否不想等
* and 检查多个条件
* or 检查多个条件
* in 检查特定的值是否已经包含在列表中
* not in 检查特定的值是否不包含在列表中

## 5.3 if语句
* if
* if - else
* if - elif - else

## 5.4 使用if语句处理列表
在if语句中将列表名用在条件表达式中，Python将在列表至少包含一个元素时返回True，否则返回False.

---

# 06 第6章 字典
## 6.1 一个简单字典
字典是一系列键值对

## 6.2 使用字典
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

# 07  第七章 用户输入和while循环
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

# 08 第八章 函数
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

## 8.5 传递任意数量的实参
```
#!/usr/bin/env python3

def make_pizza(*toppings):
    """print all toppings which customers had ordered"""
    print(toppings)
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```
### 8.5.1 结合使用位置实参和任意数量实参 
如果让函数接受不同类型的实参，必须在函数定义中将任意数量实参的形参放在最后。Python最先匹配实参和关键字实参，再将余下的实参都收集到最后一个形参中。
### 8.5.2 使用任意数量的关键字实参
有时候，需要接受任意数量的实参，但不知道传递给函数的信息，这时可以将函数编写成能够接受任意数量的键值对---调用语句提供了多少就接受多少。
```
#!/usr/bin/env python3

def build_profile(first, last, **user_info):
    """create a dictionary inclding everything about the users"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
    
user_profile = build_profile('albert', 'einstein', 
                                location = 'princeton',
                                field='physics')

print(user_profile)
```

## 8.6 将函数存储在模块中
###8.6.1 导入整个模块
使用import语句导入名为module_name.py的整个模块，就可以使用下面的语法来使用其中任何函数
```
module_name.function_name()
```
### 8.6.2 导入特定函数
```
from  module_name import function_name
```
### 8.6.3 使用as给函数指定别名
```
from  module_name import function_name as fn
```
### 8.6.4 使用as给模块指定别名
```
import module_name as mn
```
### 8.6.5导入模块中所有函数（不建议使用）
```
from module_name import *
```

--- 
# 09 第九章 类
## 9.1 创造和使用类
### 9.1.1 创建类
在Python中，首字母大写的名称指的是类。
* __init__()方法中，self形参必不可少，必须位于其他形参前面，self是一个指向实例本身的引用
* 以self为前缀的变量都可以供类中所有方法使用
### 9.1.2 根据类创建实例
* 使用句点访问实例的属性
* 使用句点使用类的方法

## 9.2 使用类和实例
### 9.2.1 Car类
可以通过三种方法修改属性的值
* 直接修改属性的值
* 通过方法修改属性的值
* 通过方法对属性的值进行递增

## 9.3继承
### 9.3.1 子类的方法__init__()
```
#!/usr/bin/env python3

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
 ---snip---

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
```
父类必须板焊在当前文件中，且位于子类的前面。super()是一个特殊的函数，让ElectricCar实例包含父类的所有属性。
### 9.3.2 给子类定义属性和方法
让一个类继承另外一个类后，可添加区分子类和父类所需的新属性和方法。
### 9.3.3 重写父类的方法
在子类中定义一个与父类同名的方法即可对父类的方法重写 
### 9.3.4 将实例用作属性
可以将类的一部分作为一个独立的类提取处理。

## 9.4 导入类
需要从一个模块导入很多类时候，最好导入整个模块，并使用module_name.class_name语法来访问类。
```
import module_name
```

## 9.5 Python标准库
使用模块collections中OrderedDict类，可以创建字典并记录其中的键值对的添加顺序。

---

# 10 第十章文件和异常
## 10.1 从文件中读取数据
### 10.1.1 读取整个文件
```
#!/usr/bin/env python3

with open('pi_digits.txt') as file_object:
 contents = file_object.read()
 print(contents)
```
* open()函数接受一个参数：要打开文件的名称，返回一个改文件的对象
* 关键字with在不再需要访问文件后将其关闭 
### 10.1.2 文件路径
```
with open('text_file/filename.txt') as file_object:
```
### 10.1.3 逐行读取
要以每次一行检测文件，可对文件对象使用for 循环
### 10.1.4 创建一个包含文件各行内容的列表
readlines()从文件读取每一行，并将其存储在一个列表中
### 10.1.5 使用文件内容
读取文本文件时候，Python将其中的所有内容都解读为字符串。如果读取的是数字，并要当数值使用，必须使用函数int()将其转换为整数或使用函数float()将其转换成浮点数。

## 10.2 写入文件
### 10.2.1 写入空文件
```
#!/usr/bin/env python3

filename = 'programming.txt'

with open(filename, 'w') as file_object:
 file_object.write("I love programming.")
```
打开文件时候，可以指定读取模式（'r'）、写入模式('w')、附加模式('a')和读写模式('r+')，默认只读模式打开文件。
Python只能把字符串写入文本文件中，要将数值数据存储在文本文件中，必须使用函数str()将其转换成字符串模式。
### 10.2.2 写入多行
write()不会在文本末尾添加换行符
### 10.2.3 附加到文件
```
with open(file_name, 'a') as file_object:
    ......
```

## 10.3 异常
### 10.3.1 处理ZeroDivisionError异常---使用try-except模块
```
#!/usr/bin/env python3
try:
 print(5/0)
except ZeroDivisionError:
 print("You can't divide by zero!")
```
### 10.3.2 else代码块
依赖try代码块成功执行的代码都应该放到else代码块中。
### 10.3.3 分析文本
http://www.gutenberg.org/提供了一系列不受版权限制的文学作品，可以用于文本分析。下面是计算一个文本中单词数量的程序。
```
#!/usr/bin/env python3

def count_words(filename):
 """count words in files"""
 try:
  with open(filename) as fo:
   contents = fo.read()
 except FileNotFoundError:
  error_message = "Sorry, the file" + filename + " does not exits."
  print(error_message)
 else:
  # count how many words in the file
  words = contents.split()
  num_words = len(words)
  print("The file " + filename + " has about " + str(num_words) + 
   " words")
   
filename = 'alice.txt'
count_words(filename)
```
split()方法将以空格为分隔符将字符串分拆为多个部分。
### 10.3.4 失败时一声不吭
在except中使用pass，也起到占位的作用，提醒在程序某个地方什么都没做，并且以后也许可以做些什么。
```
#!/usr/bin/env python3

def count_words(filename):
 """count words in files"""
 try:
  with open(filename) as fo:
   contents = fo.read()
 except FileNotFoundError:
  #~ error_message = "Sorry, the file" + filename + " does not exits."
  pass
  #~ print(error_message)
  #~ with open('missing_files.txt', 'a') as missing_obj:
   #missing_obj.write(filename + "\n")
 else:
  # count how many words in the file
  words = contents.split()
  num_words = len(words)
  print("The file " + filename + " has about " + str(num_words) + 
   " words")
   
#~ filename = 'alice.txt'
#~ count_words(filename)

filenames = ['alice.txt', 'sddhartrha.txt', 'guest_book.txt', 'missing_files.txt']
for filename in filenames:
 count_words(filename)
```
### 10.3.5 计算单词出现频率的程序
```
#!/usr/bin/env python3

def count_word_in_filename(filename, word):
 """count how many 'word' in filename"""
 try:
  with open(filename) as fo:
   contents = fo.read()
 except FileNotFoundError:
  error_message = "Sorry, the file" + filename + " does not exits.\n"
  print(error_message)
  pass
  #~ with open('missing_files.txt', 'a') as missing_obj:
   #missing_obj.write(filename + "\n")
 else:
  num_word_in_filename = contents.lower().count(word)
  print("The file " + filename + " has about " + 
   str(num_word_in_filename) + " words '"+ word + "'.\n")
   
   
filenames = ['alicea.txt', 'the_sign_of_four.txt', 'a_study_in_scarlet.txt', 'the.txt']
word = 'the'
for filename in filenames:
 count_word_in_filename(filename, word)
```

## 10.4 存储用户
### 10.4.1 json.dump()和json.load()
* json.dump()接受两个实参：要存储的数据以及可用于存储数据的文件对象
* json.load()接受一个实参：要读取数据的文件对象
```
#!/usr/bin/env python3 

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'number.json'

with open(filename, 'w') as f_obj:
 json.dump(numbers, f_obj)
```

```
#!/usr/bin/env python3

import json

filename = 'number.json'

with open(filename) as f_obj:
 numbers = json.load(f_obj)
	
print(numbers) 
```
### 10.4.2 保存和读取用户生成的数据
```
#!/usr/bin/env python3
import json

# if there is username in the file, load it
# else store it
filename = 'username.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name?")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
```
### 10.4.3 重构
将代码划分为一系列完成具体工作的函数

---

# 11 第十一章 测试代码
## 11.1 测试函数
### 11.1.1 单元测试和测试用例
* 单元猜测是用于核实函数的某个方面没有问题
* 测试用类是一组单元测试，这些单元测试一起核实函数在各种情况下的行为都符合要求
### 11.1.2 可通过的测试
要为函数编写测试用例，可先导入模块unittest以及要测试的函数，再创建一个继承unittest.TestCase类，并编写一系列方法对函数行为的不同方面进行测试。
assertEqual(a,b)是断言方法，断言a==b，否则将出现测试不提供

## 11.2 测试类
### 11.2.1 各类断言方法
unittest Module中断言方法
方法 | 用途
--- |---
assertEqual(a,b) | 核实a==b
assertNotEqual(a,b) | 核实a!=b
assertTrue(x) | 核实x为True
asserFalse(x) | 核实x为False
assertIn(item, list) | 核实item在list中
assertNotIn(item,list) | 核实item不在list中
### 11.2.2 一个要测试的类
```
#!/usr/bin/env python3

class AnonymousSurvey:
    """collect annonymous survey"""
    
    
    def __init__(self, question):
        self.question = question
        self.responses = []
                
    def show_question(self):
        print(self.question)
        
    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results: ")
        for response in self.responses:
            print('- ' + response)
```
### 11.2.3 测试类
```
#!/usr/bin/env python3

import unittest
from survey import AnonymousSurvey

class TestAnonymousCase(unittest.TestCase):
    def test_store_single_responese(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        
        self.assertIn('English', my_survey.responses)
        
    def test_store_three_responese(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)
            

unittest.main()
```
### 11.2.4 方法setUp()
TestCase类包含方法setUp()，让我们只需要创建这些对象一次，并在每个测试方法中使用他们 。一般，Python先运行setUp()，再运行各个以test_打头的方法。
### 11.2.5 单元测试结果说明
* 测试通过打印一个句点
* 测试引发错误打印一个E
* 测试导致断言失败打印一个F

# 12 第十二章 武装飞船
## 12.1 项目规划
项目启动之前，需要明确项目规划

## 12.2 安装pip和Pygame
```
$ sudo apt install python3-pip
$ pip3 install pygame
```

## 12.3 开始游戏项目
首先，创建一个空的Pygame窗口。使用Pygame编写游戏的基本结构如下：
```
#!/usr/bin/env python3

import sys
import pygame

def run_game():
    # Initialize the game and create a game object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    
    # Begin the main loop
    while True:
        
        # Monitoring mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # Make the recently painted screen visible
        pygame.display.flip()


run_game()
```

## 12.4 添加飞船图像
* 使用Pygame的blit()方法可以绘制加载的图像
* 使用get_rect获取相应surface属性rect
* center\centerx或centery 游戏元素居中
* top\bottom\left\right 游戏元素与边缘对齐
* x,y 分别调整游戏元素的水平和垂直位置
```
#!/usr/bin/env python3

import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    # Initialize the game and create a game object
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, 
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Set blackcolor
    #~ bg_color = (230, 230, 230)
    bg_color = ai_settings.bg_color
     
    # build a ship
    ship = Ship(screen)
        
    # Begin the main loop
    while True:
        
        # Monitoring mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(ai_settings.bg_color)
        ship.blitme()
                
        # Make the recently painted screen visible
        pygame.display.flip()


run_game()

```

## 12.5 重构
重构目的在于简化既有代码的结构，使其更容易扩展。

## 12.6 驾驶飞船
* 响应按键
* 允许不断移动
* 左右移动
* 调整飞船速度
* 限制飞船范围
* 重构

## 12.7 回顾
回顾现有的文件
rect的属性和方法http://bbs.fishc.org/thread-62186-1-1.html

## 12.8 射击
* 模块pygame.sprite中Sprite类，可将游戏中相关元素编组，进而同时操作编组中所有元素

---

# 13 第十三章 外星人
## 13.1 回顾项目
在给项目添加功能之前，需要回顾一下开发计划；此外，还应该审核既有代码。

## 13.2 创建一个外星人
创建飞船一样，先创建一个外星人，放在左上角

## 13.3 创建一群外星人
用sprite类创建一群外星人，首先确定屏幕可以容纳的外星人数目
 aliens.draw(screen)对编组调用draw()时候，Pygame自动绘制编组的每个元素，绘制位置由元素的属性rect决定。
创建第一行外星人
```
def create_fleet(ai_settings, screen, aliens):
    """create a group of aliens"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    
    # create aliens in the first line
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)  

```

## 13.4 让外星人移动
移动规则：向屏幕右边移动，撞到屏幕边缘后下移一定距离，再沿相反的方向移动。

## 13.5 射杀外星人
sprite.groupcollide()检测两个编组的成员之间的碰撞

## 13.6 结束游戏
### 13.6.1 检测外星人和飞船碰撞
```
    # detect collisions between aliens and spacecraft
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship hit!!!")
```
### 13.6.2 响应外星人和飞船碰撞
增加GameStats类
### 13.6.3 有外星人到达屏幕底部

---
# 14 第十四章 记分
## 14.1 添加play按钮
* 导入pygame.font模块，能够让Pygame将文本渲染到屏幕上。

* 调用font.render()将msg中的文本转化为图像
```
self.font.render(msg, True, self.text_color, self.button_color)
```
* 获取鼠标位置的方法
```
mosue_x, mouse_y = pygame.mouse.get_pos()
```
* 检查鼠标单击位置是否在Play按钮的rect内，在里面返回True 
```
play_button.rect.collidepoint(mouse_x, mouse_y)
```
* 隐藏光标
```
pygame.mouse.set_visible(False)
```

## 14.2 提高等级
initialize_dynamial_settings()初始化飞船速度、子弹速度、和外星人移动速度的设定值、increase_speed()按照比例speedup_scale提高飞船速度、子弹速度、和外星人移动速度的设定值。
```
#!/usr/bin/env python3

class Settings():
    """store all settings"""
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230, 230)
        """blue"""
        #~ self.bg_color = (0, 255, 255)
        
        # speed of a ship
        #~ self.ship_speed_factor = 1.5
        self.ship_limit = 3
        
        # settings for bullets
        #~ self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        #~ self.bullet_color = 60, 60 ,60
        self.bullets_allowed = 5
        
        # settings for alien
        #~ self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #~ #1 respects right, -1 respects left
        #~ self.fleet_direction = 1
        
        # speed up the game
        self.speedup_scale = 1.2
        self.initialize_dynamial_settings()
        
        
    def initialize_dynamial_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        #1 respects right, -1 respects left
        self.fleet_direction = 1
        
        
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

```
## 14.3 记分
* 新增记分类
```
#!/usr/bin/env python3

import pygame.font

class Scoreboard():
    """score class"""
    
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        self.prep_score()
        
    
    def prep_score(self):
        """make the score to be a picure"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
            self.ai_settings.bg_color)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
        
    def show_score(self):
        """show score"""
        self.screen.blit(self.score_image, self.score_rect)
```
