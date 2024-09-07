import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import List, Tuple

# Constants
INPUT_DIRECTORY = Path(r"<path_to_your_csv_directory>")
OUTPUT_PLOT = Path("<output_filename>.pdf")
PLOT_TITLE = "<Your Plot Title>"

# Keywords to search for in file names
KEYWORDS = ["PPO", "A2C", "DQN", "DDPG", "SAC", "TD3", "C51"]


def get_csv_files(directory: Path) -> List[Path]:
    """Get all CSV files in the given directory."""
    csv_files = list(directory.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {directory}")
    return csv_files


def load_and_process_data(file_path: Path) -> Tuple[pd.DataFrame, str, str]:
    """Load data from CSV and process it."""
    df = pd.read_csv(file_path)
    if len(df.columns) > 2:
        df = df.iloc[:, 1:]
    x_label, y_label = df.columns
    return df, x_label, y_label


def get_label_from_filename(filename: str) -> str:
    """Extract label from filename based on keywords."""
    for keyword in KEYWORDS:
        if keyword.lower() in filename.lower():
            return keyword
    return filename


def create_plot(csv_files: List[Path]) -> plt.Figure:
    """Create the plot from CSV files."""
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(12, 7))

    for file in csv_files:
        df, x_label, y_label = load_and_process_data(file)
        label = get_label_from_filename(file.name)
        sns.lineplot(data=df, x=x_label, y=y_label, ax=ax, label=label)

    ax.set_title(PLOT_TITLE, fontsize=16)
    ax.set_xlabel(x_label, fontsize=12)
    ax.set_ylabel(y_label, fontsize=12)
    plt.legend(title="Algorithms", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()

    return fig


def save_plot(fig: plt.Figure, output_path: Path):
    """Save the plot to a file."""
    fig.savefig(output_path, format="pdf", dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Plot saved successfully as {output_path}")


def main():
    """Main function to orchestrate the plot creation process."""
    try:
        csv_files = get_csv_files(INPUT_DIRECTORY)
        fig = create_plot(csv_files)
        save_plot(fig, OUTPUT_PLOT)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
