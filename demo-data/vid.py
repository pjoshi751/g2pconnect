from stdnum import verhoeff
import sys
import os

def generate_id(id_len: int) -> int:
    actual_len = id_len - 1
    rand_bytes = os.urandom(actual_len)
    rand_num = int(str(abs(int.from_bytes(rand_bytes, byteorder=sys.byteorder)))[:actual_len])
    ver_checksum = verhoeff.calc_check_digit(rand_num)
    id = int(str(rand_num) + str(ver_checksum))
    return id
