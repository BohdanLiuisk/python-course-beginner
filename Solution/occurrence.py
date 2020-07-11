s = input()
firtPoint = s.find('f')
lastPoint = s.rfind('f')
if firtPoint == -1:
    print()
elif firtPoint == lastPoint:
    print(firtPoint)
else:
    print(firtPoint, lastPoint)
