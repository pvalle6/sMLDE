load COMPLEX_1fcc_truncated.pdb
load INPUT, mutation
align mutation, COMPLEX_1fcc_truncated
select chain D
remove sele
alter (COMPLEX_1fcc_truncated), chain='A'
alter (mutation), chain='B'
save OUTPUT

