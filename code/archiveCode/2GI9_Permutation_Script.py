#>GB1_WT
#TYKLILNGKTLKGETTTEAVDAATAEKVFKQYANDNGVDGEWTYDDATKTFTVTE

#wild type variation
#

#first constant
#TYKLILNGKTLKGETTTEAVDAATAEKVFKQYANDNG

#second constant
#EWTYDDATKTFT

#third constant
#TE

#protein with permutations
#TYKLILNGKTLKGETTTEAVDAATAEKVFKQYANDNxxxGEWTYDDATKTFTxTE

amino_acid = ['A','R','N','D','C','Q','E','G','H','I','L','K',
                             'M','F','P','S','T','W','Y','V']

#constants to build sequences with after permeations 

f = open("variationPerm.txt","a")

for index1 in (range(len(amino_acid))):
    first_mutation = (amino_acid[index1])
    for index2 in (range(len(amino_acid))):
        second_mutation = amino_acid[index2]
        for index3 in (range(len(amino_acid))):
            third_mutation = amino_acid[index3]
            for index4 in (range(len(amino_acid))):
                fourth_mutation = amino_acid[index4]
                #outputs the current perm
                #f.write(first_constant + first_mutation + second_mutation + third_mutation + second_constant + fourth_mutation + third_constant + "\n")
                f.write(first_mutation + second_mutation + third_mutation + fourth_mutation + "\n")

f.close()
                
   



