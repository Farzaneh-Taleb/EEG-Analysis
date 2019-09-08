"""
@author Farzaneh.Tlb
8/11/19 2:10 PM
Implementation of .... (Fill this line)
"""

import statistics

import matplotlib.pyplot as plt
import mne

import Analysis.Utils as utils
import Analysis.Utils as ut
import  numpy as np

original_level = mne.set_config('MNE_LOGGING_LEVEL', 'ERROR')
mne.set_log_level('ERROR')

ctrl_total =  [156,129,169,211,209,188,218,
               180,234,215,145,206,146,221,
               198,230,233,222,163,135]

pfc_total = [224,108,109,207,235,239,237,219,148,220,212,114,111,178]
ctrl_encmain_le, ctrl_encmain_intact, \
pfc_encmain_le, pfc_encmain_intact, \
ctrl_pretrial_le, ctrl_pretrial_intact, \
pfc_pretrial_le, pfc_pretrial_intact, \
ctrl_proc_le, ctrl_proc_intact, \
pfc_proc_le, pfc_proc_intact = ut.read_allData()


x = [0.2,0.22]
money = [95.2765, 86.9294]
plt.figure(figsize=(4, 5))  # width:20, height:3
barlist = plt.bar(x, money ,width=0.01)
barlist[1].set_color('r')
plt.xticks(x, ('CTRL', 'PFC'))
plt.ylabel("ACCURACY")
plt.show()
# print(sum_trials_ctrl ,intact_correct_ctrl , le_correct_ctrl)
# print(sum_trials_pfc, intact_correct_pfc , le_correct_pfc)
