def readfile(filename):
    try:
            with open (filename) as f:
                text=f.read()
                print(text)
    except FileNotFoundError as e:
            print("There is no such file")

readfile("1.txt")
readfile("2.txt")
readfile("3.txt")