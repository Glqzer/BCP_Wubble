#David Wang, dwang117
#Creating encryption list
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_list = list(alphabet) 

#The User Interface and Dialog
encrypted_message = input("Enter the encrypted message: ")
encrypted_message_list = list(encrypted_message)

#Decryption
final_message = ""
for letter in encrypted_message_list:
    if letter in alphabet_list:
        final_message += alphabet_list[25 - alphabet_list.index(letter)]
    else:
        final_message += letter
        
#Final Output
print("The plaintext message is:", final_message)


    
