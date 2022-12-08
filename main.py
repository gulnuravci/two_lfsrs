class LFSR:
    # PARAM restrictions: active_registers < num_of_registers
    def __init__(self, num_of_registers, active_registers):
        self.registers = int(bin((2**num_of_registers)-1), 2) # Initialize all registers to be 1
        self.active = active_registers # Store the active registers
        self.output = []
        period = 2 ** num_of_registers - 1 # Get period of LFSR


    def step(self):
        print(self.registers)
        self.output.append(self.registers & 1) # Get output (LSB)

        self.registers = self.registers >> 1 # Shift right

        values = []
        for register in self.active:
            values.append((self.registers >> register-1) & 1) # Get values at the active registers

        new_MSB = self.XOR(values) # XOR all the values at the active registers

        self.registers = self.registers | new_MSB << len(str(self.registers))-1)

        print(self.registers)

    # Performs XOR operation on a list of values
    def XOR(self, * values):
        result = values[0] # Start with LSB active register

        # Iterate through the rest of the registers up to the MSB active register
        for i in range(1, len(values)):
            result = result ^ values[i] # XOR between last result and current active register

        return result

class G:
    def __init__(self, LFSRs):
        self.LFSRs = LFSRs # Store LFSRs

if __name__ == '__main__':
    LFSR_1 = LFSR(4,[3,4])
    LFSR_1.step()

    # LFSR_2 = LFSR(4,[3,4])
    # LFSRs = [LFSR_1, LFSR_2]
    # generator = G(LFSRs)
    # for LFSR in generator.LFSRs:
    #         print(LFSRs.registers)
    
