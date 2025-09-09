import hashlib

def make_id(unique_id: str):
    _hash = hashlib.sha256()
    _hash.update(unique_id.encode("utf-8"))
    return _hash.hexdigest()