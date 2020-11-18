import escher
from escher import Builder
import cobra
from time import sleep
escher.rc['never_ask_before_quit'] = True


Core = Builder(
    map_name='e_coli_core.Core metabolism',
    model_name='e_coli_core',
)


Core.save_html("Core.html")


CarbonMeta =  Builder(
    model_json="Recon3D.json",
    map_name= 'RECON1.Carbohydrate metabolism'
)
CarbonMeta.save_html("CarbonMeta.html")


FattyAcid = Builder(
    model_name='iMM904',
    map_name= 'iJO1366.Fatty acid beta-oxidation',
    )
FattyAcid.save_html("FattyAcid.html")


EMP_TCA_PPP = Builder (map_name= 'RECON1.Glycolysis TCA PPP')
EMP_TCA_PPP.save_html



