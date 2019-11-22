
def seldom(**kwargs):
    print(kwargs)
    for by, value in kwargs.items():
        print(by, value)

seldom(css="#el")
