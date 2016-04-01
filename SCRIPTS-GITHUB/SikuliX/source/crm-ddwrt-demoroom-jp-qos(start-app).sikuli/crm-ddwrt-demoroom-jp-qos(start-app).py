#crm-image-repository #####
#Browser
crm_address = ("crm_address.png") 
crm_close = ("crm_close.png") 

import time
import datetime
import shutil
import javax.swing.JOptionPane as JOP
import random 
import string

crmfile = open("C:\\SCRIPTS\\parameters\\app\\crm_app.txt")
crm = crmfile.read()

urlfile = open("C:\SCRIPTS\parameters\url\url_ddwrt_demoroom_jp.txt")
url = urlfile.read()

chars = "".join( [random.choice(string.letters) for i in xrange(10)] )

localtime = time.localtime(time.time())
timenow = str(datetime.datetime.now()).replace(":", "_")
timestring = time.strftime ('%Y_%m_%d_-_%H.%M.%S')

openApp(crm)
wait(1)
click(crm_address)
wait(1)
paste(url)
wait(1)
type(Key.ENTER)
wait(1)
wait(("nat-qos.png"), 20)
click("nat-qos.png")
if exists("login.png"):
    click("login.png")
wait(2)
click("qos.png")