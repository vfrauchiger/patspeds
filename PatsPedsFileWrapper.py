# PatPedsClaims
# Simple tool to download latest version of complete *file wrapper*
# of an US Patent Application using USPTO Ped
# Author: Vinz Frauchiger
# License: Ypsomed exclusive

import requests
import json
import os

import PySimpleGUI as sg 

sg.theme('Dark Blue 2')



def get_filewrapper(applId_tosearch):
    """This function takes an  application ID of an US Patent
    Application. It uses the PEDS System to get a list of all
    documents present in the filewrapper and supsequently iterates 
    through all pdfDocument Links in order download all documents. 
    The documents are stored in a subfolder named the US Appl.
    number. 
    Format: '121234567'"""

    # Choose location for filewrapper to be saved
    location = sg.popup_get_folder('Please choose location to save the filewrapper:')
    
    #base url
    url_l = "https://ped.uspto.gov/api/queries/cms/"

    #application id
    applId = str(applId_tosearch)
    applId = "".join(char for char in applId if char.isdigit())
    print(applId)

    # query the cms
    r2 = requests.get(url_l+"/"+applId)
    #convert content of repsonse to dict
    resp_l = json.loads(r2.text)

    #create a directory in the current location named the appl. number
    try:
        os.mkdir(location+ '/'+ str(applId))
    except FileExistsError:
        print('Directory exists already!\n')

    #download documents
    for doc in resp_l:
        # create filename for each file
        print(doc['pdfUrl'])
        if  doc['pdfUrl'] != None:
            print(doc['pdfUrl'])
            #create filename incl. path from ./
            filename = location +'/'+ str(applId)+ '/' \
                    + str(doc["mailRoomDate"])[-4:]+'-'+str(doc["mailRoomDate"])[:2] \
                    +str(doc["mailRoomDate"])[2:-5] \
                    +"_"+str(doc["documentDescription"]).\
                        replace(' ','_').\
                        replace('.','').\
                        replace('/', '').\
                        replace(',','').\
                        replace('\'','')+'.pdf'
            print(filename)
            r3 = requests.get(url_l + '/' + doc['pdfUrl'])
            with open(filename, 'wb') as f:
                f.write(r3.content)
        else:
            print('No DocLink avalailable!\n{}'.format(filename))

    print('\nDone!')


if __name__== "__main__":
    application_number = input('Please enter an application number: ')
    get_filewrapper(application_number)
