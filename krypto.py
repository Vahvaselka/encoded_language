import string
def action():
   
    while True: 
        print('\nWhat would you like to do? ') #menyn för att välja vad användaren vill göra
        choice = input("e: encrypt\nd: decrypt\nb: break\nq: quit\n>")
        if choice.lower() == 'q': # val om användaren vill sluta 
             break
        elif choice.lower() == 'd':
            key = get_key() # anropar funktionen som ger key
            message = get_message() # anropar funktionern som ger meddelanden
            plaintext = decrypt(message, key) # anropar funktionen som dekrypterar med givna parameter
            print("The decrypted message is %s" %plaintext ) # printar ut dekrypterad meddelanden
        elif choice.lower() == 'e':
            key = get_key() # line 10
            message = get_message() #line 11
            cryptotext = encrypt(message, key) # anropar funktionen som krypterar meddelanden med givna parameter
            print("The encrypted message is %s" %cryptotext )
        elif choice.lower() == 'b':
            message=get_message() #line 11
            break_crypt(message) #anropar funktionen som bryter krypterad meddelanden
                          
def get_key(): #funktion som frågar användaren att vad hen användar för nyckel i enkryptering samt dekryptering
    unacceptableinputKey=True #felhantering
    while unacceptableinputKey:
        try:
            key=int(input('Input the key (an integer value): '))
        except ValueError:
            print('Choose an INTEGER')
        else:
            unacceptableinputKey=False
            return key
    

def get_message(): # funktion sopm frågar användaren vad hen har för meddelande som ska krypteras/ dekrypteras eller brytas
    message=input('Enter the message: ')
    return message
    
    
def encrypt(message,key): #Funktion som enkrypterar meddelanden med ett givet värde(key) från original bokstaven
    encrypted_message=""
    for character in message: # går igenom varje tecken i message 
        if character in string.ascii_uppercase: # kollar om det finns stora bokstäver
            encrypted_bokstav = chr(((ord(character)+ key-65)%26)+65) #krypterar stora bokstäver 
            encrypted_message+=encrypted_bokstav # adderar krypterad bokstäver till krypterad meddelanden tills meddelande är färdig
        elif character in string.ascii_lowercase: # kollar om det finns lilla bokstäver
            encrypted_bokstav = chr(((ord(character)+ key-97)%26)+97) #krypterar lilla bokstäver
            encrypted_message+=encrypted_bokstav #samma som line 45
        else:
            encrypted_message+=character  #om tecken är inte ett bokstav så adderas det till enkrypterad meddelanden som det är    
    return encrypted_message 

def decrypt(message, key): #Funktion som dekrypterar meddelanden med ett givet värde(key) ta bort det från krypterad värde4
    decrypted_message=""
    for encrypted_character in message: # line 42
        if encrypted_character in string.ascii_uppercase: #line 43
            decrypted_bokstav = chr(((ord(encrypted_character)- key-65)%26)+65) # dekrypterar stora bokstäver
            decrypted_message+=decrypted_bokstav # adderar dekrypterad bokstäver till krypterad meddelanden tills meddelande är färdig
        elif encrypted_character in string.ascii_lowercase: # line 46
            decrypted_bokstav = chr(((ord(encrypted_character)- key-97)%26)+97) # dekrypterar lilla bokstäver
            decrypted_message+=decrypted_bokstav # line 58
        else:
            decrypted_message+=encrypted_character #om tecken är inte ett bokstav så adderas det till dekrypterad meddelanden som det är
    return decrypted_message

def break_crypt(message): #funktion som bryter kryptering genom att visa alla olika alternativ 
    for key in range(26): # visar alla 26 alternativ eftersom det finns 26 bokstav som ska kollas igenom
        decrypted_message=decrypt(message, key) # anropar dekrypteringsfunktionen och testar varje key i det
        print("Key "+str(key)+ ": ",decrypted_message) # printar alla alternativ så att användaren kan manuellt granska dom

action() #anropar funktionen för att det ska köras