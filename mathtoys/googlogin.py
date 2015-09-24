#!/usr/bin/env python2.7

# Google APIs
from oauth2client import client, crypt

CLIENT_ID = '788221055258-j59svg86sv121jdr7utnhc2rs9tkb9s4.apps.googleusercontent.com'

def fetchIdToken():
    url = 'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token='
    f = urllib.urlopen(url + urllib.urlencode(CLIENT_ID))
    if f.getCode() != 200:
        return None
    return f.read()

def getIdInfo(token):
    try:
        idinfo = client.verify_id_token(token, CLIENT_ID)
        if idinfo['aud'] not in [CLIENT_ID]:
            # raise crypt.AppIdentityError("Unrecognized client.")
            return None
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            # raise crypt.AppIdentityError("Wrong issuer.")
            return None
    except crypt.AppIdentityError:
        return None
    return idinfo

