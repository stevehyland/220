def encode(in_line, in_key):
#
    new_string = ""
    for letter in in_line:
        new_ord = ord(letter) + in_key
        new_chr = chr(new_ord)
        new_string = new_string + new_chr
    return new_string
#
def encode_better(msg_in, key_in):
#
    len_key = len(key_in)
    len_msg = len(msg_in)
    msg_out = ""
    for idx_in in range(len_msg):
        key_off = idx_in % len_key
        new_ord = ord((msg_in[idx_in])) + (ord(key_in[key_off]) - 130)
        new_ord1 = (new_ord % 58) + 65
        msg_out = msg_out + chr(new_ord1)
    return msg_out
#
