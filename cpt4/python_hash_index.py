
"""
How python dict/set produce hash index
"""
def get_index(key,mask,shift=3):
    hash_val = hash(key)
    i = hash_val & mask
    yield i
    while True:
        i = (i << 2) + i + hash_val
        hash_val >>= shift
        yield i



