# 符号

"""
# 关键词
关键词          描述                                             示例
and            逻辑上的“和”                                      True and False == False
as             with-as 语句的一部分                               with X as Y: pass
assert         断言某个表达式为 true（如果为 false，则会触发异常）     assert False. "Error!"
break          立即停止循环                                       while True: break
continue       不运行循环的剩余部分，重新开始循环                     while True: continue
def            定义一个函数                                       def X(): pass
del            从字典中删除                                       del X[Y]
elif else if   条件                                             if: X; elif: Y; else: J
else else      条件                                             if: X; elif: Y; else: J
except         如果例外发生，就执行该语句                            except ValueError, e: print(e)
exec           把字符串作为 python 运行 exec                      'print("Hello")'
finally        不管是否发生例外，都执行该语句                         finally: pass
for            遍历循环集合中的元素                                 for X in Y: pass
from           从模块中导入特定部分。                               from X import Y
global         声明一个全局变量                                    global X
if if          条件                                             if: X; elif: Y; else: J
import         导入一个模块来使用                                  import os
in             for循环的一部分。也用于测试 X 是否 在 Y 中.            for X in Y: pass 或 1 in [1] ==True
is             相当于 == ，测试相等性                              1 is 1 == True
lambda         创建一个短的匿名函数                                 s = lambda y: y ** y; s(3) 注1
not            逻辑上的“非”                                       not True == False
or             逻辑上的“或”                                       True or False == True
pass           该代码块为空                                       def empty(): pass
print          打印这个字符串                                      print("this string")
raise          当程序出错，抛出一个指定异常信息                       raise ValueError("No")
return         返回一个值同时退出函数                               def X(): return Y
try            尝试执行这个代码块，如果遇到例外，执行 except语句        try: pass
while          while 循环                                        while X: pass
with           把表达式作为一个变量来用                              with X as Y: pass 注2
yield          在这里暂停，然后返回函数                              def X(): yield Y; X().next()

# 数据类型
类型            描述                                              示例
True True      布尔值                                             True or False == True
False False    布尔值                                             False and True == False
None           代表“无”或者“没有”值                                 x = None
bytes          存储字节，可以是文本、PNG、文件等                       x = b"hello"
strings        存储文本信息                                        x = "hello"
numbers        存储整数                                           i = 100
floats         存储小数                                           i = 10.389
lists          存储一列元素                                        j = [1,2,3,4]
dicts          存储一系列“键=值”的元素                               e = {'x': 1, 'y': 2}

# 字符串转义序列
转义字符        描述
\             反斜杠
'             单引号
"             双引号
\a            响铃
\b            退格
\f            换页符
\n            换行符
\r            回车符
\t            Tab 制表符
\v            垂直制表符

# 老式字符串格式化
转义字符        描述                                                  示例
%d            十进制整数（不含浮点数）                                  "%d" % 45 == '45'
%i             同 %d                                                "%i" % 45 == '45'
%o            八进制数                                               "%o" % 1000 == '1750'
%u            无符号十进制整数                                         "%u" % -1000 == '-1000'
%x            十六进制数小写                                          "%x" % 1000 == '3e8'
%X            十六进制数大写                                          "%X" % 1000 == '3E8'
%e             指数计数法，小写 'e'                                    "%e" % 1000 == '1.000000e+03'
%E             指数计数法，大写 'E'                                    "%E" % 1000 == '1.000000E+03'
%f             浮点数                                                 "%f" %10.34 == '10.340000'
%F             同 %f                                                 "%F" % 10.34 == '10.340000'
%g             %f 或 %e 更短者                                        "%g" % 10.34 == '10.34'
%G             同 %g 但是大写                                          "%G" % 10.34 == '10.34'
%c             符号格式化                                              "%c" % 34 == ' " ' 注1
%r             Repr 格式化（调试格式化）                                 "%r" % int == '<type 'int'>' 注2
%s             字符串格式化                                            "%s there" % 'hi' == 'hi there'
%%             百分号                                                 "%g%%" % 10.34 == '10.34%'

# 运算符
运算符         描述                                                    示例
+             加                                                     2 + 4 == 6
-             减                                                     2 - 4 == -2
*             乘                                                     2 * 4 == 8
**            乘方                                                    2 ** 4 == 16
/             除                                                     2 / 4 == 0.5
//            地板除法（商向下取整）                                     2 // 4 = 0
%             字符串插入符；取模                                        2 % 4 == 2
<             小于                                                   4 < 4 == False
>             大于                                                   4 > 4 == False
<=            小于等于                                                4 <= 4 == True
>=            大于等于                                                4 >= 4 == True
==            等于                                                   4 == 5 == False
!=            不等于                                                  4 != 5 == True
( )           括号                                                   len('hi') == 2
[ ]           列表中括号                                               [1,3,4]
{ }           字典大括号                                               {'x': 5, 'y': 10}
@             At (修饰符)                                             @classmethod
,             逗号                                                    range(0, 10)
:             冒号                                                    def X():
.             点                                                      self.x = 10
=             赋值等号                                                 x = 10
;             分号                                                    print("hi"); print("there")
+=            加赋值                                                  x = 1; x += 2
-=            减赋值                                                  x = 1; x -= 2
*=            乘赋值                                                  x = 1; x *= 2
/=            除赋值                                                  x = 1; x /= 2
//=           地板除赋值                                               x = 1; x //= 2
%=            取模赋值                                                x = 1; x %= 2
**=           乘方赋值                                                x = 1; x **= 2
"""
