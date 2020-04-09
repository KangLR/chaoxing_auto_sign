from fastapi import FastAPI
from cloud_sign import *


app = FastAPI()


@app.post('/sign')
@app.get('/sign')
def sign(*, username: str, password: str, schoolid=None, sckey=None):
    user_info['username'] = username
    user_info['password'] = password
    user_info['schoolid'] = schoolid
    return interface(user_info, sckey)
