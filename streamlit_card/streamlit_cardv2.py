import os
from typing import Optional

import streamlit.components.v1 as components

_RELEASE = False
COMPONENT_NAME = "streamlit_cardv2"

if _RELEASE:  # use the build instead of development if release is true
    root_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(root_dir, "frontend/build")

    _streamlit_card = components.declare_component(COMPONENT_NAME, path=build_dir)
else:
    _streamlit_card = components.declare_component(
        COMPONENT_NAME, url="http://localhost:3000"
    )


def card(
    title: str,
    text: str,
    height: int,
    width: int,
    margin: int,
    text_color: str,
    bg_color: str,
    image: Optional[str] = None,
    url: Optional[str] = None,
    key: Optional[str] = None,
) -> bool:
    """Creates a UI card like component.

    Args:
        title (str): The title of the card.
        text (str): The text of the card.
        height (int): The height of the box.
        width (int): The width of the box.
        text_color (int): The color of the text.
        bg_color (str): If no image is specified, this color will be the background color.
        image (str, optional): An optional background image. Defaults to None.
        url (str, optional): An optional url to open when the card is clicked. Defaults to None.
        key (str, optional): An optional key for the component. Defaults to None.
    """
    return _streamlit_card(
        title=title, text=text, height=height, width=width, margin=margin, text_color=text_color, bg_color=bg_color, image=image, url=url, key=key, default=False
    )
