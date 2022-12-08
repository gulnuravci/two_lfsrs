""" 
    (MOSTLY) GENERAL CLASS FOR Linear Feedback Shift Registers (LFSRs
"""
class LFSR:
    def __init__(self, num_of_registers, active_registers, init_seq):
        """ 
            Parameter restrictions: 
                -> len(active_registers) < num_of_registers
                -> active_registers is a list of the decimal indexes of registers (1->MSB...num_of_registers->LSB)
                -> initialization_seq is a list with a length num_of_registers of 0s and 1s
        """
        # Initialize registers
        self.registers = init_seq
        # Store the active registers
        self.active = active_registers
        # Add output register as an active one if the user didn't include it
        if num_of_registers not in self.active:
            self.active.append(num_of_registers) 
        # Get period of LFSR
        self.period = 2 ** num_of_registers - 1 
        # Store step outputs
        self.output = 0

    def step(self):
        """ Returns: output of step"""

        # Get output (LSB)
        self.output = self.registers[-1]

        # Get values at the active registers
        values = []
        for register in self.active:
            values.append(self.registers[register-1])

        # XOR the output and all values at active registers
        new_MSB = self.XOR(values)

        # Append the XOR result as input (MSB)
        self.registers.insert(0, new_MSB)

        # "Shift" right by popping LSB
        self.registers.pop()

        print("registers: " + bin(extensions.list_to_bin(self.registers)))

        return self.output


    def XOR(self, values):
        """ Performs XOR operation on all the values in a binary number """
        
        # Start with LSB active register
        result = values[0] 

        # XOR all the remaining active registers (as the operation is commutative)
        for i in range(1, len(self.active)):
            # XOR between last result and current active register
            result = result ^ values[i]

        return result
