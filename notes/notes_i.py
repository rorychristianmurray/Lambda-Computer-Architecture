import sys

PRINT_RORY = 1

HALT = 2
SAVE_REG = 3
PRINT_REG = 4


memory = [
	PRINT_RORY,
	SAVE_REG, # SAVE_REG value 10 in R2
	24,
	2, # R2
	PRINT_REG, # PRINT_REG R2
	2,
	PRINT_RORY,
	HALT,
	0,
	0,
	0,
	0
]

## registers allow us to store values in variables

 # like variables, fixed number with fixed names
 # R0, R1, R2, R3... R7
register = [0] * 8


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