class genwordGenerator:
    def __init__(self):
        self.Session = __import__('requests').Session()
        self.url = 'https://genword.ru/generators/{}/new/'.format
        self.headers = {
            'user-agent': __import__('fake_useragent').UserAgent()['Opera'],
            'x-requested-with': 'XMLHttpRequest'
        }

    def anime(self):
        req = self.Session.post(self.url('anime'), headers = self.headers).json()['result']
        if input('1 - Eng\n2 - Rus\n>>> ') == '1': return req['nameEn']
        else: return req['nameRu']

    def words(self):
        req = self.Session.post(self.url('word'), headers=self.headers).json()['result']
        return req['word']

    def winged(self):
        req = self.Session.post(self.url('winged'), headers=self.headers).json()['result']
        phrase = req['phrase']
        source = req['source']
        return phrase, source

print(genwordGenerator().winged())