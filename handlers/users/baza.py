import requests

def userget():
    #url = 'https://temur01.pythonanywhere.com/api/telegramuser/'
    url = 'http://127.0.0.1:8000/api/usertg/'
    respons = requests.get(url)
    return respons.json()





def usercreate(first_name,username,user_id,name,phon,passport):
    #url = 'https://temur01.pythonanywhere.com/api/telegramuser/'
    url = 'http://127.0.0.1:8000/api/usertg/'
    re = requests.post(url,data={'first_name':first_name,'username':username,'user_id':user_id,'name':name,'phone':phon,'passport':passport})
    return re.status_code


def user(user_id):
    #url = 'https://temur01.pythonanywhere.com/api/user/'+ user_id + '/'
    url = 'http://127.0.0.1:8000/api/user/'+ user_id + '/'
    respons = requests.get(url)
    return respons.json()


def oylik(user_id,oy):
    #url = 'https://temur01.pythonanywhere.com/api/user/'+ user_id + '/'
    url = 'http://127.0.0.1:8000/api/oylik/'+ user_id + '/' + oy + '/'
    respons = requests.get(url)
    return respons.json()


def sana():
    url = 'http://127.0.0.1:8000/api/sana/'
    respons = requests.get(url)
    data = respons.json()
    return [entry['name'] for entry in data]




def update_user(id,status,first_name,username,user_id,name,phon,passport):
    url = 'http://127.0.0.1:8000/api/user/'+ user_id + '/'
    data = {'id': id,'status':status,'first_name':first_name,'username':username,'user_id':user_id,'name':name,'phone':phon,'passport':passport}
    response = requests.put(url, json=data)

    return response.status_code


