li=[['date','open price','close','adjclose','volume'],
	['12/09/2001',13,14,15,10],
	['13/09/2001',12,10,31,40],
	['27/09/2001',12,20,32,50],
	['02/01/2005',10,20,35,60],
	['10/01/2005',13,10,20,40],
	['21/01/2005',17,10,20,80],
	['19/08/2006',18,10,20,90],
	['24/08/2006',11,9,30,40],
	['30/08/2006',8,7,56,72],]
# print(len(li))



li.pop(0)

monthlyAverageList = []
monthly_sales =[]
monthly_vol = []
dates = []
index = 1
for j in li:
	date = j[0][3:]
	dates.append(date)
print(dates)
for i in li:
	mine = i[0][3:]
	m_y = i[0][3:]
	vol = i[4]
	close = i[3]
	try:
		if m_y == dates[index]:
			sales = vol*close
			monthly_sales.append(sales)
			monthly_vol.append(vol)
			# avg = sum(monthly_sales)/sum(monthly_vol)
			# print(avg)
			index += 1
		else:
			sales = vol*close
			monthly_sales.append(sales)
			monthly_vol.append(vol)
			avg = sum(monthly_sales)/sum(monthly_vol)
			print(avg)
			my_tuple = (avg,m_y)
			monthlyAverageList.append(my_tuple)
			monthly_vol.clear()
			monthly_sales.clear()
			index += 1
			
	except IndexError:
		sales = vol*close
		monthly_sales.append(sales)
		monthly_vol.append(vol)
		avg = sum(monthly_sales)/sum(monthly_vol)
		w = round(avg,4)
		my_tuple = (w,m_y)
		monthlyAverageList.append(my_tuple)
		print(avg)
print(monthlyAverageList)
print('my name is joe')
# 15*10=150
# 31*40=1240
# 32*50=1600
# 1876



		


