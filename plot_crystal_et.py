import os
import sys
import uproot
import numpy as np
import matplotlib.pyplot as plt

event_no = 0
for filename in os.listdir("crystal_data"):
    if "output_" in filename:
        data = uproot.open(f"crystal_data/{filename}")
        tree = data["analyzer;1"]
        events = tree["tree;1"]
        for event in events.arrays():
            if(event_no != 0):
                plt.close()
            event_no += 1
            crystal_et = event['crystal_Et']
            crystal_ieta = event['crystal_iEta']
            crystal_iphi = event['crystal_iPhi']
            fig, ax = plt.subplots()
            ax.scatter(crystal_ieta, crystal_iphi, c=crystal_et, s=crystal_et, alpha=0.5)
            ax.set_xlabel(r'$i_\eta$', fontsize=15)
            ax.set_ylabel(r'$i_\phi$', fontsize=15)
            ax.set_title(f'Crystal $E_T$ for event {event_no}')
            ax.grid(True)
            fig.tight_layout()
            plt.pause(1)
