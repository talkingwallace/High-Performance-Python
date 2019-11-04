"""
Bloom Filter

理想参数:
num_bits = -capacity * log(error)/log(2)^2
num_hash = num_bits * log(2) / capacity
"""
import math
import mmh3
import bitarray

class BloomFilter(object):

    def __init__(self,capacity,error_rate):
        num_bits,num_hashes = self.ideal_bloom_parameters(capacity,error_rate)
        self.num_bits = int(num_bits) + 1
        self.num_hashes = int(num_hashes) + 1
        self.bitarr = bitarray.bitarray(self.num_bits)
        self.bitarr.setall(0)
        self._len = 0

    def ideal_bloom_parameters(self,record_num, error_rate):
        e = math.e
        num_bits = math.log(error_rate, e) * -record_num / pow(math.log(2, e), 2)
        num_hashes = num_bits * math.log(2) / record_num

        return num_bits, num_hashes

    def _get_index(self,val):
        hash1,hash2 = mmh3.hash64(val)
        for i in range(self.num_hashes):
            yield (hash1 + hash2*i) % self.num_bits

    def add(self,val):
        flag = True
        for key in self._get_index(val):
            if self.bitarr[key] == False and flag:
                self._len += 1
                flag = False
            self.bitarr[key] = True

    def __contains__(self, item):
        for key in self._get_index(item):
            if self.bitarr[key] == False:
                return False
        return True

    def __len__(self):
        return self._len

if __name__ == '__main__':
    bloom = BloomFilter(50000,0.05/100)