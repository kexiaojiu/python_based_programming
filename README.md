#<center>《Python编程：从入门到实践》复习笔记</center>
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
