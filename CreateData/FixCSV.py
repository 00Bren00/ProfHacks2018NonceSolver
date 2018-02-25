input_file = open("solutions2.csv", 'r')

input_file2 = open("solutions3.csv", 'r')

output_file = open("solutions4.csv", 'w')

word = ""
number = ""
content = input_file.next()
for char in content:
    if(char == ','):
        print "here"
        if(len(number) > 0):
            print "here"
            word = input_file2.next()
            output_file.write(word[:len(word) - 1] + ',' + number + '\n')
            number = ''
    else:
        try:
            int(char)
            number = number + str(char)
        except Exception:
            word = word + char
output_file.close()