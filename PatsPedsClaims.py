# PatPedsClaims
# Simple tool to download latest version of patent claims
# of an US Patent Application using USPTO Ped
# Author: Vinz Frauchiger

# Copyright (C) 2021 Vinz Frauchiger

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or any later version.


# imports
import datetime
import json
import time

import PySimpleGUI as sg
import requests


#print(os.environ)

def get_claims(applId, publno="NoNo"):
    """This function takes an application ID of an US Patent Application saves a pdf with the
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

    if publno == "NoNo":
        filewopath = str(last_claims[0]['mailRoomDate'].strftime('%Y_%m_%d') +'_'+applId + '_claims.pdf')
    else:
        filewopath = str(last_claims[0]['mailRoomDate'].strftime('%Y_%m_%d') +'_'+applId + '_US'+publno+'_claims.pdf')
    print(filewopath)

    location = sg.popup_get_folder('Please choose location to save the claims:')

    filename = location + '/' + filewopath


    
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