import hmac
import hashlib
import random
import ecdsa


# Constants for BIP-32
CURVE_ORDER = ecdsa.SECP256k1.order  # Order of the SECP256k1 elliptic curve
BIP32_SEED_KEY = b'Bitcoin seed'  # Key for HMAC-SHA512



# Function to generate a random 128-bit seed
def generate_seed():
    random_seed = random.getrandbits(128)  
    return random_seed.to_bytes(16)  



# Function to generate master private key and chain code from the seed
def generate_master_key_and_chain(seed):

    # Apply HMAC-SHA512 to the seed using the BIP32_SEED_KEY
    master_hmac = hmac.new(BIP32_SEED_KEY, seed, hashlib.sha512).digest()

    # First half of the HMAC output as master private key
    master_private_key = int.from_bytes(master_hmac[:32]) % CURVE_ORDER  

    # Second half of the HMAC output as chain code
    chain_code = master_hmac[32:]  

    return master_private_key, chain_code



# Function to generate the master public key from the private key
def generate_master_public_key(master_private_key):

    # Create a SigningKey object from the private key
    sk = ecdsa.SigningKey.from_string(master_private_key.to_bytes(32), curve=ecdsa.SECP256k1)

    # Get the master public key as a byte string
    master_public_key = sk.get_verifying_key().to_string()

    return master_public_key



def derive_child_key_no_index(master_private_key, chain_code):
    # Simply use the master_private_key and chain_code

    # Prepare the data for HMAC: 0x00 + master private key
    data = b'\x01' + master_private_key.to_bytes(32, byteorder='big')

    # HMAC of the chain code and data
    child_hmac = hmac.new(chain_code, data, hashlib.sha512).digest()

    # Calculate the child private key by adding the result to the master private key, modulo the curve order
    child_private_key = (int.from_bytes(child_hmac[:32], byteorder='big') + master_private_key) % CURVE_ORDER

    return child_private_key



# Function to derive a child private key at a given index
def derive_child_key(master_private_key, chain_code, index):

    # Prepare the data for HMAC: 0x00 + master private key + index
    data = b'\x00' + master_private_key.to_bytes(32, byteorder='big') + index.to_bytes(4, byteorder='big')

    # HMAC of the chain code and data
    child_hmac = hmac.new(chain_code, data, hashlib.sha512).digest()  

    # Calculate the child private key by adding the result to the master private key, modulo the curve order
    child_private_key = (int.from_bytes(child_hmac[:32], byteorder='big') + master_private_key) % CURVE_ORDER

    return child_private_key



# Function to derive a child private key at a given index and level of derivation
def derive_child_key_with_level(master_private_key, chain_code, index, level):

    # Prepare the data: 0x00 + master private key + level + index
    data = (b'\x00' + master_private_key.to_bytes(32, byteorder='big') 
            + level.to_bytes(4, byteorder='big') + index.to_bytes(4, byteorder='big'))
    
    # HMAC with the chain code
    child_hmac = hmac.new(chain_code, data, hashlib.sha512).digest()  

    child_private_key = (int.from_bytes(child_hmac[:32], byteorder='big') + master_private_key) % CURVE_ORDER

    return child_private_key 





if __name__ == "__main__":

    # Generate a random seed
    seed = generate_seed()  
    # Generate master key and chain code
    master_private_key, chain_code = generate_master_key_and_chain(seed)  
    # Generate master public key
    master_public_key = generate_master_public_key(master_private_key)  
    # Derive child key without index
    child_private_key_no_index = derive_child_key_no_index(master_private_key, chain_code)
    # Derive child key at index 0
    child_private_key_0 = derive_child_key(master_private_key, chain_code, 0)  
    # Derive child key at index N (5)
    child_private_key_n = derive_child_key(master_private_key, chain_code, 5)  
    # Derive child key at index N (5) and level M (2)
    child_private_key_nm = derive_child_key_with_level(master_private_key, chain_code, 5, 2)  

    print("Seed : ", seed.hex()) 
    print("Master Private Key : ", master_private_key.to_bytes(32, byteorder='big').hex())
    print("Chain Code : ", chain_code.hex())
    print("Master Public Key : ", master_public_key.hex())
    print("Child Private Key (no index) : ", child_private_key_no_index)
    print("Child Private Key (index 0) : ", child_private_key_0.to_bytes(32, byteorder='big').hex())
    print("Child Private Key (index 5) : ", child_private_key_n.to_bytes(32, byteorder='big').hex())
    print("Child Private Key (index 5, level 2) : ", child_private_key_nm.to_bytes(32, byteorder='big').hex())

