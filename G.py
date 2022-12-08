from LFSR import LFSR
"""
    A SPECIFIC GENERATOR OUTLINED BY THE ASSIGNMENT
"""   
class G:
    def __init__(self):
        self.LFSR1 = LFSR(num_of_registers=6, active_registers=[5, 6], init_seq=[1]*6)
        self.LFSR2 = LFSR(num_of_registers=4, active_registers=[3, 4], init_seq=[1]*4)
        self.output = 0
        self.period = self.LFSR1.period * self.LFSR2.period

    def step(self):
        """ Returns: output of step"""
        output1 = self.LFSR1.step()
        output2 = self.LFSR2.step()
        self.output = output1 ^ output2
        if self.output == 1:
            output1 = self.LFSR1.step()
            if output1 == 1:
                output2 = self.LFSR2.step()
        elif self.output == 0:
            output2 = self.LFSR2.step()

        return self.output