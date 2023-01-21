from requests_oauthlib import OAuth1Session
from settings import CONFIG

consumer_key = CONFIG["CONSUMER_KEY"]
consumer_secret = CONFIG["CONSUMER_SECRET"]


def get_oauth_token():
    callback_url = "http://kakip1919.pythonanywhere.com/oauth"
    request_endpoint_url = "https://api.twitter.com/oauth/request_token"
    authenticate_url = "https://api.twitter.com/oauth/authenticate"

    session_req = OAuth1Session(consumer_key, consumer_secret)
    response_req = session_req.post(request_endpoint_url, params={"oauth_callback": callback_url})
    response_req_text = response_req.text

    oauth_token_str = response_req_text.split("&")
    token_dict = {x.split("=")[0]: x.split("=")[1] for x in oauth_token_str}
    oauth_token = token_dict["oauth_token"]
    return f"{authenticate_url}?oauth_token={oauth_token}"


def get_access_token(oauth_token, oauth_verifier):
    access_endpoint_url = "https://api.twitter.com/oauth/access_token"

    session_acc = OAuth1Session(consumer_key, consumer_secret, oauth_token, oauth_verifier)
    response_acc = session_acc.post(access_endpoint_url, params={"oauth_verifier": oauth_verifier})
    response_acc_text = response_acc.text

    access_token_kvstr = response_acc_text.split("&")
    acc_token_dict = {x.split("=")[0]: x.split("=")[1] for x in access_token_kvstr}
    access_token = acc_token_dict["oauth_token"]
    access_token_secret = acc_token_dict["oauth_token_secret"]
    return acc_token_dict["screen_name"]
    print("Access Token       :", access_token)
    print("Access Token Secret:", access_token_secret)
    print("User ID            :", acc_token_dict["user_id"])
    print("Screen Name        :", acc_token_dict["screen_name"])