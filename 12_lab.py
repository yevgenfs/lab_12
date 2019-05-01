import re

with open('access_log2.txt', 'r') as file:
    step = 1
    for lines_of_file in file.readlines():
        pattern = r".+((09/Mar/2004:(21:[10-59]:[44-59]|2[2-3]:[0-59]:[0-59]))|(10/Mar/2004:\d\d:\d\d:\d\d)|(11/Mar/2004:(0[0-9]:[0-59]:[0-59]|1[0-8]:[0-59]:[0-59]|19:[0-29]:[0-28]))).+"
        if re.search(pattern, lines_of_file):
            step = step + 1
print("Amount of request : " + str(step-1))
#09/Mar/2004:(19:[29-59]:[28-59]|1[0-9]:[0-59]:[0-59]|20:[0-59]:[0-59])
#|(10/Mar/2004:([0-23]:[0-59]:[0-59])|(11/Mar/2004:([0-18]:[0-59]:[0-59]|19:[0-29]:[0-28]))