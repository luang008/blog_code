'''
    Comparing different ways to sample from a given discrete distribution
    Inspired by 11761 hw 5
    Author: Ang Lu
    Date: 03/14/2015
'''
import sys, random
import numpy as np
from scipy import stats
from timeit import default_timer as timer

def generate_dist(voca):
    unnormed_dist = [random.random() for x in range(voca)]
    norm = sum(unnormed_dist)
    dist = [x * 1.0 / norm for x in unnormed_dist]
    return dist

def naive_sample(size,dist):
    #dist = sorted(dist,reverse=True)
    sample = []
    for i in range(size):
        rp = random.random()
        cum = 0
        for j,p in enumerate(dist):
            cum += p
            if rp <= cum:
                sample.append(j)
                break
    return sample

def scipy_rv_wrapper(size,dist):
    sample_machine = stats.rv_discrete(values = (range(len(dist)),dist))
    sample = sample_machine.rvs(size = size)
    return sample

def sample_with(function, dist, size):
    print "Sample with " + function.__name__
    start = timer()
    sample = function(size,dist)
    end = timer()
    print "Time usage: %f" %(end-start)

def main():
    voca = int(sys.argv[1])
    size = int(sys.argv[2])
    dist = generate_dist(voca)
    methods = [naive_sample,np.random.multinomial,scipy_rv_wrapper]
    for method in methods:
        sample_with(method, dist, size)

if __name__ == '__main__':
    main()