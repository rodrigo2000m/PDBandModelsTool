# standar modules
from Bio import SeqIO
import numpy as np

def read_fasta(fasta_file):
    print("\nSequences in the fasta file:\n")
    identifiers = np.array([])
    for record in SeqIO.parse(fasta_file, "fasta"):
        print(f"ID: {record.id}") # complete sequence identifier
        identifiers = np.append(identifiers, record.id.split("|")[1]) #only the code to search the proteom identifier
        print(f"Descripción: {record.description}")  # description
        print(f"Secuencia: {record.seq}")  # protein sequece
        print("-" * 50)
    
    print(f"\nThere are {len(identifiers)} sequences in {fasta_file}\n")
    return identifiers

