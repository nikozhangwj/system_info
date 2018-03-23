# encoding: utf-8
def _cpu_info(file):
    fhandler = open(file,'rt')
    for line in fhandler:
        if len(line) < 12:
            continue
        cpu_info = line.split()
        if cpu_info[0] == 'model' and cpu_info[1] == 'name':
            data=' '.join(cpu_info[3:])
            print(data)
            print(type(data))

_cpu_info('/proc/cpuinfo')