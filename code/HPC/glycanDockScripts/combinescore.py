import os
import re
import pandas as pd
import numpy as np
import time

ts = time.time()


# Variables
opath = "/work/pvalle6/Protocol_guide/GlycanDock_refinement_output"        # Output file path
colns = ["total_score", \
         "I_sc", \
         "pep_sc", \
         "reweighted_sc", \
         "rmsALL", \
         "rmsALL_CAPRI_if", \
         "rmsALL_allIF", \
         "rmsALL_if", \
         "rmsBB", \
         "rmsBB_CAPRI_if", \
         "rmsBB_allIF", \
         "rmsBB_if", \
         "rmsCA", \
         "rmsCA_if", \
         "rmsPHIPSI", \
         "rmsPHIPSI_if", \
         "rmsSC_CAPRI_if", \
         "rmsSC_allIF"
]                       # List of column names to be extracted


# 1. List all score files under output directory

scfns = [scfn.strip() for scfn in os.popen("find "+opath+" -name *.score.sc")]


# 2. For each score file, read in as pandas dataframe

scdfs = {scdf : pd.read_csv(scdf, sep="\s+", skiprows=1, usecols=colns)[colns] for scdf in scfns}
    

# 3. Join each table    

sctbs = {}
p = re.compile("([^/\.]+).score.sc")
for coln in colns:
    sctbs[coln] = scdfs[scfns[0]][[coln]].rename(columns={coln:p.search(scfns[0]).group(1)})
    for i in range(1,len(scfns)):
        sctbs[coln] = sctbs[coln].join(scdfs[scfns[i]][[coln]].rename(columns={coln:p.search(scfns[i]).group(1)}))
        

# 4. Export to xlsx file

with pd.ExcelWriter('output.xlsx') as f:
    for coln in colns:
        sctbs[coln].to_excel(f, sheet_name=coln)
    

print("Total time cost: " + str(time.time()-ts) + " sec")
