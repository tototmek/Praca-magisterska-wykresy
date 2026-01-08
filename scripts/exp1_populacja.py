#!/usr/bin python3

import pandas as pd
import matplotlib.pyplot as plt
import argparse
import numpy as np
from utils import *

def get_data(channel_idx):
    # Load data
    annotation_file = f'/home/tototmek/Studia/Magisterka/code/bee_counter_firmware/data/experiments/manual-annotation/tunel{channel_idx}.csv'
    annotations = pd.read_csv(annotation_file)
    x, y, bee = [], [], 0
    for timestamp, type in zip(annotations['timestamp'], annotations['event_type']):
        if type == 'enter':
            bee+=1
        if type == 'leave':
            bee-=1
        x.append(timestamp)
        y.append(bee)
    return np.array(x), np.array(y)

def get_sum_data():
    annotations = pd.DataFrame()
    for i in range(8):
        annotation_file = f'/home/tototmek/Studia/Magisterka/code/bee_counter_firmware/data/experiments/manual-annotation/tunel{i}.csv'
        annotations = pd.concat((annotations, pd.read_csv(annotation_file)), ignore_index=True)
    annotations.sort_values('timestamp', inplace=True, ignore_index=True)
    
    x, y, bee = [], [], 0
    for timestamp, type in zip(annotations['timestamp'], annotations['event_type']):
        if type == 'enter':
            bee+=1
        if type == 'leave':
            bee-=1
        x.append(timestamp)
        y.append(bee)
    return np.array(x), np.array(y)


def generate_plot():
    sum_x, sum_y = get_sum_data()
    setup_latex_plots()
    
    plt.figure(figsize=(TEXT_WIDTH, 0.6*TEXT_WIDTH))

    for i in range(8):
        x, y = get_data(i)
        plt.plot(x, y, label=f"Tunel {i}", lw=0.6)
    
    plt.plot(sum_x, sum_y, label=f"Łącznie", lw=1, c="black")
    
    plt.ylabel(f'Bilans pszczół')
    plt.xlabel(r'$t [s]$')
    plt.legend(ncol=3, fancybox=False)
    
    save_plot()


if __name__=="__main__":
    generate_plot()
    plt.show()