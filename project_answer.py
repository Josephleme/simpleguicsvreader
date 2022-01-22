FILE_NAME = 'table.csv'
def getDataList(FILE_NAME):
    with open(FILE_NAME, "r") as dataFile:
        data_list = []
        for line in dataFile:
            data_list.append(line.strip().split(','))
    return data_list

data_list=getDataList(FILE_NAME)
def get_monthly_averages(data_list):
    monthly_average_list = []
    monthly_sales = []
    monthly_vol = []
    dates = []
    data_list.pop(0) 
    index=1
    for j in data_list:
        month = j[0][5:7]
        year = j[0][:4]
        mydate = month + '-' + year
        dates.append(mydate)
    
    for i in data_list:
        month = i[0][5:7]
        year = i[0][:4]
        m_y = month + '-' + year
        v = float(i[5])
        c = float(i[6])
        try:
            if m_y == dates[index]:
                sales = v*c
                monthly_sales.append(sales)
                monthly_vol.append(v)
#                 avg = sum(monthly_sales)/sum(monthly_vol)
                index += 1
            else:
                sales =v*c
                monthly_sales.append(sales)
                monthly_vol.append(v)
                avg = sum(monthly_sales)/sum(monthly_vol)
                w=round(avg,2)
                my_tuple = (w,m_y)
                monthly_average_list.append(my_tuple)
                monthly_sales.clear()
                monthly_vol.clear()
                index+=1
        except IndexError:
            sales = v*c
            monthly_sales.append(sales)
            monthly_vol.append(v)
            avg = sum(monthly_sales)/sum(monthly_vol)
            x=round(avg,2)
            my_tuple = (x,m_y)
            monthly_average_list.append(my_tuple)
            print(x)
    return monthly_average_list
monthlyAverageList = get_monthly_averages(data_list)
def printInfo(monthlyAverageList):
    with open('Monthly_averages.txt', 'w') as txt:
        print('6 best months for google stock:', file=txt)
        monthlyAverageList.sort(reverse=True)
        # print ('6 best months for google stock:')
        w= monthlyAverageList[:6]
        for i in w:
            print(str(i[1])+(','),i[0],file=txt)
        print(file=txt)
        monthlyAverageList.reverse()
        print ('6 worst months for google stock:',file=txt)
        z=monthlyAverageList[:6]
        for i in z:
            print(str(i[1])+(','),i[0],file=txt)


getDataList(FILE_NAME)
printInfo(monthlyAverageList)
