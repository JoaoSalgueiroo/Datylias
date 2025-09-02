#Datylias python module

def qword(data: list, index: int) -> list:
    return data[index: index+8]

def dword(data: list, index: int) -> list: 
    return data[index: index+4]

def hidword(data: list, index: int) -> list:
    qword = data[index: index+8]
    return qword[4:8]

def lodword(data: list, index: int) -> list:
    qword = data[index: index+8]
    return qword[0:4]

def word(data: list, index: int) -> list:
    return data[index: index+2]

def loword(data: list, index: int) -> list:
    dword = data[index: index+4]
    return dword[0:2]

def hiword(data: list, index: int) -> list:
    dword = data[index: index+4]
    return dword[2:4]

def byte(data: list, index: int) -> int:
    return data[index]

def lobyte(data: list, index: int) -> int:
    word = data[index: index+2]
    return word[0]

def hibyte(data: list, index: int) -> int:
    word = data[index: index+2]
    return word[1]

__all__ = [
    "qword", "dword", "hidword", "lodword",
    "word", "loword", "hiword", "byte", "lobyte", "hibyte"
]