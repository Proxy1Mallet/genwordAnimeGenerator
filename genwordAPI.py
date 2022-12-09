from .util import headers, objects
from requests import Session

class genwordAPI:
    def __init__(self, proxies : dict = None):
        self.Session = Session()
        self.url = 'https://genword.ru/generators/{}/new/'.format
        self.headers = headers.Headers().headers
        self.proxies = proxies

    def anime(self) -> str:
        req = self.Session.post(url = self.url('anime'), headers = self.headers, proxies = self.proxies)
        return objects.Anime(req.json()).Anime

    def words(self) -> str:
        req = self.Session.post(url = self.url('word'), headers = self.headers, proxies = self.proxies)
        return objects.Words(req.json()).Words

    def winged(self) -> str:
        req = self.Session.post(url = self.url('winged'), headers = self.headers, proxies = self.proxies)
        return objects.Winged(req.json()).Winged

    def alcoholDrinking(self) -> str:
        req = self.Session.post(url = self.url('alcohol-drinking'), headers = self.headers, proxies = self.proxies)
        return objects.AlcoholDrinking(req.json()).AlcoholDrinking

    #sex : 1 or 2
    #alias : cat, dog, bird, fish, rodent, horse, reptile, amphibia
    def alias(self, alias : str, sex : int) -> str:
        data = {'alias': alias, 'sex': sex}
        req = self.Session.post(url = self.url('alias'), headers = self.headers, data = data, proxies = self.proxies)
        return objects.Alias(req.json()).Alias

    def slogan(self, slogan : str) -> str:
        data = {'slogan': slogan}
        req = self.Session.post(url = self.url('slogan'), headers = self.headers, data = data, proxies = self.proxies)
        return objects.Slogan(req.json()).Slogan

    def login(self, firstname : str, surname : str, patronymic : str, nickname : str) -> str:
        data = {'firstname': firstname, 'surname': surname, 'patronymic': patronymic, 'nickname': nickname}
        req = self.Session.post(url = self.url('login'), headers = self.headers, data = data, proxies = self.proxies)
        return objects.Login(req.json()).Login