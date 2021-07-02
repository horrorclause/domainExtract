
import re


"""

Extract domains from text, and export them to a clean file.

"""

# File you want to extract domains from
file = open('C:\\YOUR\\PATH\\HERE\\samplesites.txt', 'r', errors='ignore')
lines = file.readlines()

# File you want to export extracted domains to
newFileName = input('Name of new list: ')
newList = open("C:\\PATH\\TO\\NEW\\FILE\\HERE\\{}.txt".format(newFileName), 'a')

# Extracted domains are held in this list before being written to the new file
toBeWritten = []

# Regex to pull domains
try:
    for i in lines:
        found = re.findall(r'(?:[\w+-]+\w+\.\w+)', i)

        if not found:
            pass
        else:
            #print(found[0])
            if found[0] not in toBeWritten: # Removes duplicates in list toBeWritten
                toBeWritten.append(found[0])

except Exception as e:
    print(e)
    pass

# Write clean list to new file
for x in toBeWritten:
    print(x)
    newList.write(x+'\n')

newList.close()
file.close()
