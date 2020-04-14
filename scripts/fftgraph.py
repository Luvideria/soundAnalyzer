import numpy.fft as npf
from scipy.signal import find_peaks
from scipy.io import wavfile

def getfft(data,r=True):
    '''r is to keep only the non redundant data (split at half)
    '''
    fft=npf.fftshift(abs(npf.fft(data)))
    if r :
        return fft[int(len(fft)/2):]
    else:
        return fft

def xfft(datafft,SR=44100):
    N=len(datafft)
    t=2*N/SR#because we get the fft data that has been already cut in half to remove the redundant part 
    return [a/t for a in range(N)]

def low_pass_index(datafft,lim,SR=44100):
    N=len(datafft)
    t=2*N/SR#because we get the fft data that has been already cut in half to remove the redundant part 
    alim=int(lim*t)
    return [a/t for a in range(alim+1)]

def detectNMaxFreq(data,threshold=100000,d=30):
    '''data is the signal where peaks have to be detected
    basically just calls scipy to do the job, but bundles the height of peaks
    '''
    peaks=list(find_peaks(data, threshold,distance=d)[0])
    height=data[peaks]
    return peaks,height
