from .objects import *
from requests import Session
from fake_useragent import FakeUserAgent
class genword_API:
    def __init__(self, proxies : dict = None):
        self.session = Session()
        self.url = 'https://genword.ru/generators/{}/new/'.format
        self.headers = {
            'user-agent': FakeUserAgent().random,
            'accept-encoding': 'gzip, deflate, br',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'x-requested-with': 'XMLHttpRequest'
        }
        self.data = {
            'x-csrf-token': self.session.get(url = 'https://genword.ru/', headers = self.headers).text[6901:][:64],
            'x-powered-by': 'PHP/7.2.34',
            'vary': 'Accept-Encoding'
        }
        self.proxies = proxies

    def anime(self) -> str:
        req = self.session.post(url = self.url('anime'), data = self.data, headers = self.headers, proxies = self.proxies)
        if req.status_code != 200: return req.status_code
        else: return obj_anime(data = req.json()).obj_anime

    def words(self) -> str:
        req = self.session.post(url = self.url('word'), data = self.data, headers = self.headers, proxies = self.proxies)
        if req.status_code != 200: return req.status_code
        else: return obj_words(data = req.json()).obj_words

    def winged(self) -> str:
        req = self.session.post(url = self.url('winged'), data = self.data, headers = self.headers, proxies = self.proxies)
        if req.status_code != 200: return req.status_code
        else: return obj_winged(data = req.json()).obj_winged

    def alcohol_drinking(self) -> str:
        req = self.session.post(url = self.url('alcohol-drinking'), data = self.data, headers = self.headers, proxies = self.proxies)
        if req.status_code != 200: return  req.status_code
        else: return obj_alcohol_drinking(data = req.json()).obj_alcohol_drinking

    def alias(self, animal : str, sex : int) -> str:
        """
        This function is designed to generate an alias for an animal

        :param animal: subspecies of animals, variants : cat, dog, bird, fish, rodent, horse, reptile, amphibia
        :type animal: :obj: `str`

        :param sex: sex - gender, variants : 1 or 2
        :type sex: :obj: `str`

        :return: an alias for an animal in json format
        """
        self.data.update(alias = animal, sex = sex)
        req = self.session.post(url = self.url('alias'), headers = self.headers, data = self.data, proxies = self.proxies)
        if req.status_code != 200: return req.status_code
        else: return obj_alias(data = req.json()).obj_alias

    def slogan(self, slogan : str) -> str:
        """
        This function generates your slogan

        :param slogan: The name of an object
        :type slogan: :obj: `str`

        :return: Slogan in json format
        """
        self.data.update(slogan = slogan)
        req = self.session.post(url = self.url('slogan'), headers = self.headers, data = self.data, proxies = self.proxies)
        if req.status_code != 200: return req.status_code
        else: return obj_slogan(data = req.json()).obj_slogan

    def login(self, firstname : str, surname : str, patronymic : str, nickname : str) -> str:
        """
        This function is designed to generate logins

        :param firstname: your or not your firstname, but a made-up one
        :type firstname: :obj: `str`

        :param surname: your or not your surname, but a made-up one
        :type surname: :obj: `str`

        :param patronymic: your patronymic or fictional
        :type patronymic: :obj: `str`

        :param nickname: your nickname or fictional
        :type nickname: :obj: `str`

        :return: 10 logins in json format
        """
        self.data.update(firstname = firstname, surname = surname, patronymic = patronymic, nickname = nickname)
        req = self.session.post(url = self.url('login'), headers = self.headers, data = self.data, proxies = self.proxies)
        if req.status_code != 200: return req.status_code
        else: return obj_login(data = req.json()).obj_login