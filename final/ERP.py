"""
@author Farzaneh.Tlb
8/27/19 10:54 AM
Implementation of .... (Fill this line)
"""

import mne
import matplotlib.pyplot as plt
import numpy as np
import Analysis.Utils as ut

sfreq=256
n_channels_selected =4

def baseline_correction(data_to_correct ,baseline_data):
    avg = np.mean(baseline_data.data, axis=1)
    row_means_col_vec = avg.reshape((n_channels_selected, 1))
    data_to_correct.data = data_to_correct.data - row_means_col_vec
    return data_to_correct
pick_list = ["P6", "P8", "P10", "PO8"]
ctrl_encmain_le, ctrl_encmain_intact, \
pfc_encmain_le, pfc_encmain_intact, \
ctrl_pretrial_le, ctrl_pretrial_intact, \
pfc_pretrial_le, pfc_pretrial_intact, \
ctrl_proc_le, ctrl_proc_intact, \
pfc_proc_le, pfc_proc_intact = ut.read_allAverages(pick_list)


avg_ctrls_encmains_intact = mne.grand_average(ctrl_encmain_intact)
avg_pfcs_encmains_intact = mne.grand_average(pfc_encmain_intact)

avg_ctrls_pretrial_intact = mne.grand_average(ctrl_pretrial_intact)
avg_pfcs_pretrial_intact = mne.grand_average(pfc_pretrial_intact)

avg_pfcs_encmains_intact =baseline_correction(avg_pfcs_encmains_intact,avg_pfcs_pretrial_intact )
avg_ctrls_encmains_intact =baseline_correction(avg_ctrls_encmains_intact,avg_ctrls_pretrial_intact )

avg_ctrls_encmains_le = mne.grand_average(ctrl_encmain_le)
avg_pfcs_encmains_le = mne.grand_average(pfc_encmain_le)


avg_ctrls_pretrial_le = mne.grand_average(ctrl_pretrial_le)
avg_pfcs_pretrial_le = mne.grand_average(pfc_pretrial_le)

avg_pfcs_encmains_le =baseline_correction(avg_pfcs_encmains_le,avg_pfcs_pretrial_le )
avg_ctrls_encmains_le =baseline_correction(avg_ctrls_encmains_le,avg_ctrls_pretrial_le )


evokeds_1 = {'ctrl': avg_ctrls_encmains_intact, 'pfc': avg_pfcs_encmains_intact}
evokeds_2 = {'ctrl': avg_ctrls_encmains_le, 'pfc': avg_pfcs_encmains_le}

picks1 = [avg_ctrls_encmains_intact.ch_names.index(ch) for ch in ["P6", "P8", "P10", "PO8"]]
picks2 = [avg_ctrls_encmains_le.ch_names.index(ch) for ch in ["P6", "P8", "P10", "PO8"]]


fig1= mne.viz.plot_compare_evokeds(evokeds_2,colors={"ctrl":'CornFlowerBlue', 'pfc':'Crimson'},truncate_xaxis=False ,  vlines= [0.6,0.8], show_sensors='upper right',title="LESION VISUAL HEMIFIELD POSTERIOR",show=False)
fig2 = mne.viz.plot_compare_evokeds(evokeds_1,colors={"ctrl":'CornFlowerBlue', 'pfc':'Crimson'},truncate_xaxis=True , vlines= [0.6,0.8],  show_sensors='upper right',title="INTACT VISUAL HEMIFIELD POSTERIOR",show=False)

plt.show()


T_obs, clusters, cluster_p_values, H0 = mne.stats.permutation_cluster_test([avg_ctrls_encmains_intact.data, avg_pfcs_encmains_intact.data], n_permutations=1000,)


times = evokeds_1['ctrl'].times
plt.close('all')
# plt.title('Channel : ' + channel)
# plt.plot(times, condition1.mean(axis=0) - condition2.mean(axis=0),
#          label="ERF Contrast (Event 1 - Event 2)")
# plt.ylabel("MEG (T / m)")
# plt.legend()
for i_c, c in enumerate(clusters):
    c = c[0]
    if cluster_p_values[i_c] <= 0.03:
        h = plt.axvspan(times[c.start], times[c.stop - 1],
                        color='r', alpha=0.3)
    # else:
    #     plt.axvspan(times[c.start], times[c.stop - 1], color=(0.3, 0.3, 0.3),
    #                 alpha=0.3)
hf = plt.plot(times, T_obs, 'g')
# plt.legend((h, ), ('cluster p-value < 0.05', ))
plt.xlabel("time (ms)")
plt.ylabel("f-values  ")
plt.title("f-values for INTACT VISUAL HEMIFIELD POSTERIOR")
plt.show()





T_obs, clusters, cluster_p_values, H0 = mne.stats.permutation_cluster_test([avg_ctrls_encmains_le.data, avg_pfcs_encmains_le.data], n_permutations=1000,)


times = evokeds_2['ctrl'].times
plt.close('all')
# plt.title('Channel : ' + channel)
# plt.plot(times, condition1.mean(axis=0) - condition2.mean(axis=0),
#          label="ERF Contrast (Event 1 - Event 2)")
# plt.ylabel("MEG (T / m)")
# plt.legend()
# plt.subplot(212)
for i_c, c in enumerate(clusters):
    c = c[0]
    if cluster_p_values[i_c] <= 0.03:
        h = plt.axvspan(times[c.start], times[c.stop - 1],
                        color='r', alpha=0.3)
    # else:
    #     plt.axvspan(times[c.start], times[c.stop - 1], color=(0.3, 0.3, 0.3),
    #                 alpha=0.3)
hf = plt.plot(times, T_obs, 'g')
# plt.legend((h, ), ('cluster p-value < 0.05', ))
plt.xlabel("time (ms)")
plt.ylabel("f-values")
plt.title("f-values for LESION VISUAL HEMIFIELD POSTERIOR")

plt.show()