import os
import shutil
'''
def dirList(path):
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path,filename)
        if  os.path.isdir(filepath):
            dirList(filepath)
        print filepath
        
allfile = dirList('f:\\python27\\test')
'''
disk = raw_input('�������̷�:')
f_name = raw_input('�������ļ��������ܺ��е��ַ�:')
doc_name = raw_input('�������ĵ������ܺ��е��ַ�:')

def delSthif(l,str1,path):  #����б�l�е�ĳ��Ԫ�غ����ַ���str1,��ɾ����Ԫ�أ�����ӡ���б�
    count = 0
    for i in l:
        if str1 not in i:
            count += 1
        else:
            os.remove(path+'\\'+l[count])
    #print "�����к���'f'���ĵ��ѱ�ɾ�����������ļ��У�"


def deldirif(var_path,str1):#���·���к����ַ���str1,ɾ����·�����������ļ�
    if str1 in var_path:
        shutil.rmtree(var_path)
  
for path,d,filename in os.walk(disk):
    #print path,filename
    deldirif(path,f_name) #��walkһ�飬�������к���fl���ļ��� ����ɾ��
for path,d,filename in os.walk(disk):
    delSthif(filename,doc_name,path) #��walkһ�飬�������к���f���ĵ�������ɾ��

a = raw_input("Mission Accomplished!\nPress any key to close:")
while a :
    break

    


