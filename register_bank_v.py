from amaranth.back import verilog

from register_bank import RegisterBank

top = RegisterBank()


with open("register_bank.v", "w") as f:
    f.write(verilog.convert(top, ports=[top.reset, top.regNum0, top.regNum1, top.wRegNum, top.writeEnable, top.dataOut0, top.dataOut1, top.dataIn]))