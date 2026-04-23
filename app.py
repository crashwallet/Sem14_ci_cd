def list_ops(a: list) -> int:
    evens, odds = 0, 1
    for x in a:
        if x % 2 == 1:
            odds *= x
        else:
            evens += x 
    return odds - evens

if __name__ == "__main__":
    print("Result:", list_ops([1,2,3,4,5,6,7,8,9,10]))
    