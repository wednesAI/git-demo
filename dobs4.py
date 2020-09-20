# -*- coding: utf-8 -*- 
# @Time : 2020/9/15 21:27 
# @Author : wednes 
# @File : dobs4.py
from bs4 import BeautifulSoup
import requests
import re
import time

url = 'https://www.baidu.com'
response = requests.get(url)
response.encoding = 'utf-8'
# html.parse 是内置的不需要安装的
# 但是如果一段HTML或XML文档格式不正确的话,那么在不同的解析器中返回的结果可能是不一样的
# soup = BeautifulSoup(response.text,'html.parser') #xml #html5lib
# soup = BeautifulSoup(response.text,'html5lib')
# prettify()Pretty-print this PageElement as a string
# print(soup.prettify())

html = "<body><div><a href=''>Python知识学堂</div></body>"
soup = BeautifulSoup(html, 'html.parser')
print("html.parser 结果：")
print(soup)  # <body><div><a href="">Python知识学堂</a></div></body>
soup1 = BeautifulSoup(html, 'lxml')
print("lxml 结果：")
print(soup1)  # <html><body><div><a href="">Python知识学堂</a></div></body></html>
soup2 = BeautifulSoup(html, 'xml')
print("xml 结果：")
print(soup2)  # <?xml version="1.0" encoding="utf-8"?>
# <body><div><a href="">Python知识学堂</a></div></body>
soup3 = BeautifulSoup(html, 'html5lib')
print("html5lib 结果：")
print(soup3)  # <html><head></head><body><div><a href="">Python知识学堂</a></div></body></html>

'''
可以看出html.parser与lxml 差不多的 都会给标签补齐，
但lxml会把html 标签给补齐，xml也会给标签补齐，
而且还会加上xml文档的版本编码方式等信息,但是不会把html标签补齐，
html5lib 也会补齐不但补齐了html标签而且给整个页面补齐head 标签。

这就验证了上面表格上的html5lib 的容错性最好，但是html5lib 解析器的速度不快，内容比较少的话是比较不出速度的差别的，
所以推荐使用lxml作为解析器,因为效率更高. 在Python2.7.3之前的版本和Python3中3.2.2之前的版本,必须安装lxml或html5lib, 
因为那些Python版本的标准库中内置的HTML解析方法不够稳定.

>>>     soup = BeautifulSoup(html)      print("html.parser 结果：")
不指定解析器的话，他会给出系统最好的解析器，我的系统是lxml,如果你在别的环境没有安装lxml的话，可能会是别的解析器，
总之系统会给你选择一个默认最好的解析器给你，所以你可以不指定，这还不是比较人性化的吧
'''

html2 = "<body><div><a data-id='234' href='' class='hyyh'>Python知识学堂</a></div><test>Python知识学堂</test></body>"
soup = BeautifulSoup(html, 'lxml')
tag1 = soup.a  # a标签就相当于一个标签
print(tag1.name)  # a
print(tag1.attrs)  # {'href': ''}
print(tag1['href'])  # 输出是空的
print(tag1.string)  # Python知识学堂
tag2 = soup.div  # test 也是算是标签(运行时报错)
tag2.name
print(tag2.name)  # div
print(tag2.attrs)  # {}

html3 = "<b><!--python 知识学堂 --></b>"
soup = BeautifulSoup(html3, 'lxml')
comment = soup.b.string
print(comment)  # python 知识学堂 若是"<b>我是谁？<!--python 知识学堂 --></b>"为None

html4 = '<html> <head> ' \
        '<meta content="text/html;charset=utf-8" http-equiv="content-type"/> ' \
        '<meta content="IE=Edge" http-equiv="X-UA-Compatible"/> <meta content="always" name="referrer"/> ' \
        '<title> python 知识学堂 </title> </head> ' \
        '<body > <div id="wrapper"> <div id="head"> <div class="head_wrapper"> <div class="s_form"> ' \
        '<div class="s_form_wrapper"> <div id="lg"> ' \
        '<img height="129" hidefocus="true" src="/bd_logo1.png" width="270"/> </div> ' \
        '<form action="/" class="form" id="form" name="fm"> <span class="bg s_ipt_wr"> ' \
        '<input autocomplete="off" autofocus="autofocus" class="keyword" id="kw" maxlength="255" name="wd" value=""/> </span>' \
        ' <span class="bg s_btn_wr"> <input autofocus="" class="bg s_btn" id="su" type="submit" value="搜索"/> </span> </form> ' \
        '</div> </div> <div id="u1"> <a class="mnav" href="/link_1" > Python</a> <a class="mnav" href="/link_2" > 知识 </a> ' \
        '<a class="mnav" href="/link_3"> 学堂 </a> <a class="mnav" href="/link_4" > 欢迎 </a> ' \
        '<a class="mnav" href="/link_5"> 您 </a> </div> </div> </div> </div> </body> </html>'
# 上面是随便写的一个页面代码
soupl=BeautifulSoup(html4,'lxml')
print('-------分割线1----------')
print(soupl.head)# 获取head 标签
print('-------分割线2----------')
print(soupl.a) #获取a 标签 默认是第一个
print(soupl.a.contents) #tag的 .contents 属性可以将tag的子节点以列表的方式输出
print('-------分割线3----------')
for child in soupl.form.children:
    print(child)##获取标签下的一级子标签
print('-------分割线4----------')
for child in soupl.form.descendants:
    print(child)#获取标签下的所有tag子孙节点进行递归循环
print('-------分割线5----------')
for sts in soupl.strings:
    print(sts)#输入标签内的字符串
print('-------分割线6----------')
for sts in soupl.stripped_strings:
    print(sts)#输入标签内的字符串 去除空字符串
print('-------分割线7----------')
print(soupl.find_all('a'))#会查找与字符串完整匹配的内容,下面的例子用于查找文档中所有的<a>标签
print('-------分割线8----------')
print(soupl.find_all(re.compile('^a')))#会通过正则表达式的 match()来匹配内容.找出所有以a开头的标签,这表示所有<a>标签都应该被找到
print('-------分割线9----------')
print(soupl.find_all(['a','head']))#找到文档中所有<a>标签和<head>标签
print('-------分割线10----------')
print(soupl.find_all(True))#True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点,即[html中所有节点按一个空格连接]
print('-------分割线11----------')
'''
find_all(self, name=None, attrs={}, recursive=True, text=None,limit=None, **kwargs)
        :param name: A filter on tag name.查找所有名字为 name 的tag,字符串对象会被自动忽略掉;
        :param attrs: A dictionary of filters on attribute values.
        :param recursive: If this is True, find_all() will perform a
            recursive search of this PageElement's children. Otherwise,
            only the direct children will be considered.
        :param limit: Stop looking after finding this many results.
        :kwargs: A dictionary of filters on attribute values.
        :return: A ResultSet of PageElements.
        :rtype: bs4.element.ResultSet
keyword 参数：如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索,
    如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性;
按CSS搜索：按照CSS类名搜索tag的功能非常实用,但标识CSS类名的关键字 class 在Python中是保留字,
    使用 class 做参数会导致语法错误.从Beautiful Soup的4.1.1版本开始,可以通过 class_ 参数搜索有指定CSS类名的tag;
string 参数:通过 string 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, 
    string 参数接受 字符串 , 正则表达式 , 列表, True .;
limit 参数:find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,
    可以使用 limit 参数限制返回结果的数量.效果与SQL中的limit关键字类似,当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果;
recursive 参数:调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,
    如果只想搜索tag的直接子节点,可以使用参数 recursive=False .
'''
print("通过tag的name：")
print(soupl.find_all('head'))              #获取head 标签
print("通过keyword获取：")
print(soupl.find_all(id="head"))           #获取Id 为head的所有标签
print("通过css类名获取：")
print(soupl.find_all('a',class_='mnav'))   #获取所有a标签 并且class属性值为mnav
print("通过string获取：")
print(soupl.find_all(string="知识"))       #获取所有a标签内容为python 的所有标签,全字符匹配
print("limit参数：")
print(soupl.find_all("a",limit=2))         #limit表示获取的数量
print("recursive 参数：")
print(soupl.find_all("a",recursive=False)) #recursive 默认为true 表示获取当前tag的所有子孙节点，如果为false 只搜索tag直接子节点
'''
注意只有 find_all() 和 find() 支持 recursive 参数.
find()的方法跟find_all()基本一样，唯一的区别是 find_all() 方法的返回结果是值包含一个元素的列表,
    而 find() 方法直接返回结果。
'''
print("格式化输出：")
print(soupl.prettify())
#如果只想得到结果字符串,不重视格式,那么可以对一个 BeautifulSoup 对象或 Tag 对象使用Python的 unicode() 或 str() 方法
print("压缩输出:")
print(str(soupl))
#Beautiful Soup输出是会将HTML中的特殊字符转换成Unicode,比如“&lquot;”
print("输出格式:")
print(str(BeautifulSoup("&&*&*",'lxml')))
#如果只想得到tag中包含的文本内容,那么可以用 get_text() 方法,这个方法获取到tag中包含的所有文版内容包括子孙tag中的内容,并将结果作为Unicode字符串返回
print("get_text():")
print(soupl.get_text())

class Demo():
    def __init__(self):
        try:
            base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/'
            trlist = self.get_data(base_url, "provincetable",'provincetr') #查看页面，就知道所有的省所在的tr上都有唯一的class='provincetr'
            for tr in trlist:
                for td in tr:
                    if td.a is None:
                        continue
                    p_name = td.a.get_text()
                    c_url = base_url + td.a.get('href')             #获取下级城市的地址
                    print("省:" + p_name) #获取每个省
                    # time.sleep(0.5)
                    trs = self.get_data(c_url, "citytable","citytr")
                    for tr in trs:  #循环每个市
                        if tr.find_all('td')[1] is None:
                            continue
                        #c_code = tr.find_all('td')[0].string       #获取城市code
                        c_name = tr.find_all('td')[1].string        #获取城市 name
                        ct_url = base_url + tr.find_all('td')[1].a.get('href') #获取下级区的地址
                        print(p_name+"-"+c_name)
                        time.sleep(0.5)
                        trs1 = self.get_courtydata(ct_url)
                        if trs1 is None:
                            continue
                        for tr1 in trs1:  #循环每个区
                            if tr1.find_all('td')[1] is None:
                                continue
                            #ct_code = tr.find_all('td')[0].string  #获取区code
                            ct_name = tr1.find_all('td')[1].string  #获取区name
                            print(p_name+"-"+c_name+"-"+ct_name)
        except:
            print("出错了")

    def get_data(self, url, table_attr,attr):
        response = requests.get(url)
        response.encoding = 'gb2312'  #编码转换
        soup = BeautifulSoup(response.text, 'lxml')  #使用lxml的解析器
        table = soup.find('table',class_=table_attr) #查看页面元素就知道数据都在第二个 tbody
        trlist = table.find_all('tr',class_=attr)
        return trlist

    def get_courtydata(self, url):
        response = requests.get(url)
        response.encoding = 'gb2312'                 #编码转换
        soup = BeautifulSoup(response.text, 'lxml')  #使用lxml的解析器
        towntr=soup.find('table',class_='towntable')
        if towntr is not None:
            table = soup.find('table',class_='towntable')
            trlist = table.find_all('tr',class_='towntr')
        else:
            table = soup.find('table',class_='countytable')
            trlist = table.find_all('tr',class_='countytr')
        return trlist

if __name__ == '__main__':
    Demo()