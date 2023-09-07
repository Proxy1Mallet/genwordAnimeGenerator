from requests import Session
from fake_useragent import FakeUserAgent

from .objects import *

class Data:
    _session = Session()
    _url = 'https://genword.ru/generators/{}/new/'.format
    _headers = {
        'user-agent': FakeUserAgent().random,
        'x-requested-with': 'XMLHttpRequest'
    }
    _data = {
        'x-csrf-token': _session.get(url = 'https://genword.ru/', headers = _headers).headers['X-CSRF-Token']
    }

class GenwordAPI(Data):
    @classmethod
    def anime(cls) -> int | Anime:
        _req = cls._session.post(url = cls._url('anime'), data = cls._data, headers = cls._headers)
        return _req.status_code if _req.status_code != 200 else Anime(**_req.json()['result'])

    @classmethod
    def words(cls) -> int | Words:
        _req = cls._session.post(url = cls._url('word'), data = cls._data, headers = cls._headers)
        return _req.status_code if _req.status_code != 200 else Words(**_req.json()['result'])

    @classmethod
    def winged(cls) -> int | Winged:
        _req = cls._session.post(url = cls._url('winged'), data = cls._data, headers = cls._headers)
        return _req.status_code if _req.status_code != 200 else Winged(**_req.json()['result'])

    @classmethod
    def alcohol_drinking(cls) -> int | AlcoholDrinking:
        _req = cls._session.post(url = cls._url('alcohol-drinking'), data = cls._data, headers = cls._headers)
        return _req.status_code if _req.status_code != 200 else AlcoholDrinking(**_req.json()['result'])

    @classmethod
    def alias(cls, animal : str, sex : int) -> int | Alias:
        """
        This function is designed to generate an alias for an animal

        :param animal: subspecies of animals, variants : cat, dog, bird, fish, rodent, horse, reptile, amphibia
        :type animal: :obj: `str`

        :param sex: sex - gender, variants : 1 or 2
        :type sex: :obj: `str`

        :return: an alias for an animal in json format
        """
        cls._data.update(alias = animal, sex = sex)
        _req = cls._session.post(url = cls._url('alias'), headers = cls._headers, data = cls._data)
        return _req.status_code if _req.status_code != 200 else Alias(**_req.json()['result'])

    @classmethod
    def slogan(cls, slogan : str) -> int | ObjectSlogan:
        """
        This function generates your slogan

        :param slogan: The name of an object
        :type slogan: :obj: `str`

        :return: Slogan in json format
        """
        cls._data.update(slogan = slogan)
        _req = cls._session.post(url = cls._url('slogan'), headers = cls._headers, data = cls._data)
        return _req.status_code if _req.status_code != 200 else Slogan(**_req.json()['result'])

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
        _req = cls._session.post(url = cls._url('login'), headers = cls._headers, data = cls._data)
        return _req.status_code if _req.status_code != 200 else Login(**_req.json())