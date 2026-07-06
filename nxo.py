import os
import itertools
import sys
import time

def clear():
    os.system('clear')

def open_github():
    print("\033[1;32m[*] Redirecting to Creator's GitHub: https://github.com/onxx-x143\033[0m")
    time.sleep(1.5)
    os.system('termux-open-url https://github.com/onxx-x143 > /dev/null 2>&1')

def print_banner():
    # Banner in Red Color
    banner = """\033[1;34m
                ⣀⣠⣰⣶⣶⣦⣤⣤⢄⡀           
             ⢀⣴⣯⣶⠿⢿⡿⣿⣿⡍⠻⣷⡌⢆          
            ⢀⡾⣿⣿⣵⡟⣿⠃⠨⣿⣧⣠⣹⡧ ⠡⣄        
            ⢸⣷⣿⣿⢹⠂⢿⣸⣄⢨⡻⣿⣿⣿⣦⣐⣽⣷⣤      
            ⣼⣿⣿⣿⡘⣿⣤⣙⢝⣪⢿⣮⣻⣿⣿⣿⢿⣿⣾⢾⡆	    
           ⣀⢿⣿⣿⣯⠿⠿⠏⠉⢫⡵⣶⣾⣿⣿⣿⣿⣇⠹⣿⡇⢾⡆        
     ⣀⠠⠄⠒⠈⢁⢠⢺⣽⣿⣷⣖⢶⡆   ⠉⢑⣿⣿⣿⣿⣿⣷⣿⢾⡆    
  ⡠⠔⠉    ⡠⣪⣿⣿⣿⣿⣿⣿⡁ ⠤  ⢠⣟⣿⣿⣿⣿⣿⣿⣿⡿⠇    	by onxx-x143 
⢰⠩⠂   ⢀⢠⣪⠋⢹⣿⣿⣿⣿⡿⣿⣿⣦⣄⠙⠁⢘⣿⣿⡿⣿⣿⣿⣿⣿⠇     
⠘⢟⡠  ⠉⠉⠙⡿⣢⠤⠽⣿⣿⣿⣿⣿⣿⣿⣿⡿⠞⡫⠋⠙⠳⣿⠽⠛⠋⠁      
  ⠑⢦⡀    ⡇⠰⡄⠉⠋⠻⠿⠽⡛⡟⢏⡐⠉   ⣀⠟⣹⠂⠤⣤⡀     
    ⠈⢢⣄⠠⢃⡇ ⡇ ⢸   ⠱⠈⠢⢕⡂ ⠒⣚⠡⠾⠋ ⢠ ⠈⠑⢢   
     ⠸⣿⣷⣾⢻ ⡇ ⡸ ⡇  ⢃  ⠈⠉⡡⠂   ⢰⠃⣴⡾ ⡰⣡	IG _insrnx_  
      ⢿⣿⡟⠘⢠⡇ ⡇ ⡇  ⠈⢆ ⠠⠊     ⠁⢀⠟⠁⣴⠁⢿⡀ 
      ⠸⣿⣣⠃⢸ ⢸  ⠁    ⡔        ⡘⢠⡾⠁⡞ ⡇ 
       ⠈⠣⣄⣼ ⣦     ⠠⠘       ⢀⡜⡱⢡⠂⡸  ⠇ 
         ⠙⢿⢠⣸      ⢃      ⢀⣾⣿⢡⠇⢠⠃⣀⣀⢸ 
          ⢸⡜⣿⡄     ⢋⡀    ⢀⣸⣿⣷⠯⢰⣏⣩⣤⣤⣝⡄
           ⡇⢹⣧⢰⠐⡀  ⢸⢡  ⢀ ⡌⣿⣿⠗⠂⠉⢀⣿⣿⣿⠟⠁
           ⠘⡘⣿⡆⢣⠐   ⡇⢃ ⢸⢠⢃⡟⠁ ⡀⠤⡚⠛⠋⠁  
            ⢣⣱⠹⡜⣆ ⠠⡀⠐⡜⣆⢸⡌⣸⠇⡠⠊ ⢀⡇     
             ⢻⡆⢡⠹⣦⣄⠈⢄⡸⢸⣿⣿⡟⠜   ⡸      
              ⠙⠚⠈⠙⠛⠓⠊⠁ ⠙⠛⠛⠒⠊⠉⠑⠁   \033[0m"""
    print(banner)
    print("\033[1;31m" + "="*70)
    print("        PRO PASSWORD I'd - BY ONXX (PYTHON VER)")
    print("        GitHub : https://github.com/onxx-x143")
    print("="*70 + "\033[0m\n")

def make_leet(word):
    leets = {'a': '@', 'i': '1', 's': '$', 'e': '3', 'o': '0'}
    leet_word = word.lower()
    for k, v in leets.items():
        leet_word = leet_word.replace(k, v)
    return leet_word

def loading_animation():
    chars = ["|", "/", "-", "\\"]
    end_time = time.time() + 10  # 10 second animation
    while time.time() < end_time:
        for char in chars:
            sys.stdout.write(f'\r\033[1;34m[*] Processing Passwords in Background... {char}\033[0m')
            sys.stdout.flush()
            time.sleep(0.1)
    print("\r\033[1;32m[*] Processing Passwords in Background... Done!      \033[0m\n")

def generate_passwords():
    clear()
    print_banner()
    open_github() 
    
    print("\n\033[1;32m[+] Please enter Target Details (Leave blank if unknown):\033[0m\n")
    
    username = input("\033[1;32m[?] Username/First Name : \033[0m").strip()
    father = input("\033[1;32m[?] Father's Name       : \033[0m").strip()
    mother = input("\033[1;32m[?] Mother's Name       : \033[0m").strip()
    pet = input("\033[1;32m[?] Pet's Name          : \033[0m").strip()
    dob = input("\033[1;32m[?] Date of Birth (ex: DD/MM/YYY) : \033[0m").strip()

    print()
    
    passwords = set()
    inputs = [username, father, mother, pet]
    base_words = [w for w in inputs if w]
    words_variations = []
    
    for word in base_words:
        words_variations.extend([word.lower(), word.upper(), word.capitalize(), make_leet(word)])
        
    dob_parts = []
    if dob:
        dob_parts.append(dob)
        if len(dob) == 8 and dob.isdigit():
            dob_parts.extend([dob[:2], dob[2:4], dob[4:], dob[:4]])
        elif len(dob) == 4 and dob.isdigit():
            dob_parts.append(dob)

    common_numbers = ['123', '1234', '12345', '123456', '007', '143', '111', '999', '12', '11', '69', '100', '0000']
    symbols = ['@', '#', '$', '_', '&']
    
    for word in words_variations:
        passwords.add(word)
        for num in common_numbers:
            passwords.add(word + num)
            for sym in symbols:
                passwords.add(word + sym + num)
        for d in dob_parts:
            passwords.add(word + d)
            for sym in symbols:
                passwords.add(word + sym + d)
                passwords.add(sym + word + d)
                
    for w1, w2 in itertools.permutations(base_words, 2):
        for v1 in [w1.lower(), w1.capitalize(), make_leet(w1)]:
            for v2 in [w2.lower(), w2.capitalize(), make_leet(w2)]:
                passwords.add(v1 + v2)
                for sym in symbols[:3]:
                    passwords.add(v1 + sym + v2)

    final_passwords = {pwd for pwd in passwords if 6 <= len(pwd) <= 20}

    loading_animation()

    filename = "password.txt"
    try:
        with open(filename, 'w') as f:
            for pwd in final_passwords:
                f.write(pwd + '\n')
        print(f"\033[1;32m[✔] {len(final_passwords)} Unique Passwords Successfully Saved!\033[0m")
        print(f"\033[1;32m[✔] Check File : {os.path.abspath(filename)}\033[0m\n")
    except Exception as e:
        print(f"\n\033[1;31m[!] Error saving file: {e}\033[0m")

if __name__ == "__main__":
    try:
        generate_passwords()
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Tool Stopped by User.\033[0m")
