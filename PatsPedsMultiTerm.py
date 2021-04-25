# Helper function for PatPeds
# Copyright (C) 2021 Vinz Frauchiger

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or any later version.


from PatsPedsTermDisc import terms_and_disclaimer


def multi_term_disc(list_of_publnos):
    output = []
    for publno in list_of_publnos:
        days, disc = terms_and_disclaimer(publno)

        output.append((publno, days, disc))

    
    print(output)
    return output




if __name__ == "__main__":
    liste =["US6542343","US8883241","US7896841","US8883243", "US8883247"]


    multi_term_disc(liste)