# stanfard modules
import argparse
import os
# modules
from fasta_handler import read_fasta
from downloader import download_AF_models, download_swiss_models, download_pdb_structures, download_esm_atlas_models

def main():
    # comments on the arguments
    parser = argparse.ArgumentParser(
        description = "Script to download protein 3D structures, align sequences, superpose 2D structures and generate a report."
        )
    parser.add_argument(
        "fasta_file",
        type = str,
        help = "Path to the FASTA file containing the sequences to process.",
        )

    # reading fasta file 
    args = parser.parse_args()
    fasta_file = args.fasta_file
    name_fasta_file = os.path.basename(fasta_file)

    #automated setting working directory  
    working_dir = os.path.dirname(fasta_file)
    print(f"Working directory: {working_dir}")
    
    outputs_dir = os.path.join(working_dir, "outputs")
    os.mkdir(outputs_dir)
    print(f"Output directory created in {outputs_dir}")
    
    print(f"Processign file: {name_fasta_file}")
    sequences = read_fasta(fasta_file)
    print("Reading fasta file finished")
    

    # download AF models
    AF_dir = os.path.join(outputs_dir, "AF_models")
    os.mkdir(AF_dir)
    download_AF_models(AF_dir, sequences)

    # download swiss models
    swiss_dir = os.path.join(outputs_dir, "swiss_models")
    os.mkdir(swiss_dir)
    download_swiss_models(swiss_dir, sequences)

    # download pdb structures from pdb
    pdb_dir = os.path.join(outputs_dir, "pdb_structures")
    os.mkdir(pdb_dir)
    download_pdb_structures(pdb_dir, sequences)

    # download ESM Atlas models
    esm_atlas_dir = os.path.join(outputs_dir, "ESM_Atlas_models")
    os.mkdir(esm_atlas_dir)
    download_esm_atlas_models(esm_atlas_dir, fasta_file, sequences)


if __name__ == "__main__":
    main()
        

