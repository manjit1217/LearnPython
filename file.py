def file():
    f=open("demo.txt","w+")
    for i in range(10):
        f.write("this is a file")
    f.close()


file()