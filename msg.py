def decode(input_code):
    def shift_char(c, shift):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            return chr((ord(c) - base + shift) % 26 + base)
        elif c.isdigit():
            return chr((ord(c) - ord('0') + shift) % 10 + ord('0'))
        return c

    decoded = ''.join(shift_char(c, 3) if c != '=' else c for c in input_code)

    return decoded


//PASS CODE HERE
decoded = decode()


print("Decoded Code:", decoded)
