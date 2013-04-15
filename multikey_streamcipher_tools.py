# multikey_streamcipher_tools.py
# Written by James Wang

"""
Given multiple ciphers encrypted by the same stream cipher, decrypt a target
ciphered text. If executed directly, expects a cipher file with multiple
messages named 'cipher.txt' (hex format) in the same directory as file.

Functions:
read_ciphers(file) -- takes a hex cipher file, returns base 10 array of
                      contents
                      
xor_ciphers(ciphers) -- takes array of base 10 ciphers, returns xor of ciphers
                        against one another (for xor'ed plaintext messages)

xor_against(infile, outfile, character) -- takes hex cipher file, xor given
                                           character against messages, outputs 
                                           to outfile.
"""

def read_ciphers (file):
    """Returns contents of cipher file in long base 10 in an array. Expects
    filename string.

    Arguments:
    file -- filename to be read as a string, expects hex input

    """
    ciphers = []
    infile = open(file, "r")
    for line in infile:
        if line == "\n": pass
        else:
            convertline = long(line[:-1],16) # cut newline
            ciphers.append(convertline)
    infile.close()
    return ciphers

def xor_ciphers (ciphers):
    """XOR ciphers against another another for XOR'ed plaintext.
    Expects array of ciphers in base 10 format. Returns array with every
    combination of XOR'ed ciphers in base 10 form.

    Arguments:
    ciphers -- array of ciphers in base 10 format

    """
    xor_msgs = []
    for cipher_msg in ciphers:
        for element in ciphers:
            xor_cm = cipher_msg ^ element
            if xor_cm == 0: pass # skip xor of msg vs itself
            else: xor_msgs.append(xor_cm)
    return xor_msgs

def xor_against (infile, outfile, character):
    """Takes a file and runs xor of a specific character against entire
    file. Outputs results in an outfile. To be used on xor'ed ciphers that have
    used the same key to reveal key in plaintext.

    Arguments:
    infile -- filename string for file to be xor'ed against
              (e.g. "cipher.txt"); expects hex format for file
    outfile -- filename string for file to output results of xor analysis
    character -- character to xor against (e.g. space)
    
    """
    to_xor = open(infile, "r")
    to_out = open(outfile, "w")
    xor_character = 0
    
    if len(character) > 1:
        raise "Cannot enter multiple characters."
    else:
        xor_char = ord(character)
        
    for l in to_xor:
        if l == "\n": pass
        else:
                xor_line = str(long(l[:-1],16) ^ long(str(xor_char) *
                                                      (len(str(l))/2)))
                out_line = ''.join(chr(int(x + y)) for (x, y) in 
                                   zip(xor_line[0::2], xor_line[1::2]))
                to_out.write(str(out_line) + "\n\n")

    to_xor.close()
    to_out.close()
    
def freq_analysis (file, gram):
    """Performs frequency analysis on given file.

    Arguments:
    file -- filename string; hex format expected in file, with underlying
            ascii encoded plaintext
    gram -- 1, 2, or 3. Performs mono, di, or trigram analysis.

    TO BE IMPLEMENTED
    """
    
def main():
    msgs = xor_ciphers(read_ciphers("cipher.txt"))
    outfile_hex = open("result_hex.txt", "w")
    outfile_base10 = open("result_base10.txt", "w")

    for m in msgs:
        outfile_hex.write(hex(m)[2:-1] + "\n\n") # hex output
        outfile_base10.write(str(m) + "\n\n") # base 10 output

    freq_analysis("result_base10.txt", 1) # Not yet implemented

    # Test to see if sensible plaintext key comes out of xor against space
    xor_against("cipher.txt", "result_space.txt", " ")

    outfile_hex.close()
    outfile_base10.close()

if __name__ == "__main__":
    main()














