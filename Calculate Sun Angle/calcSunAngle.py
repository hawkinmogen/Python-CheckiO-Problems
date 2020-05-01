#Link to my solution on CheckiO:
#https://py.checkio.org/mission/sun-angle/publications/hawkinmogen/python-3/first/share/1711f340599164a049040d689a3d3863/

def sun_angle(time):
    time = time.split(":")
    time = (int(time[0])*60)+int(time[1])
    
    if time > 1080 or time < 360:
        return "I don't see the sun!"
    else:
     timeFromSunRise= time - 360
     sunAngle= .25*timeFromSunRise
     return round(sunAngle,2)
