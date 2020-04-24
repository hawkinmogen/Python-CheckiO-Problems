# Link to my solution on CheckiO:
# https://py.checkio.org/mission/time-converter-24h-to-12h/publications/hawkinmogen/python-3/first/share/80b47cb6a740f51df3f0bc35ac5ea87b/

def time_converter(time):
    time=time.split(':')
    
    if time[0]=='00':
        return "12:00 a.m."
    
    if time[0]=='12':
        return "%s:%s p.m."%(time[0],time[1])
    
    if int(time[0])>12:
        time[0]=int(time[0])-12
        return "%d:%s p.m."%(time[0],time[1])
    
    else:
        if time[0][0]=='0':
            time[0]=time[0][1:]
        return "%s:%s a.m."%(time[0],time[1])
