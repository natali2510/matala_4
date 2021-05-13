import requests
file=open('dests.txt','r',encoding='utf-8')
my_key='__________'
adress='תל אביב'
response1=dict()
response2=dict()
order_data=dict()
dist=dict()

try: 
    for line in file:
        url_g="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (line.strip(),my_key) 
        url_d="https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&key=%s&destinations=%s" % (adress,my_key,line.strip())
        response1[line.strip()] = requests.get(url_g).json()
        response2[line.strip()] = requests.get(url_d).json()
        order_data[line.strip()] = (response1[line.strip()]['results'][0]['geometry']['location']['lng'],response1[line.strip()]['results'][0]['geometry']['location']['lat'],response2[line.strip()]['rows'][0]['elements'][0]['distance']['text'], response2[line.strip()]['rows'][0]['elements'][0]['duration']['text'])
        print("The destination:" + str(line.strip()))
        print('The distance is: '+ str(order_data[line.strip()][2]))
        print('The time from Tel-aviv is: '+ str(order_data[line.strip()][3]))
        print('The lag is:'+ str(order_data[line.strip()][0]))
        print('The lat is: '+ str(order_data[line.strip()][1]))
        print('*********************************')
        dist[line.strip()]= (response2[line.strip()]['rows'][0]['elements'][0]['distance']['value'])
    
    from operator import itemgetter
    maxd=(sorted(dist.items(),key= itemgetter(1),reverse=True))
    print("The three furthest destinations are: " )
    print(maxd[0])
    print(maxd[1])
    print(maxd[2])
  
except:
   print("There is no such destination in your file txt")