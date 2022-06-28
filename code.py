import time

record = []
event = ['33', '22', '44', '55', '66', '77', '3BLD', 'FMC', 'OH',
         'Clock', 'Mega', 'Pyra', 'Skewb', 'SQ-1', '4BLD', '5BLD', 'MBLD']
worst = 0.0001
best = 1000000.0

ev = int(input('종목 코드: '))
print('당신이 선택한 종목은', event[ev-1], '입니다.')
print('')

if ev-1 < 4 or ev-1 > 8 and ev-1 < 14:
    for i in range(5):
        print(i+1, '회차')
        r = float(input('기록 : '))
        record. append(r)
        print('')
        time.sleep(0.1)

    for i in range(5):
        if best > record[i]:
            best = record[i]

    for i in range(5):
        if worst < record[i]:
            worst = record[i]

    avg = 0.001
    for i in range(5):
        avg = avg+record[i]

    print(record)
    print(f"Ao 5 : {(avg-best-worst-0.001)/3 : .2f}")

elif ev-1 > 3 and ev-1 < 8 or ev-1 == 14 and ev-1 == 15:
    for i in range(3):
        print(i+1, '회차')
        r = float(input('기록 : '))
        record. append(r)
        print('')
        time.sleep(0.1)

    avg = 0.001
    for i in range(3):
        avg = avg+record[i]

    print(record)
    print(f"Mo 3 : {(avg-0.001)/3 : .2f}")

elif ev-1 == 16:
    c = int(input('시도한 큐브 개수 : '))
    time.sleep(0.1)
    s = int(input('성공한 큐브 개수 : '))
    time.sleep(0.1)
    f = int(input('실패한 큐브 개수 : '))
    time.sleep(0.1)
    t = float(input('시간 : '))

    print(s, '/', c, '%(', s-f, '점%)', t)
