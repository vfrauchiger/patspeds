## Description of PatsPedsTools (Wrapper) ##

### Functions ###

_PatsPedsGUI.py_: **Top Level App with GUI** for *all* tools

_PatsPedsClaims.py_: Takes an appl. Id and download the latest claims (cli)

_PatsPedsClaimsWrapper.py_: Takes a pre-grant publication number or a patent number and 
returns on the cli the according term extension days. But used from PatsPedsGUI it also may return
the latest claims or the combination of term extension days and presence of a terminal
disclaimer (True or False)

_PatsPedsFileWrapper.py_: Takes an application ID and download the **full file wrapper** from USPTO

PatsPedsListProcessorTerm.py: 
PatsPedsMultiTerm.py
PatsPedsPublNoTreat.py
PatsPedsTermDisc.py

- Download latest version of claims available at the USPTO
- Discriminate between US application numbers, publication number, and patent numbers
- If wanted: save whole filewrapper

*PatsPedsClaims.py*
Takes an application Id

*PatsPedsClaimsWrapper.py* 
Takes  a pre-grant publication or patent number. Morover this script uses **PatsPedsClaims.py** in order to download the claims.


*PatsPedsFileWrapper.py*
Takes an application Id and downloads the whole filewrapper for the application. 

*PatsPedsGUI.py*
Is a very simple GUI for the tools.

![Alt text](./PatsPedsGUI.svg)


April 24, 2021  

(c) Vinz Frauchiger
