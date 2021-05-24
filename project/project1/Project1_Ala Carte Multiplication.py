def multiplication(x, y):
    ans = 0
    a = abs(x)
    b = abs(y)
    dict = {a: b}
    while a > 1:
        a = a//2
        b = b*2
        dict.update({a: b})
    for key, value in dict.items():
        if int(key)%2 == 1:
            ans = ans+int(value)
    if (x > 0 and y < 0) or (x <0 and y > 0):
        print('-', ans, sep='')
    else:
        print(ans)


if __name__ == '__main__':
    multiplication(7000, 7294)
    multiplication(25, 5038385)
    multiplication(-59724, 783)
    multiplication(8516, -82147953548159344)
    multiplication(45952456856498465985, 98654651986546519856)
    multiplication(-45952456856498465985, -98654651986546519856)