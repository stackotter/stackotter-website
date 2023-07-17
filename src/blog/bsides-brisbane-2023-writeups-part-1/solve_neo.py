from base64 import b64decode, b64encode
from pwn import *

SUCCESS = 0
ACCESS_DENIED = 1
MALFORMED = 2

BLOCK_SIZE = 16

iv = b64decode("ORYo2QThghEvpHv+wD3D6w==")
ciphertext = b64decode("01jm3AZpstbCZ3WQwbNAsQ==")

p = remote("neo.crypto.ctf.bsidesbne.com", 3302)
p.recvline()

def login(iv: bytes, password: bytes):
    p.recvuntil(b"> ")
    p.sendline(b"1")
    p.recvuntil(b"IV:\n")
    p.sendline(b64encode(iv))
    p.recvuntil(b"password:\n")
    p.sendline(b64encode(password))
    response = p.recvline()
    if response == b"Access denied.\n":
        return ACCESS_DENIED
    elif response == b"Error: malformed message\n":
        return MALFORMED
    else:
        print("key:", response.decode("utf8"))
        return SUCCESS

def oracle(iv, password):
    return login(iv, password) != MALFORMED

# Source: https://research.nccgroup.com/2021/02/17/cryptopals-exploiting-cbc-padding-oracles/
def single_block_attack(block, oracle):
    """Returns the decryption of the given ciphertext block"""

    # zeroing_iv starts out nulled. each iteration of the main loop will add
    # one byte to it, working from right to left, until it is fully populated,
    # at which point it contains the result of DEC(ct_block)
    zeroing_iv = [0] * BLOCK_SIZE

    for pad_val in range(1, BLOCK_SIZE+1):
        padding_iv = [pad_val ^ b for b in zeroing_iv]

        print("Working on %d" % pad_val)
        for candidate in range(256):
            padding_iv[-pad_val] = candidate
            iv = bytes(padding_iv)
            if oracle(iv, block):
                if pad_val == 1:
                    # make sure the padding really is of length 1 by changing
                    # the penultimate block and querying the oracle again
                    padding_iv[-2] ^= 1
                    iv = bytes(padding_iv)
                    if not oracle(iv, block):
                        continue  # false positive; keep searching
                break
        else:
            raise Exception("no valid padding byte found (is the oracle working correctly?)")

        zeroing_iv[-pad_val] = candidate ^ pad_val

    return zeroing_iv

# Source: https://research.nccgroup.com/2021/02/17/cryptopals-exploiting-cbc-padding-oracles/
def full_attack(iv, ct, oracle):
    """Given the iv, ciphertext, and a padding oracle, finds and returns the plaintext"""
    assert len(iv) == BLOCK_SIZE and len(ct) % BLOCK_SIZE == 0

    msg = iv + ct
    blocks = [msg[i:i+BLOCK_SIZE] for i in range(0, len(msg), BLOCK_SIZE)]
    result = b''

    # loop over pairs of consecutive blocks performing CBC decryption on them
    iv = blocks[0]
    for ct in blocks[1:]:
        dec = single_block_attack(ct, oracle)
        pt = bytes(iv_byte ^ dec_byte for iv_byte, dec_byte in zip(iv, dec))
        result += pt
        iv = ct

    return result

print(full_attack(iv, ciphertext, oracle))

