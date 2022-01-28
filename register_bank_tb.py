from amaranth.sim import Simulator
import random

from register_bank import RegisterBank

dut = RegisterBank()

def bench():
    # Reset all inputs
    yield dut.reset.eq(1)
    yield dut.regNum0.eq(0)
    yield dut.regNum1.eq(0)
    yield dut.wRegNum.eq(0)

    yield

    valuesToWrite = [ int(random.random() * 0xFFFFFFFF) & 0xFFFFFFFF for _ in range(16) ]
    valuesExpected = [ x for x in valuesToWrite ]
    valuesExpected[0] = 0 # X0 is always 0

    yield dut.reset.eq(0)
    yield

    for i in range(len(valuesToWrite)):
        yield dut.wRegNum.eq(i)
        yield dut.writeEnable.eq(1)
        yield dut.dataIn.eq(valuesToWrite[i])
        yield
        yield dut.writeEnable.eq(0)
        yield dut.dataIn.eq(~valuesToWrite[i])
        yield

    # Test dataOut0
    for i in range(len(valuesToWrite)):
        yield dut.regNum0.eq(i)
        yield
        yield
        print((yield dut.dataOut0), valuesExpected[i])
        assert ((yield dut.dataOut0) == valuesExpected[i])


    # Test dataOut1
    for i in range(len(valuesToWrite)):
        yield dut.regNum1.eq(i)
        yield
        yield
        assert ((yield dut.dataOut1) == valuesExpected[i])



sim = Simulator(dut)
sim.add_clock(1e-6) # 1 MHz
sim.add_sync_process(bench)
with sim.write_vcd("register_bank.vcd"):
    sim.run()
