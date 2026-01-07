#!/usr/bin/env python3
"""
Data Pipeline Flow Diagram
Week 1: Data Collection Lecture
Illustrates the ML data pipeline stages from collection to deployment
"""

from graphviz import Digraph
import os

OUTPUT_DIR = "../figures"
OUTPUT_FILE = "data_pipeline_flow"

def create_data_pipeline_flow():
    dot = Digraph(comment='ML Data Pipeline', format='png')
    dot.attr(rankdir='LR', dpi='300', nodesep='0.4', ranksep='0.6')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Arial',
            fontsize='14', height='0.5', width='1.3')
    dot.attr('edge', penwidth='2')

    # Data Engineering cluster (80%)
    with dot.subgraph(name='cluster_data') as c:
        c.attr(label='Data Engineering (80%)', fontsize='16', fontname='Arial Bold',
               style='rounded,dashed', color='#e74c3c', penwidth='2', bgcolor='#fff5f5')
        c.node('A', 'Collection', fillcolor='#ff9966', penwidth='3')
        c.node('B', 'Validation', fillcolor='#ffcc99')
        c.node('C', 'Labeling', fillcolor='#ffcc99')

    # Modeling cluster (20%)
    with dot.subgraph(name='cluster_model') as c:
        c.attr(label='Modeling (20%)', fontsize='16', fontname='Arial Bold',
               style='rounded,dashed', color='#27ae60', penwidth='2', bgcolor='#f5fff5')
        c.node('D', 'Training', fillcolor='#99ccff')
        c.node('E', 'Evaluation', fillcolor='#99ccff')
        c.node('F', 'Deployment', fillcolor='#99ff99')

    # Edges
    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('D', 'E')
    dot.edge('E', 'F')

    return dot

if __name__ == "__main__":
    output_dir = os.path.join(os.path.dirname(__file__), OUTPUT_DIR)
    os.makedirs(output_dir, exist_ok=True)

    dot = create_data_pipeline_flow()
    output_path = os.path.join(output_dir, OUTPUT_FILE)
    dot.render(output_path, cleanup=True)
    print(f"Generated: {output_path}.png")
