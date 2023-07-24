class ObjectAnime:
    def __init__(self, data):
        self.json = data
        self.result =  None
        self.name_ru = None
        self.name_en = None

    @property
    def object_anime(self):
        try:
            self.result = self.json['result']
            self.name_ru = self.json['result']['nameRu']
            self.name_en = self.json['result']['nameEn']
        except(KeyError, TypeError): pass
        return self

class ObjectWords:
    def __init__(self, data):
        self.json = data
        self.result = None
        self.word = None
        self.w_data = None

    @property
    def object_words(self):
        try:
            self.result = self.json['result']
            self.word = self.json['result']['word']
            self.w_data = self.json['result']['wData']
        except(KeyError, TypeError): pass
        return self

class ObjectWinged:
    def __init__(self, data):
        self.json = data
        self.result = None
        self.phrase = None
        self.source = None

    @property
    def object_winged(self):
        try:
            self.result = self.json['result']
            self.phrase = self.json['result']['phrase']
            self.source = self.json['result']['source']
        except(KeyError, TypeError): pass
        return self

class ObjectAlcoholDrinking:
    def __init__(self, data):
        self.json = data
        self.result = None
        self.name_ru = None
        self.name_en = None
        self.type_alcohol = None
        self.ingredients = None

    @property
    def object_alcohol_drinking(self):
        try:
            self.result = self.json['result']
            self.name_ru = self.json['result']['nameRu']
            self.name_en = self.json['result']['nameEn']
            self.type_alcohol = self.json['result']['typeAlcohol']
            self.ingridients = self.json['ingridients']
        except(KeyError, TypeError): pass
        return self

class ObjectAlias:
    def __init__(self, data):
        self.json = data
        self.result = None
        self.alias = None

    @property
    def object_alias(self):
        try:
            self.result = self.json['result']
            self.alias = self.json['result']['alias']
        except(KeyError, TypeError): pass
        return self

class ObjectSlogan:
    def __init__(self, data):
        self.json = data
        self.slogan = None

    @property
    def object_slogan(self):
        try:
            self.slogan = self.json['result']
        except(KeyError, TypeError): pass
        return self

class ObjectLogin:
    def __init__(self, data):
        self.json = data
        self.result = None

    @property
    def object_login(self):
        try: self.result = self.json['result']
        except(KeyError, TypeError): pass
        return self
