# @CODE_CO :) | TELEGRAM: @CODE_CO | GITHUB: CODE-CO |----------------------------------------------
#---------------------------------------------------------------------------------------------------
import os, re, requests
from os.path import exists
from getpass import getuser
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
#---------------------------------------------------------------------------------------------------
os.system("CLS" if os.name == "nt" else "clear")
URL, WHICH_MODE = input("ENTER A WEBSITE TO EXTRACT THE URL'S: "), input("\nINDEX | SITE | LINKS: ").upper()
LIST_OF_LINKS, BOOLEAN = list(), False
#---------------------------------------------------------------------------------------------------
def REQUESTS_METHOD():
    global LINKS
    try:
        URL_REQUEST = requests.get(URL).text
        LINKS = list(map(lambda X: X.get("href"), BeautifulSoup(URL_REQUEST, "html.parser").find_all(r"a")))
    except:
        print("\nCHECK YOUR INTERNET CONNECTION OR URL !\n")
        exit() 
#---------------------------------------------------------------------------------------------------
def URLLIB_METHOD():
    global LIST_OF_LINKS
    print("\nWITH URLLIB METHOD !!!")
    try:
        URL_REQUEST = Request(URL)
        WEBPAGE = urlopen(URL_REQUEST).read()
        LINKS = BeautifulSoup(WEBPAGE, "html.parser").find_all(r"a")
        try:
            LINKS = list(map(lambda X: X.get("href"), LINKS))
        except:
            pass
    except:
        print("\nCHECK YOUR INTERNET CONNECTION OR URL !\n")
        exit()
    LIST_OF_LINKS = LINKS
#---------------------------------------------------------------------------------------------------
def PRINT_LIST_OF_LINKS():
    print("\n")
    for i, o in enumerate(LIST_OF_LINKS, start= 0):
        print(str(i) + " - ( " + str(o) + " )")
#---------------------------------------------------------------------------------------------------
def MAKE_LIST_OF_LINKS():
    global LIST_OF_LINKS
    if WHICH_MODE == "INDEX":
        REQUESTS_METHOD()
        try:
            LIST_OF_LINKS = list(map(lambda X: URL + X, LINKS[1:]))
        except:
            pass
    elif WHICH_MODE == "SITE":
        REQUESTS_METHOD()
        SEASON, QUALITY = input("\nWHICH SEASON (EXAMPLE S01): ").upper(), input("\nWHICH QUALITY DO YOU WANT (EXAMPLE 720P): ").upper()
        for LINK in LINKS:
            try:
                if SEASON[0] + SEASON[2] in LINK.upper() or SEASON in LINK.upper():
                    if QUALITY in LINK.upper() or QUALITY[:-1] in LINK.upper():
                        LIST_OF_LINKS.append(LINK)
            except:
                pass
    elif WHICH_MODE == "LINKS":
        URLLIB_METHOD()
    else:
        print("WRONG !")
#---------------------------------------------------------------------------------------------------
def PASS_TO_INTERNET_DOWNLAOD_MANAGER():
    global BOOLEAN
    BOOLEAN = True
    TXT_FILE()
    IDM_PATH = ["C:/Program Files (x86)/Internet Download Manager", "/home/{0}/.wine/drive_c/Program Files (x86)/Internet Download Manager".format(getuser())]
    for i in IDM_PATH:
        if exists(i) == True:
            IDM_PATH = i
    while exists(IDM_PATH[0]) == False:
            IDM_PATH = input("\nIDM PATH: ")
    os.chdir(IDM_PATH)
    for i in LIST_OF_LINKS:
        os.system("IDMan.exe /n /d {0}" if os.name == "nt" else "wine IDMan.exe /n /d {0}".format(i))
#---------------------------------------------------------------------------------------------------
def DOWNLOAD_FROM():
    global LIST_OF_LINKS
    LIST_OF_LINKS = LIST_OF_LINKS[int(input("\nSTART: ")):(int(input("\nEND: "))) + 1]
#---------------------------------------------------------------------------------------------------
def COUNTER_DOWNLOAD():
    global LIST_OF_LINKS
    COUNTER = int(input("\nSET COUNTER NUMBER: 0 OR 1...: "))
    ADD_COUNTER = int(input("\nAND PLEASE ENTER HOW MANY YOU WANT TO ADD TO THE COUNTER VALUE EACH TIME: "))
    TEMP_LIST = list()
    try:
        for i in LIST_OF_LINKS:
            i = i # JUST FOR SOLVE (UNUSED VARIABLE 'i') WARNING :)
            TEMP_LIST.append(LIST_OF_LINKS[COUNTER])
            COUNTER += ADD_COUNTER
    except:
        pass
    LIST_OF_LINKS = TEMP_LIST
#---------------------------------------------------------------------------------------------------
def SELECT():
    global LIST_OF_LINKS
    TEMP_LIST, INDEX = list(), str()
    print()
    while INDEX != "END":
        INDEX = input("ENTER THE LINK NUMBER: ").upper()
        if INDEX == "END":
            pass
        else:
            if INDEX.isdigit() == True:
                if int(INDEX) < len(LIST_OF_LINKS):
                    if LIST_OF_LINKS[int(INDEX)] not in TEMP_LIST:
                        TEMP_LIST.append(LIST_OF_LINKS[int(INDEX)])
                    else:
                        print("\nYOU HAVE SELECTED THIS LINK !\n")
                else:
                    print("\nWRONG NUMBER !\n")
            else:
                print("\nWRONG !\n")
    LIST_OF_LINKS = TEMP_LIST
#---------------------------------------------------------------------------------------------------
def DELETE():
    global LIST_OF_LINKS
    TEMP_LIST, LIST, INDEX = list(), list(), str()
    print()
    while INDEX != "END":
        INDEX = input("ENTER THE LINK NUMBER: ").upper()
        if INDEX == "END":
            pass
        else:
            if INDEX.isdigit() == True:
                if int(INDEX) < len(LIST_OF_LINKS):
                    if LIST_OF_LINKS[int(INDEX)] not in TEMP_LIST:
                        TEMP_LIST.append(LIST_OF_LINKS[int(INDEX)])
                    else:
                        print("\nYOU HAVE DELETED THIS LINK !\n")
                else:
                    print("\nWRONG NUMBER !\n")
            else:
                print("\nWRONG !\n")
    for i in LIST_OF_LINKS:
        if i not in TEMP_LIST:
            LIST.append(i)
    LIST_OF_LINKS = LIST
#---------------------------------------------------------------------------------------------------
def TXT_FILE():
    with open("LINKS.TXT", "a") as TXT_FILE:
        TXT_FILE.write("------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        for i in LIST_OF_LINKS:
            TXT_FILE.write(i + "\n")
    print("\nTXT FILE IS DONE.")
#---------------------------------------------------------------------------------------------------
MAKE_LIST_OF_LINKS()
#---------------------------------------------------------------------------------------------------
while BOOLEAN == False:
    if LIST_OF_LINKS == []:
        URLLIB_METHOD()
    PRINT_LIST_OF_LINKS()
    DOWNLOAD_MODE = input("\nDOWNLOAD MODES (FROM / COUNTER / SELECT / DELETE / DOWNLOAD): ").upper()
    if DOWNLOAD_MODE == "DOWNLOAD":
        PASS_TO_INTERNET_DOWNLAOD_MANAGER()
    elif DOWNLOAD_MODE == "FROM":    
        DOWNLOAD_FROM()
    elif DOWNLOAD_MODE == "COUNTER":
        COUNTER_DOWNLOAD()
    elif DOWNLOAD_MODE == "SELECT":
        SELECT()
    elif DOWNLOAD_MODE == "DELETE":
        DELETE()
    elif DOWNLOAD_MODE == "LINKS":
        PRINT_LIST_OF_LINKS()
    else:
        print("\nWRONG !")