import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


from meta import get_meta
from hero_grid import generate_json

meta = get_meta()
new_cfg = generate_json(meta)

with open(config['dota']['HERO_GRID_CONFIG_FILE'], 'r+') as f:
    data = json.load(f)
    if data['configs'] is not None:
        found = False
        for i, cfg in enumerate(data['configs']):
            if cfg['config_name'] == new_cfg['config_name']:
                data['configs'][i] = new_cfg
                found = True
        if not found:
            data['configs'].append(new_cfg)
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()