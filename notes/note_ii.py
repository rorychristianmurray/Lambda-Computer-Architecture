import sys

print(sys.argv)

# sys.exit()

PRINT_RORY = 1
HALT = 2
SAVE_REG = 3 # LDI
PRINT_REG = 4 # PRN


memory = [
	1,
	3, # SAVE_REG value 10 in R2
	24,
	2, # R2
	4, # PRINT_REG R2
	2,
	1,
	2,
	0,
	0,
	0,
	0
]

## registers allow us to store values in variables

 # like variables, fixed number with fixed names
 # R0, R1, R2, R3... R7
register = [0] * 8

filename = sys.argv[1]

# read the file
address = 0

with open(filename) as f:
	for line in f:
		print(line)
		n = line.split("#")
		n[0] = n[0].strip()

		if n[0] == '':
			continue
		val = int(n[0])
		memory[address] = val
		address += 1
	

s = "10100101" # create string

int(s) # convert string to int

int(s, 2) # specify base

int(line.split('#')[0])


## loop
running = True
pc = 0 # program counter - index into memory of current instruction

while running:
	## do stuff
	current_instruction = memory[pc]

	if current_instruction == PRINT_RORY:
		print("Rory!")
		pc += 1 # pointer to currently executing instruction

	elif current_instruction == SAVE_REG:
		## get value to save
		value = memory[pc + 1] 

		## get register
		reg_num = memory[pc + 2]

		register[reg_num] = value

		pc += 3 # pointer to currently executing instruction

	elif current_instruction == PRINT_REG:
		reg_num = memory[pc + 1]
		reg_val = register[reg_num]
		print(f"register value is {reg_val}")
		pc += 2
	

	elif current_instruction == HALT:
		print(f"halting at pc : {pc}")
		running = False
		pc += 1 # pointer to currently executing instruction

	else:
		print(f"unknown instruction at address {pc}")
		sys.exit(1)

	

## use a hashmap