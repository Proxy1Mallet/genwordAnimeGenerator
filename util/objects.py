class Anime:
    def __init__(self, data):
        self.json = data
        self.result =  None
        self.nameRu = None
        self.nameEn = None

    @property
    def Anime(self):
        self.result = self.json['result']
        self.nameRu = self.json['result']['nameRu']
        self.nameEn = self.json['result']['nameEn']
        return self

class Words:
    def __init__(self, data):
        self.json = data
        self.result = None
        self.word = None

    @property
    def Words(self):
        self.result = self.json['result']
        self.word = self.json['result']['word']
        return self

class Winged:
    def __init__(self, data):
        self.json = data
        self.result = None
        self.phrase = None
        self.source = None

    @property
    def Winged(self):
        self.result = self.json['result']
        self.phrase = self.json['result']['phrase']
        self.source = self.json['result']['source']
        return self

class AlcoholDrinking:
    def __init__(self, data):
        self.json = data
        self.result = None
        self.nameRu = None
        self.nameEn = None
        self.typeAlcohol = None

    @property
    def AlcoholDrinking(self):
        self.result = self.json['result']
        self.nameRu = self.json['result']['nameRu']
        self.nameEn = self.json['result']['nameEn']
        self.typeAlcohol = self.json['result']['typeAlcohol']
        return self

class Alias:
    def __init__(self, data):
        self.json = data
        self.result = None
        self.alias = None

    @property
    def Alias(self):
        self.result = self.json['result']
        self.alias = self.json['result']['alias']
        return self

class Slogan:
    def __init__(self, data):
        self.json = data
        self.slogan = None

    @property
    def Slogan(self):
        self.slogan = self.json
        return self

class Login:
    def __init__(self, data):
        self.json = data
        self.result = None
        self.login1 = None
        self.login2 = None
        self.login3 = None
        self.login4 = None
        self.login5 = None
        self.login6 = None
        self.login7 = None
        self.login8 = None
        self.login9 = None

    @property
    def Login(self):
        self.result = self.json['result']
        self.login1 = self.json['result'][0]['login']
        self.login2 = self.json['result'][1]['login']
        self.login3 = self.json['result'][2]['login']
        self.login4 = self.json['result'][3]['login']
        self.login5 = self.json['result'][4]['login']
        self.login6 = self.json['result'][5]['login']
        self.login7 = self.json['result'][6]['login']
        self.login8 = self.json['result'][7]['login']
        self.login9 = self.json['result'][8]['login']
        return self
