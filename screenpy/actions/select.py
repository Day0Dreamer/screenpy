from selenium.webdriver.support.ui import Select as SelSelect

from ..decorators import beat, MINOR


class Select(object):
    @staticmethod
    def the_option_named(text):
        return SelectByText(text)

    @staticmethod
    def the_opton_at_index(index):
        return SelectByIndex(index)

    @staticmethod
    def the_option_with_value(value):
        return SelectByValue(value)

    def from_the(self, target):
        self.target = target


class SelectByText(Select):
    @beat(
        "{0} selects the option '{text}' from the {target}.",
        desc_attrs=["text", "target"],
        severity=MINOR,
    )
    def perform_as(self, the_actor):
        element = self.target.resolve_for(the_actor)
        select = SelSelect(element)
        select.select_by_visible_text(self.text)

    def __init__(self, text):
        self.text = text


class SelectByIndex(Select):
    @beat(
        "{0} selects the option at index {index} from the {target}.",
        desc_attrs=["index", "target"],
        severity=MINOR,
    )
    def perform_as(self, the_actor):
        element = self.target.resolve_for(the_actor)
        select = SelSelect(element)
        select.select_by_index(self.index)

    def __init__(self, index):
        self.index = index


class SelectByValue(Select):
    @beat(
        "{0} selects the option with value '{value}' from the {target}.",
        desc_attrs=["value", "target"],
        severity=MINOR,
    )
    def perform_as(self, the_actor):
        element = self.target.resolve_for(the_actor)
        select = SelSelect(element)
        select.select_by_value(self.value)

    def __init__(self, value):
        self.value = value
