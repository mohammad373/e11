# e11


import os
import sys
import time
import requests
from colorama import Fore

def __target__():
    os.system("clear")
    print(Fore.RED + """
            ///////////////////
            //////////////////
            /////////////////
            ////////////////
            ///////////////
            //////////////
            /////////////
            ////////////
            ///////////
            //////////
            /////////
            ////////
            ///////
            //////
            /////
            ////
            ///
            //
            /""")
    print(Fore.YELLOW + "\nHeloo , Welcome Back ;)")
    time.sleep(2)
    target = input(Fore.BLUE + "\n[" + Fore.RED + "!" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Pleass Enter Your address Target" + Fore.GREEN + " ==>  ")
    if target == "" or None:
            print(Fore.RED + "\n[!] ~ Error : Your Target Is None Or Not Found ;(")
            time.sleep(0.4)
            sys.exit()

    if not "http" in target or not "https" in target:
        target = "http://" + target
    r1 = target + "/" + "/wp-content/plugins/"
    wp = requests.get(r1)
    if wp.status_code == 404 or wp.status_code == 500:
        try:
            time.sleep(0.5)
            print(Fore.RED + "\n[!] ~ Error : Your Target Is Not Word Press ;(")
            time.sleep(0.5)
            sys.exit()
        except:
            pass
    else:
        time.sleep(0.5)
        print(Fore.GREEN + "\n[+] ~ ok Your Target Is Word Press ;)")
        time.sleep(0.5)
    my_list = ["xmlrpc.php" , "xmlrpc" , "xmlrpc/login" , "xmlrpc/admin"]
    for i in my_list:
        wp2 = target + "/" + i
        r2 = requests.get(wp2)
        if r2.status_code == 404 or r2.status_code == 500:
            print(Fore.RED + "[-]  " + Fore.RED + wp2 + Fore.YELLOW + " > " + Fore.RED + "Not Found ;(")
        else:
            print(Fore.GREEN + "[+]  " + Fore.GREEN + wp2 + Fore.YELLOW + " > " + Fore.GREEN + "Found ;)")
    time.sleep(4)
    print(Fore.BLUE + "\n[*] ~ Good Bay ;)))")
__target__()
