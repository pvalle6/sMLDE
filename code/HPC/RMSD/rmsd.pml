load 1pga.pdb #[file path to reference GB1 mutant]
load ID_1_VDGV.pdb #[file path to test GB1 mutant]
# align 1pga.pdb, ID_1_VDGV.pdb

output = cmd.align(ID_1_VDGV.pdb, 1pga.pdb)
python
with open("rmsd_out.txt", "w") as f:
   f.write(output)
f.close()
python end