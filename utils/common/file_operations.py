#from utils.find import NotFoundError

def save_to_file(content, filename):
    with open(filename, "w") as file:
        file.write(content)

def read_file(filename):
    with open(filename,"r") as file:
        return file.read()

print(__name__)
print("Padre file_operations.py")
