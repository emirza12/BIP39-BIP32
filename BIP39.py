from BIP39_words import bip39_words
import random
import hashlib 
from hashlib import pbkdf2_hmac 
import hmac


# Function to generate a seed with a checksum from a random seed
def seed_and_checksum(random_seed):  
    # Convert the random seed to bytes (16 bytes)
    random_seed_bytes = random_seed.to_bytes(16, byteorder='big')  
    
    # Compute SHA256 hash of the seed bytes
    sha256_hash = hashlib.sha256(random_seed_bytes).digest()  
    
    # Extract the first 4 bits (1/2 byte) of the hash as the checksum
    checksum = sha256_hash[0] >> 4  
    
    # Shift the seed left by 4 bits and combine with checksum
    seed_with_checksum = (int.from_bytes(random_seed_bytes) << 4) | checksum  
    
    # Convert to hex and remove the '0x' prefix
    hex_seed = hex(seed_with_checksum)[2:]  
    
    # Return the seed combined with the checksum in hex
    return hex_seed  




# Function to convert the seed into a mnemonic phrase
def mnemonic_seed():

    # Convert hex to binary and remove '0b'
    binary_seed = bin(int(seed_and_checksum(random_seed), 16))[2:]  
    
    # Ensure the length of the binary seed is a multiple of 11
    while len(binary_seed) % 11 != 0:  
        # Add leading zero to the binary seed
        binary_seed = '0' + binary_seed  
    
    # Create 11-bit chunks of the binary seed
    chunks = [binary_seed[i:i+11] for i in range(0, len(binary_seed), 11)]  

    mnemonic = []  
    # Convert each 11-bit chunk into a word
    for chunk in chunks:
        index = int(chunk, 2)  
        mnemonic.append(bip39_words[index])  
    
    return " ".join(mnemonic)  




# Function to import a mnemonic phrase and convert it back to the seed
def import_mnemonic():  

    mnemonic_phrase = input("Enter your seed phrase: ")  
    words = mnemonic_phrase.split()  
    
    # Check if there are exactly 12 words
    if len(words) != 12:  
        print("Error : Invalid number of words in mnemonic phrase. It must be 12 words.")
    
    # Validate each word is in the BIP39 word list
    if not all(word in bip39_words for word in words):  
        print("Error : One or more words in the mnemonic phrase are invalid.")
    
    # Get the index of each word in the BIP39 list
    indices = [bip39_words.index(word) for word in words]  
    
    # Create a binary representation for each index
    binary_seed = ''.join([bin(index)[2:].zfill(11) for index in indices])  
    
    # Calculate the length of the checksum based on the number of words
    checksum_length = len(words) * 11 // 33  
    # Remove the checksum bits from the binary seed
    seed_bits = binary_seed[:-checksum_length]  
    
    # Convert the binary seed back to an integer
    seed = int(seed_bits, 2)  

    print("Imported seed :", seed)  





if __name__ == "__main__":  

    # Generate a random 128-bit seed
    random_seed = random.getrandbits(128) 

    print('Seed aléatoire :', random_seed)  
    print('Seed aléatoire en mnémonique :', mnemonic_seed())  
    import_mnemonic()  
