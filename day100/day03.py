item1 = [1, "hello", 2.3]
print(item1)
print(type(item1))

# List函数
item2 = list(range(1, 10))
item3 = list("hello")
print(item2)
print(item3)

# 列表的运算
print(item3 + item2)
print(item3 * 3)
print("O" in item3)

# 列表索引
print(item3[0])
print(item3[1])
print(item3[-1])

# 列表切片
print(item3[1:3:1])
print(item3[::])
item3[0:1] = "1"
print(item3)

# 遍历元素
for item in item3:
    print(item)

for index in range(len(item3)):
    print(item3[index])

# 列表删除元素
item5 = list("helol")
item5.remove("l")
print(item5)