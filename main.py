#-*- codeing = utf-8 -*-
#@Time : 2021/9/18 23:01
#@Author : 陈浠
#File : main.py
#Software : PyCharm

# import time
import codecs
import os

# starttime = time.time()

#获取指定路径下文件的内容
def get_file_contents(path):
    str = ''
    f = codecs.open(path, mode='r', encoding='utf-8') # 打开txt文件，以"utf-8'编码读取
    line = f.readline() # 以行的形式进行读取文件
    while line:
        str = str + line
        line = f.readline()
    f.close()
    return str

from Analyse import Analyse
Analyse = Analyse()

def main_test():
    path1 = input("请输入论文原文的文件的绝对路径：")
    path2 = input("请输入抄袭版论文的文件的绝对路径：")
    if not os.path.exists(path1) :
        print("论文原文文件不存在！")
        exit()
    if not os.path.exists(path2):
        print("抄袭版论文文件不存在！")
        exit()
    save_path = input('请输入保存答案的绝对路径：')
    str1 = get_file_contents(path1)
    str2 = get_file_contents(path2)
    result = Analyse.get_Tfidf(str1, str2)
    # 把相似度写入文件
    f = open(save_path, 'w', encoding="utf-8")
    f.write("文章相似度： %.2f" % result)
    f.close()
    return result

if __name__ == '__main__':
    print('%.2f'%main_test())

# endtime = time.time()
# dtime = endtime - starttime
# print("程序运行时间：%.8s s" % dtime)  # 显示到微秒

