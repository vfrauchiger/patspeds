"""
Wrapper and helper for PatsPedsClaims

Takes Publication Numbers. 
"""



import requests
import json

import PatsPedsClaims as pdc



def get_appl(no, go_back='full'):
    """takes a publication number or a patent number and checks its application number at PEDS.
    Return the application number as string
    
    publication numbers : US20120123456; US2016158441

    patent numbers:  US1234567, US12345678
    
    
    """


    number = str(no).strip()
    # if no number is provided the function is exited with code 0
    if no == '':
        return 0

    #remove Country Code
    if number[:2].upper() == 'US':
        number = number[2:]
    elif number[0].isdigit():
        pass
    else:
        print('this is not a US number!')
        #exit function with code 1
        return 1
    print('With removed CC: {}'.format(number))
    
    #remove Kind Code
    if number[-2].isalpha():
        number= number[:-2]
    else:
        pass
    
    #remove whitespace
    number = number.strip()
    print('With removed KD: {}'.format(number))

    number = number.replace('/', '').replace(' ', '')

    print('with removed characters and whitespace: {}'.format(number))

    if len(number) == 7:
        print('{} is a patent'.format(number))
        tosearch = "patentNumber"
    elif len(number) == 8:
        print('{} is a young patent'.format(number))
        tosearch = "patentNumber"
    elif len(number) == 10:
        print('{} is a short format publication'.format(number))
        number = number[:4]+'0'+number[4:]
        number = 'US'+ number +"A1"
        tosearch = "appEarlyPubNumber"
    elif len(number) == 11:
        print('{} is a USPTO format publication'.format(number))
        tosearch = "appEarlyPubNumber"
        number = 'US'+ number +"A1"
    
    # use the extracted number to fetch the publication number
    url = "https://ped.uspto.gov/api/queries"
    payload = { \
                "searchText": tosearch +":("+str(number)+")", \
                "fl":"*", \
                "mm":"20", \
                "qf":"appEarlyPubNumber applId appLocation appType appStatus_txt appConfrNumber appCustNumber appGrpArtNumber \
                    appCls appSubCls appEntityStatus_txt patentNumber patentTitle primaryInventor firstNamedApplicant appExamName \
                    appExamPrefrdName appAttrDockNumber appPCTNumber appIntlPubNumber wipoEarlyPubNumber pctAppType firstInventorFile \
                    appClsSubCls rankAndInventorsList", \
                "facet":"false", \
                "sort":"applId asc",\
                "start":"0"\
                }
    response = requests.post(url, json=payload)
    doc_text =json.loads(response.text)["queryResults"]['searchResponse']['response']['docs'][0]
    print(doc_text)
    total_delay = '0'
    try: 
        # Get Patent Term Extension in Days
        total_delay = json.loads(response.text)["queryResults"]['searchResponse']['response']['docs'][0]['totalPtoDays']
        print("The Patent Term Extension [d]: {}".format(total_delay))
        
        # Get all transaction from within the file
        transactions =json.loads(response.text)["queryResults"]['searchResponse']['response']['docs'][0]['transactions']
        # Disclaimer is set to False as long no Terminal Disclaimed is found
        disclaimer = False
        # iterate through all transactions
        for element in transactions:
            if element['code'] == "DIST":
                print(element)
                # as a Terminal Disclaimer is found the Value is set to True
                disclaimer = True
        if disclaimer == False:
            print('No Terminal Disclaimer Found!')
        if go_back =='delay':
            # if only extension and disclaimer are requested, the function is exited with return values
            return total_delay, disclaimer
        else:
            pass
    except:
        pass
    
    applId = json.loads(response.text)["queryResults"]['searchResponse']['response']['docs'][0]['applId']
    print('The application ID of the searched publication or patent number: {} \n'.format(applId))
    pdc.get_claims(applId, str(number))
    return total_delay

if __name__== "__main__":
    
    
    status = 1

    while status == 1:
        no = str(input('Please enter *US* publ. or patent number: '))
        status = get_appl(no)
