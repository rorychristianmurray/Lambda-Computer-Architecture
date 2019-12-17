"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [] # 256 bytes of memory
        self.register = [0] * 8 # general purpose registers
        self.pc = 0

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def ram_read(self, MAR):
        ## takes an adr as an arg and returns
        ## value at that adr in RAM
        read_val = self.ram[MAR]
        return read_val
            

    def ram_write(self, MAR, MDR):
        ## takes and adr and a val as an argument 
        ## and assigns that val to the associated
        ## adr in RAM
        self.ram[MAR] = MDR
        return   

    def run(self):
        """Run the CPU."""

        # declare opcodes for clarity
        LDI = 0b10000010
        PRN = 0b01000111
        R0 = 00000000
        
        ## boot cpu
        running = True

        # reset instruction register
        ir = 0

        ## reset program counter
        self.pc = 0

        ## figure out how many instructions
        ## to increment progr by
        # inc_prog_by = 1
        # instrx_bytes = ir

        # if ir == 0b10:
        #     inc_prog_by = 3

        # elif ir == 0b01:
        #     inc_prog_by = 2
        
        # elif ir == 0b00:
        #     inc_prog_by = 1

        ## run program
        while running:
            ## read memory address stored in register pc
             ## and store results in ir
            ir = self.ram[self.pc]

            ## store next two bytes of data after ir
            operand_a = ram_read(pc + 1)
            operand_b = ram_read(pc + 2)


            ## implement LDI opcode
            if ir == LDI:
                print("LDI")
                # get value to save
                value = operand_b

                ## get register
                reg_num = operand_a

                self.register[reg_num] = value

                ## increment program counter
                self.pc += 3
            
            elif ir == PRN:
                ## get value from register
                value = self.register[operand_a]

                ## print value
                print(f"value at register {operand_a} is value : {value}")



               
        

