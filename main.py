command_pointer = 0

'''
bytecode


0x00 IDLE,    1 byte, no ops - idle command
0x01 LOAD     3 byte, 2 op   - load op2 to R(op1)
0X02 AND      3 byte, 2 ops  - R(op1) = R(op1) & R(op2)
0Х03 MOV      3 byte, 2 ops  - R(op1) -> R(op2)
0X04 ADD      3 byte, 2 ops  - R(op1) = R(op1) + R(op2)
0X05 CMP      3 byte, 2 ops  - if R(op1) == R(op2) => ZF=1; else ZF=0
'''

bytecode = [0x00,
            0x01, 0x00, 0x03,
            0x01, 0x01, 0x03,
            0x05, 0x01, 0x00,
            0x04, 0x01, 0x00,
            0x03, 0x01, 0x00,
            0x02, 0x00, 0x01]

# Registers
R = [0] * 16

# Flags
ZF = 0

# Stack
S = [0] * 16


def get_op():
    global command_pointer
    ret = bytecode[command_pointer]
    command_pointer = command_pointer + 1
    return ret


while command_pointer < len(bytecode):
    command = bytecode[command_pointer]
    command_pointer = command_pointer + 1
    print("Command: ", str(command))

    # IDLE
    if command == 0x00:
        continue

    # LOAD
    if command == 0x01:
        op1 = get_op()
        op2 = get_op()

        R[op1] = op2
        print("R[", op1, "]: ", R[op1])

        continue

    # AND R(op1) & R(op2)
    if command == 0x02:
        op1 = get_op()
        op2 = get_op()
        R[op1] = R[op1] & R[op2]
        print("R[", op1, "]: ", R[op1])
        continue

    # MOV  R(op2) -> R(op1)
    if command == 0x03:
        op1 = get_op()
        op2 = get_op()

        R[op1] = R[op2]
        print("R[", op1, "]: ", R[op1])
        continue

    # ADD  R(op1) = R(op1) + R(op2)
    if command == 0x04:
        op1 = get_op()
        op2 = get_op()

        R[op1] = R[op1] + R[op2]
        print("R[", op1, "]: ", R[op1])
        continue

    # CMP  if R(op1) == R(op2) => ZF=1; else ZF=0
    if command == 0x05:
        op1 = get_op()
        op2 = get_op()

        if R[op1] == R[op2]:
            ZF = 1

        print("R[", op1, "]: ", R[op1], "R[", op2, "]: ", R[op2], "ZF: ", ZF)
        continue
