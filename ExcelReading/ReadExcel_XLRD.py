import xlrd as exl

path=r'C:\Users\Hanshik\Desktop\Testadata.xlsx'

workbook=exl.open_workbook(path)

#it will give total number of sheets available in the workbook
print(len(workbook.sheets()))
print(workbook.sheet_names())

sheet=workbook.sheet_by_name("Data")

print("Total Rows Count :"+str(sheet.nrows))
print("Total Columns Count :"+str(sheet.ncols))

#get cell data

print(sheet.cell_value(0,0))


#Print all the rows and columns data

for r in range(1,sheet.nrows):

    for c in range(0,sheet.ncols):

        print(sheet.cell_value(r,c))

