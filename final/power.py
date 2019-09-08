"""
@author Farzaneh.Tlb
8/27/19 4:40 PM
Implementation of .... (Fill this line)
"""

import mne
import Analysis.Utils as ut
from mne.time_frequency import psd_welch
import  matplotlib.pyplot as plt
from spectrum import Periodogram
import numpy as np
ctrl_encmain_le, ctrl_encmain_intact, \
pfc_encmain_le, pfc_encmain_intact, \
ctrl_pretrial_le, ctrl_pretrial_intact, \
pfc_pretrial_le, pfc_pretrial_intact, \
ctrl_proc_le, ctrl_proc_intact, \
pfc_proc_le, pfc_proc_intact = ut.read_allData()

# ctrl_le_ant = ctrl_pretrial_le.pick(["AF3","F3","F5"])

def calculate_power(data,pick_list):

    psds_mean_array = np.empty([len(data),40])
    psds_std_array = np.empty([len(data),40])
    for i in range(len(data)):
        data[i] = data[i].pick(pick_list)
        psds, freqs = psd_welch(data[i], fmin=1, fmax=40,n_per_seg=100)
        # psds = 10. * np.log10(psds)
        psds_mean = psds.mean(0).mean(0)
        psds_std = psds.mean(0).std(0)
        # psds_std = psds.mean(0).std(0)
        psds_mean_array[i] = psds_mean
        psds_std_array[i] = psds_std
        # psds_std_array.append(psds_std)
    return psds_mean_array,psds_std_array,freqs

def plot_power(ax, psds_mean_array,psds_std_array,freqs,color,label):
    mean = psds_mean_array.mean(0)
    std = psds_std_array.std(0)
    mean =np.divide(mean, 10)
    std =np.divide(std, 10)

    ax.plot(freqs, mean, color=color,label=label)
    ax.fill_between(freqs, mean - std, mean + std,color=color, alpha=.3)

    ax.set(xlabel='Frequency',
           ylabel='Power')
    ax.legend()
f, ax = plt.subplots(2,2)

data ,std, freqs = calculate_power(ctrl_pretrial_le,["AF3", "F3", "F5"])
plot_power(ax[0,0],data,std,freqs,'blue','ANT LESION')

data,std,freqs = calculate_power(ctrl_pretrial_intact,["AF4", "F4", "F6"])
plot_power(ax[0,0],data,std,freqs,'pink','ANT INTACT')

data1 ,std, freqs = calculate_power(pfc_pretrial_le,["AF3", "F3", "F5"])
plot_power(ax[0,1],data1,std,freqs,'red','ANT LESION')

data2,std , freqs = calculate_power(pfc_pretrial_intact,["AF4", "F4", "F6"])
plot_power(ax[0,1],data2,std,freqs,'pink','ANT INTACT')


ctrl_encmain_le, ctrl_encmain_intact, \
pfc_encmain_le, pfc_encmain_intact, \
ctrl_pretrial_le, ctrl_pretrial_intact, \
pfc_pretrial_le, pfc_pretrial_intact, \
ctrl_proc_le, ctrl_proc_intact, \
pfc_proc_le, pfc_proc_intact = ut.read_allData()


data ,std, freqs = calculate_power(ctrl_pretrial_le,["P1", "P3", "P5","P7" ,"P9", "PO3", "PO7" ,"O1"])
plot_power(ax[1,0],data,std,freqs,'blue','POST LESION')

data,std , freqs = calculate_power(ctrl_pretrial_intact,["P2", "P4", "P6","P8" ,"P10", "PO4", "PO8" ,"O2"])
plot_power(ax[1,0],data,std,freqs,'pink','POST INTACT')

data ,std, freqs = calculate_power(pfc_pretrial_le,["P1", "P3", "P5","P7" ,"P9", "PO3", "PO7" ,"O1"])
plot_power(ax[1,1],data,std,freqs,'red','POST LESION')

data ,std, freqs = calculate_power(pfc_pretrial_intact,["P2", "P4", "P6","P8" ,"P10", "PO4", "PO8" ,"O2"])
plot_power(ax[1,1],data,std,freqs,'pink','POST INTACT')


plt.show()

#
# T_obs, clusters, cluster_p_values, H0 = mne.stats.permutation_cluster_test([data1, data2], n_permutations=1000,)
#
#
# times =freqs
# plt.close('all')
# # plt.title('Channel : ' + channel)
# # plt.plot(times, condition1.mean(axis=0) - condition2.mean(axis=0),
# #          label="ERF Contrast (Event 1 - Event 2)")
# # plt.ylabel("MEG (T / m)")
# # plt.legend()
# for i_c, c in enumerate(clusters):
#     c = c[0]
#     if cluster_p_values[i_c] <= 0.05:
#         h = plt.axvspan(times[c.start], times[c.stop - 1],
#                         color='r', alpha=0.3)
#     # else:
#     #     plt.axvspan(times[c.start], times[c.stop - 1], color=(0.3, 0.3, 0.3),
#     #                 alpha=0.3)
# hf = plt.plot(times, T_obs, 'g')
# # plt.legend((h, ), ('cluster p-value < 0.05', ))
# plt.xlabel("time (ms)")
# plt.ylabel("f-values  ")
# plt.title("f-values for INTACT VISUAL HEMIFIELD POSTERIOR")
# plt.show()