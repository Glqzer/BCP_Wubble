#David Wang, dwang117

import random


def encode_sequence(message):
    
    """Inputting a string of characters, returns the sequence of DNA bases that contain the same information as the string"""
    
    message_characters = list(message)
    integer_list = []
    for character in message_characters:
        integer_list.append(ord(character))
    
    #Create the binary representations for each character
    binary_representations = []
    for integer in integer_list:
        binary_representations.append(format(integer, '08b'))
        
    #Split the binary representations into groups of 2
    split_binary = []
    for binary in binary_representations:
        split_binary.append([binary[i:i+2] for i in range(0, len(binary), 2)])
    
    #Construct the final message using the split binary representations and the dictionary for the DNA sequencing
    final_message = ""
    dictionary = {"00":"A", "01":"T", "10":"C", "11":"G"}
    for character in split_binary:
        for binary in character:
            final_message += dictionary[binary]
    
    return final_message

def decode_sequence(message):
    
    """Inputting a DNA sequence, returns the English text equivalent of its information"""
    
    message_characters = list(message)
    binary_representation = ""
    
    #Create the dictionary used to decode the message
    dictionary = {"A":"00", "T":"01", "C":"10", "G":"11"}
    for character in message_characters:
        binary_representation += dictionary[character]
        
    #Split the full binary representation into a list of groups of 8 for character conversion
    binary_grouping = [binary_representation[i:i+8] for i in range(0, len(binary_representation), 8)]
    
    #Convert each group of binary characters into integers, and then into characters for the message
    final_message = ""
    for binary in binary_grouping:
        final_message += chr(int(binary, 2))

    return final_message

def encrypt_decrypt(message, key = "CAT"):
    
    """Given required argument message to be encrypted, and an optional argument for the key, return the encrypted sequence using XOR conversion"""
    
    changed_letters = list(message)
    key_list = list(key)
    
    #Cycle through the key and encrypt all characters
    for letter in key_list:
        for i in range(len(changed_letters)):
            changed_letters[i] = xor_conversion(letter, changed_letters[i])
            
    #Return the encrypted message
    return ''.join(changed_letters)

def xor_conversion(char_1, char_2):
    
    """Helper Function for encrypt_decrypt, input 2 characters and outputs the XOR operation result"""
    
    if (char_1 == char_2):
        return "A"
    
    elif (char_1 == "A"):
        return char_2
    
    elif (char_2 == "A"):
        return char_1
    
    elif ((char_1 == "C" and char_2 == "T") or (char_1 == "T" and char_2 == "C")):
        return "G"
    
    elif ((char_1 == "G" and char_2 == "T") or (char_1 == "T" and char_2 == "G")):
        return "C"
    
    elif ((char_1 == "G" and char_2 == "C") or (char_1 == "C" and char_2 == "G")):
        return "T"
    
    else:
        return
    
def synthesizer_helper(character):
    
    """Given a DNA sequence character, synthesize it using the probabilities given and a random integer, and output the synthesized character"""
    
    #100% Chance for A Synthesis
    if (character == 'A'):
        return 'A'
    
    probability = random.random() * 100
    
    #90% Chance for T Synthesis
    if (character == 'T'):
        if (probability < 90):
            return 'T'
        if (probability < 92):
            return 'G'
        if (probability < 95):
            return 'C'
        if (probability < 100):
            return 'A'
        
    #97% Chance for C Synthesis
    if (character == 'C'):
        if (probability < 97):
            return 'C'
        if (probability < 98):
            return 'G'
        if (probability < 99):
            return 'T'
        if (probability < 100):
            return 'A'
        
    #95% Chance for G Synthesis
    if (character == 'G'):
        if (probability < 95):
            return 'G'
        if (probability < 97):
            return 'C'
        if (probability < 99):
            return 'T'
        if (probability < 100):
            return 'A'
    return

def synthesizer(sequence):
    
    """Given an input DNA sequence, simulates the manufacturing process using the given probabilities and returns the sequence of DNA synthesized by the robot"""
    list_sequence = list(sequence)
    final_sequence = ""
    for character in list_sequence:
        final_sequence += synthesizer_helper(character)
    
    return final_sequence

def error_count(sequence_1, sequence_2):
    
    """Given two DNA sequences, returns the number of mismatches found between them"""
    
    list_1 = list(sequence_1)
    list_2 = list(sequence_2)
    error_count = 0
    
    min_length = min(len(list_1), len(list_2))
    
    # Iterate through the elements up to the length of the shorter list
    for i in range(min_length):
        # Compare elements and increment the counter if different
        if (list_1[i] != list_2[i]):
            error_count += 1

    # Add the remaining elements from the longer list
    error_count += abs(len(list_1) - len(list_2))
            
    return error_count

def redundancy(n, sequence):
    
    """Takes as input an integer n and a string to synthesize, in that order, obtains n copies of the synthesized DNA, then compares all n copies to find the correct letter in each position, and returns the error-corrected string."""
    
    list_sequences = []
    list_split_sequences = []
    for i in range(n):
        list_sequences.append(synthesizer(sequence))
    
    for sequence in list_sequences:
        list_split_sequences.append(list(sequence))
        
    final_sequence = ""
    
    for i in range(len(sequence)):
        a_count = 0
        c_count = 0
        g_count = 0
        t_count = 0
        for sequence_list in list_split_sequences:
            if (sequence_list[i] == 'A'):
                a_count += 1
            if (sequence_list[i] == 'C'):
                c_count += 1
            if (sequence_list[i] == 'G'):
                g_count += 1
            if (sequence_list[i] == 'T'):
                t_count += 1
        correct_letter = max(a_count, c_count, g_count, t_count)
        if (correct_letter == a_count):
            final_sequence += 'A'
        if (correct_letter == c_count):
            final_sequence += 'C'
        if (correct_letter == g_count):
            final_sequence += 'G'
        if (correct_letter == t_count):
            final_sequence += 'T'

    return final_sequence
    
    

        
    