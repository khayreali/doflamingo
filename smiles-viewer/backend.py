from flask import Flask, request, send_file
from flask_cors import CORS
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.rdDepictor import Compute2DCoords
from PIL import Image
import io

app = Flask(__name__)
CORS(app)  # Handle Cross Origin Resource Sharing

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    smiles = request.json['smiles']

    # Create molecule object
    mol = Chem.MolFromSmiles(smiles)

    # Generate 2D coordinates
    Compute2DCoords(mol)

    # Draw molecule as PIL image
    img = Draw.MolToImage(mol, size=(400, 400))

    # Convert PIL image to BytesIO 
    bio = io.BytesIO()
    img.save(bio, format='PNG')
    bio.seek(0)

    # Return PNG file
    return send_file(bio, mimetype='image/png')

if __name__ == '__main__':
    app.run(port=5000)  # Specify the port number here
