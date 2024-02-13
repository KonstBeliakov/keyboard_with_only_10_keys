import keyboard
from time import perf_counter
from string import ascii_lowercase

if __name__ == '__main__':
    t = perf_counter()
    prev_pressed = None
    d2 = []
    for i in 'qwerv':
        for j in 'nuiop':
            d2.append(i + j)
    d2.append('qw')
    d2.append('qe')
    d2.append('qr')

    d2 = {i: j for i, j in zip(d2, list(ascii_lowercase) + [' ', '\n'])}
    d3 = {value: key for key, value in d2.items()}

    for i, key in enumerate(d3.keys()):
        print(key if key != '\n' else '\\n', d3[key], end='\t')
        if i % 4 == 3:
            print()

    while True:
        for i in d2:
            if all([keyboard.is_pressed(j) for j in i]):
                if prev_pressed != d2[i] or perf_counter() - t > 0.2:
                    print(d2[i], end='')
                    prev_pressed = d2[i]
                    t = perf_counter()
