import configuration
import requests
import data

#новый пользователь
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

#response = post_new_user(data.user_body);
#print(response.status_code)
#print(response.text)

#  новый набор с authToken нового пользователя
def post_new_client_kit(kit_body, auth_token):
    auth_headers = data.headers.copy()
    auth_headers["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=auth_headers)

def post_new_client_kit(kit_body, headers):
    auth_headers = data.headers.copy()
    auth_headers["Authorization"] = "Bearer " + headers
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=auth_headers)




