import escher
from escher import Builder
import cobra
from time import sleep
escher.rc['never_ask_before_quit'] = True


builder = Builder(
    map_name='e_coli_core.Core metabolism',
    model_name='e_coli_core',
)


builder


builder = Builder(
    map_name='iMM904.Central carbon metabolism',
    model_name='iMM904',
)
builder


builder = Builder(map_name= 'iJO1366.Fatty acid beta-oxidation')
builder


builder = Builder(model_json="Recon3D.json",
                 map_name= 'RECON1.Carbohydrate metabolism')
builder


reverse = True
step = 0.1
timestep = 0.1
duration = 1500 # seconds
lim = [0, 0.5]
val = lim[-1]
for _ in range(int(duration / timestep)):
    model.reactions.EX_mal__L_e.lower_bound = -val
    solution = model.optimize()
    builder.reaction_data = solution.fluxes
    if val <= lim[0]:
        reverse = True
    if val >= lim[1]:
        reverse = False
    if reverse:
        val += step
    else:
        val -= step
    sleep(timestep)


import pyinspect as pi
pi.what(model.reactions)


builder = Builder(map_name= 'RECON1.Glycolysis TCA PPP')
builder


builder_Ac = Builder(map_name= 'RECON1.Amino acid metabolism (partial)')
builder_Ac


builder = Builder(map_name= 'iJO1366.Nucleotide and histidine biosynthesis')
builder


builder_Fa = Builder(map_name= 'iJO1366.Fatty acid biosynthesis (saturated)')
builder_Fa


bu



