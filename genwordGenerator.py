from .util import headers, objects
from requests import Session

class genwordGenerator:
    def __init__(self):
        self.Session = Session()
        self.url = 'https://genword.ru/generators/{}/new/'.format
        self.headers = headers.Headers().headers

    def anime(self):
        req = self.Session.post(url = self.url('anime'), headers = self.headers)
        return objects.Anime(req.json()).Anime

    def words(self):
        req = self.Session.post(url = self.url('word'), headers = self.headers)
        return objects.Words(req.json()).Words

    def winged(self):
        req = self.Session.post(url = self.url('winged'), headers = self.headers)
        return objects.Winged(req.json()).Winged

    def alcoholDrinking(self):
        req = self.Session.post(url = self.url('alcohol-drinking'), headers = self.headers)
        return objects.AlcoholDrinking(req.json()).AlcoholDrinking

    def alias(self, alias, sex):
        data = {'alias': alias, 'sex': sex}
        req = self.Session.post(url = self.url('alias'), headers = self.headers, data = data)
        return objects.Alias(req.json()).Alias

    def slogan(self, slogan):
        data = {'slogan': slogan}
        req = self.Session.post(url = self.url('slogan'), headers = self.headers, data = data)
        return objects.Slogan(req.json()).Slogan

    def login(self, firstname, surname, patronymic, nickname):
        data = {'firstname': firstname, 'surname': surname, 'patronymic': patronymic, 'nickname': nickname}
        req = self.Session.post(url = self.url('login'), headers = self.headers, data = data)
        return objects.Login(req.json()).Login