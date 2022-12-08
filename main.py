from LFSR import LFSR
from G import G
import extensions

def test_LFSR1():
    generator = G()
    LFSR_1 = generator.LFSR1
    expected_outputs1 = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 
                         0, 1, 0, 0, 0, 0, 1, 1, 0, 0,
                         0, 1, 0, 1, 0, 0, 1, 1, 1, 1,
                         0, 1, 0, 0, 0, 1, 1, 1, 0, 0,
                         1, 0, 0, 1, 0, 1, 1, 0, 1, 1,
                         1, 0, 1, 1, 0, 0, 1, 1, 0, 1,
                         0, 1, 0]

    for i in range(LFSR_1.period):
        if LFSR_1.step() != expected_outputs1[i]:
            print("test_LFSR1 failed :(")
            return
    print("test_LFSR1 passed!!! :D")

def test_LFSR2():
    generator = G()
    LFSR_2 = generator.LFSR2
    expected_outputs2 = [1, 1, 1, 1, 0, 0, 0, 1, 0, 0,
                         1, 1, 0, 1, 0]

    for i in range(LFSR_2.period):
        if LFSR_2.step() != expected_outputs2[i]:
            print("test_LFSR2 failed :(")
            return
    print("test_LFSR2 passed!!! :D")

def test_G():
    generator = G()
    outputs = []

    for i in range(10000):
        outputs.append(generator.step())

    print(''.join(str(e) for e in outputs))
if __name__ == '__main__':
    test_LFSR1()
    test_LFSR2()
    test_G()