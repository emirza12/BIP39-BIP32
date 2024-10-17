import random
print(random.getrandbits(128)
      
      
      
    
    )


def import_mnemonic():
    mnemonic_phrase = input("Enter your seed phrase: ")
    # Split the mnemonic phrase into words
    words = mnemonic_phrase.split()
    
    # Validate the length of the mnemonic phrase
    if len(words) != 12:
        print("Error: Invalid number of words in mnemonic phrase. It must be 12 words.")
        return
    
    binary_seed = ""
    for word in words:
        # Validate if each word is in the BIP39 word list
        if word not in bip39_words:
            print("Error: The word '" + word + "' is not in the BIP39 word list.")
        index = bip39_words.index(word)
        # Convert index to binary, padding to 11 bits
        binary_seed += ('0' * (11 - len(bin(index)[2:]))) + bin(index)[2:]  # Add leading zeros
        
     # Convert binary seed to integer
    seed_int = int(binary_seed, 2)  
    # Convert the seed integer to hexadecimal
    seed_hex = hex(seed_int)[2:]  
    
    print("Imported seed in hex:", seed_hex)

# Confirm if the generated seed matches the imported seed
    if random_seed == import_mnemonic():
        print("The generated seed and the imported seed are identical.")
    else:
        print("The generated seed and the imported seed are different.")

    print(f"Seed derived from the imported mnemonic: {import_mnemonic()}")