class LineNotify():
    def __init__(self,token):
        self.url = "https://notify-api.line.me/api/notify"
        self.access_token = token

    def sendMessage(self, message):
        headers = {'Authorization': 'Bearer ' + self.access_token}
        payload = {'message': message}
        requests.post(self.url, headers=headers, params=payload,)
    
    def sendMessageWithImage(self,message,img_pass):
        headers = {'Authorization': 'Bearer ' + self.access_token}
        payload = {'message': message}
        files = {'imageFile' : open(img_pass,'rb')}
        requests.post(self.url, headers=headers, params=payload,files=files)
