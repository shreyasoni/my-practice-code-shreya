import xlrd
loc = ("sample.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
#print sheet
sheet.cell_value(0, 0)
for i in range(sheet.nrows):
    #for k in range(sheet.cell_value):
        #print k
    print(sheet.cell_value(i, 0))
