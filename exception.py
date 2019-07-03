# Video tutorial dari https://youtu.be/NIWwJbo-9_8

try:
    f = open('test.txt')
    # var = var_bad
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("executing finally")