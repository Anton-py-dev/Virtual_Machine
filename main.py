from VM import VirtualMachine

bytecode = [0x00,
            0x01, 0x00, 0x03,
            0x01, 0x01, 0x03,
            0x05, 0x01, 0x00,
            0x04, 0x01, 0x00,
            0x03, 0x01, 0x00,
            0x02, 0x00, 0x01]

VM = VirtualMachine(bytecode)
