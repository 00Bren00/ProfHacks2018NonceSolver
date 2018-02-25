input_file = open("solutions4.csv", 'r')

size = 0
total = 0
for line in input_file:
    data = line.split(',')
    problem = data[0]
    answer = data[1]
    size = size + 1
    total = total + int(answer) + 1
print "Total is:        " + str(total)
print "Size is:         " + str(size)
print "Average is:      " + str (float(total)/size)

