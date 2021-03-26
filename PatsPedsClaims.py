# PatPedsClaims
# Simple tool to download latest version of patent claims
# of an US Patent Application using USPTO Ped
# Author: Vinz Frauchiger
# License: Ypsomed exclusive

# imports
import json
import requests
import datetime
import time
import base64

import win32gui, win32con, os



#print(os.environ)

def get_claims(applId):
    """This function takes an application ID of an US Patent Application saves a pdf with the 12555321
    latest version of the claims to disk and return "Finished!" in case success.
    applId : 12123456
    """
    # URL needed
    url_l = "https://ped.uspto.gov/api/queries/cms/"

    
    
    # get biblio for application
    r2 = requests.get(url_l+"/"+applId)
    resp_l = json.loads(r2.text)
    clm = [ doc for doc in resp_l if doc['documentCode']=='CLM']

    #extract dates for newly filed claims
    dates = []
    print('New claims were filed on the following dates:')
    for doc in clm:
        print(doc['mailRoomDate'])
        doc['mailRoomDate'] = datetime.datetime.strptime(doc['mailRoomDate'],'%m-%d-%Y')
        dates.append(doc['mailRoomDate'])

    #get the latest claims
    last_claims = [doc for doc in clm if doc['mailRoomDate']==max(dates)]
    print('\n...Thank you for waiting!')
    r3 = requests.get(url_l + '/' + last_claims[0]['pdfUrl'])
    #save the claims to file

    
    filewopath = str(last_claims[0]['mailRoomDate'].strftime('%Y_%m_%d') +'_'+applId +'_claims.pdf')
    print(filewopath)


    filter='Acrobat files\0*.pdf\0Otherfiles\0*.*'
    customfilter='Other file types\0*.*'
    filename, customfilter, flags=win32gui.GetSaveFileNameW(
        InitialDir=os.environ['userprofile'],
        Flags=win32con.OFN_EXPLORER,
        MaxFile = 1300,
        File=str(filewopath), DefExt='pdf',
        Title='Bitte Ordner und Dateiname wählen',
        Filter=filter,
        CustomFilter=customfilter,
        FilterIndex=0)


    
    with open(filename, 'wb') as f:
        f.write(r3.content)

    #conclude the function
    return 'Finished!'

if __name__== "__main__":
    #kind welcome message
    print("##Welcome to PatPedsClaims!##\n")
    print("Blessed are the cheese-makers.\n")
    
    # enter an appropriate Application ID
    applId= str(input('\nPlease enter a valid Application ID [11666666]: '))
    print(get_claims(applId))

    #wait before closing the app
    time.sleep(1)