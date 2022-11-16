chimera --nogui matchmaker.py > results.dat
more results.dat | grep RMSD > rmsd.dat
more results.dat | grep "sequence alignment" > models.dat
paste rmsd.dat models.dat  > rmsd_models.dat
awk 'BEGIN {min = 999999} {if($8 < min) min = $8} END {print min}' rmsd_models.dat
