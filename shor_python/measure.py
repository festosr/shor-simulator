# Takes in a normalized vector representing system of qubits.
# "Measures" the system and returns the resulting state.

import random
import cmath
import numpy as np

# Say the system is in state j with probability p:
    # - The probability p that a qubit is in state j is given by
    #   the the jth amplitude multiplied by its complex conjugate.
    # - We can write p as the (sum of the first j+1 elements
    #   of the probability list) - (the sum of the first j elements).
    # - The probability that a uniformly random float n in [0,1] is in 
    #   the interval [a,b] where b-a = p is p.
    # - Therefore we find the first element  <n in the cumulative sum array.
 
def measure(qubits):
    # Gets random float in the range [0,1)
    random.seed()
    n = random.random()
    
    # multiply by complex conjugate element-wise to obtain list of probabilities
    amp_sq = []
    for q in qubits:
        print q
        # The cumulative sum of this list represents a histogram.
        amp_sq.append(q * q.conjugate()) 
        
    hist = np.cumsum(amp_sq)
    for i in range(len(hist)):
        if hist[i] > n:
            return i
    return -1
   
