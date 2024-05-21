from requests import Session, get

from .objects import *

class Genword:
    _url = 'https://genword.ru/generators/{}/new/'.format

    @classmethod
    def __request_method(cls, method: str, url: str, data: dict = None):
        session = Session()

        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 YaBrowser/24.4.0.0 Safari/537.36",
            'x-requested-with': 'XMLHttpRequest'
        }

        if method == 'post': req = session.post(url = url,
                                                data = data,
                                                headers = headers)
        else: req = session.get(url = url,
                                headers = headers)

        if req.status_code == 200: return req
        print(f'Error >>> {req.status_code} {req.text}')
        exit()


    @classmethod
    def anime(cls) -> Anime:
        return Anime(
            **cls.__request_method(method = 'post',
                                   url = cls._url('anime')
                                   ).json()['result']
        )

    @classmethod
    def words(cls) -> Words:
        return Words(
            **cls.__request_method(method = 'post',
                                   url = cls._url('word')
                                   ).json()['result']
        )

    @classmethod
    def winged(cls) -> Winged:
        return Winged(
            **cls.__request_method(method = 'post',
                                   url = cls._url('winged')
                                   ).json()['result']
        )

    @classmethod
    def alcohol_drinking(cls) -> AlcoholDrinking:
        return AlcoholDrinking(
            **cls.__request_method(method = 'post',
                                   url = cls._url('alcohol-drinking')
                                   ).json()['result']
        )

    @classmethod
    def alias(cls, animal : str, sex : int) -> Alias:
        """
        This function is designed to generate an alias for an animal

        :param animal: subspecies of animals, variants : cat, dog, bird, fish, rodent, horse, reptile, amphibia
        :type animal: :obj: `str`

        :param sex: sex - gender, variants : 1 or 2
        :type sex: :obj: `str`

        :return: an alias for an animal in json format
        """
        data = {
            'alias': animal,
            'sex': sex
        }

        return Alias(
            **cls.__request_method(method = 'post',
                                   url = cls._url('alias'),
                                   data = data
                                   ).json()['result']
        )

    @classmethod
    def slogan(cls, slogan : str):
        """
        This function generates your slogan

        :param slogan: The name of an object
        :type slogan: :obj: `str`

        :return: Slogan in json format
        """
        data = {
            'slogan': slogan
        }

        return (
            cls.__request_method(method = 'post',
                                 url = cls._url('slogan'),
                                 data = data
                                 ).json()['result']
        )

    @classmethod
    def login(cls, firstname : str, surname : str, patronymic : str, nickname : str) -> list[Login]:
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
        #cls._data.update(firstname = firstname, surname = surname, patronymic = patronymic, nickname = nickname)
        data = {
            'firstname': firstname,
            'surname': surname,
            'patronymic': patronymic,
            'nickname': nickname
        }

        return [
            Login(**data) for data in cls.__request_method(method = 'post',
                                   url = cls._url('login'),
                                   data = data
                                   ).json()['result']
        ]