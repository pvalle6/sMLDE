load 1pga.pdb #[file path to reference GB1 mutant]
load INPUT, id_
# align 1pga.pdb, id_

output = cmd.align(id_, 1pga.pdb)
python
with open("rmsd_out.txt", "w") as f:
   f.write(output)
f.close()
python end