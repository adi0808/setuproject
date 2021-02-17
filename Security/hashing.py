import hashlib


# Hashing class and methods
class Hashing:
    def hash(self, info, format):
        hashing_type = get_hashing_format(format)
        return hashing_type(info)


def get_hashing_format(format):
    if format == 'sha1':
        return _sha1_hashing
    else:
        return ValueError


def _sha1_hashing(info):
    result = hashlib.sha1(info)
    checksum = str(result.hexdigest())
    return checksum

