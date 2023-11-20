# uncompyle6 version 3.9.0a1
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.4 (main, Mar 24 2022, 13:07:27) [GCC 11.2.0]
# Embedded file name: sitegrabber.py
# Compiled at: 2020-11-29 02:07:33
import re, requests
from colorama import Fore
banner = '\n\x1b[36;1m\n $$$$$$\\                     $$\\                 $$\\   $$\\               \n$$  __$$\\                    $$ |                \\__|  $$ |              \n$$ /  \\__| $$$$$$\\  $$$$$$\\  $$$$$$$\\   $$$$$$$\\ $$\\ $$$$$$\\    $$$$$$\\  \n$$ |$$$$\\ $$  __$$\\ \\____$$\\ $$  __$$\\ $$  _____|$$ |\\_$$  _|  $$  __$$\\ \n$$ |\\_$$ |$$ |  \\__|$$$$$$$ |$$ |  $$ |\\$$$$$$\\  $$ |  $$ |    $$$$$$$$ |\n$$ |  $$ |$$ |     $$  __$$ |$$ |  $$ | \\____$$\\ $$ |  $$ |$$\\ $$   ____|\n\\$$$$$$  |$$ |     \\$$$$$$$ |$$$$$$$  |$$$$$$$  |$$ |  \\$$$$  |\\$$$$$$$\\ \n \\______/ \\__|      \\_______|\\_______/ \\_______/ \\__|   \\____/  \\_______|\n                                                                                                                       \n\t Site Grabber From Date\n\t Max Page : 15\n\t [ C0ded by #No_Identity ]\x1b[36;1m\n'
print banner
tahun = raw_input('root@youez:~# tahun : ')
bulan = raw_input('root@youez:~# bulan : ')
tanggal = raw_input('root@youez:~# tanggal : ')
for i in range(15):
    i = int(i) + 1
    print 'Halaman: ' + str(i)
    x = requests.get('https://www.cubdomain.com/domains-registered-by-date/' + str(tahun) + '-' + str(bulan) + '-' + str(tanggal) + '/' + str(i) + '')
    r = re.findall('">(.+?)</a>\n</div>', x.text)
    sv = open('hasil-grab.txt', 'a')
    for z in r:
        if '/' in z or '=' in z or 'Download Extension' in z:
            pass
        else:
            print z
            sv.write(z + '\n')

    print 'Total Domains: ' + str(len(r))
# okay decompiling grabsite.pyc
