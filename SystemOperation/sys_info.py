#!/usr/bin/env python
# coding=utf-8

import commands,os,platform

def system():
    system = {}
    #system['os_name'] = platform.uname()[0]
    system['os_name'] = commands.getstatusoutput("sed -n 1p /etc/issue")[1]
    system['hostname'] = platform.uname()[1]
    system['kernel_version'] = platform.uname()[2]
    # 操作系统位数
    system['os_machine'] = platform.uname()[4]
    return system
def disk_info():
    disk = {}
    # 四舍五入，转为int类型
    disk['disk_total'] = str(int(round(float(commands.getstatusoutput("df -P | sed 1d | awk '{disk_total += $2 / 1024 / 1024}END{print disk_total}'")[1])))) + ' GB'
    disk['disk_used'] = str(int(round(float(commands.getstatusoutput("df -P | sed 1d | awk '{disk_used += $3 / 1024 / 1024}END{print disk_used}'")[1])))) + ' GB'
    return disk

def memory_info():
    memory={}
    memory['mem_total'] = commands.getstatusoutput("free -m | grep -i mem | awk {'print $2'}")[1] + ' MB'
    memory['mem_used'] = commands.getstatusoutput("free -m | grep -i 'mem' | awk {'print $3'}")[1] + ' MB'
    print memory
def ip_info():
    dev = []
    ip = []
    ipinfo = os.popen("ip addr | grep 'inet ' | awk -F'[ /]+' '{print $3,$NF}'")
    for info in ipinfo.readlines():
        #print(info),
        info = info.split(' ')
        ip.append(info[0])
        dev.append(info[1].split('\n')[0])
    new_ip =  dict(zip(dev,ip))
    return new_ip
# 获取CPU信息
def cpu_info():
    # commands.getstatusoutput('commands') 返回一个元组，第一个值是命令的返回值，第二个值是命令的输出结果
    # CPU 型号
    cpu_type = commands.getstatusoutput("grep 'model name' /proc/cpuinfo |  cut -d':' -f2 | uniq")[1].lstrip()
    # 物理CPU个数
    physical_cpu_num = commands.getstatusoutput("grep 'physical id' /proc/cpuinfo| sort| uniq| wc -l")[1].lstrip()
    # 每个物理CPU的逻辑CPU个数
    cpu_cores =  commands.getstatusoutput("grep 'cpu cores' /proc/cpuinfo | uniq | cut -d':' -f2")[1].lstrip()
    # 所有逻辑CPU个数
    processer_cpu_num = commands.getstatusoutput("grep 'processor' /proc/cpuinfo | wc -l")[1].lstrip()
    cpu = {'cpu_type':cpu_type,
           'physical_cpu_num':physical_cpu_num,
           'cpu_cores':cpu_cores,
           'processer_cpu_num':processer_cpu_num}
    return cpu

system = system()
disk = disk_info()
cpu = cpu_info()
ip = ip_info()
memory_info()
print system
print disk
print ip
print cpu
