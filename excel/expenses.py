import xlsxwriter
wb =xlsxwriter .Workbook ('filename.xlsx',{'strings_to_numbers':True })
wsb =wb .add_worksheet (name ='Деловые расходы 2022')
wsp =wb .add_worksheet (name ='Личные расходы 2022')
bold =wb .add_format ({'bold':True })
row =2
col =0
wsb .write ('A1','Деловые расходы',bold )
wsb .write ('A2','Date:',bold )
wsb .write ('B2','Вид расходов:',bold )
wsb .write ('C2','Сумма расходов:',bold )
wsb .write ('D2','Total:',bold )
wsp .write ('A1','Личные расходы',bold )
wsp .write ('A2','Date:',bold )
wsp .write ('B2','Вид расходов:',bold )
wsp .write ('C2','Сумма расходов:',bold )
wsp .write ('D2','Total:',bold )
currency_format =wb .add_format ({'num_format':'# ##0.00 €'})
business =(
['01.01.2022','type1','1000'],
['01.01.2022','type2','1000'],
['01.01.2022','type3','1000'],
['01.01.2022','type4','1000'],
['01.01.2022','type4','1000'],
['01.01.2022','type5','1000'],
)
personal =(
['01.01.2022','type1','1000'],
['01.01.2022','type2','1000'],
['01.01.2022','type3','1000'],
['01.01.2022','type4','1000'],
['01.01.2022','type4','1000'],
['01.01.2022','type5','1000'],
)
for i ,r ,c in (business ):
    wsb .write (row ,col ,i )
    wsb .write (row ,col +1 ,r )
    wsb .write (row ,col +2 ,c )
    row +=1
wsb .write_formula ("D3","=СУММ(C3:C7)",currency_format )
for i ,r ,c in (personal ):
    wsp .write (row ,col ,i )
    wsp .write (row ,col +1 ,r )
    wsp .write (row ,col +2 ,c )
    row +=1
wsp .write_formula ("D3","=СУММ(C3:C7)",currency_format )
wb .close ()