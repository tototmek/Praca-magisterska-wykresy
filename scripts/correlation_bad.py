import matplotlib.pyplot as plt
import numpy as np
from matplotlib.legend_handler import HandlerTuple

from utils import *
from filtr_brak import moving_average, moving_median, data_range

def generate_plot():
    setup_latex_plots()
    data = np.load("src/correlation-bad.npz")

    # Extract the arrays using the keys defined above
    time = data['time']
    detrended = data['detrended']
    enter_times = data['enter_ts']
    leave_times = data['leave_ts']
    static_up_threshold = data['up_threshold']
    static_bottom_threshold = data['bottom_threshold']
    static_correlation_signal = data['correlation_signal']
    static_fsm_enter_ts = data['fsm_enter_ts']
    static_fsm_leave_ts = data['fsm_leave_ts']
    data.close()

    data = np.load("src/correlation-adaptive-bad.npz")
    adaptive_up_threshold = data['up_threshold']
    adaptive_bottom_threshold = data['bottom_threshold']
    adaptive_correlation_signal = data['correlation_signal']
    adaptive_fsm_enter_ts = data['fsm_enter_ts']
    adaptive_fsm_leave_ts = data['fsm_leave_ts']
    data.close()

    fig, (ax0, ax1, ax2) = plt.subplots(3, 1, figsize=(TEXT_WIDTH, TEXT_WIDTH), sharex=True, gridspec_kw={'height_ratios': [1/1.618, 1, 1]})


    enter_times = (enter_times-time[0])*100
    leave_times = (leave_times-time[0])*100
    static_fsm_enter_ts = (static_fsm_enter_ts-time[0])*100
    static_fsm_leave_ts = (static_fsm_leave_ts-time[0])*100
    adaptive_fsm_enter_ts = (adaptive_fsm_enter_ts-time[0])*100
    adaptive_fsm_leave_ts = (adaptive_fsm_leave_ts-time[0])*100

    for ts in list(enter_times) + list(leave_times):
        ax0.axvline(x=ts, color='gray', ls=':', lw=0.5)
        ax1.axvline(x=ts, color='gray', ls=':', lw=0.5)
    ax0.axhline(y=0, color='gray', ls='--', lw=0.5)
    ax1.axhline(y=0, color='gray', ls='--', lw=0.5)


    ax0_pinheight = np.max(detrended) * 1.1
    ax0_minuspinheight = np.min(detrended) * 1.1
    ax0.set_title(r"\small \textbf{(a) Sygnał wejściowy}")
    ax0.vlines(enter_times, 0, ax0_pinheight, colors='green', linewidth=1.0)
    s1 = ax0.scatter(enter_times, [ax0_pinheight] * len(enter_times), color='green', marker='o', s=20, zorder=5)
    ax0.vlines(leave_times, ax0_minuspinheight, 0, colors='red', linewidth=1.0)
    s2 = ax0.scatter(leave_times, [ax0_minuspinheight] * len(leave_times), color='red', marker='o', s=20, zorder=5)
    p, = ax0.plot(detrended, c="black", lw=0.75)
    ax0.set_ylabel(r'$y(k)$')
    ax0.legend([p, (s1, s2)], ["$y(k)$", "Anotacja"], 
           handler_map={tuple: HandlerTuple(ndivide=None)},
           loc='upper right')

    ax1_pinheight = np.max(static_correlation_signal) * 1.1
    ax1_minuspinheight = np.min(static_correlation_signal) * 1.1
    ax1.set_title(r"\small \textbf{(b) Algorytm z progowaniem statycznym}")
    t1, = ax1.plot(static_up_threshold, c="green", ls="--", lw=0.75)
    __, = ax1.plot(static_bottom_threshold, c="green", ls="--", lw=0.75)
    ax1.vlines(static_fsm_enter_ts, 0, ax1_pinheight, colors='green', linewidth=1.0)
    s1 = ax1.scatter(static_fsm_enter_ts, [ax1_pinheight] * len(static_fsm_enter_ts), color='green', marker='o', s=20, zorder=5)
    ax1.vlines(static_fsm_leave_ts, ax1_minuspinheight, 0, colors='red', linewidth=1.0)
    s2 = ax1.scatter(static_fsm_leave_ts, [ax1_minuspinheight] * len(static_fsm_leave_ts), color='red', marker='o', s=20, zorder=5)
    ax1.set_ylabel(r'$r_{wy}(k)$')
    p, = ax1.plot(static_correlation_signal, c="black", lw=0.75)
    ax1.legend([p, t1, (s1, s2)], [r'$r_{wy}(k)$', r'$\gamma(k)$', "Detekcja"], 
           handler_map={tuple: HandlerTuple(ndivide=None)},
           loc='upper right')

    ax2_pinheight = np.max(adaptive_correlation_signal) * 1.1
    ax2_minuspinheight = np.min(adaptive_correlation_signal) * 1.1
    ax2.set_title(r"\small \textbf{(c) Algorytm z progowaniem adaptacyjnym}")
    t1, = ax2.plot(adaptive_up_threshold, c="green", ls="--", lw=0.75)
    __, = ax2.plot(adaptive_bottom_threshold, c="green", ls="--", lw=0.75)
    ax2.vlines(adaptive_fsm_enter_ts, 0, ax2_pinheight, colors='green', linewidth=1.0)
    s1 = ax2.scatter(adaptive_fsm_enter_ts, [ax2_pinheight] * len(adaptive_fsm_enter_ts), color='green', marker='o', s=20, zorder=5)
    ax2.vlines(adaptive_fsm_leave_ts, ax2_minuspinheight, 0, colors='red', linewidth=1.0)
    s2 = ax2.scatter(adaptive_fsm_leave_ts, [ax2_minuspinheight] * len(adaptive_fsm_leave_ts), color='red', marker='o', s=20, zorder=5)
    ax2.set_ylabel(r'$r_{wy}(k)$')
    p, = ax2.plot(adaptive_correlation_signal, c="black", lw=0.75)
    ax2.legend([p, t1, (s1, s2)], [r'$r_{wy}(k)$', r'$\gamma(k)$', "Detekcja"], 
           handler_map={tuple: HandlerTuple(ndivide=None)},
           loc='upper right')
    ax2.set_xlabel(r'$k$')
    ax2.set_xlim((0, 11500))

    save_plot()

if __name__=="__main__":
    generate_plot()
    plt.show()