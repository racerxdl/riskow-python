from amaranth import *


class ProgramCounter(Elaboratable):

    def __init__(self):
        self.programCounter = Signal(32)
        self.dataIn = Signal(32)
        self.dataOut = Signal(32)
        self.writeEnable = Signal()
        self.writeAdd = Signal()
        self.countEnable = Signal()

    def elaborate(self, platform):
        m = Module()

        with m.If(self.writeEnable == 1):
            with m.If(self.writeAdd == 1):
                m.d.sync += self.programCounter.eq(self.programCounter + self.dataIn.as_signed() - 4)
            with m.Else():
                m.d.sync += self.programCounter.eq(self.dataIn)
        with m.Elif(self.countEnable == 1):
            m.d.sync += self.programCounter.eq(self.programCounter + 4)

        m.d.comb += self.dataOut.eq(self.programCounter)

        return m