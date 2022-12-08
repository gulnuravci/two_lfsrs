import LFSR
import G
import extensions

if __name__ == '__main__':
    LFSR_1 = LFSR(num_of_registers=6, active_registers=[5,6], init_seq=extensions.all_one_bin(6))
    LFSR_1.step()
    # LFSR_2 = LFSR(num_of_registers=4, active_registers=[3,4], init_seq=extensions.all_one_bin(4))
    # generator = G(LFSR1=LFSR_1, LFSR2=LFSR_2)
