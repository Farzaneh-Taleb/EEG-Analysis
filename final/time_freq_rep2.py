"""
@author Farzaneh.Tlb
8/29/19 11:01 AM
Implementation of .... (Fill this line)
"""

import Analysis.Utils as ut
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

from mne.time_frequency import tfr_multitaper
import mne

ctrl_encmain, pfc_encmain, ctrl_pretrial, pfc_pretrial, ctrl_proc ,pfc_proc = ut.read_intact_lesion()



def pool_into_one2(all_baseline):
    # ar= np.empty([all_baseline.shape[1],all_baseline.shape[2],all_baseline.shape[3]])
    ar =np.concatenate(all_baseline,axis=2)
    return ar

def bootstrapping2(data,size):
    selected   = np.empty(shape = [data.shape[0], data.shape[1],size])
    i=0
    for d in data:
        j=0
        for d1 in d:
            np.random.shuffle(d1)
            selected[i,j] = d1[:size]
            j += 1
        i+=1
    mean = np.mean(selected, axis=2)
    std = np.std(selected, axis=2)
    return  mean , std



def cal_tfr2(data ,index,mean,std,list_pick):
    freqs = np.arange(1,40,1)
    n_cycles = freqs/2
    # power_pfcs_pretrials_intact = tfr_multitaper(ctrl_encmain_le[0], freqs=freqs, n_cycles=n_cycles, use_fft=True,return_itc=False, average=True,picks=["P1","P3","P5","P7","P9","PO3","PO7","O"])
    data[index] = data[index].resample(sfreq=256,npad=1715,pad='constant',window='hann')
    power_data = tfr_multitaper(data[index], freqs=freqs, n_cycles=n_cycles, use_fft=True,return_itc=False, average=True,picks=list_pick)

    power_mean = np.empty([8,2])

    for ch in range(power_data.data.shape[0]):
        for fr in range(power_data.data.shape[1]):
            power_data.data[ch,fr] =np.divide(np.subtract(power_data.data[ch,fr,:],mean[ch,fr]) , std[ch,fr])

    return power_data

posterior_picks= ["P1","P3","P5","P7","P9","PO3","PO7","O1"]
anterior_picks = ["AF7", "F5" ,"F7" ,"FC5" , "FT7" ]

def  plot_tfr(power_data,times,f,ax,row,col):
    # avg = np.mean(power_data._data,0)
    avg = np.mean(np.mean(power_data,axis=0),axis=0)
    im = ax[row,col].pcolormesh(times, np.arange(1,40,1), avg, cmap='viridis')
    f.colorbar(im, ax=ax)

def ca_tfr_baseline(data,list_pick,size) :
    freqs = np.arange(1, 40, 1)
    n_cycles = freqs / 2
    first = tfr_multitaper(data[0], freqs=freqs, n_cycles=n_cycles, use_fft=True, return_itc=False,
                   average=True, picks=list_pick)
    power_baseline = np.empty([len(data),len(list_pick) ,len(freqs) ,first._data.shape[2]])
    for i in range(len(data)) :
        power_baseline[i] = tfr_multitaper(data[i], freqs=freqs, n_cycles=n_cycles, use_fft=True, return_itc=False,average=True, picks=list_pick)._data
    baseline_pool =  pool_into_one2(power_baseline)
    baseline_pool = bootstrapping2(baseline_pool,size)
    return baseline_pool


f ,ax = plt.subplots(2,2)

b=[]
for i in range(len(ctrl_proc)):
    mean, std = ca_tfr_baseline(ctrl_pretrial, anterior_picks,ctrl_proc[i]._data.shape[0])
    power = cal_tfr2(ctrl_proc, i, mean, std, anterior_picks)
    b.append(power._data)


plot_tfr(b,power.times,f,ax,0,0)

b=[]
for i in range(len(ctrl_encmain)):
    mean, std = ca_tfr_baseline(ctrl_pretrial, anterior_picks,ctrl_encmain[i]._data.shape[0])
    power = cal_tfr2(ctrl_encmain, i, mean, std, anterior_picks)
    b.append(power._data)

plot_tfr(b,power.times,f,ax,0,1)


b=[]
for i in range(len(ctrl_proc)):
    mean, std = ca_tfr_baseline(ctrl_pretrial, posterior_picks,ctrl_proc[i]._data.shape[0])
    power = cal_tfr2(ctrl_proc, i, mean, std, posterior_picks)
    b.append(power._data)


plot_tfr(b,power.times,f,ax,1,0)

b=[]
for i in range(len(ctrl_encmain)):
    mean, std = ca_tfr_baseline(ctrl_pretrial, posterior_picks,ctrl_encmain[i]._data.shape[0])
    power = cal_tfr2(ctrl_encmain, i, mean, std, posterior_picks)
    b.append(power._data)


plot_tfr(b,power.times,f,ax,1,1)





plt.show()

