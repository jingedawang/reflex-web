import re

import pytest
from playwright.sync_api import Page, expect

from reflex.testing import AppHarness
import time


@pytest.fixture
def event_argument_url() -> str:
    from pcweb.pages import docs

    return docs.events.event_arguments.path


def test_lambdas(
    reflex_web_app: AppHarness,
    page: Page,
    event_argument_url: str,
):
    assert reflex_web_app.frontend_url is not None

    page.goto(reflex_web_app.frontend_url + event_argument_url)

    inputs = page.get_by_role("textbox")

    def check_box_color(i, initial_color, input_color, expected_color):
        expect(page.locator(".rt-TextFieldRoot").nth(i)).to_have_css(
            "background-color", initial_color
        )
        inputs.nth(i).fill(input_color)
        inputs.nth(i).blur()
        expect(page.locator(".rt-TextFieldRoot").nth(i)).to_have_css(
            "background-color", expected_color
        )

    check_box_color(0, "rgb(245, 168, 152)", "rgba(4, 168, 152)", "rgb(4, 168, 152)")
    check_box_color(1, "rgb(60, 179, 113)", "DarkBlue", "rgb(0, 0, 139)")
    check_box_color(2, "rgb(222, 173, 227)", "#AEADE3", "rgb(174, 173, 227)")
