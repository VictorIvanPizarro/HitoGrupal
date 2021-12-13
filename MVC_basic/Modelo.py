# model_view_controller.py
import Basic_CRUD
import mvc_exceptions as mvc_exc


class ModelBasic(object):

    def __init__(self, application_items):
        self._item_type = 'product'
        self.create_items(application_items)

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type

    def create_item(self, name, price, quantity):
        Basic_CRUD.create_item(name, price, quantity)

    def create_items(self, items):
        Basic_CRUD.create_items(items)

    def read_item(self, name):
        return Basic_CRUD.read_item(name)

    def read_items(self):
        return Basic_CRUD.read_items()

    def update_item(self, name, price, quantity):
        Basic_CRUD.update_item(name, price, quantity)

    def delete_item(self, name):
        Basic_CRUD.delete_item(name)