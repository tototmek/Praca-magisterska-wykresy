import os
import sys
import matplotlib.pyplot as plt
import pandas as pd

TEXT_WIDTH = 6.5

def setup_latex_plots():
    latex_preamble = r"""
        \usepackage[utf8]{inputenc} 
        \usepackage[T1]{fontenc}
        """
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "serif",
        "font.serif": ["Computer Modern Roman"],
        "text.latex.preamble": latex_preamble,
        # "mathtext.fontset": "cm" 
    })

def save_plot():
    script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    plot_name = script_name.replace("_", "-") + ".pdf"
    plot_path = "plots/" + plot_name
    plt.savefig(plot_path, bbox_inches="tight")
    print(f"Saved plot as {plot_path}")

def load_csv_column(file_path, column_name):
    df = pd.read_csv(file_path)
    column_series = df[column_name]
    column_list = column_series.tolist()
    return column_list