class ImmDict:
    def __init__(self, the_dict={}):
        self.dict = the_dict

    def put(self, key, val):
        new_dict = self.dict.copy()
        new_dict[key] = val
        return ImmDict(new_dict)

    def get(self, val):
        if self.dict.__contains__(val):
            return self.dict[val]
        return None

    def keys(self):
        return [i for i in self.dict.keys()]

    def values(self):
        return [i for i in self.dict.values()]
