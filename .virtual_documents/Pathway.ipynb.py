import escher
from escher import Builder
import cobra
from time import sleep
escher.rc['never_ask_before_quit'] = True


Core = Builder(
    map_name='e_coli_core.Core metabolism',
    model_name='e_coli_core',
)
Core


model = cobra.io.load_json_model('e_coli_core.json')
reverse = True
step = 0.1
timestep = 0.1
duration = 1500 # seconds
lim = [0, 0.5]
val = lim[-1]
for _ in range(int(duration / timestep)):
    model.reactions.EX_o2_e.lower_bound = -val
    solution = model.optimize()
    Core.reaction_data = solution.fluxes
    if val <= lim[0]:
        reverse = True
    if val >= lim[1]:
        reverse = False
    if reverse:
        val += step
    else:
        val -= step
    sleep(timestep)


Core.save_html("Core.html")


CarbonMeta =  Builder(
    model_json="Recon3D.json",
    map_name= 'RECON1.Carbohydrate metabolism'
)
CarbonMeta.save_html("CarbonMeta.html")


CarbonMeta.save_html("CarbonMeta.html")


model = cobra.io.load_json_model('Recon3D.json')
reverse = True
step = 0.1
timestep = 0.1
duration = 1500 # seconds
lim = [0, 0.5]
val = lim[-1]
for _ in range(int(duration / timestep)):
    model.reactions.EX_o2_e.lower_bound = -val
    solution = model.optimize()
    EMP_TCA_PPP.reaction_data = solution.fluxes
    if val <= lim[0]:
        reverse = True
    if val >= lim[1]:
        reverse = False
    if reverse:
        val += step
    else:
        val -= step
    sleep(timestep)


FattyAcid = Builder(
    model_name='iMM904',
    map_name= 'iJO1366.Fatty acid beta-oxidation',
    )
FattyAcid.save_html("FattyAcid.html")


FattyAcid


FattyAcid.save_html("FattyAcid.html")


EMP_TCA_PPP = Builder (map_name= 'RECON1.Glycolysis TCA PPP')


EMP_TCA_PPP


EMP_TCA_PPP.save_html("EMP_TCA_PPP.html")


AA = Builder(map_name= 'RECON1.Amino acid metabolism (partial)')
AA.save_html("AA.html")


AA


Nucleotide = Builder(map_name= 'iJO1366.Nucleotide and histidine biosynthesis')
Nucleotide.save_html("Nucleotide.html")


FAS = Builder(map_name= 'iJO1366.Fatty acid biosynthesis (saturated)')
FAS.save_html("FAS.html")



