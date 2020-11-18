import escher
from escher import Builder
import cobra
from time import sleep


escher.rc['never_ask_before_quit'] = True


builder = Builder()


builder


get_ipython().getoutput("wget -nc http://bigg.ucsd.edu/static/models/iAB_RBC_283.json")


builder = Builder(
    model_json='iAB_RBC_283.json'
)


builder


escher.list_available_maps()


escher.list_available_models()


builder = Builder(
    map_name='e_coli_core.Core metabolism',
    model_name='e_coli_core',
)


builder


builder = Builder()


builder


# Load an Escher map
builder.map_name = 'iJO1366.Central metabolism'


# Load a COBRA model
builder.model_name = 'e_coli_core'


# Find any reactions that are in the map and not in the model, and turn them red
builder.highlight_missing = True


get_ipython().getoutput("wget -nc http://bigg.ucsd.edu/static/models/iJO1366.json")
builder.model = cobra.io.load_json_model('iJO1366.json')


# Run FBA with the model and add the flux data to the map
solution = builder.model.optimize()
builder.reaction_data = solution.fluxes


# Add some data for metabolites
builder.metabolite_data = solution.shadow_prices


# Simplify the map by hiding some labels
builder.hide_secondary_metabolites = True
builder.hide_all_labels = True


builder.reaction_scale = [
    { 'type': 'min', 'color': '#000000', 'size': 12 },
    { 'type': 'median', 'color': '#ffffff', 'size': 20 },
    { 'type': 'max', 'color': '#ff0000', 'size': 25 }
]


builder.reaction_scale_preset = 'GaBuRd'


# Make all the arrows three times as thick
builder.reaction_scale = [
    {k: v * 3 if k == 'size' else v for k, v in x.items()} 
    for x in builder.reaction_scale
]


# some other things to try:
# builder.scroll_behavior = 'zoom'
# builder.reaction_styles = ['size']


builder = Builder(
    height=600, 
    map_name=None, 
    model_name='e_coli_core',
    map_json='https://escher.github.io/1-0-0/5/maps/Escherichiaget_ipython().run_line_magic("20coli/e_coli_core.Core%20metabolism.json',", "")
)
builder


get_ipython().getoutput("wget -nc http://bigg.ucsd.edu/static/models/e_coli_core.json")
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


builder.save_html('example_map.svg')



