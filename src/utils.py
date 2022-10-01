import yaml
import os


def load_config(path):
    with open(path, 'r', encoding='utf-8') as open_yml:
        return yaml.safe_load(open_yml)

dir_path = os.path.dirname(os.path.realpath(__file__))
conf = load_config(os.path.join(dir_path, "resources/config.yml"))
