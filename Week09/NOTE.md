三个月好快，但是收获真的是颇丰

最重要的是自信和成就感，五分钟搞定一个题的感觉真是太好了~

特别感谢超哥、各位助教老师和很多热心同学，分享，鼓励，帮助，真挚感谢。

当然这只是一个开始，很多题还要继续刷，很多思路和方法还需要继续理解，这是一个好的开始。

此致，深深地感谢~



### 字符串基础知识

Ptyhon字符串拼接，效率较慢

因为在python 和 java中，字符串不可变，必须要创建新的变量，然后copy

 Each time you append to the end of a string, the Python interpreter must create a new string object and copy the contents of both the existing string and the appended string into it. As the strings you are manipulating become large this proces becomes increasingly slow.

refer：https://waymoot.org/home/python_string/

其他语言，字符串可变，如C，最早，字符串，就是个字符数组



**字符串遍历**

```
Python:
for ch in "abbc":
	print(ch)
	
Java:

```



**字符串比较**

```python
Java：

String x = new String("abb")；             // 存储的是内存地址
String y = new String("abb");

x == y   --> false

x.equals(y)    --> true
x.equalsIgnoreCase(y)     --> true
```





### 相关函数

回顾一下 Python 中常用处理字符串的相关函数

string.capitalize() 把字符串的第一个字符大写
string.count(str, beg=0, end=len(string)) 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
string.endswith(obj, beg=0, end=len(string)) 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
string.find(str, beg=0, end=len(string)) 检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
string.index(str, beg=0, end=len(string)) 跟find()方法一样，只不过如果str不在 string中会报一个异常.
string.isalnum() 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
string.isalpha() 如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
string.isdecimal() 如果 string 只包含十进制数字则返回 True 否则返回 False.
string.isdigit() 如果 string 只包含数字则返回 True 否则返回 False.
string.islower() 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
string.isnumeric() 如果 string 中只包含数字字符，则返回 True，否则返回 False
string.isspace() 如果 string 中只包含空格，则返回 True，否则返回 False.
string.istitle() 如果 string 是标题化的(见 title())则返回 True，否则返回 False
string.isupper() 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
string.join(seq) 以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
string.lower() 转换 string 中所有大写字符为小写.
string.lstrip() 截掉 string 左边的空格
max(str) 返回字符串 str 中最大的字母。
min(str) 返回字符串 str 中最小的字母。
string.replace(str1, str2, num=string.count(str1)) 把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
string.split(str="", num=string.count(str)) 以 str 为分隔符切片 string，如果 num 有指定值，则仅分隔 num+ 个子字符串
string.startswith(obj, beg=0,end=len(string)) 检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.
string.strip([obj]) 在 string 上执行 lstrip()和 rstrip()
string.swapcase() 翻转 string 中的大小写
string.title() 返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
string.translate(str, del="") 根据 str 给出的表(包含 256 个字符)转换 string 的字符,要过滤掉的字符放到 del 参数中
string.upper() 转换 string 中的小写字母为大写