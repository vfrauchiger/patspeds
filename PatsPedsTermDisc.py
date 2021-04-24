import requests
import json

from PatsPedsPublNoTreat import treat_publno

def terms_and_disclaimer(no):

    number, tosearch = treat_publno(no)

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
            else:
                continue
        if not disclaimer:
            print('No Terminal Disclaimer Found!')
        
        return total_delay, disclaimer
        
    except:
        return -1, False


if __name__ == "__main__":
    no = input("Please provide a publication number: ")
    print(terms_and_disclaimer(no))
