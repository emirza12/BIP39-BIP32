"""
# 📜 BIP39 & BIP32 Key Derivation in Python

Welcome to the **BIP39 & BIP32** repository! This project is designed to help you understand and implement key derivation processes used in blockchains like **Bitcoin** through Python code. The repository is divided into two parts:

- **BIP39**: Mnemonic phrase generation.
- **BIP32**: Hierarchical deterministic (HD) wallet key derivation.

## 🔐 BIP39: Mnemonic Phrase Generation

In this section, you’ll explore how to generate a **secure cryptographic seed** and convert it into a human-readable **mnemonic phrase**. Here's a breakdown of the process:

1. **Entropy Generation**: A random 128-bit integer is generated.
2. **Checksum**: The first 4 bits of the SHA-256 hash of the entropy are added as a checksum.
3. **Binary Conversion**: The result is converted into a binary string.
4. **Word Mapping**: The binary string is split into 11-bit chunks, and each chunk is mapped to a word from the official BIP39 word list, forming the final mnemonic.
   
### Features:
- **Generate a New Seed**: Create a random 12-word mnemonic phrase.
- **Import an Existing Mnemonic**: Validate an existing mnemonic phrase by checking it against the BIP39 word list.

---

## 🔑 BIP32: Hierarchical Deterministic (HD) Wallet

The second part focuses on implementing **BIP32 key derivation**, where a single master key can generate a family of child keys. This is the foundation of HD wallets used in cryptocurrencies like Bitcoin.

### Key Steps:
1. **Master Private Key & Chain Code Extraction**: Start by deriving the master private key and chain code from the seed.
2. **Master Public Key**: Generate the corresponding master public key.
3. **Child Key Derivation**: Derive child keys at specific indices.
   - **Default Index**: Derive a child key at the default index.
   - **Custom Index**: Generate child keys at any index N.
4. **Derivation Path**: Extend key derivation to multiple levels, allowing hierarchical key generation.

---
