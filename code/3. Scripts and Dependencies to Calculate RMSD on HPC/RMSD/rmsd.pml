load 1pga.pdb
load INPUT, PETER

output = align(1pga,PETER)
python
with open("rmsd_out.txt", "a") as f:
   f.write(output)
f.close()
python end