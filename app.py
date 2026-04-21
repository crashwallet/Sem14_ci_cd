def compare(a: int, b: int) -> bool:
    if a > b:
        return f"{a} is bigger than {b}"
    elif a < b:
        return f"{a} is smaller than {b}"
    else:
        return f"{a} is equal to {b}"

if __name__ == "__main__":
    print("Result:", compare(10, 9))
    