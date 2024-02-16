def fungsi(x):
    fx = 2*x**3 + 2*x + 15/x
    return fx

def main():
    x = int(input("masukkan bilangan bulat: "))
    hasil = fungsi(x)
    print ("hasil: ", hasil)

if __name__ == "__main__":
    main()