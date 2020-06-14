# ---------------------------------------------<1>---------------------------------------------

kata = 'hello there how are you doing'


def hastag(string):
    if string == '':
        output = 'False'
    else:
        word = string.split(' ')
        output = '#'
        for x in range(len(word)):
            txt = word[x]
            txt = txt.capitalize()
            output += txt
    if len(output) - 1 > 140 or output == '#':
        output = 'False'
    return print(output)


hastag(kata)


# ---------------------------------------------<2>---------------------------------------------


pon = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def create_phone_number(number):
    output = '(xxx) xxx-xxxx'
    for num in number:
        output = output.replace('x', str(num), 1)
    return print(output)


create_phone_number(pon)


# ---------------------------------------------<3>---------------------------------------------


number = [5, 3, 2, 8, 1, 4]


def sort_odd_even(num):
    indexOdd = []
    indexEven = []

    # tracing

    for each in num:
        if each % 2 == 0 or each == 0:
            indexEven.append(num.index(each))
        else:
            indexOdd.append(num.index(each))

    # sorting

    for odd in range(len(indexOdd)-1):
        for oddx in range(odd+1, (len(indexOdd))):
            if num[(indexOdd[odd])] > num[(indexOdd[oddx])]:
                num[(indexOdd[odd])], num[(indexOdd[oddx])] = num[(
                    indexOdd[oddx])], num[(indexOdd[odd])]

    for even in range(len(indexEven)-1):
        for evenx in range(even+1, (len(indexEven))):
            if num[(indexEven[even])] < num[(indexEven[evenx])]:
                num[(indexEven[even])], num[(indexEven[evenx])] = num[(
                    indexEven[evenx])], num[(indexEven[even])]

    return print(num)


sort_odd_even(number)
