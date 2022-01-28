from amaranth.sim import Simulator, Settle
from alu import ALU, ALUOps
from inttools import *

import random

dut = ALU()

def randInt():
    return int(random.random() * 0xFFFFFFFF) & 0xFFFFFFFF

iters = 16

def bench():
    # Test ADD
    print("Testing ADD")
    for i in range(iters):
        x = randInt()
        y = randInt()
        expectedResult = (x+y) & 0xFFFFFFFF
        yield dut.X.eq(x)
        yield dut.Y.eq(y)
        yield dut.Operation.eq(ALUOps.ADD)
        yield Settle()

        result = yield dut.O
        assert(result == expectedResult)

    # Test SUB
    print("Testing SUB")
    for i in range(iters):
        x = randInt()
        y = randInt()
        expectedResult = (x-y) & 0xFFFFFFFF
        yield dut.X.eq(x)
        yield dut.Y.eq(y)
        yield dut.Operation.eq(ALUOps.SUB)
        yield Settle()

        result = yield dut.O
        assert(result == expectedResult)

    # Test OR
    print("Testing OR")
    for i in range(iters):
        x = randInt()
        y = randInt()
        expectedResult = (x|y) & 0xFFFFFFFF
        yield dut.X.eq(x)
        yield dut.Y.eq(y)
        yield dut.Operation.eq(ALUOps.OR)
        yield Settle()

        result = yield dut.O
        assert(result == expectedResult)

    # Test XOR
    print("Testing XOR")
    for i in range(iters):
        x = randInt()
        y = randInt()
        expectedResult = (x^y) & 0xFFFFFFFF
        yield dut.X.eq(x)
        yield dut.Y.eq(y)
        yield dut.Operation.eq(ALUOps.XOR)
        yield Settle()

        result = yield dut.O
        assert(result == expectedResult)

    # Test AND
    print("Testing AND")
    for i in range(iters):
        x = randInt()
        y = randInt()
        expectedResult = (x&y) & 0xFFFFFFFF
        yield dut.X.eq(x)
        yield dut.Y.eq(y)
        yield dut.Operation.eq(ALUOps.AND)
        yield Settle()

        result = yield dut.O
        assert(result == expectedResult)

    # Test LesserThanUnsigned
    print("Testing LesserThanUnsigned")
    for i in range(iters):
        x = randInt()
        y = randInt()
        expectedResult = 1 if (x < y) else 0
        yield dut.X.eq(x)
        yield dut.Y.eq(y)
        yield dut.Operation.eq(ALUOps.LesserThanUnsigned)
        yield Settle()

        result = yield dut.O
        assert(result == expectedResult)

    # Test LesserThanSigned
    print("Testing LesserThanSigned")
    for i in range(iters):
        x = randInt()
        y = randInt()
        expectedResult = 1 if (int32(x) < int32(y)) else 0
        yield dut.X.eq(x)
        yield dut.Y.eq(y)
        yield dut.Operation.eq(ALUOps.LesserThanSigned)
        yield Settle()

        result = yield dut.O
        assert(result == expectedResult)

    # Test ShiftRightUnsigned
    print("Testing ShiftRightUnsigned")
    for i in range(iters):
        x = randInt()
        y = randInt()
        expectedResult = (x >> (y % 32))
        yield dut.X.eq(x)
        yield dut.Y.eq(y)
        yield dut.Operation.eq(ALUOps.ShiftRightUnsigned)
        yield Settle()

        result = yield dut.O
        assert(result == expectedResult)

    # Test ShiftRightSigned
    print("Testing ShiftRightSigned")
    for i in range(iters):
        x = randInt()
        y = randInt()
        expectedResult = (int32(x) >> (y % 32)) & 0xFFFFFFFF
        yield dut.X.eq(x)
        yield dut.Y.eq(y)
        yield dut.Operation.eq(ALUOps.ShiftRightSigned)
        yield Settle()

        result = yield dut.O
        assert(result == expectedResult)

    # Test ShiftLeftUnsigned
    print("Testing ShiftLeftUnsigned")
    for i in range(iters):
        x = randInt()
        y = randInt()
        expectedResult = (x << (y % 32)) & 0xFFFFFFFF
        yield dut.X.eq(x)
        yield dut.Y.eq(y)
        yield dut.Operation.eq(ALUOps.ShiftLeftUnsigned)
        yield Settle()

        result = yield dut.O
        assert(result == expectedResult)

    # Test ShiftLeftSigned
    print("Testing ShiftLeftSigned")
    for i in range(iters):
        x = randInt()
        y = randInt()
        expectedResult = (int32(x) << (y % 32)) & 0xFFFFFFFF
        yield dut.X.eq(x)
        yield dut.Y.eq(y)
        yield dut.Operation.eq(ALUOps.ShiftLeftSigned)
        yield Settle()

        result = yield dut.O
        assert(result == expectedResult)

    # Test GreaterThanOrEqualUnsigned
    print("Testing GreaterThanOrEqualUnsigned")
    for i in range(iters):
        x = randInt()
        y = randInt()
        expectedResult = 1 if (x > y) else 0
        yield dut.X.eq(x)
        yield dut.Y.eq(y)
        yield dut.Operation.eq(ALUOps.GreaterThanOrEqualUnsigned)
        yield Settle()

        result = yield dut.O
        assert(result == expectedResult)

    # Test GreaterThanOrEqualSigned
    print("Testing GreaterThanOrEqualSigned")
    for i in range(iters):
        x = randInt()
        y = randInt()
        expectedResult = 1 if (int32(x) > int32(y)) else 0
        yield dut.X.eq(x)
        yield dut.Y.eq(y)
        yield dut.Operation.eq(ALUOps.GreaterThanOrEqualSigned)
        yield Settle()

        result = yield dut.O
        assert(result == expectedResult)

    # Test Equal
    print("Testing Equal")
    for i in range(iters):
        x = randInt()
        y = randInt()
        expectedResult = 1 if (x == y) else 0
        yield dut.X.eq(x)
        yield dut.Y.eq(y)
        yield dut.Operation.eq(ALUOps.Equal)
        yield Settle()

        result = yield dut.O
        assert(result == expectedResult)

    # Test NotEqual
    print("Testing NotEqual")
    for i in range(iters):
        x = randInt()
        y = randInt()
        expectedResult = 1 if (x != y) else 0
        yield dut.X.eq(x)
        yield dut.Y.eq(y)
        yield dut.Operation.eq(ALUOps.NotEqual)
        yield Settle()

        result = yield dut.O
        assert(result == expectedResult)

sim = Simulator(dut)
sim.add_process(bench)
with sim.write_vcd("alu.vcd"):
    sim.run()
