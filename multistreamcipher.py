# multistreamcipher.py
# Written by James Wang

# Given multiple ciphers encrypted by the same stream cipher, decrypt a target
# ciphered text. Assumes normal XOR operation by stream cipher on key.

def read_ciphers (file):
    """Returns contents of cipher file in long base 16 in an array. Expects
    filename string.

    """
    ciphers = []
    infile = open(file, "r")
    for line in infile:
        if line == "\n": pass
        else:
            hexline = long(line[:-1],16) # cut newline
            ciphers.append(hexline)
    infile.close()
    return ciphers

def xor_ciphers (ciphers):
    """XOR ciphers against another another for XOR'ed plaintext.
    Expects array of ciphers in hexidecimal format. Returns array with every
    combination of XOR'ed ciphers in hex form.

    """
    xor_msgs = []
    for cipher_msg in ciphers:
        for element in ciphers:
            xor_cm = cipher_msg ^ element
            if xor_cm == 0: pass # skip xor of msg vs itself
            else: xor_msgs.append(xor_cm)
    return xor_msgs

def freq_analysis (file, gram):
    """Performs frequency analysis on given file.

    Arguments:
    file -- filename string; hex format expected in file, with underlying
            ascii encoded plaintext
    gram -- 1, 2, or 3. Performs mono, di, or trigram analysis.

    """
    
    
def main ():
    msgs = xor_ciphers(read_ciphers("cipher.txt"))
    outfile = open("result.txt", "w")
    for m in msgs:
        outfile.write(hex(m)[2:-1] + "\n\n")
    freq_analysis("results.txt", 1)

if __name__ == "__main__":
    main()
