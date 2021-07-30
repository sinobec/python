def convertToLower(*arug, **kvarug):
    thislist = list(arug)
    for index, value in enumerate(thislist):
        thislist[index] = value.lower()
    return print(*arug, **kvarug)

t1 = convertToLower('Hello', 'Canada',sep='_')