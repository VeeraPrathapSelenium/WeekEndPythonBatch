input_str='The Transaction Id:74125 the Voucher Number is : 8526 the Journal Number :89562'

temp=""
for i in range(0,len(input_str)):

    if i+1!=len(input_str):
        crntChar=input_str[i:i+1]

        if crntChar.isdigit() and input_str[i+1].isspace():
            temp=temp+crntChar+"@"

        else:
            temp=temp+crntChar

print(temp)

splitdata=temp.split("@")

for x in splitdata:
    print(x.strip().title())
