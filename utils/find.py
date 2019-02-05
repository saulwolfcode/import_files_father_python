def find_in(iterable,finder,expected):
    for i in iterable:
        if finder(i)==expected:
            return  i
    raise NotFoundError(f"{expected} not found provited iterable")

class NotFoundError(Exception):
  pass


if __name__=="__main__":
    print(find_in(["Saul","Jose","Jon"], lambda x:x,"Jose"))
    print(__name__)
    print("Padre find.py")

