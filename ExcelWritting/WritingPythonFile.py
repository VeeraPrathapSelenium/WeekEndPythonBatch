import  xlsxwriter

#create a workbook instance
workbook=xlsxwriter.Workbook("Data.xlsx")

#create Worksheet instance
sheet=workbook.add_worksheet("Testdata")

# write data into the cell

sheet.write(0,0,'Country')
sheet.write("A2","India")
workbook.close()



