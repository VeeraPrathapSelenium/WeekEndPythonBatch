import json

#sample Json data
employeedata='''{
    "Name":"Prathap",
    "Place":"Hyderabad",
    "Age":30,
    "Mobile":9626272284
}'''

# Convert Json to Python Object

alterdata=json.loads(employeedata)

#print(alterdata["Name"])


# Convert the Python data into JSON
myjsonfile="data.json"

jsonfile=open(myjsonfile,"w")

schools={
    "School Name":"HYD PUBLIC SCHOOL",
    "LOC":"KPHB",
    "Country":"INDIA"
}

y=json.dump(schools,jsonfile,indent=4,sort_keys=True)
print(y)


