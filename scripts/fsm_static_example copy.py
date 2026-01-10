import matplotlib.pyplot as plt
import numpy as np
from matplotlib.legend_handler import HandlerTuple

from utils import *
from filtr_brak import moving_average, moving_median, data_range

def generate_plot():
    setup_latex_plots()
    data = np.load("src/fsm-static.npz")

    # Extract the arrays using the keys defined above
    time = data['time']
    detrended = data['detrended']
    up_threshold = data['up_threshold']
    bottom_threshold = data['bottom_threshold']
    signal_thresholded = data['signal_thresholded']
    fsm_enter_ts = data['fsm_enter_ts']
    fsm_leave_ts = data['fsm_leave_ts']
    enter_times = data['enter_ts']
    leave_times = data['leave_ts']
    data.close()

    fig, (ax0, ax1, ax2) = plt.subplots(3, 1, figsize=(TEXT_WIDTH, 0.75*TEXT_WIDTH), sharex=True, gridspec_kw={'height_ratios': [0.5/1.618, 1, 1/1.618]})


    enter_times = (enter_times-time[0])*100
    leave_times = (leave_times-time[0])*100
    fsm_enter_ts = (fsm_enter_ts-time[0])*100
    fsm_leave_ts = (fsm_leave_ts-time[0])*100

    for ts in list(enter_times) + list(leave_times):
        ax0.axvline(x=ts, color='gray', ls=':', lw=0.5)
        ax1.axvline(x=ts, color='gray', ls=':', lw=0.5)
        ax2.axvline(x=ts, color='gray', ls=':', lw=0.5)
    ax0.axhline(y=0, color='gray', ls='--', lw=0.5)
    ax1.axhline(y=0, color='gray', ls='--', lw=0.5)
    ax2.axhline(y=0, color='gray', ls='--', lw=0.5)


    ax0.vlines(enter_times, 0, 1, colors='green', linewidth=1.0)
    s1 = ax0.scatter(enter_times, [1] * len(enter_times), color='green', marker='o', s=20, zorder=5)
    ax0.vlines(leave_times, -1, 0, colors='red', linewidth=1.0)
    s2 = ax0.scatter(leave_times, [-1] * len(leave_times), color='red', marker='o', s=20, zorder=5)
    ax0.set_ylim((-1.4, 1.4))
    ax0.set_yticks([-1, 0, 1])
    ax0.set_yticklabels(['Wyjście', '', 'Wejście'])
    ax0.legend([(s1, s2)], ["Anotacja"], 
           handler_map={tuple: HandlerTuple(ndivide=None)},
           loc='upper right')

    ax1.plot(up_threshold, c="green", ls="--", lw=0.75, label=r'$\gamma(k)$')
    ax1.plot(bottom_threshold, c="green", ls="--", lw=0.75, label="_")
    ax1.plot(detrended, c="black", lw=0.75, label='$y(k)$')
    ax1.set_ylabel(r'$y(k)$')
    handles, labels = ax1.get_legend_handles_labels()
    ax1.legend(handles[::-1], labels[::-1])

    p, = ax2.plot(signal_thresholded, c="black", lw=0.75)
    ax2.vlines(fsm_enter_ts, 0, 1.3, colors='green', linewidth=1.0)
    s1 = ax2.scatter(fsm_enter_ts, [1.3] * len(fsm_enter_ts), color='green', marker='o', s=20, zorder=5)
    ax2.vlines(fsm_leave_ts, -1.3, 0, colors='red', linewidth=1.0)
    s2 = ax2.scatter(fsm_leave_ts, [-1.3] * len(fsm_leave_ts), color='red', marker='o', s=20, zorder=5)
    ax2.set_ylim((-1.5, 1.5))
    ax2.set_ylabel(r'$Y(k)$')
    ax2.legend([p, (s1, s2)], [r'$Y(k)$', "Detekcja"], 
           handler_map={tuple: HandlerTuple(ndivide=None)},
           loc='upper right')
    ax2.set_xlabel(r'$k$')
    ax2.set_xlim((0, 11500))


    save_plot()

if __name__=="__main__":
    generate_plot()
    plt.show()