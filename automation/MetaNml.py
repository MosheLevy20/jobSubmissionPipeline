from __future__ import division
import math as m
exp = m.exp
sqrt = m.sqrt
log10 = m.log10
log = m.log


#this was edited from vscode





patch = "zFix"
runName = "zFix"

chi = 0.76*0.588
k_b=1.3806490e-16
mp = 1.6605390e-24
mu = 0.588*mp


mHeating = []

lcools = [3e22]
tcools = [5e15]

#zmets = [1e-3]
#zs = [4]
zmets = [1e-3]
zs=[4]
resolutions = [3,4,5,6,7,8,9]
Tnns = [[10**5,1e-3]]

#Tnns = [[1e5,1e-3]]
levelmin = [] 
levelmax = []


units_length = []
units_density = []
units_time = []

tout = []
noutput = []
z_ave = []
z_UV = []

d_region = []

subRunNames = []
nOut = 200
for zmindex, zmet in enumerate(zmets):
        for zindex, z in enumerate(zs):
            for Tindex, Tn in enumerate(Tnns):
                T,nH = Tn
                n = nH/chi
                tCool = tcools[Tindex]
                lCool = lcools[Tindex]

                for res in resolutions:
                    subRunNames.append(runName+"_res-"+str(res)+"_z-"+str(z)+"_Z-"+str(zmet)+"_Tindex-"+str(Tindex))

                    levelmin.append(res)
                    levelmax.append(res)

                    unit_l = 16*lCool
                    units_length.append(unit_l)

                    unit_d = nH*mp/0.76
                    #unit_d=nH*mp
                    units_density.append(unit_d)
                    
                    unit_t = unit_l*m.sqrt(mu/(k_b*T))
                    units_time.append(unit_t)
                    touti = []
                    for t0 in range(nOut):
                        t = t0/nOut*tCool*5
                        touti.append(t/unit_t)
                    tout.append(touti)
                    noutput.append(nOut)
                    z_ave.append(zmet)
                    z_UV.append(z)

                    d_region.append(1)
                    #print(T,nH,heatingTerm(T,nH,z,zmet))
                    #mHeating.append(heatingTerm(T,nH,z,zmet,1,1))



#for each parameter to edit, write an array with the i'th value corresponding to the i'th subrun
#then add the name of your array to the correct "parameter type" array, e.g. AMR_PARAMS_TO_EDIT



amr_params = ["levelmin", "levelmax"]
cooling_params = ["z_ave","z_UV"]#,"mHeating"]
units_params = ["units_density","units_length","units_time"]
output_params = ["tout","noutput"]
init_params = ["d_region"]
parameter_master_list = ["amr_params","cooling_params","units_params","output_params","init_params"]

