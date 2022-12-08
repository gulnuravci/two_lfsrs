"""
    A SPECIFIC GENERATOR OUTLINED BY THE ASSIGNMENT
"""   
class G:
    def __init__(self, LFSR1, LFSR2):
        self.LFSR1 = LFSR1
        self.LFSR2 = LFSR2
        self.output = 0

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