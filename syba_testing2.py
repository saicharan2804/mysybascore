from rdkit import Chem
from syba.syba import SybaClassifier
syba = SybaClassifier()
syba.fitDefaultScore()
smi = "O=C(C)Oc1ccccc1C(=O)O"
print(syba.predict(smi))