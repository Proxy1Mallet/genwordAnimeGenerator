class Anime:
    def __init__(self, data):
        self.json = data
        self.result =  None
        self.nameRu = None
        self.nameEn = None

    @property
    def Anime(self):
        try: self.result = self.json['result']
        except(KeyError, TypeError): pass
        try: self.nameRu = self.json['result']['nameRu']
        except(KeyError, TypeError): pass
        try: self.nameEn = self.json['result']['nameEn']
        except(KeyError, TypeError): pass
        return self

class Words:
    def __init__(self, data):
        self.json = data
        self.result = None
        self.word = None
        self.wData = None

    @property
    def Words(self):
        try: self.result = self.json['result']
        except(KeyError, TypeError): pass
        try: self.word = self.json['result']['word']
        except(KeyError, TypeError): pass
        try: self.wData = self.json['result']['wData']
        except(KeyError, TypeError): pass
        return self

class Winged:
    def __init__(self, data):
        self.json = data
        self.result = None
        self.phrase = None
        self.source = None

    @property
    def Winged(self):
        try: self.result = self.json['result']
        except(KeyError, TypeError): pass
        try: self.phrase = self.json['result']['phrase']
        except(KeyError, TypeError): pass
        try: self.source = self.json['result']['source']
        except(KeyError, TypeError): pass
        return self

class AlcoholDrinking:
    def __init__(self, data):
        self.json = data
        self.result = None
        self.nameRu = None
        self.nameEn = None
        self.typeAlcohol = None
        self.ingredients = None

    @property
    def AlcoholDrinking(self):
        try: self.result = self.json['result']
        except(KeyError, TypeError): pass
        try: self.nameRu = self.json['result']['nameRu']
        except(KeyError, TypeError): pass
        try: self.nameEn = self.json['result']['nameEn']
        except(KeyError, TypeError): pass
        try: self.typeAlcohol = self.json['result']['typeAlcohol']
        except(KeyError, TypeError): pass
        try: self.typeAlcohol = self.json['ingridients']
        except(KeyError, TypeError): pass
        return self

class Alias:
    def __init__(self, data):
        self.json = data
        self.result = None
        self.alias = None

    @property
    def Alias(self):
        try: self.result = self.json['result']
        except(KeyError, TypeError): pass
        try: self.alias = self.json['result']['alias']
        except(KeyError, TypeError): pass
        return self

class Slogan:
    def __init__(self, data):
        self.json = data
        self.slogan = None

    @property
    def Slogan(self):
        try: self.slogan = self.json['result']
        except(KeyError, TypeError): pass
        return self

class Login:
    def __init__(self, data):
        self.json = data
        self.result = None

    @property
    def Login(self):
        try: self.result = self.json['result']
        except(KeyError, TypeError): pass