import requests

auth_token = 'YjQ3NDMzMzYtMGIzZS00MzllLWExOTctZGU3YzU4MzFmNTljZWNjZDljNjEtZTE3'
hed = {'Authorization': 'Bearer ' + auth_token}

url = "https://api.ciscospark.com/v1/people"

querystring = {"email":"dragan@netvirtexpert.com"}

headers = {
    'cache-control': "no-cache",
    'Postman-Token': "YjQ3NDMzMzYtMGIzZS00MzllLWExOTctZGU3YzU4MzFmNTljZWNjZDljNjEtZTE3"
    }

response = requests.request("GET", url, headers=hed, params=querystring)

print(response.text)
