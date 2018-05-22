import requests

def host():
    return

def pb():
    return

def pw():
    return

def session(pb,pw):
    session = requests.session()
    session.headers.update({
                                "X-Source": "AppStore|iOS|3.1.1|1|A9AF51FD-4D20-41AE-8B19-935673C0DB0B|iPhone|iOS 10.3.3|WiFi|6f7ca9d6b62a7e5124a3fe69d372e166c0123d63"})
    session.headers.update({"User-Agent": "Guihua/3.1.1 (iOS)"})
    session.headers.update({"X-Device-ID": "1517bfd3f7f1e6d542e"})
    session.headers.update({"X-Device-Alias": "76DA806408F6CDCE152161DBC0F380DE"})
    client_auth = requests.auth.HTTPBasicAuth("iJxiDEc4eb71V7IoElYmWCxL7gByIm","wqbzmP5pOTkrsq03VlJubDV3kWMhbZ")
    print (client_auth)
    post_data = {"grant_type": "password",
                     "password": pw,
                     "username": pb,
                     "scope": "basic user_info savings_r savings_w wallet_r wallet_w"}
    response = session.post("https://www.guihua.com/oauth/token", auth=client_auth, data=post_data)
    token_json = response.json()
    authorization = "%s %s" % (token_json["token_type"], token_json["access_token"])
    session.headers.update({"Authorization": authorization})
    return session

def sign():
    url="%sapi/v2/checkin/welfare/"%(host())
    for i in range(0,2):
        rep =session(,).post(url)
        print (rep.status_code)

if __name__ == "__main__":
    sign()