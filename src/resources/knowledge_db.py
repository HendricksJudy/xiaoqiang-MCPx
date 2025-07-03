"""Simple knowledge database resource."""

class KnowledgeDB:
    def __init__(self) -> None:
        self._data = {
            "癌症": "有关癌症的基础知识。",
            "治疗": "常见治疗手段介绍。",
        }

    def lookup(self, term: str) -> str:
        """Return information string for a given term."""
        return self._data.get(term, "")
