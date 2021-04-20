import pandas as pd

import PySimpleGUI as sg 

from PatsPedsMultiTerm import multi_term_disc


def list_processor(filename):
    df = pd.read_excel(filename)

    publno_list = df['PN'].tolist()

    publno_list = [no for no in publno_list if no[:2].upper()=='US']

    # print(publno_list)

    result = multi_term_disc(publno_list)

    dfr = pd.DataFrame(result, columns =['Publication', 'Term Extension', 'Terminal Disclaimer'])



    return dfr



    



if __name__ == "__main__":

    filename = sg.popup_get_file("Get File for processing: ")
    print(filename)
    resultdf = list_processor(filename)

    savename = sg.popup_get_file("Choose Location and Filename for Output!", default_extension='xlsx', save_as=True)
    


    resultdf.to_excel(savename)

    print('Done!')