
import os

k=3
folder='simulation_data/abpot/'

f = open("simulation_data/metadata.dat", "w")
for n in range(0,1000):
    datafile=folder+str(n)+'.dat'
    if os.path.exists(datafile):
        # read the imposed position is the expected one
        with open(datafile) as g:
            _ = g.readline()
            _ = g.readline()
            firstline = g.readline()
        imposed_position = firstline.split(' ')[-1][:-1]
        datafile = datafile.replace('simulation_data/','')
        # write one file per file
        f.write(datafile+' '+str(imposed_position)+' '+str(k)+'\n')
f.close()