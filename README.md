#<center>《Python编程：从入门到实践》复习笔记</center>
[toc]
---

## 01 第1章 起步
搭建环境，推荐编辑器geany.

---

## 02 第2章 变量和简单数据类型
title() --- 首字母大写
upper() --- 所有字母大写
lower() --- 所有字母小写
rstrip() --- 删除字符串末尾空白
lstrip() --- 删除字符串开头空白
strip() --- 删除字符串两端空白
str() --- 将非字符串值表示为字符串

---

## 03 第3章 列表简介
### 3.1 列表定义
**列表**由一系列按照特定顺序排列的元素组成。索引从0而不是1开始。

### 3.2 修改、添加和删除列表
假设list是列表，i是其索引坐标，value是对应的值
list[i] = value --- 直接修改列表的值
list.append(value) --- 将value添加到列表list末尾
list.instert(i, value) --- 将value插入索引坐标i对于的位置
del list[i] --- 删除list[i]对应的值
list_pop = list.pop(i) --- 删除list[i]对应的值，并赋值给list_pop,list.pop()默认删除列表最后一个值
list.remove(value) --- 删除与value相同值的列表值，只删除第一个指定值，如果需要全部删除，使用循环来处理。

### 3.2 组织列表
list.sort() --- 对列表进行永久性排序，list.sort(reverse=True)反向排序
**sorted(list)** --- 对列表临时性排序
list.reverse() --- 倒着排序，对列表修改具有永久性
len(list) --- 确定列表长度

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

### 4.6
* 每级缩进四个空格
* 每行不能超过80字符

