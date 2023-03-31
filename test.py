import unittest
from VM import VirtualMachine


class TestStringMethods(unittest.TestCase):
    # 3 -> R[0]
    def test_LOAD(self):
        bytecode = [0x01, 0x00, 0x03]
        virtM = VirtualMachine(bytecode)
        self.assertEqual(virtM.R[0], 3)

    def test_AND(self):
        bytecode = [0x01, 0x00, 0x03,
                    0x01, 0x01, 0x02,
                    0x02, 0x00, 0x01]
        virtM = VirtualMachine(bytecode)
        self.assertEqual(virtM.R[0], 2)

    def test_MOV(self):
        bytecode = [0x01, 0x00, 0x03,
                    0x01, 0x01, 0x07,
                    0x03, 0x00, 0x01]
        virtM = VirtualMachine(bytecode)
        self.assertEqual(virtM.R[0], 7)

    def test_ADD(self):
        bytecode = [0x01, 0x00, 0x03,
                    0x01, 0x01, 0x07,
                    0x04, 0x00, 0x01]
        virtM = VirtualMachine(bytecode)
        self.assertEqual(virtM.R[0], 10)

    def test_CMP_pos(self):
        bytecode = [0x01, 0x00, 0x03,
                    0x01, 0x01, 0x03,
                    0x05, 0x00, 0x01]
        virtM = VirtualMachine(bytecode)
        self.assertEqual(virtM.ZF, 1)

    def test_CMP_neg(self):
        bytecode = [0x01, 0x00, 0x03,
                    0x01, 0x01, 0x04,
                    0x05, 0x00, 0x01]
        virtM = VirtualMachine(bytecode)
        self.assertEqual(virtM.ZF, 0)


if __name__ == '__main__':
    unittest.main()
