import os
import anyconfig

from attrdict import AttrDict


def load_yaml(yaml_path):
    return AttrDict(anyconfig.load(yaml_path))

if 'settings' not in globals():
    settings = load_yaml(
        os.path.join(os.getenv('CONFIG_DIR', './config/'), '*.yml')
    )
