#Link to my solution on CheckiO:
# https://py.checkio.org/mission/time-converter-12h-to-24h/publications/hawkinmogen/python-3/first/share/6ddd61ca7f97a31ac3d715b3f961df49/

def time_converter(time):
    if 'p.m.' in time:
        if time[0:2]=='12':
            time=time[0:time.index(' ')]
            time=time.split(':')
            return time[0]+':'+time[1]
        else:
            time=time[0:time.index(' ')]
            time=time.split(':')
            return str((int(time[0])+12))+':'+time[1]
    else:
        if time[0:2]=='12':
            return '00:00'
        elif len(time[:time.index(':')])==1:
            return '0'+time[:time.index(' ')]
        else:
            return time[:time.index(' ')]
