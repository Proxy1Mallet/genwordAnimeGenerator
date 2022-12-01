class animeGenerator:
    def __init__(self):
        self.Session = __import__('requests').Session()
        self.url = 'https://genword.ru/generators/anime/{}'.format
        self.headers = {
            'user-agent': __import__('fake_useragent').UserAgent()['Opera'],
            'x-requested-with': 'XMLHttpRequest'
        }

    def generate(self):
        req = self.Session.post(self.url('new/'), headers = self.headers).json()['result']
        if input('1 - Eng\n2 - Rus\n>>> ') == '1': return req['nameEn']
        else: return req['nameRu']

print(animeGenerator().generate())