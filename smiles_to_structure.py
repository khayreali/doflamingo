from rdkit import Chem
from rdkit.Chem import Draw
from PIL import Image
import streamlit as st
import io

st.title('doflamingo')

# Input SMILES string
smiles_string = st.text_input('Enter a SMILES string:')

if smiles_string:
    # Create molecule object
    molecule = Chem.MolFromSmiles(smiles_string)

    if molecule is not None:
        # Generate 2D coordinates
        Chem.rdDepictor.Compute2DCoords(molecule)
        
        # Draw molecule as PIL image
        img = Draw.MolToImage(molecule, size=(400, 400))

        # Convert PIL image to BytesIO
        bio = io.BytesIO()
        img.save(bio, format='png')
        bio.seek(0)
        
        # Display the molecule
        st.image(bio, caption="2D Structure", use_column_width=True)
    else:
        st.write("Invalid SMILES string")
