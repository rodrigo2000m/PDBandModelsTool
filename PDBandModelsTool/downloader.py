#standar modules
import requests
import os
from Bio import SeqIO


# code to download model from AlphaFold database
def download_AF_models(AF_dir, id_sequences):
    for uniprot_id in id_sequences:
        #AlphaFold url for download models
        alphafold_url = f"https://alphafold.ebi.ac.uk/files/AF-{uniprot_id}-F1-model_v4.pdb"
        #download the model if the response is correct
        response = requests.get(alphafold_url)
        if response.status_code == 200:
            AF_out = os.path.join(AF_dir, uniprot_id+"_AF.pdb")
            with open(AF_out, "w") as file:
                file.write(response.text)
            print(f"{uniprot_id}_AF.pdb downloaded in {AF_dir}")

        else:
            print(f"No model found for UniProt ID in AlphaFold db: {uniprot_id}")

# code to download model from Swiss database
def download_swiss_models(swiss_dir, id_sequences):
    for uniprot_id in id_sequences:
        #swiss url
        swiss_url = f"https://swissmodel.expasy.org/repository/uniprot/{uniprot_id}.pdb"
        response = requests.get(swiss_url)
        if response.status_code == 200:
            swiss_out = os.path.join(swiss_dir, uniprot_id+"_swiss.pdb")
            with open(swiss_out, "w") as file:
                file.write(response.text)
            print(f"{uniprot_id}_swiss.pdb downloaded in {swiss_dir}")

        else:
            print(f"No model found for UniProt ID is Swiss db: {uniprot_id}")

# code to download structure from PDB database
def get_pdb_codes(uniprot_id):
    #uniprot url to found pdb codes
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        pdb_entries = []
        for ref in data.get("uniProtKBCrossReferences", []):
            if ref["database"] == "PDB":
                pdb_entries.append(ref["id"])

        # check if PDB entries there are
        if pdb_entries:
            print(f"{uniprot_id} have structures in PDB: {', '.join(pdb_entries)}")
            return pdb_entries
        else:
            print(f"{uniprot_id} haven´t structures in PDB.")
    else:
        print(f"Error culting {uniprot_id} uniprot code. Status code: {response.status_code}")



def download_pdb_structures(pdb_dir, id_sequences):
    for uniprot_id in id_sequences:
        # get pdb codes from uniprot code usuing uniprot api 
        pdb_codes = get_pdb_codes(uniprot_id)

        if pdb_codes:
            for pdb_code in pdb_codes:
                # pdb url
                pdb_url = f"https://files.rcsb.org/download/{pdb_code}.pdb"

                response = requests.get(pdb_url)
                if response.status_code == 200:
                    pdb_out = os.path.join(pdb_dir, uniprot_id+"_"+pdb_code+".pdb")
                    with open(pdb_out,  "w") as file:
                        file.write(response.text)
                    print(f"{uniprot_id}_{pdb_code}.pdb downloaded in {pdb_dir}")

                else:
                    print(f"Error getting {pdb_code} from PDB")



#code to download model from ESM Atlas database

def search_sequence_by_uniprot(fasta_file, id_sequence):
    for record in SeqIO.parse(fasta_file, "fasta"):
        if id_sequence in record.id:
            if len(record.seq) < 400:
                print(f"Sequence of {id_sequence} is shorter than 400")
                return str(record.seq)
            else: 
                print(f"Sequence of {id_sequence} is longer than 400")

def download_esm_atlas_models(esm_atlas_dir, fasta_file,  id_sequences):
    for uniprot_id in id_sequences:
        #search sequence with id_sequences
        sequence = search_sequence_by_uniprot(fasta_file, uniprot_id)
        if sequence:
            #ESM Atlas url for download models
            esm_atlas_url =url = "https://api.esmatlas.com/foldSequence/v1/pdb/"

            #download the model if the response is correct
            response = requests.post(esm_atlas_url, data=sequence)
            
            if response.status_code == 200:
                ESM_atlas_out = os. path.join(esm_atlas_dir, uniprot_id+"_ESMAtlas.pdb")
                with open(ESM_atlas_out, "w") as file:
                    file.write(response.text)
                print(f"{uniprot_id}_ESMAtlas.pdb downloaded in {esm_atlas_dir}")
            else :
                print("No model found with {uniprot_id} sequence in ESM Atlas db.")

