import math
import json

category_names = ["Carry", "Midlane", "Offlane", "Soft Support", "Hard Support"]
category_subfix = ["Meta", "Niche"]

width = 1100
max_row_height = 450
spacing = 0

def generate_json(meta):

    config = {}
    config['config_name'] = "Dota2ProTracker"
    categories = []
    for posi, pos in enumerate(meta):
        y = 0
        for cati, cat in enumerate(pos):
            category = {}
            category['category_name'] = "{} {}".format(category_names[posi], category_subfix[cati])
            category['x_position'] = posi * width / 5 + posi * spacing / 2
            category['y_position'] = y + cati * spacing / 2
            category['width'] = width / 5 - spacing / 2
            height = min(max_row_height, 100 * math.ceil(len(cat) / 4) + spacing / 2) # 4 columns, 100 per hero?
            category['height'] = height
            y += max_row_height
            hero_ids = []
            for heroes in cat:
                hero_ids.append(int(heroes['id']))
            category['hero_ids'] = hero_ids
            categories.append(category)
    config['categories'] = categories
    return config
