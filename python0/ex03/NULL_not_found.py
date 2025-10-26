def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None <class 'NoneType'>")
    elif isinstance(object, float) and str(object) == 'nan':
        print("Cheese: nan <class 'float'>")
    elif object == 0 and not isinstance(object, bool):
        print("Zero: 0 <class 'int'>")
    elif object == "":
        print("Empty: <class 'str'>")
    elif object is False:
        print("Fake: False <class 'bool'>")
    else:
        print("Type not Found")
        return 1
    return 0