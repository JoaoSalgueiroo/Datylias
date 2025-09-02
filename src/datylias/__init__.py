#Datalyas module

from z3 import Concat, BitVecRef

def qword(data: list[BitVecRef], index: int) -> BitVecRef:
    return Concat(*data[index:index+8])

def dword(data: list[BitVecRef], index: int) -> BitVecRef:
    return Concat(*data[index:index+4])

def hidword(data: list[BitVecRef], index: int) -> BitVecRef:
    return Concat(*data[index+4:index+8])

def lodword(data: list[BitVecRef], index: int) -> BitVecRef:
    return Concat(*data[index:index+4])

def word(data: list[BitVecRef], index: int) -> BitVecRef:
    return Concat(*data[index:index+2])

def loword(data: list[BitVecRef], index: int) -> BitVecRef:
    return Concat(*data[index:index+2])

def hiword(data: list[BitVecRef], index: int) -> BitVecRef:
    return Concat(*data[index+2:index+4])

def byte(data: list[BitVecRef], index: int) -> BitVecRef:
    return data[index]

def lobyte(data: list[BitVecRef], index: int) -> BitVecRef:
    return data[index]

def hibyte(data: list[BitVecRef], index: int) -> BitVecRef:
    return data[index+1]


__all__ = [
    "qword", "dword", "hidword", "lodword",
    "word", "loword", "hiword", "byte", "lobyte", "hibyte"
]
