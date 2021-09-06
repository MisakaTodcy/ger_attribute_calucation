#读取module文件夹下的文件
#1、data_ger文件
import configparser
import os
config = configparser.ConfigParser()
import re
ger_path = r'C:\Users\1\Desktop\game\config\moduleconfig'#文件夹路径配置

def read_ger(file_name):
    file_path = os.path.join(ger_path,file_name)
    ger_list = []
    ger_dic = {}
    #读取data_ger文件
    with open(file_path,'r',encoding='utf-8') as ff:
        #data_ger中有中文，encodeing='utf-8表示使用utf-8的方式解读该配置文件
        while True:
            ger_lins=ff.readline()
            print('',ger_lins,end="")
            #ger_lins_new = ger_lins.replace("{","").replace("}","").replace("[","").replace("]","")
            #这里使用replace()方法来去掉每个列表中的{}和[]
            #everyger= re.split(r'[,]',ger_lins_new.strip())
            #分割每个元素
           # print('every',everyger)
            #num = len(everyger)
           # #print('数量',num)
            if not ger_lins:      
                break
            '''if ger_id == everyger[1]:
                ger_life == everyger[39]
                ger_attactk == everyger[40]   
                '''
            print("000",ger_lins[2])



read_ger('data_ger.config')