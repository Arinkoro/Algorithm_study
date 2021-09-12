

def function(*args):
    print(args, type(args))
    return 

def func(**kwargs):
    print(kwargs, type(kwargs))

class FilePathNamingError(Exception):
    pass
raise FilePathNamingError
def main():
    function(1, 2, 3, 4, 5)
    d = {"a":1, "b": 2}
    func(a=1, b=2)
    divisor = 100
    dividend = 1
    try: 
        result = divisor / dividend
    except Exception as e:
        # raise e
        print(e)
        result = 0
    else:
        print("ELSE")
    finally:
        print("FINALLY")
    

if __name__ == '__main__':
    main()