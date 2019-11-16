stringdata="ABCBBNAAANBBBDFGJKBBBB"

temp=""

for char in stringdata:
    crntchar=char

    if not crntchar in temp:
        temp=temp+crntchar
        print(crntchar+" is repeated for "+str(stringdata.count(crntchar))+" Times")