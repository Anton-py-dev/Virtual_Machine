"""
bytecode

0x00 IDLE,    1 byte, no ops - idle command
0x01 LOAD     3 byte, 2 op   - load op2 to R(op1)
0X02 AND      3 byte, 2 ops  - R(op1) = R(op1) & R(op2)
0Х03 MOV      3 byte, 2 ops  - R(op2) -> R(op1)
0X04 ADD      3 byte, 2 ops  - R(op1) = R(op1) + R(op2)
0X05 CMP      3 byte, 2 ops  - if R(op1) == R(op2) => ZF=1; else ZF=0
"""


class VirtualMachine:
    def __init__(self, bytecode):
        self.bytecode = bytecode
        self.command_pointer = 0
        # Registers
        self.R = [0] * 16
        # Flags
        self.ZF = 0
        self.run()

    def get_op(self):
        ret = self.bytecode[self.command_pointer]
        self.command_pointer = self.command_pointer + 1
        return ret

    def run(self):
        while self.command_pointer < len(self.bytecode):
            command = self.bytecode[self.command_pointer]
            self.command_pointer = self.command_pointer + 1
            print("Command: ", str(command))

            # IDLE
            if command == 0x00:
                continue

            # LOAD
            if command == 0x01:
                op1 = self.get_op()
                op2 = self.get_op()

                self.R[op1] = op2
                print("R[", op1, "]: ", self.R[op1])

                continue

            # AND R(op1) & R(op2)
            if command == 0x02:
                op1 = self.get_op()
                op2 = self.get_op()
                self.R[op1] = self.R[op1] & self.R[op2]
                print("R[", op1, "]: ", self.R[op1])
                continue

            # MOV  R(op2) -> R(op1)
            if command == 0x03:
                op1 = self.get_op()
                op2 = self.get_op()

                self.R[op1] = self.R[op2]
                print("R[", op1, "]: ", self.R[op1])
                continue

            # ADD  R(op1) = R(op1) + R(op2)
            if command == 0x04:
                op1 = self.get_op()
                op2 = self.get_op()

                self.R[op1] = self.R[op1] + self.R[op2]
                print("R[", op1, "]: ", self.R[op1])
                continue

            # CMP  if R(op1) == R(op2) => ZF=1; else ZF=0
            if command == 0x05:
                op1 = self.get_op()
                op2 = self.get_op()

                if self.R[op1] == self.R[op2]:
                    self.ZF = 1

                print("R[", op1, "]: ", self.R[op1], "R[", op2, "]: ", self.R[op2], "ZF: ", self.ZF)
                continue
