class TreeStore:
    def __init__(self, items: list):
        self._items = items

    def getAll(self):
        return self._items

    def getItem(self, id:int) -> dict:
        for item in self._items:
            if item["id"] == id:
                return item

    def getChildren(self, id: int) -> list:
        childrens = []
        for item in self._items:
            if item["parent"] == id:
                childrens.append(item)

        return childrens

    def getAllParents(self, id: int) -> list:
        all_parents = []

        parent_id = 0
        for item in self._items[::-1]:

            if item["id"] == parent_id:
                all_parents.append(item)
                parent_id = item["parent"]
            elif item["id"] == id:
                parent_id = item["parent"]
                continue

        return all_parents