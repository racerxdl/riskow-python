import enum
from amaranth import *

class ALUOps(enum.Enum):
    ADD = enum.auto()
    SUB = enum.auto()
    OR = enum.auto()
    XOR = enum.auto()
    AND = enum.auto()
    LesserThanUnsigned = enum.auto()
    LesserThanSigned = enum.auto()
    ShiftRightUnsigned = enum.auto()
    ShiftRightSigned = enum.auto()
    ShiftLeftUnsigned = enum.auto()
    ShiftLeftSigned = enum.auto()
    GreaterThanOrEqualUnsigned = enum.auto()
    GreaterThanOrEqualSigned = enum.auto()
    Equal = enum.auto()
    NotEqual = enum.auto()

class ALU(Elaboratable):

    def __init__(self):
        self.X = Signal(32)
        self.Y = Signal(32)
        self.O = Signal(32)
        self.Operation = Signal(4)

    def elaborate(self, platform):
        m = Module()

        with m.Switch(self.Operation):
            with m.Case(ALUOps.ADD):
                m.d.comb += self.O.eq(self.X + self.Y)
            with m.Case(ALUOps.SUB):
                m.d.comb += self.O.eq(self.X - self.Y)
            with m.Case(ALUOps.OR):
                m.d.comb += self.O.eq(self.X | self.Y)
            with m.Case(ALUOps.XOR):
                m.d.comb += self.O.eq(self.X ^ self.Y)
            with m.Case(ALUOps.AND):
                m.d.comb += self.O.eq(self.X & self.Y)
            with m.Case(ALUOps.LesserThanUnsigned):
                m.d.comb += self.O.eq(self.X < self.Y)
            with m.Case(ALUOps.LesserThanSigned):
                m.d.comb += self.O.eq(self.X.as_signed() < self.Y.as_signed())
            with m.Case(ALUOps.ShiftRightUnsigned):
                m.d.comb += self.O.eq(self.X >> self.Y[0:5])
            with m.Case(ALUOps.ShiftRightSigned):
                m.d.comb += self.O.eq(self.X.as_signed() >> self.Y[0:5])
            with m.Case(ALUOps.ShiftLeftUnsigned):
                m.d.comb += self.O.eq(self.X << self.Y[0:5])
            with m.Case(ALUOps.ShiftLeftSigned):
                m.d.comb += self.O.eq(self.X.as_signed() << self.Y[0:5])
            with m.Case(ALUOps.GreaterThanOrEqualUnsigned):
                m.d.comb += self.O.eq(self.X >= self.Y)
            with m.Case(ALUOps.GreaterThanOrEqualSigned):
                m.d.comb += self.O.eq(self.X.as_signed() >= self.Y.as_signed())
            with m.Case(ALUOps.Equal):
                m.d.comb += self.O.eq(self.X == self.Y)
            with m.Case(ALUOps.NotEqual):
                m.d.comb += self.O.eq(self.X != self.Y)

        return m