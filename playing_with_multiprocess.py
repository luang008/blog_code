'''
    Playing with multiprocessing module of python
    Following the book "High performance python"
    Author: Ang Lu
    Date: 04/12/2016
'''
'''
    Interesting part is that I learnt more about statistics (confidence interval)
    than parallel computing by this experiment
'''
import random
from multiprocessing import Pool
def estimating_pi_one_thread(sample_num):
    valid = 0
    for i in range(sample_num):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) <= 1.0:
            valid += 1
    return valid

if __name__ == '__main__':
    sample_num = 1000000000
    #print estimating_pi_one_thread(sample_num)
    process_num = 8
    pool = Pool(processes=process_num)
    sample_num_per_process = sample_num/process_num
    print sample_num_per_process
    sample_num_per_process_list = [sample_num_per_process] * process_num
    valid_list = pool.map(estimating_pi_one_thread,sample_num_per_process_list)
    pi_est_mp = sum(valid_list) * 4.0 /sample_num
    print pi_est_mp