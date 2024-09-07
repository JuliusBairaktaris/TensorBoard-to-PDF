# TensorBoard-to-PDF

This script converts TensorBoard CSV exports into high-quality PDF plots using pandas, matplotlib, and seaborn for use in LaTeX.

## Features

- Automatically reads all CSV files from a specified directory
- Detects algorithm names from filenames using keywords (e.g., ALE_Tetris-v5__dqn_atari_jax --> DQN). Can easily be expanded and adapted.
- Creates a line plot for each CSV file
- Saves the plot as a high-quality PDF

## Requirements

- Python 3.x
- pandas
- matplotlib
- seaborn
