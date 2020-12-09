import argparse
import json
import os
import sys


def createParser():
    """
    Парсер аргументов командной строки
    """
    pars = argparse.ArgumentParser()
    pars.add_argument('path')
    pars.add_argument('-j', '--json', action='store_true', default=False)
    return pars


parser = createParser()
namespace = parser.parse_args(sys.argv[1:])
path_to_log = os.path.abspath(namespace.path)
jsn = namespace.json

json_file = {'First task': {}, 'Second task': {}, 'Third task': [], 'Forth task': [], 'Fifth task': []}
value = {'GET': 0, 'POST': 0, 'HEAD': 0, 'PUT': 0,  'DELETE': 0, 'OPTIONS': 0, 'PATCH': 0, 'TRACE': 0, 'CONNECT': 0}
parsed = []
total = 0
with open(path_to_log, 'r') as f:
    for i in f:
        parsed += [i.strip().split()]

"""
Первое и второе задание:
Количество запросов по типу, например: GET - 20, POST - 10 и т.д. (0,5 балла)
Общее количество запросов (0,5 балла)
"""
for i in parsed:
    method = i[5].lstrip('"')
    if method in value:
        value[method] += 1
        total += 1

for key, values in value.items():
    if values:
        if jsn:
            json_file['First task'][key] = values
        else:
            print(values, key)
else:
    if jsn:
        json_file['Second task']['total requests'] = total
    else:
        print('\n####### Next task #######\n')
        print('total requests: ', total)

"""
Третье задание: 
Топ 10 самых больших по размеру запросов, 
должно быть видно url, код, число запросов (1 балл)
"""
if not jsn:
    print('\n####### Next task #######\n')

task = sorted(parsed, key=lambda x: -int(x[9]) if x[9] != '-' else 0)[0:10]
for i in task:
    url = i[6]
    status = i[8]
    length = i[9]
    if jsn:
        json_file['Third task'] += [{'url': url, 'status': status, 'length': length}]
    else:
        print(url, status, length)

"""
Четвертое задание:
Топ 10 запросов по количеству, которые завершились клиентской ошибкой, 
должно быть видно url, статус код, ip адрес (1 балл)
"""
if not jsn:
    print('\n####### Next task #######\n')

filtered = [" ".join(i) for i in parsed if int(i[8]) in list(range(400, 499))]
buf = {}
uniq = set(filtered)
for i in uniq:
    buf[i] = filtered.count(i)

unpack = [(i.split(), j) for i, j in buf.items()]
unpack.sort(key=lambda x: -int(x[1]))

for value in unpack[0:10]:
    obj = value[0]
    count = value[1]
    url = obj[6]
    status = obj[8]
    ip = obj[0]
    if jsn:
        json_file['Forth task'] += [{'count': count, 'url': url, 'status': status, 'ip': ip}]
    else:
        print(count, url, status, ip)

"""
Пятое задание:
Топ 10 запросов серверных ошибок по размеру запроса, 
должно быть видно url, статус код, ip адрес (1 балл)
"""
if not jsn:
    print('\n####### Next task #######\n')

filtered = [i for i in parsed if int(i[8]) in list(range(500, 599))]
task = sorted(filtered, key=lambda x: -int(x[9]) if x[9] != '-' else 0)[0:10]
for i in task:
    url = i[6]
    status = i[8]
    length = i[9]
    ip = i[0]
    if jsn:
        json_file['Fifth task'] += [{'url': url, 'status': status, 'ip': ip, 'length': length}]
    else:
        print(url, status, ip, length)
if jsn:
    with open('result.json', 'w') as f:
        json.dump(json_file, f)
