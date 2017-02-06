import math

# input file
inFile = open("progress_pie.txt", 'r')
numOfPoints = int(inFile.readline())

# output file
outFile = open("progress_pie_output.txt", 'w')

# calculate
for i in xrange(numOfPoints):
    [p, x, y] = [int(num) for num in inFile.readline().strip().split()]
    color = "white"
    if (x-50)**2 + (y-50)**2 < 2500:
        if (x >= 50 and y >= 50) or (x > 50 and y < 50):
            if (p*math.pi/50 > math.atan((x-50)/(y-50))):
                color = "black"
        else:
            if (p*math.pi/50 > math.atan((x-50)/(y-50))+math.pi):
                color = "black"
    outFile.write("Case #" + str(i+1) + ": " + color + "\n")

inFile.close()
outFile.close()
