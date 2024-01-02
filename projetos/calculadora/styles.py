import qdarktheme
from variables import PRIMARY_COLOR, DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR


qss = f"""
    buttom[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    buttom[cssClass="specialButton"]:hover {{
        background: {DARKER_PRIMARY_COLOR};
    }}
    buttom[cssClass="specialButton"]:pressed {{
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""


def setup():
    qdarktheme.setup_theme(
        theme='dark',#light
        corner_shape='rounded',#sharp
        custom_colors={
            "[dark]": {
                'primary': '#1e81b0'
            },
            '[light]': { 
                'primary': '#1e81b0'
            },
        },
        additional_qss=qss
    )