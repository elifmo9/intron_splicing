# This script removes introns from an mRNA sequence and adds a poly-A tail.
import os

#ask the user for the mRNA and intron file names
mrna_file = input("Enter the mRNA file name (e.g. mRNA.txt): ").strip()
intron_file = input("Enter the intron file name (e.g. intron.txt): ").strip()

#read mRNA sequence and strip whitespace
with open(mrna_file, 'r') as file:
    mrna = file.read().strip()

#read intron sequence and strip whitespace
with open(intron_file, 'r') as file:
    intron = file.read().strip()

# Print original lengths
print("mRNA length:", len(mrna))
print("Intron length:", len(intron))

# Try to find the intron in the mRNA
start_pos = mrna.find(intron)

if start_pos == -1:
    print("⚠️ Intron not found in mRNA. Saving original mRNA with poly-A tail.")
    spliced = mrna
else:
    print("✅ Intron starts at position:", start_pos)
    spliced = mrna[:start_pos] + mrna[start_pos + len(intron):]

# Add a '7' at the start and 70 A's at the end (poly-A tail)
# This is a common practice in molecular biology to indicate the start of a sequence and to add stability to the mRNA.
final_seq = '7' + spliced + ('A' * 70)

# Get the current directory where the script is located as we want to save the output in the same directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Save to the same directory as the script
output_path = os.path.join(script_dir, 'splicedmrna.txt')
with open(output_path, 'w') as file:
    file.write(final_seq)

print(f"📁 Spliced mRNA saved to: {output_path}")
print("✅ Splicing complete.")