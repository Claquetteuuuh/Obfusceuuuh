import random

def commentropy(payload: str):
    r_p = payload.replace(";", f";<#{'*' * random.randint(30, 40)}#>")
    return r_p

if __name__ == "__main__": 
    pass