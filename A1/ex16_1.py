# 读取文件

# 导入 sys 的 argv 模块
from sys import argv

# 获取文件名
script, filename = argv

# 打开获取的文件名的文件
txt = open(filename)

# 读取文件内容
content = txt.read()
# 打印文件内容
print(content)