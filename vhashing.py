def rs_hash(key: str) -> int:
    a = 378551
    b = 63689

    hashed = 0
    for c in key:
        hashed *= a + ord(c)
        a *= b
    return hashed


def js_hash(key: str) -> int:
    hashed = 1315423911

    for c in key:
        hashed ^= ((hashed << 5) + ord(c) + (hashed >> 2))
    return hashed


def pjw_hash(key: str) -> int:
    sizeof_uint32 = 32
    three_quarters = int((sizeof_uint32 * 3) / 4)
    one_eight = int(sizeof_uint32 / 8)
    high_bits = (0xFFFFFFFF) << (sizeof_uint32 - one_eight)

    hashed = 0
    test = 0
    for c in key:
        hashed = (hashed << one_eight) + ord(c)
        test = hashed & high_bits
        if test != 0:
            hashed = ((hashed ^ (test >> three_quarters)) & (~high_bits))
    return hashed & 0x7FFFFFFF


def elf_hash(key: str) -> int:
    hashed = 0
    x = 0
    for c in key:
        hashed = (hashed << 4) + ord(c)
        x = hashed & 0xF0000000
        if x != 0:
            hashed ^= (x >> 24)
        hashed &= ~x
    return hashed


def bkdr_hash(key: str) -> int:
    seed = 131  # 31 131 1313 13131 131313 ..

    hashed = 0
    for c in key:
        hashed = (hashed * seed) + ord(c)
    return hashed


def sdbm_hash(key: str) -> int:
    hashed = 0
    for c in key:
        hashed = ord(c) + (hashed << 6) + (hashed << 16) - hashed
    return hashed


def djb_hash(key: str) -> int:
    hashed = 5381
    for c in key:
        hashed = ((hashed << 5) + hashed) + ord(c)
    return hashed


def dek_hash(key: str) -> int:
    hashed = len(key)
    for c in key:
        hashed = ((hashed << 5) ^ (hashed >> 27)) ^ ord(c)
    return hashed


def bp_hash(key: str) -> int:
    hashed = 0
    for c in key:
        hashed = hashed << 7 ^ ord(c)
    return hashed


def fnv_hash(key: str) -> int:
    fnv_prime = 0x811C9DC5
    hashed = 0
    for c in key:
        hashed *= fnv_prime
        hashed ^= ord(c)
    return hashed


def ap_hash(key: str) -> int:
    hashed = 0xAAAAAAAA
    for i, c in enumerate(key):
        if ((i & 1) == 0):
            hashed ^= ((hashed << 7) ^ ord(c) * (hashed >> 3))
        else:
            hashed ^= (~((hashed << 11) + ord(c) ^ (hashed >> 5)))
    return hashed


if __name__ == '__main__':
    pass
