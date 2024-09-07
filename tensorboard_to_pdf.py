import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import List, Tuple, Dict
import numpy as np

# Constants
INPUT_DIRECTORY = Path(r"<path_to_your_csv_directory>")
OUTPUT_PLOT = Path("<output_filename>.pdf")
PLOT_TITLE = "<Your Plot Title>"

# Keywords to search for in file names, maintaining order
KEYWORDS = ["C51", "DQN", "PPO"]


def get_csv_files(directory: Path) -> List[Path]:
    """Get all CSV files in the given directory."""
    csv_files = list(directory.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {directory}")
    return csv_files


def load_and_process_data(file_path: Path) -> Tuple[np.ndarray, np.ndarray, str, str]:
    """Load data from CSV and process it."""
    df = pd.read_csv(file_path)
    columns = df.columns.tolist()
    x_label, y_label = columns[1], columns[2] if len(columns) > 2 else columns[1]
    return df[x_label].to_numpy(), df[y_label].to_numpy(), x_label, y_label


def get_label_from_filename(filename: str, keywords: List[str]) -> str:
    """Extract label from filename based on keywords."""
    filename_lower = filename.lower()
    for keyword in keywords:
        if keyword.lower() in filename_lower:
            return keyword
    return filename


def create_plot(csv_files: List[Path], keywords: List[str]) -> plt.Figure:
    """Create the plot from CSV files."""
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(12, 7))

    color_palette = sns.color_palette(n_colors=len(keywords))
    keyword_colors = dict(zip(keywords, color_palette))

    data_dict: Dict[str, Tuple[np.ndarray, np.ndarray]] = {}
    x_label, y_label = "", ""

    for file in csv_files:
        x, y, x_label, y_label = load_and_process_data(file)
        label = get_label_from_filename(file.name, keywords)
        data_dict[label] = (x, y)

    # Plot data in the order of keywords
    for label in keywords:
        if label in data_dict:
            x, y = data_dict[label]
            color = keyword_colors[label]
            ax.plot(x, y, label=label, color=color)

    # Plot any remaining data not in keywords
    for label, (x, y) in data_dict.items():
        if label not in keywords:
            ax.plot(x, y, label=label)

    ax.set_title(PLOT_TITLE, fontsize=16)
    ax.set_xlabel(x_label, fontsize=12)
    ax.set_ylabel(y_label, fontsize=12)
    ax.legend(title="Algorithms", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()

    return fig


def save_plot(fig: plt.Figure, output_path: Path) -> None:
    """Save the plot to a file."""
    fig.savefig(output_path, format="pdf", dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Plot saved successfully as {output_path}")


def main() -> None:
    """Main function to orchestrate the plot creation process."""
    try:
        csv_files = get_csv_files(INPUT_DIRECTORY)
        fig = create_plot(csv_files, KEYWORDS)
        save_plot(fig, OUTPUT_PLOT)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
