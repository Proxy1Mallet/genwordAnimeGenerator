from .objects import *
from requests import Session
from fake_useragent import FakeUserAgent
class Data:
    _session = Session()
    _url = 'https://genword.ru/generators/{}/new/'.format
    _headers = {
        'user-agent': FakeUserAgent().random,
        'accept-encoding': 'gzip, deflate, br',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-requested-with': 'XMLHttpRequest'
    }
    _data = {
        'x-csrf-token': _session.get(url = 'https://genword.ru/', headers = _headers).text[6901:][:64],
        'x-powered-by': 'PHP/7.2.34',
        'vary': 'Accept-Encoding'
    }

class GenwordAPI(Data):
    @classmethod
    def anime(cls) -> int | ObjectAnime:
        req = cls._session.post(url = cls._url('anime'), data = cls._data, headers = cls._headers)
        if req.status_code != 200: return req.status_code
        else: return ObjectAnime(data = req.json()).object_anime

    @classmethod
    def words(cls) -> int | ObjectWords:
        req = cls._session.post(url = cls._url('word'), data = cls._data, headers = cls._headers)
        if req.status_code != 200: return req.status_code
        else: return ObjectWords(data = req.json()).object_words

    @classmethod
    def winged(cls) -> int | ObjectWinged:
        req = cls._session.post(url = cls._url('winged'), data = cls._data, headers = cls._headers)
        if req.status_code != 200: return req.status_code
        else: return ObjectWinged(data = req.json()).object_winged

    @classmethod
    def alcohol_drinking(cls) -> int | ObjectAlcoholDrinking:
        req = cls._session.post(url = cls._url('alcohol-drinking'), data = cls._data, headers = cls._headers)
        if req.status_code != 200: return  req.status_code
        else: return ObjectAlcoholDrinking(data = req.json()).object_alcohol_drinking

    @classmethod
    def alias(cls, animal : str, sex : int) -> int | ObjectAlias:
        """
        This function is designed to generate an alias for an animal

        :param animal: subspecies of animals, variants : cat, dog, bird, fish, rodent, horse, reptile, amphibia
        :type animal: :obj: `str`

        :param sex: sex - gender, variants : 1 or 2
        :type sex: :obj: `str`

        :return: an alias for an animal in json format
        """
        cls._data.update(alias = animal, sex = sex)
        req = cls._session.post(url = cls._url('alias'), headers = cls._headers, data = cls._data)
        if req.status_code != 200: return req.status_code
        else: return ObjectAlias(data = req.json()).object_alias

    @classmethod
    def slogan(cls, slogan : str) -> int | ObjectSlogan:
        """
        This function generates your slogan

        :param slogan: The name of an object
        :type slogan: :obj: `str`

        :return: Slogan in json format
        """
        cls._data.update(slogan = slogan)
        req = cls._session.post(url = cls._url('slogan'), headers = cls._headers, data = cls._data)
        if req.status_code != 200: return req.status_code
        else: return ObjectSlogan(data = req.json()).object_slogan

    @classmethod
    def login(cls, firstname : str, surname : str, patronymic : str, nickname : str) -> int | ObjectLogin:
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
        cls._data.update(firstname = firstname, surname = surname, patronymic = patronymic, nickname = nickname)
        req = cls._session.post(url = cls._url('login'), headers = cls._headers, data = cls._data)
        if req.status_code != 200: return req.status_code
        else: return ObjectLogin(data = req.json()).object_login