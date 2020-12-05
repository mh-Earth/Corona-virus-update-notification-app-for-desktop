# ___________________importing all needed modules ________________________________________________
import requests
from bs4 import BeautifulSoup
from plyer import notification
import time
import winsound
import datetime
import pymsgbox as pm

# _________________________function to get notification___________________________________________
def notifications(title="title",massage="massage",timeout=10):
    notification.notify(
    title = title,
    message = massage,
    app_icon='icon.ico',
    timeout = 15
    )
# _________________________function for HTML requset______________________________________________
def getDataInformation(url):
    a=requests.get(url)
    return a.text

#_________ ________________function to get the HTML Data__________________________________________
def getData():
    try :
        myhtmlData=getDataInformation('https://www.worldometers.info/coronavirus/')
    except Exception as e:
        pm.alert("Please check your internet connection and try again ","Error")        
        quit()
    return myhtmlData

myHTMLdata=getData()
# __________________function for get usefull Data from the HTML data_______________________________
def GetDataList():
    global myHTMLdata
    # ______________________getting main data from the HTML data___________________________________
    soup = BeautifulSoup(myHTMLdata,'html.parser')
    mydataStr=''
    mainData=''
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        mydataStr += tr.get_text()
    mydataList=mydataStr.split('\n\n')
    for item in mydataList:
        mainData += item
    # _______________________________________Getting the countyry data____________________________
    mainData=mainData.split('\n')
    itemIndex=mainData.index('Mexico') # Enter your country name here ( ) like 'Mexico','Belgium'
    mainData=mainData[itemIndex:itemIndex+5]

    return mainData
# ________________________________________function for beep sound_________________________________

def beep():
    frequency = 2000  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency,duration)

if __name__ == "__main__":
    mainData=GetDataList()
    # ___________________________+++++___________for debug________________________________________
    # print(mainData)
    # ____________________________________________________________________________________________

    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")

        if current_time==current_time: # Enter the time when you want to show the notification (7:00 pm Recommended or later)
            try:
                ntitle=f"Covid-19 update in {mainData[0]}"
                nMesg=f"New cases {mainData[2]} and New deaths {mainData[4]}"
                notifications(ntitle,nMesg)
                beep()
                break
            except Exception as e:
                pm.alert("Unable to show information")
                break
        
        else:
            continue

    quit()

