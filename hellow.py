print("hello world")
print("update from remote")

str_a =r"abc\n!sfjicso"
print(str_a)

str_multiline = """
这是一段字符串
并且能换行
哈哈哈哈
"""
print(str_multiline)

print("Emma and %s "%"maomao pig")

#format 面量插值
demo = "Tom is a {}"
demo_res = demo.format("cat")
print(demo_res)
print(demo)

demo = "Tom is a {}, Jerry is a {}"
demo_res = demo.format("cat","mouse")
print(demo_res)
print(demo)

demo = "Tom is a {类别}, Jerry is a {类别2}"
demo_res = demo.format(类别="cat",类别2="mouse")
print(demo_res)

name = 'Emma'
school = "UB"
print(f"我的名字是{name},毕业于{school}")

vocab = ['i','m','e','m','m','a']
print("".join(vocab))