import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Constants
INPUT_FILE = r"PATH TO THE CSV FILE"
OUTPUT_PLOT = "TITLE"
PLOT_TITLE = "TITLE"

try:
    # Load data
    df = pd.read_csv(INPUT_FILE)

    # Remove the first column
    df = df.iloc[:, 1:]

    # Extract labels from the remaining columns
    x_label, y_label = df.columns

    # Set up the plot style
    sns.set_style("whitegrid")

    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 7))
    sns.lineplot(data=df, x=x_label, y=y_label, ax=ax)

    # Customize the plot
    ax.set_title(PLOT_TITLE, fontsize=16)
    ax.set_xlabel(x_label, fontsize=12)
    ax.set_ylabel(y_label, fontsize=12)
    plt.tight_layout()

    # Save the plot
    fig.savefig(OUTPUT_PLOT, format="pdf", dpi=300)
    plt.close(fig)

    print(f"Plot saved successfully as {OUTPUT_PLOT}")

except FileNotFoundError:
    print(f"Error: The input file '{INPUT_FILE}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
