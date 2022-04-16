import time, random, string

def make_salt(size=16, chars=None):
    if not chars:
        chars = ''.join(
            [string.ascii_uppercase, 
             string.ascii_lowercase]
        )
    return ''.join(random.choice(chars) for x in range(size))

def hello():
    for i in range(10):
        time.sleep(1)
        yield i

def clean_submit_scripts():
    pass