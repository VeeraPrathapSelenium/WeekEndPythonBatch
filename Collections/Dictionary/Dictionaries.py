
mydict={

    "Name":"Prathap",
    "Place":"Hyderabad",
    "Location":"KPHB"


}

#print(mydict['Name'])

#loop

# for x in mydict:
#     print(x)

#Get only keys

for x in mydict.keys():
    print(x)
print("***********************************")

for x in mydict.values():
    print(x)


print("***********************************")

# Change the value of a dict

mydict["Name"]="Hari"


for k,v in mydict.items():

    print(k,v)
# check for the key existance

print( "Name" in mydict)

# Get the length of the dict

print(len(mydict))

# Add the items to the dict

mydict["Age"]=29

print(mydict)

#Remove a key

mydict.pop("Age")

mydict.clear()
print(mydict)



