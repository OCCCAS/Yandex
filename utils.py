from hashlib import sha256


def hash_data(data):
    return sha256(data.encode('utf-8')).hexdigest()

