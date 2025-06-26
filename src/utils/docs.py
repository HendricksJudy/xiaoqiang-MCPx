from typing import Any, Dict, get_type_hints


def generate_tool_docs(tool_class: type) -> Dict[str, Any]:
    """Generate MCP standard documentation for a tool class."""
    docs: Dict[str, Any] = {
        "name": tool_class.__name__,
        "description": tool_class.__doc__,
        "methods": [],
        "schemas": {},
    }

    for method_name in dir(tool_class):
        if method_name.startswith("tool_"):
            method = getattr(tool_class, method_name)
            hints = get_type_hints(method)
            docs["methods"].append(
                {
                    "name": method_name,
                    "description": method.__doc__,
                    "input_schema": hints.get("input", {}),
                    "output_schema": hints.get("return", {}),
                }
            )

    return docs


if __name__ == "__main__":
    import json
    from ..tools.knowledge_base import KnowledgeBase

    print(json.dumps(generate_tool_docs(KnowledgeBase), ensure_ascii=False, indent=2))

