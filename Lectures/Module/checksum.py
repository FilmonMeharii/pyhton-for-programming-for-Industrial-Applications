

def is_valid(id_number):
    pnr = id_number.replace("-", "")
    if len(pnr) != 10:
        return False
    checksum = 0
    for i in range(10):
        val = int(pnr[i])
        if i % 2 == 0:
            val *= 2
            val = val // 10 + val % 10
        checksum += val 
    if checksum % 10 == 0:
        return True
    return False