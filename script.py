import requests
import os
import time
import datetime

#music file location
music="C:\\Users\\Username\\Desktop\\Whistle.mp3"
tried=0

try:
    while(True):
        day=datetime.datetime.now().day
        month=datetime.datetime.now().month
        date="{}-{}-2021".format(day,month)
        
        district_id="211"
        #edit the district_id 
        
        x=requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict",params={'district_id':district_id,'date':date},headers={'accept':'application/json','Accept-Language':'en_US',})
        tried=tried+1
        if(x.status_code==200):
            x=x.json()
            for data in x["sessions"]:
                #edit the center_id according to your need 
                if(data["center_id"]==97386 or data["center_id"]==56394 or data["center_id"]==96947 or data["center_id"]==595208):
                    if(data["available_capacity_dose1"]>0):            
                        print("Vaccine slot found at:{}".format(data["name"]))
                        print("\n")
                        os.system(music)

        else:
            print("Error is fetching data")
            os.system(music)

        print("Tried {}".format(tried))
        time.sleep(35)           

except:
    print("Something went wrong.")
