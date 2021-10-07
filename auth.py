import hashlib

from model import getCursor, User

def generate_locationkey(username):
    h = hashlib.sha1()
    s = "mysterymeeting-" + username
    se = str.encode(s)
    h.update(se)
    print(h.hexdigest())

def hash_password(password):
    h = hashlib.sha256()
    pe = str.encode(password)
    h.update(pe)
    return h.hexdigest()
