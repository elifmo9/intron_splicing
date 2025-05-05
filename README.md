# intron_splicing
Python code that performs a common modification in molecular biology (intron splicing and polyA tail addition)
# mRNA Intron Removal and Poly-A Tail Addition Script

This Python script processes an mRNA sequence by removing introns and appending a poly-A tail. The poly-A tail is commonly used in molecular biology to add stability to mRNA sequences, and this script automates the process of modifying mRNA sequences for downstream applications.

## Features

- **Intron Removal**: The script finds and removes the intron sequence from the provided mRNA sequence.
- **Poly-A Tail Addition**: After removing the intron, the script adds a '7' at the start of the sequence and a poly-A tail (70 adenine bases) to the end.
- **Output**: The modified mRNA sequence is saved to a new file named `splicedmrna.txt` in the same directory as the script.

## Use Cases

- **mRNA Sequence Preparation**: Ideal for researchers working with mRNA sequences who need to remove introns and add a poly-A tail.
- **Bioinformatics**: Useful for bioinformaticians who are processing sequences for genetic research, gene expression studies, or synthetic biology.
- **Educational Purpose**: A great script for learning about sequence manipulation in bioinformatics.

## Requirements

- Python 3.x

## How to Use

1. Clone or download this repository.
2. Prepare two text files:
   - One containing the **mRNA sequence** (e.g., `mRNA.txt`).
   - One containing the **intron sequence** (e.g., `intron.txt`).
   - Example files have been added for you to play around with but feel free to add your own files
3. Run the script, and provide the file names when prompted:

```bash
$ python spliced_mrna.py
Enter the mRNA file name (e.g. mRNA.txt): mRNA.txt
Enter the intron file name (e.g. intron.txt): intron.txt
