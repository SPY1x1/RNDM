import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from SpY64 import key_chack
 
        key_chack()
 
 
 
elif bit == "32bit":
 
        print("   your device is 32 bit ")
        
        print("   32 bit will update soon")
        
        os.system("am start https://www.facebook.com/SPY1x1/")
        
        exit()
 
 
 
