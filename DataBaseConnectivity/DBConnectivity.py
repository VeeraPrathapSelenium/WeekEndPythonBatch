import pyodbc
import xlrd


cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=LAPTOP-S1LVCJIH\SQLEXPRESS;"
                      "Database=Python;"
                      "Trusted_Connection=yes;")
cursor = cnxn.cursor()

workbook=xlrd.open_workbook(r"C:\Users\Hanshik\PycharmProjects\WeekEnd-FastTrack\ExcelWritting\Data.xlsx")
worksheet=workbook.sheet_by_name("Testdata")

for r in range(1,worksheet.nrows):

        studentname=worksheet.cell_value(r,0)
        course=worksheet.cell_value(r,1)
        place=worksheet.cell_value(r,2)
        cursor.execute("insert into std_details(Name,Course,Place) values('{studentname}','{course}','{place}')".format(studentname=studentname,course=course,place=place))
        cursor.commit()

