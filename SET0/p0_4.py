# Thays Rodrigues 
# SET 0 - Problema 4

year = 2017
month = 1  # 1 = janeiro, 2 = fevereiro, ..., 12 = dezembro
day = 9

if month == 1 or month == 2:
    year1=year-1
    month1=month+12
else:
    year1=year  
    month1=month
year2=year1%100
c=year1//100

out = (day + 13*(month1 + 1)//5  + year2 + year2//4 + c//4 -2*c)%7
print (out)