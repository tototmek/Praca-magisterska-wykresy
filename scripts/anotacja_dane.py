#!/usr/bin python3

import pandas as pd
import matplotlib.pyplot as plt
import argparse
import numpy as np
from utils import *

def generate_plot():
    setup_latex_plots()
    channel_idx = 0
    start_time = 460
    end_time = 520
    # Load data
    raw_data = pd.read_csv('/home/tototmek/Studia/Magisterka/code/bee_counter_firmware/data/experiments/processed-data/raw-time-adjusted.csv')
    annotation_file = f'/home/tototmek/Studia/Magisterka/code/bee_counter_firmware/data/experiments/manual-annotation/tunel{channel_idx}.csv'
    annotations = pd.read_csv(annotation_file)
    
    # Filter data by time range
    raw_mask = (raw_data['time'] >= start_time) & (raw_data['time'] <= end_time)
    raw_filtered = raw_data[raw_mask]
    
    annotation_mask = (annotations['timestamp'] >= start_time) & (annotations['timestamp'] <= end_time)
    annotations_filtered = annotations[annotation_mask]
    
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(TEXT_WIDTH, 0.6*TEXT_WIDTH), sharex=True, gridspec_kw={'height_ratios': [1.618, 1]})
    
    # Plot raw data
    channel_name = f'delta{channel_idx}'
    ax1.plot(raw_filtered['time'], raw_filtered[channel_name], linewidth=0.5,  c='lightgrey', label='Dane surowe')
    
    # Apply rolling average filter with window size 30
    filtered_data = raw_filtered[channel_name].rolling(window=30, center=True).mean()
    ax1.plot(raw_filtered['time'], filtered_data, c="black", linewidth=0.75, alpha=0.8, label='Dane filtrowane')
    
    # Scale the plot according to filtered data range
    filtered_min = filtered_data.min()
    filtered_max = filtered_data.max()
    margin = (filtered_max - filtered_min) * 0.1  # Add 10% margin
    ax1.set_ylim(filtered_min - margin, filtered_max + margin)
    
    ax1.set_ylabel(f'$x_{channel_idx}(t)$')
    ax1.legend(frameon=True, loc="upper right")
    
    # Plot annotations
    enter_times = annotations_filtered[annotations_filtered['event_type'] == 'enter']['timestamp']
    leave_times = annotations_filtered[annotations_filtered['event_type'] == 'leave']['timestamp']
    
    # Plot enter events as +1 with vertical lines
    if not enter_times.empty:
        ax2.vlines(enter_times, 0, 1, colors='green', linewidth=0.5)
        ax2.scatter(enter_times, [1] * len(enter_times), color='green', marker='o', s=20, zorder=5, label="Wejście")
    
    # Plot leave events as -1 with vertical lines
    if not leave_times.empty:
        ax2.vlines(leave_times, -1, 0, colors='red', linewidth=0.5)
        ax2.scatter(leave_times, [-1] * len(leave_times), color='red', marker='o', s=20, zorder=5, label="Wyjście")
    
    ax2.set_ylabel(f'Etykieta $L_{channel_idx}$')
    ax2.set_xlabel(r'$t [s]$')
    ax2.set_ylim(-1.5, 1.5)
    ax2.set_yticks([-1, 0, 1])
    ax2.set_yticklabels(['Wyjście', '', 'Wejście'])
    ax2.legend(frameon=True)
    ax2.grid(alpha=0.3)
    
    # Set x-axis limits
    ax1.set_xlim(start_time, end_time)
    
    save_plot()


if __name__=="__main__":
    generate_plot()
    plt.show()