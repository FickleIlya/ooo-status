import pytest


class TestTreeStore:

    def test_getAll(self, instance, items):
        assert instance.getAll() == items

    @pytest.mark.parametrize("id, item", [(1, {"id": 1, "parent": "root"}),
                                          (4, {"id": 4, "parent": 2, "type": "test"}),
                                          (8, {"id": 8, "parent": 4, "type": None}),
                                          (9, None)])
    def test_getItem(self, instance, id, item):
        item_from_method = instance.getItem(id)
        assert item_from_method == item

    @pytest.mark.parametrize("id, childrens", [(4, [{"id": 7, "parent": 4, "type": None},
                                                    {"id": 8, "parent": 4, "type": None}]),
                                               (5, []),
                                               (2, [{"id": 4, "parent": 2, "type": "test"},
                                                    {"id": 5, "parent": 2, "type": "test"},
                                                    {"id": 6, "parent": 2, "type": "test"}]),
                                               (9, [])])
    def test_getChildren(self, instance, id, childrens):
        childrens_from_method = instance.getChildren(id)
        assert childrens_from_method == childrens

    @pytest.mark.parametrize("id, parents",
                             [(7, [{"id": 4, "parent": 2, "type": "test"},
                                   {"id": 2, "parent": 1, "type": "test"},
                                   {"id": 1, "parent": "root"}]),
                              (5, [{"id": 2, "parent": 1, "type": "test"},
                                   {"id": 1, "parent": "root"}]),
                              (2, [{"id": 1, "parent": "root"}]),
                              (9, [])])
    def test_getAllParents(self, instance, id, parents):
        parents_from_method = instance.getAllParents(id)
        assert parents_from_method == parents
