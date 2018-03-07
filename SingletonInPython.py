class MySingleton:
    
    __instance = None
    
    def __setattr__(self, prop, value):
        self.__dict__[prop] = value
        
    def __getattr__(self, prop):
        return self.__dict__[prop]

    @staticmethod
    def getMySingleton(name, age):
        if MySingleton.__instance is None:
            print "MySingleton instance is None"
            MySingleton.__instance = MySingleton()
            setattr(MySingleton.__instance, 'name', name)
            setattr(MySingleton.__instance, 'age', age)
            self = MySingleton.__instance
            return MySingleton.__instance
        else:
            self = MySingleton.__instance
            return MySingleton.__instance
        
    def __str__(self):
        return 'name : {0} & age: {1}'.format(MySingleton.__instance.name, MySingleton.__instance.age)
    
    def __hash__(self):
        return hash(MySingleton.__instance.name) + hash(MySingleton.__instance.age) 
        

ram = MySingleton.getMySingleton('ram', '23')
MySingleton.__instance = None
laki = MySingleton.getMySingleton('laki', '22')

print hash(ram), id(ram), ram.__dict__, ram
print hash(laki), id(laki), laki.__dict__, laki
