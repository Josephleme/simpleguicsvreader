FILE_NAME = 'table.csv'

def getDataList(FILE_NAME):
    dataFile = open(FILE_NAME, "r")
    data_list = []
    for line in dataFile:
        data_list.append(line.strip().split(','))
    return data_list


def getMonthlyAverage(data_list):
    m ='08'
    n='2008'
    monthlyAverageList=[]
    numerator=[]
    denominator=[]
    for i in data_list:       
        month=i[0].split('-')[1]  
        year=i[0].split('-')[0]
        vol=float(i[5])
        volMultAdj=vol*float(i[6])        #multiply volume and adjusted close price
        #if m==month and n==year:
        numerator.append(volMultAdj)   #sum of volume times adjusted close price
        denominator.append(vol)     # sum of volumes                        
        if month!=m and year!=n:
            sumNum=sum(numerator)
            sumDen=sum(denominator)
            average=float(sumNum)/float(sumDen)     #average
            print (average)          
                #a-tuple=(month, year, average)
               # monthlyAverageList.append(a-tuple)
        m=month                          #redefine month
        n=year							  #redefine year
    return monthlyAverageList


def printInfo(monthlyAverageList):
    monthlyAverageList.sort()
    print ('The 6 best averages for google are:')
    print (monthlyAverageList)
    monthlyAverageList.reverse()
    print ('The 6 worst averages for google are:')
    print (monthlyAverageList)

getDataList(FILE_NAME)
print('hi joe')