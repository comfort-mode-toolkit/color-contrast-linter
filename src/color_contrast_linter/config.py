import yaml
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass

CONFIG_FILE_NAME = ".color_pairs.yml"

@dataclass
class ColorPairConfig:
    foreground: str
    background: str

@dataclass
class Config:
    min_contrast: str
    pairs: List[ColorPairConfig]

def load_config(path: Path = Path(CONFIG_FILE_NAME)) -> Optional[Config]:
    if not path.exists():
        return None
    
    with open(path, "r") as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError:
            return None
            
    if not data:
        return None

    min_contrast = data.get("min_contrast", "AA")
    pairs = []
    for item in data.get("pairs", []):
        pairs.append(ColorPairConfig(
            foreground=item.get("foreground", ""),
            background=item.get("background", "")
        ))
    
    return Config(min_contrast=min_contrast, pairs=pairs)

def create_default_config(path: Path = Path(CONFIG_FILE_NAME)):
    default_data = {
        "min_contrast": "AA",
        "pairs": [
            {
                "foreground": "#000000",
                "background": "#ffffff"
            },
            {
                "foreground": "#ffffff",
                "background": "#000000"
            }
        ]
    }
    with open(path, "w") as f:
        yaml.dump(default_data, f, default_flow_style=False)
