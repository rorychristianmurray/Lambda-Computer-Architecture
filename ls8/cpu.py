"""CPU functionality."""

import sys

# declare opcodes for clarity

LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010
HLT = 0b00000001
POP = 0b01000110
PUSH = 0b01000101
SP = 7

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256 # 256 bytes of memory
        self.register = [0] * 8 # general purpose registers
        self.pc = 0

    def load(self):
        """Load a program into memory."""

        # get filename from CL
        filename = sys.argv[1]

        address = 0
        
        with open(filename) as f:
            for line in f:
                print(line)
                n = line.split('#')
                n[0] = n[0].strip()

                if n[0] == '':
                    continue
                val = int(n[0], 2)
                self.ram[address] = val
                address += 1
        
        print(f"self.ram : {self.ram}")




        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1


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
        print(f" value of SP : {SP}")
        
        ## boot cpu
        running = True

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
            ir = self.ram_read(self.pc)

            ## store next two bytes of data after ir
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            ## implement LDI opcode
            if ir == LDI:
                print("LDI")

                ## get register
                reg_num = operand_a

                # get value to save
                value = operand_b


                self.register[reg_num] = value

                ## increment program counter
                self.pc += 3
            
            elif ir == PRN:
                ## get value from register
                value = self.register[operand_a]

                ## print value
                print(f"value at register {operand_a} is value : {value}")

                ## increment pc
                self.pc += 2
            
            elif ir == MUL:
                ## multiply following two instrx
                ## which are the values from 
                # the specified registers
                ## operand_a and operand_b

                mult_val = self.register[operand_a] * self.register[operand_b]
  
                ## store computed value in
                ## register a
                self.register[operand_a] = mult_val

                ## increment program counter
                self.pc += 3
    
            elif ir == HLT:
                ## halt
                running = False
                self.pc += 1

            elif ir == PUSH:
                # decrement sp 
                self.register[SP] -=1
                print(f"pc pusha : {self.pc}")

                # copy value from register 
                # to memory at sp
                reg_num = self.ram[self.pc + 1]
                value = self.register[reg_num]
                self.ram[self.register[SP]] = value

                # increment pc
                self.pc += 2

            
            elif ir == POP:
                # copy the value from the
                # top of the stack into the
                # given register
                print(f"pc poppa : {self.pc}")
                reg_num = self.ram[self.pc + 1]
                value = self.ram[self.register[SP]]
                self.register[reg_num] = value

                # increment sp
                self.register[SP] += 1

                # increment pc
                self.pc += 2

            else: 
                print(f"unknown instruction at address pc {self.pc}")
                sys.exit(1)
        return



               
        

