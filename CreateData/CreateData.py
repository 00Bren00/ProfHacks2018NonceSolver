import hashlib, binascii

word = ""
nonce = 0
found = False
finishedWords = 0

output_file = open("solutions.csv", 'w')

for line in open("words.txt", 'r'):
    word = line
    nonce = 0
    print "I finished " + str(finishedWords) + " words"
    finishedWords = finishedWords + 1
    found = False

    while not found:
        input = word + str(nonce)
        dk = hashlib.pbkdf2_hmac('sha256', input, b'salt', 100000)

        if(binascii.hexlify(dk)[0] == '0'):
            output_file.write(word + ',' + str(nonce))
            # print "found"
            # print binascii.hexlify(dk)
            # print nonce
            found = True
        else:
            nonce = nonce + 1

    #
    # print type(binascii.hexlify(dk))
    # print binascii.hexlify(dk)[0]
    # found = True
output_file.close()
