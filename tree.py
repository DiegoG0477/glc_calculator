from graphviz import Digraph

def generate_tree(tree):
    nodes = []
    edges = []
    node_count = 0

    def add_nodes_edges(node, parent=None):
        nonlocal node_count
        
        # Handle dictionary with single key
        if isinstance(node, dict) and len(node) == 1:
            label = list(node.keys())[0]
            node = node[label]
        
        current_id = f"node{node_count}"
        
        # Determine label
        if isinstance(node, dict):
            label = list(node.keys())[0]
            
            if(node_count == 0):
                label="S"

        elif isinstance(node, list):
            label = "E"
        else:
            label = str(node)
        
        nodes.append({"data": {"id": current_id, "label": label}})
        
        if parent is not None:
            edges.append({"data": {"source": parent, "target": current_id}})
        
        node_count += 1

        # Recursive processing of children
        if isinstance(node, list):
            for child in node:
                if isinstance(child, (dict, list, str, int, float)):
                    add_nodes_edges(child, current_id)
        elif isinstance(node, dict):
            for key, value in node.items():
                if isinstance(value, (dict, list, str, int, float)):
                    add_nodes_edges({key: value}, current_id)

    add_nodes_edges(tree)
    return {"nodes": nodes, "edges": edges}