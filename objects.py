class obj_anime:
    def __init__(self, data):
        self.json = data
        self.result =  None
        self.nameRu = None
        self.nameEn = None

    @property
    def obj_anime(self):
        try: self.result = self.json['result']
        except(KeyError, TypeError): pass
        try: self.nameRu = self.json['result']['nameRu']
        except(KeyError, TypeError): pass
        try: self.nameEn = self.json['result']['nameEn']
        except(KeyError, TypeError): pass
        return self

class obj_words:
    def __init__(self, data):
        self.json = data
        self.result = None
        self.word = None
        self.wData = None

    @property
    def obj_words(self):
        try: self.result = self.json['result']
        except(KeyError, TypeError): pass
        try: self.word = self.json['result']['word']
        except(KeyError, TypeError): pass
        try: self.wData = self.json['result']['wData']
        except(KeyError, TypeError): pass
        return self

class obj_winged:
    def __init__(self, data):
        self.json = data
        self.result = None
        self.phrase = None
        self.source = None

    @property
    def obj_winged(self):
        try: self.result = self.json['result']
        except(KeyError, TypeError): pass
        try: self.phrase = self.json['result']['phrase']
        except(KeyError, TypeError): pass
        try: self.source = self.json['result']['source']
        except(KeyError, TypeError): pass
        return self

class obj_alcohol_drinking:
    def __init__(self, data):
        self.json = data
        self.result = None
        self.nameRu = None
        self.nameEn = None
        self.typeAlcohol = None
        self.ingredients = None

    @property
    def obj_alcohol_drinking(self):
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

class obj_alias:
    def __init__(self, data):
        self.json = data
        self.result = None
        self.alias = None

    @property
    def obj_alias(self):
        try: self.result = self.json['result']
        except(KeyError, TypeError): pass
        try: self.alias = self.json['result']['alias']
        except(KeyError, TypeError): pass
        return self

class obj_slogan:
    def __init__(self, data):
        self.json = data
        self.slogan = None

    @property
    def obj_slogan(self):
        try: self.slogan = self.json['result']
        except(KeyError, TypeError): pass
        return self

class obj_login:
    def __init__(self, data):
        self.json = data
        self.result = None

    @property
    def obj_login(self):
        try: self.result = self.json['result']
        except(KeyError, TypeError): pass
        return self
