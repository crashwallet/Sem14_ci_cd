from app import list_ops 

lst = [1,2,3,4,5,6,7,8,9,10]

def test_app(a: list):
    assert list_ops(a) == 915
    
