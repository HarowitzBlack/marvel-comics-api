
import requests
import hashlib
import datetime

class Marvel():

    def __init__(self,public_key,private_key):
        # private_key and public_key are used to generate an md5 hash string
        self.private_key = private_key
        self.public_key  = public_key
        self.baseURI = "http://gateway.marvel.com/v1/public"
        self.hasedString,self.timestamp = self.md5_Hash()
        self.url_params = {
                            'ts':self.timestamp,
                            'apikey':self.public_key,
                            'hash':self.hasedString
                          }

    def fetch_characters(self):
        self.baseURI +="/characters"
        print(self.baseURI)
        resp = requests.get(self.baseURI,params=self.url_params)
        return resp.json()

    def fetch_characters_by_id(self,char_id="1009368",limit=2):
        # limit specifies how  many items to display
        if limit is not None:
            self.url_params['limit'] = limit
        self.char_id = char_id
        # add the item in the param payload
        self.baseURI += "/characters" + "/{}".format(self.char_id)
        resp = requests.get(self.baseURI,params=self.url_params)
        print(resp.url)
        return resp.json()

    def fetch_comics_by_characterId(self,char_id="1009368",limit=2):
        # limit specifies how  many items to display
        if limit is not None:
            self.url_params['limit'] = limit
        self.char_id = char_id
        self.baseURI += "/characters" + "/{}".format(self.char_id) +"/comics"
        resp = requests.get(self.baseURI,params=self.url_params)
        print(resp.url)
        return resp.json()


    def md5_Hash(self):
        '''
        hash changes everytime this function is called.
        returns hashed string and a timestamp
        '''
        self.timestamp = '{:%Y%m%d%H%M%S}'.format(datetime.datetime.now()) # generate a timestamp
        self.hash_input = self.timestamp + self.private_key + self.public_key
        self.hashed_string = hashlib.md5(self.hash_input.encode('utf-8')).hexdigest() # generate md5 hash
        return self.hashed_string,self.timestamp


pub_key = ""
pri_key = ""
x = Marvel(pub_key,pri_key)
print(x.fetch_characters_by_id())
