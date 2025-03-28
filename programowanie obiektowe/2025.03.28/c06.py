class BaseClass:
    def __new__(cls):
        obj = super().__new__(cls)
        obj._from_base_class = type(obj) == BaseClass
        return obj
    
class SubClass(BaseClass):
    pass


base_instance = BaseClass()
sub_instance = SubClass()

print(base_instance._from_base_class)
print(sub_instance._from_base_class) 