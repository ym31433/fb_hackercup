
# input
inFile = open("lazyloading.in", 'r')
numOfDays = int(inFile.readline())

# output
outFile = open("lazy_loading_output.txt", 'w')

# calculation
for day in xrange(numOfDays):
    # parse and prepare the items list
    numOfItems = int(inFile.readline())
    items = []
    for i in xrange(numOfItems):
        items.append(int(inFile.readline()))
    items.sort(reverse = True)
    # start computing
    numOfTrips = 0
    while items:
        numOfTrips += 1
        w = items.pop(0)
        # how many items should be put in the bag this time
        # remove them from the list
        for i in xrange(50/w):
            if not items:
                numOfTrips -= 1
                break
            items.pop()
    # write the result to the output file
    outFile.write("Case #" + str(day+1) + ": " + str(numOfTrips) + "\n")


# close file
inFile.close()
outFile.close()
