i = 1
while True:
    i += 1
    print(i)
    cmd = 1
    if i % 2 == 0:
        cmd = input('是否终止？')
        print(cmd)
    if cmd == '2':
        break


