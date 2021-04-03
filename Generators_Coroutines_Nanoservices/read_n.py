def read_n(filename, n):
    f = open(filename)

    while True:
        output = ''.join(f.readline()
                         for i in range(n))

        if output:
            yield output
        else:
            break
