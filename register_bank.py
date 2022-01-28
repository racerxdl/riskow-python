from amaranth import *

class RegisterBank(Elaboratable):
    """
    RV32E Register Bank
    """

    def __init__(self):
        self.reset = Signal()
        self.regNum0 = Signal(4)
        self.regNum1 = Signal(4)
        self.wRegNum = Signal(4)
        self.writeEnable = Signal()

        self.dataOut0 = Signal(32)
        self.dataOut1 = Signal(32)
        self.dataIn = Signal(32)

    def elaborate(self, platform):
        m = Module()

        storage = Memory(width=32, depth=16)
        w_port  = m.submodules.w_port = storage.write_port()
        r0_port = m.submodules.r0_port = storage.read_port()
        r1_port = m.submodules.r1_port = storage.read_port()

        enable = (self.reset == 0)
        do_write = (enable) & (self.writeEnable == 1) & (self.wRegNum != 0)

        m.d.comb += [
            w_port.addr.eq(self.wRegNum),
            w_port.data.eq(self.dataIn),
            w_port.en.eq(do_write),

            r0_port.addr.eq(self.regNum0),
            self.dataOut0.eq(r0_port.data),

            r1_port.addr.eq(self.regNum1),
            self.dataOut1.eq(r1_port.data),
        ]

        return m

