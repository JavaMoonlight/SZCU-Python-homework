import urllib.request
import re

# 获取指定url的源码信息
def getHTMLText(url):
    try:
        #模拟浏览器向服务器发送请求 response响应
        response = urllib.request.urlopen(url, timeout=30)
        #获取响应中的页面的源码  content 内容的意思
        # read方法  返回的是字节形式的二进制数据
        # 我们要将二进制的数据转换为字符串
        # 二进制--》字符串  解码  decode('编码的格式')
        html = response.read().decode('utf-8')
        return html
    except:
        return "access the web error"
    return ""

# 根据具体结构匹配需要的排名信息，最终以列表的形式返回
def fullTextToSchoolList(html):
    # 正则匹配所有语言名称
    expr = "<tr><td>(.*?)</td><td>(.*?)</td><td>(<img.*?>)?</td><td.*?><img.*?></td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>"
    #匹配排名信息
    #使用re.S参数以后，正则表达式会将这个字符串作为一个整体，在整体中进行匹配。
    reg = re.compile(expr,re.S)
    urank = re.findall(reg, html)
    return urank

# 格式化输出结果
def printSchoolList(ulist, num):
    print("{:^9}\t{:^9}\t{:^70}\t{:^15}\t{:^18}\t{:^5}".format("Apr 2023","Apr 2022","Change","Programming Language","Ratings","Change"))
    print('============================'
          '==============================='
          '================================='
          '==================================='
          '=====================')
    for i in range(num):
        u = ulist[i]
        print("{:^6}\t{:^15}\t{:^70}\t{:^25}\t{:^10}\t{:^15}".format(u[0].strip(),u[1].strip(),u[2].strip(),u[3].strip(),u[4].strip(),u[5].strip()))

#主函数
def main():
    # 定义一个url，就是要访问的网站的地址
    url = "https://www.tiobe.com/tiobe-index/"
    html = getHTMLText(url)
    ulist = fullTextToSchoolList(html)
    print(ulist)
    printSchoolList(ulist, 10)

#执行main主函数
if __name__ == "__main__":
    main()

