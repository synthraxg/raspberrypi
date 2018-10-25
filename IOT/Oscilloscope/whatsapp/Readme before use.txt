Link: https://iamjagjeetubhi.wordpress.com/2017/09/21/how-to-use-yowsup-the-python-whatsapp-library-in-ubuntu/#step2


Step1: Update your raspberrypi
sudo apt-get update

Step2: Download Dependencies
sudo apt-get install python-dateutil
sudo apt-get install python-setuptools
sudo apt-get install python-dev
sudo apt-get install libevent-dev
sudo apt-get install ncurses-dev

Step3: Download Yowsup Library
git clone git://github.com/tgalal/yowsup.git

Step4: Installing library
cd yowsup
sudo python setup.py install

Step5: Registration on whatsapp
Create New file 'dexMD5.py'
Paste the code written below


####################################################################################################
import sys

import base64

import zipfile

import hashlib



if len(sys.argv) < 2:

    print("Usage: python dexMD5.py <WhatsApp.apk>")

    exit()

else:

    apkFile = sys.argv[1]

try:

    zipFile = zipfile.ZipFile(apkFile,'r')

    classesDexFile = zipFile.read('classes.dex')

    hash = hashlib.md5()

    hash.update(classesDexFile)


    version = classesDexFile.decode("utf-8", errors = 'ignore').partition('App: ')[-1].partition(',')[0]


    print("Version: " + version)

    print("ClassesDex: " + base64.b64encode(hash.digest()).decode("utf-8"));

except Exception as e:

    print(sys.argv[1] + " not found.")


##############################################################################################


Step6: Download the latest version of whatsapp from the link "https://www.whatsapp.com/android/"
and move whatsapp.apk file to the current directory.

Run the command  
python dexMD5.py WhatsApp.apk

you will get output like this
Version: 2.17.344
ClassesDex: OxVSHnBDYNBZmSiYzwF9+A==

Goto yowsup/env/env_android.py
Replace version and _MD5CLASSES with above values
If version is not printed then check it from the site where you have downloaded.

Run
python setup.py build
python setup.py install

Step7: Registration
Run
python yowsup-cli registration --requestcode sms --phone 91xxxxxxxxxx --cc 91 --mcc 222 --mnc 10 -E android
check your MCC and MNC on this site 'https://en.wikipedia.org/wiki/Mobile_country_code'
Replace all the values with your values

You will receive 6digit code.
Now Run 
python yowsup-cli registration --register xxx-xxx --phone 91xxxxxxxxxx --cc 91 -E android
Replace xxx-xxx with your 6digit code.

You should receive output like this
-------------------------------------------------
status: ok
kind: free
pw: xxxxxxxxxxxxxxxxxx= #this is the password
price: ? 55
price_expiration: 1509040085
currency: INR
cost: 55.00
expiration: 4444444444.0
login: 91xxxxxxxxxx
type: new
------------------------------------------------------

here pw is your password.

Step8:
Create new file in yowsup directory with the name 'config'
open file and write 
cc=91 
phone=91xxxxxxxxxx
password=xxxxxxxxxxxxxxxxxx=                     (from the output in the command terminal)

save and close the file.

Step9: Check demo
cd /home/pi/yowsup
yowsup-cli demos --yowsup --config config

You will get prompt 'Type /help for available commands'
Login using 
/L

for sending message 