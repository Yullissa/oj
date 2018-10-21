from openpyxl import *
wb = load_workbook('test.xlsx', data_only=True)
sh = wb["Sheet1"]
val=(sh['C1'].value)
print(val)