#David Wang, dwang117
#Open File, Add Lines, Close File
text_file = open("pride_prejudice.txt", 'r', encoding='utf-8-sig')
text_list = []
for line in text_file:
    text_list.append(line.split()) #Sets up list of words

text_file.close()


#Setup Lists and Variables
full_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
full_alphabet_list = list(full_alphabet)

lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
upper_alphabet = lower_alphabet.upper()
lower_alphabet_list = list(lower_alphabet)
upper_alphabet_list = list(upper_alphabet)


#Count Total File Characters
total_text_characters = 0
for line in text_list:
    for word in line:
        for char in word:
            if char in full_alphabet_list:
                total_text_characters += 1
            

#Calculate likelihood values P
likelihood_values = []
for i in range(26):
    character_count = 0
    for line in text_list:
        for word in line:
            for char in word:
                if (char == lower_alphabet_list[i] or char == upper_alphabet_list[i]):
                    character_count += 1
    likelihood_values.append(character_count/total_text_characters)
    

#The User Dialog and Interface
encrypted_message = input("Enter the encrypted message: ")
encrypted_message_list = list(encrypted_message)
message_length = len(encrypted_message_list)

#Create Shifting Algorithm
def shift(seq, n):
    return seq[(26-n):]+seq[:(26-n)]

#Calculate chi score for all shifts
chi_scores = []
for i in range(26):
    encryption = shift(lower_alphabet_list, i)
    shifted_message = []
    chi_key = 0
    
    for letter in encrypted_message_list: #Creating Shift
        if letter in lower_alphabet_list:
            shifted_message.append(encryption[lower_alphabet_list.index(letter)])
        else:
            shifted_message.append(letter)
    
    for j in range(26): #Chi-Score Calculation
        letter_count = 0
        for char in shifted_message:
            if (char == lower_alphabet_list[j]):
                letter_count += 1
        chi_key += ((letter_count - likelihood_values[j] * message_length) ** 2) / (likelihood_values[j] * message_length) #The Chi-Score Formula
        
    chi_scores.append(chi_key)
    
    
#Find minimum chi score
shifted_by = chi_scores.index(min(chi_scores))
encryption = shift(lower_alphabet_list, shifted_by)

#Output result
final_message = ""
for letter in encrypted_message_list:
    if letter in encryption:
        final_message += encryption[lower_alphabet_list.index(letter)]
    else:
        final_message += letter
        
print("The plaintext message is:", final_message)

