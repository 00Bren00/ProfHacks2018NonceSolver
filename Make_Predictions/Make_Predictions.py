from sklearn import tree
from sklearn.naive_bayes import GaussianNB
import hashlib, binascii


input_file = open("solutions4.csv", 'r')
alldata = [None] * 2129
alllabels = [None] * 2129

alldatatest = [None] * 113
alllabelstest = [None] * 113

linenum = 0

trainNum = 0
testNum = 0


# training:    2129
# testing:     113


for line in input_file:
    data = line.split(',')
    problem = data[0]
    answer = data[1]
    answer = answer[:len(answer) -1]
    if(linenum%20 == 0):
        alldatatest[testNum] = problem
        alllabelstest[testNum] = answer
        testNum = testNum + 1
    else:
        alldata[trainNum] = [problem.__hash__()]
        alllabels[trainNum] = answer
        trainNum = trainNum + 1

    linenum = linenum + 1
        # data = line.split(',')
        # problem = data[0]
        # answer = data[1]
        # alldata[linenum] = data
        # alllabels[linenum] = answer

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()

clf.fit(alldata,
        alllabels
        )
correct = 0
wrong = 0

for mystring in alldatatest:
    predicted_nonce = clf.predict(mystring.__hash__())
    predicted_nonce = predicted_nonce[0]

    check = mystring + str(predicted_nonce)
    dk = hashlib.pbkdf2_hmac('sha256',
                             check,
                             b'salt', 100000)

    if (binascii.hexlify(dk)[0] == '0'):
        correct = correct + 1
    else:
        wrong = wrong + 1

print "Correct:     " + str(correct)
print "Wrong:       " + str(wrong)


