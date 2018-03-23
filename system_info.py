# encoding: utf-8
# python3
import time
from datetime import datetime


def mem_info(file):
    fhandler = open(file,'rt')
    print('='*20)
    print('MEM INFO')
    print('='*20)
    for line in fhandler:
        _node = line.split()
        if _node[0] == 'MemTotal:':
            _MemTotal = '总内存： ' + str(int(line.split()[1])//1024) + 'MB'
            print (_MemTotal)
        if _node[0] == 'MemFree:':
            _MemFree = '空闲内存： ' +str(int(line.split()[1])//1024) + 'MB'
            print (_MemFree)
        if _node[0] == 'MemAvailable:':
            _MemAvailable = '可用内存： ' +str(int(line.split()[1])//1024) + 'MB'
            print (_MemAvailable)
    print('')
    fhandler.close()

def _cpu_info(file):
    fhandler = open(file,'rt')
    print('='*20)
    print('CPU INFO')
    print('='*20)
    for line in fhandler:
        if len(line) < 12:
            continue
        cpu_info = line.split()
        if cpu_info[0] == 'model' and cpu_info[1] == 'name':
            cpu_model=' '.join(cpu_info[3:])
            print('CPU型号:' + cpu_model)
        if cpu_info[0] == 'cpu' and cpu_info[1] == 'MHz':
            cpu_MHz=float(''.join(cpu_info[3]))
            print('CPU频率: ',end='\t')
            print(cpu_MHz,'MHz')
        if cpu_info[0] == 'cache':
            cpu_cache=int(''.join(cpu_info[3]))//1024
            print('CPU缓存: ',end='\t')
            print(cpu_cache,'MB')
        if cpu_info[1] == 'cores':
            cpu_cores=int(''.join(cpu_info[3]))
            print('CPU核数:',end='\t')
            print(cpu_cores)
    fhandler.close()


print ('系统时间: ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
mem_info('/proc/meminfo')
_cpu_info('/proc/cpuinfo')