import  re

str_sourceString='company Email Address:firstname.lastname@cts.com'

str_pattern='[a-z]*\.[a-z0-9]*\@cts\.com'


status=re.search(str_pattern,str_sourceString)

if(status!=None):

    #data = re.findall(str_pattern, str_sourceString)

    print(status.span())
    print(status.string)
    print(status.group())


    #print(data)
else:
    print("Invalid Pattern, or Data available on the source string")



