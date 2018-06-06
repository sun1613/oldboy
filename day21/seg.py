#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:BanShaoHuan
@file: seg.py 
@time: 2018/05/03
@contact: banshaohuan@163.com
@site:  
@software: PyCharm

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃  永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""
import os

def file_handler(backend_data, res=None, type='fetch'):
    if type == 'fetch':
        with open('haproxy.conf', 'r') as read_f:
            tag = False
            ret = []
            for read_line in read_f:
                if read_line.strip() == backend_data:
                    tag = True
                    continue
                if read_line.startswith('backend') and tag:
                    break
                if tag:
                    print('\033[1;45m%s\033[0m' %read_line, end='')
                    ret.append(read_line)
        return ret
    elif type == 'change':
        with open('haproxy.conf', 'r') as read_f,\
            open('haproxy.conf.new', 'w') as write_f:
            tag = False
            has_write = False
            for read_line in read_f:
                if read_line.strip() == backend_data:
                    tag = True
                    continue
                if tag and read_line.startswith('backend'):
                    tag = False
                if not tag:
                    write_f.write(read_line)
                else:
                    if not has_write:
                        for record in res:
                            write_f.write(record)
                        has_write = True
        os.rename('haproxy.conf', 'haproxy.conf.bak')
        os.rename('haproxy.conf.new', 'haproxy.conf')
        os.remove('haproxy.conf.bak')

def fetch(data):
    backend_data = 'backend %s' %data
    return file_handler(backend_data)
def add():
    pass

def change(data):
    backend = data[0]['backend']
    backend_data = 'backend %s' %backend

    old_server_record= '%sserver %s %s weight %s maxconn %s\n' %(' '*8,data[0]['record']['server'],
                                                           data[0]['record']['server'],
                                                           data[0]['record']['weight'],
                                                           data[0]['record']['maxconn']
                                                           )

    new_server_record = '%sserver %s %s weight %s maxconn %s\n' % (' ' * 8, data[1]['record']['server'],
                                                            data[1]['record']['server'],
                                                            data[1]['record']['weight'],
                                                            data[1]['record']['maxconn']
                                                            )
    print('用户想要修改的记录是', old_server_record)
    res = fetch(backend)
    print('data from fetch function', res)
    if not res or old_server_record not in res:
        return 'The record you want to change not exits'
    else:
        index = res.index(old_server_record)
        res[index] = new_server_record

    res.insert(0,'%s\n' %backend_data)
    file_handler(backend_data, res=res, type='change')
def delete():
    pass

if __name__ == '__main__':
    msg = '''
    1:查询
    2:添加
    3:修改
    4:删除
    5:退出
    '''
    msg_dic = {
        '1':fetch,
        '2':add,
        '3':change,
        '4':delete
    }
    while True:
        print(msg)
        choice = input('请输入你的选项:').strip()
        if not choice:continue
        if choice == '5':break

        data = input('请输入你的数据：').strip()

        if choice != '1':
            data = eval(data)

        res = msg_dic[choice](data)
        print('最终的结果是', res)


# [{'backend':'www.oldboy1.org','record':{'server':'2.2.2.5','weight':30,'maxconn':4000}},{'backend':'www.oldboy1.org','record':{'server':'2.2.2.4','weight':20,'maxconn':3000}}]
