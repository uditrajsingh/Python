import requests, json, datetime
import matplotlib.pyplot as plt

__access_key = 'a2c0ec0155a860456bfdfeded2576d69'

def getUrl(date):
    base = 'http://data.fixer.io/api/'
    return base+date+'?'+'access_key='+__access_key

def getJsonResponse(url):
    res = requests.get(url)
    return res.json()

def getRates(jsonResponse):
    return jsonResponse['rates']

def getCountryRate(ratesArray, countryCode):
    return ratesArray[countryCode]


def getRateOn(date, code):
    url = getUrl(date)
    jsonRes = getJsonResponse(url)
    ratesArray = getRates(jsonRes)
    rate = getCountryRate(ratesArray, code) 
    return round(rate, 4)

def genX(dateArray):
    result = []
    for i in dateArray:
        l = i.split('-')
        result.append(int(l[2]))

    return result

def genY(dateArray, countryCode):
    result = []
    for i in dateArray:
        result.append(getRateOn(i, countryCode))

    return result

def plot(dateArray):
    plt.xlabel('Date')
    plt.ylabel('Rate')
    plt.title('Stock Analysis Of EUR to INR')

    x = genX(dateArray)

    y1 = genY(dateArray, 'INR')

    dt = genDate('2018-03-01', '2018-03-30')

    y2 = genY(dt, 'INR')

    y3 = []

    for i in range(len(y1)):
        y3.append((y1[i]+y2[i])/2.0)
        

    plt.plot(x, y1, 'go:', label='2018-01-01 TO 2018-01-30')
    plt.plot(x, y2, 'ro:', label='2018-03-01 TO 2018-03-30')

    plt.plot(x, y3, label='Average')

    plt.grid()    

    plt.legend(loc='best')

    plt.show()
    
        
    

def genDate(frm, to):
    frm = frm.split('-')
    to = to.split('-')
    start = datetime.datetime(int(frm[0]),int(frm[1]), int(frm[2]))
    end = datetime.datetime(int(to[0]),int(to[1]), int(to[2]))
    step = datetime.timedelta(seconds=86400)
    result = []
    while start <= end:
        result.append(start.strftime('%Y-%m-%d'))
        start += step
    return result


plot(genDate('2018-01-01','2018-01-30'))
