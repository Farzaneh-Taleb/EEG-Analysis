"""
@author Farzaneh.Tlb
7/19/19 10:16 PM
Implementation of Utilties
"""
import os.path
from scipy.io import loadmat
import hdf5storage
import mne


def load_data(data_name):
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../data/" + data_name)
    data = loadmat(path)
    return data

def load_data_hdf(data_name):
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../data/" + data_name)
    data = hdf5storage.loadmat(path)
    return data

def get_three_vars(data):
    return data['pretrial'] , data['encmain'] , data['proc']

def read_fif(path, filename):
    epochs = mne.read_epochs(path+filename)
    # epochs = filters_data(epochs,low_pass=1,high_pass=30)
    return epochs


def read_allAverages(pick_list):
    path_ctrl_encmain_le = "../../data/final_out/ctrl/le/encmain/"
    path_ctrl_encmain_intact = "../../data/final_out/ctrl/intact/encmain/"

    path_pfc_encmain_le = "../../data/final_out/pfc/le/encmain/"
    path_pfc_encmain_intact = "../../data/final_out/pfc/intact/encmain/"

    path_ctrl_pretrial_le = "../../data/final_out/ctrl/le/pretrial/"
    path_ctrl_pretrial_intact = "../../data/final_out/ctrl/intact/pretrial/"

    path_pfc_pretrial_le = "../../data/final_out/pfc/le/pretrial/"
    path_pfc_pretrial_intact = "../../data/final_out/pfc/intact/pretrial/"

    path_ctrl_proc_le = "../../data/final_out/ctrl/le/proc/"
    path_ctrl_proc_intact = "../../data/final_out/ctrl/intact/proc/"

    path_pfc_proc_le = "../../data/final_out/pfc/le/proc/"
    path_pfc_proc_intact = "../../data/final_out/pfc/intact/proc/"

    pathes = [path_ctrl_encmain_le, path_ctrl_encmain_intact, path_pfc_encmain_le, path_pfc_encmain_intact]
    data_ctrl = [
        "ctrl01", "ctrl02", "ctrl03", "ctrl04", "ctrl05", "ctrl06", "ctrl07",
        "ctrl08", "ctrl09", "ctrl10", "ctrl11", "ctrl12", "ctrl13", "ctrl14", "ctrl15",
        "ctrl16", "ctrl17", "ctrl18", "ctrl19", "ctrl20"]
    data_pfc = ["pfc01", "pfc02", "pfc03", "pfc04"
        , "pfc05", "pfc06", "pfc07", "pfc08", "pfc09", "pfc10",
                "pfc11", "pfc12", "pfc13", "pfc14"]

    ctrl_encmain_le = []
    ctrl_encmain_intact = []
    pfc_encmain_le = []
    pfc_encmain_intact = []

    ctrl_pretrial_le = []
    ctrl_pretrial_intact = []
    pfc_pretrial_le = []
    pfc_pretrial_intact = []

    ctrl_proc_le = []
    ctrl_proc_intact = []
    pfc_proc_le = []
    pfc_proc_intact = []

    for data in data_ctrl:
        ctrl_encmain_le.append(read_fif(path_ctrl_encmain_le, data).average(picks=pick_list))
        ctrl_encmain_intact.append(read_fif(path_ctrl_encmain_intact, data).average(picks=pick_list))

    for data in data_pfc:
        pfc_encmain_le.append(read_fif(path_pfc_encmain_le, data).average(picks=pick_list))
        pfc_encmain_intact.append(read_fif(path_pfc_encmain_intact, data).average(picks=pick_list))

    for data in data_ctrl:
        ctrl_pretrial_le.append(read_fif(path_ctrl_pretrial_le, data).average(picks=pick_list))
        ctrl_pretrial_intact.append(read_fif(path_ctrl_pretrial_intact, data).average(picks=pick_list))

    for data in data_pfc:
        pfc_pretrial_le.append(read_fif(path_pfc_pretrial_le, data).average(picks=pick_list))
        pfc_pretrial_intact.append(read_fif(path_pfc_pretrial_intact, data).average(picks=pick_list))

    for data in data_ctrl:
        ctrl_proc_le.append(read_fif(path_ctrl_proc_le, data).average(picks=pick_list))
        ctrl_proc_intact.append(read_fif(path_ctrl_proc_intact, data).average(picks=pick_list))

    for data in data_pfc:
        pfc_proc_le.append(read_fif(path_pfc_proc_le, data).average(picks=pick_list))
        pfc_proc_intact.append(read_fif(path_pfc_proc_intact, data).average(picks=pick_list))

    return  ctrl_encmain_le ,ctrl_encmain_intact , \
            pfc_encmain_le ,pfc_encmain_intact ,\
            ctrl_pretrial_le ,ctrl_pretrial_intact ,\
            pfc_pretrial_le  ,pfc_pretrial_intact ,\
            ctrl_proc_le  ,ctrl_proc_intact  ,\
            pfc_proc_le  ,pfc_proc_intact

def read_allData():
    path_ctrl_encmain_le = "../../data/final_out/ctrl/le/encmain/"
    path_ctrl_encmain_intact = "../../data/final_out/ctrl/intact/encmain/"

    path_pfc_encmain_le = "../../data/final_out/pfc/le/encmain/"
    path_pfc_encmain_intact = "../../data/final_out/pfc/intact/encmain/"

    path_ctrl_pretrial_le = "../../data/final_out/ctrl/le/pretrial/"
    path_ctrl_pretrial_intact = "../../data/final_out/ctrl/intact/pretrial/"

    path_pfc_pretrial_le = "../../data/final_out/pfc/le/pretrial/"
    path_pfc_pretrial_intact = "../../data/final_out/pfc/intact/pretrial/"

    path_ctrl_proc_le = "../../data/final_out/ctrl/le/proc/"
    path_ctrl_proc_intact = "../../data/final_out/ctrl/intact/proc/"

    path_pfc_proc_le = "../../data/final_out/pfc/le/proc/"
    path_pfc_proc_intact = "../../data/final_out/pfc/intact/proc/"

    pathes = [path_ctrl_encmain_le, path_ctrl_encmain_intact, path_pfc_encmain_le, path_pfc_encmain_intact]
    data_ctrl = [
        "ctrl01", "ctrl02",
        "ctrl03", "ctrl04", "ctrl05", "ctrl06", "ctrl07",
        "ctrl08", "ctrl09", "ctrl10", "ctrl11", "ctrl12", "ctrl13", "ctrl14", "ctrl15",
        "ctrl16", "ctrl17", "ctrl18", "ctrl19", "ctrl20"
    ]
    data_pfc = ["pfc01", "pfc02",
                "pfc03", "pfc04"
        , "pfc05", "pfc06", "pfc07", "pfc08", "pfc09", "pfc10",
                "pfc11", "pfc12", "pfc13", "pfc14"
                ]

    ctrl_encmain_le = []
    ctrl_encmain_intact = []
    pfc_encmain_le = []
    pfc_encmain_intact = []

    ctrl_pretrial_le = []
    ctrl_pretrial_intact = []
    pfc_pretrial_le = []
    pfc_pretrial_intact = []

    ctrl_proc_le = []
    ctrl_proc_intact = []
    pfc_proc_le = []
    pfc_proc_intact = []

    for data in data_ctrl:
        ctrl_encmain_le.append(read_fif(path_ctrl_encmain_le, data))
        ctrl_encmain_intact.append(read_fif(path_ctrl_encmain_intact, data))

    for data in data_pfc:
        pfc_encmain_le.append(read_fif(path_pfc_encmain_le, data))
        pfc_encmain_intact.append(read_fif(path_pfc_encmain_intact, data))

    for data in data_ctrl:
        ctrl_pretrial_le.append(read_fif(path_ctrl_pretrial_le, data))
        ctrl_pretrial_intact.append(read_fif(path_ctrl_pretrial_intact, data))

    for data in data_pfc:
        pfc_pretrial_le.append(read_fif(path_pfc_pretrial_le, data))
        pfc_pretrial_intact.append(read_fif(path_pfc_pretrial_intact, data))

    for data in data_ctrl:
        ctrl_proc_le.append(read_fif(path_ctrl_proc_le, data))
        ctrl_proc_intact.append(read_fif(path_ctrl_proc_intact, data))

    for data in data_pfc:
        pfc_proc_le.append(read_fif(path_pfc_proc_le, data))
        pfc_proc_intact.append(read_fif(path_pfc_proc_intact, data))


    return  ctrl_encmain_le ,ctrl_encmain_intact , \
            pfc_encmain_le ,pfc_encmain_intact ,\
            ctrl_pretrial_le ,ctrl_pretrial_intact ,\
            pfc_pretrial_le  ,pfc_pretrial_intact ,\
            ctrl_proc_le  ,ctrl_proc_intact  ,\
            pfc_proc_le  ,pfc_proc_intact

def read_intact_lesion():
    path_ctrl_encmain= "../../data/final_out/ctrl/all/encmain/"

    path_pfc_encmain = "../../data/final_out/pfc/all/encmain/"

    path_ctrl_pretrial = "../../data/final_out/ctrl/all/pretrial/"

    path_pfc_pretrial = "../../data/final_out/pfc/all/pretrial/"

    path_ctrl_proc = "../../data/final_out/ctrl/all/proc/"

    path_pfc_proc = "../../data/final_out/pfc/all/proc/"

    data_ctrl = [
        "ctrl01", "ctrl02",
        "ctrl03", "ctrl04", "ctrl05", "ctrl06", "ctrl07",
        "ctrl08", "ctrl09", "ctrl10", "ctrl11", "ctrl12", "ctrl13", "ctrl14", "ctrl15",
        "ctrl16", "ctrl17", "ctrl18", "ctrl19", "ctrl20"
    ]
    data_pfc = ["pfc01", "pfc02",
                "pfc03", "pfc04"
        , "pfc05", "pfc06", "pfc07", "pfc08", "pfc09", "pfc10",
                "pfc11", "pfc12", "pfc13", "pfc14"
                ]

    ctrl_encmain = []
    pfc_encmain = []

    ctrl_pretrial = []
    pfc_pretrial = []

    ctrl_proc= []
    pfc_proc = []

    for data in data_ctrl:
        ctrl_encmain.append(read_fif(path_ctrl_encmain, data))

    for data in data_pfc:
        pfc_encmain.append(read_fif(path_pfc_encmain, data))

    for data in data_ctrl:
        ctrl_pretrial.append(read_fif(path_ctrl_pretrial, data))

    for data in data_pfc:
        pfc_pretrial.append(read_fif(path_pfc_pretrial, data))

    for data in data_ctrl:
        ctrl_proc.append(read_fif(path_ctrl_proc, data))

    for data in data_pfc:
        pfc_proc.append(read_fif(path_pfc_proc, data))

    return ctrl_encmain,pfc_encmain,ctrl_pretrial, pfc_pretrial,ctrl_proc, pfc_proc,
