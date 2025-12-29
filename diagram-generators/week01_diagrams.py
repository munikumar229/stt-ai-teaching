#!/usr/bin/env python3
"""
Generate diagrams for Week 01: Data Collection lecture.
Uses graphviz for flowcharts and diagrams.
"""

from graphviz import Digraph
import os

# Output directory for figures
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'figures')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# High DPI for sharp images
DPI = '300'


def create_ml_model_flow():
    """Create the ML model black box diagram (lines 50-54)."""
    dot = Digraph('ml_model_flow', format='png')
    dot.attr(rankdir='LR', bgcolor='transparent', dpi=DPI)
    dot.attr('node', shape='box', style='rounded,filled', fontname='Inter', fontsize='14')

    # Input
    dot.node('features', 'Movie Features', fillcolor='#dbeafe', color='#3b82f6', penwidth='2')

    # ML Model (black box)
    dot.node('model', 'ML Model\n(Black Box)', fillcolor='#1e3a5f', fontcolor='white', color='#1e3a5f', penwidth='2')

    # Output
    dot.node('revenue', 'Predicted\nRevenue', fillcolor='#c6f6d5', color='#2a9d8f', penwidth='2')

    # Edges
    dot.edge('features', 'model', penwidth='2', color='#4a5568')
    dot.edge('model', 'revenue', penwidth='2', color='#4a5568')

    dot.render(os.path.join(OUTPUT_DIR, 'ml_model_flow'), cleanup=True)
    print("Created: ml_model_flow.png")


def create_three_data_options():
    """Create the three data options diagram (lines 131-145)."""
    dot = Digraph('data_options', format='png')
    dot.attr(rankdir='TB', bgcolor='transparent', dpi=DPI)
    dot.attr('node', shape='box', style='rounded,filled', fontname='Inter', fontsize='12')

    # Create subgraph for horizontal alignment
    with dot.subgraph() as s:
        s.attr(rank='same')

        # Option 1
        s.node('opt1_title', 'OPTION 1', fillcolor='#1e3a5f', fontcolor='white', color='#1e3a5f')

        # Option 2
        s.node('opt2_title', 'OPTION 2', fillcolor='#1e3a5f', fontcolor='white', color='#1e3a5f')

        # Option 3
        s.node('opt3_title', 'OPTION 3', fillcolor='#1e3a5f', fontcolor='white', color='#1e3a5f')

    # Details
    dot.node('opt1_detail', 'Existing\nDatasets\n\nKaggle, UCI,\nHuggingFace', fillcolor='#eff6ff', color='#3b82f6')
    dot.node('opt2_detail', 'APIs\n\nOMDb, TMDb,\nTwitter, etc.', fillcolor='#f0fff4', color='#2a9d8f')
    dot.node('opt3_detail', 'Web Scraping\n\nIMDb, Rotten\nTomatoes, etc.', fillcolor='#fffbeb', color='#e9c46a')

    # Methods
    dot.node('opt1_method', 'Download\ndirectly', fillcolor='#e2e8f0', color='#4a5568')
    dot.node('opt2_method', 'Programmatic\nrequests', fillcolor='#e2e8f0', color='#4a5568')
    dot.node('opt3_method', 'Parse HTML\nfrom pages', fillcolor='#e2e8f0', color='#4a5568')

    # Connect
    dot.edge('opt1_title', 'opt1_detail', style='invis')
    dot.edge('opt2_title', 'opt2_detail', style='invis')
    dot.edge('opt3_title', 'opt3_detail', style='invis')

    dot.edge('opt1_detail', 'opt1_method', penwidth='2', color='#4a5568')
    dot.edge('opt2_detail', 'opt2_method', penwidth='2', color='#4a5568')
    dot.edge('opt3_detail', 'opt3_method', penwidth='2', color='#4a5568')

    dot.render(os.path.join(OUTPUT_DIR, 'three_data_options'), cleanup=True)
    print("Created: three_data_options.png")


def create_api_client_server():
    """Create the API client-server diagram (lines 166-172, 188-202)."""
    dot = Digraph('api_client_server', format='png')
    dot.attr(rankdir='LR', bgcolor='transparent', dpi=DPI)
    dot.attr('node', shape='box', style='rounded,filled', fontname='Inter', fontsize='14')

    # Client
    dot.node('client', 'Your Code\n(Client)', fillcolor='#dbeafe', color='#3b82f6', penwidth='2')

    # Server
    dot.node('server', 'API Server\n(OMDb)', fillcolor='#f0fff4', color='#2a9d8f', penwidth='2')

    # Edges with labels
    dot.edge('client', 'server', label='  HTTP Request  ', fontname='Inter', fontsize='11',
             penwidth='2', color='#1e3a5f')
    dot.edge('server', 'client', label='  JSON Response  ', fontname='Inter', fontsize='11',
             penwidth='2', color='#2a9d8f', style='dashed')

    dot.render(os.path.join(OUTPUT_DIR, 'api_client_server'), cleanup=True)
    print("Created: api_client_server.png")


def create_scraping_flow():
    """Create the web scraping flow diagram (lines 188-202)."""
    dot = Digraph('scraping_flow', format='png')
    dot.attr(rankdir='TB', bgcolor='transparent', dpi=DPI)
    dot.attr('node', shape='box', style='rounded,filled', fontname='Inter', fontsize='14')

    # Top row - same rank
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('client', 'Your Code\n(Client)', fillcolor='#dbeafe', color='#3b82f6', penwidth='2')
        s.node('website', 'Website\n(IMDb)', fillcolor='#fef3c7', color='#e9c46a', penwidth='2')

    # Bottom row
    dot.node('extracted', 'Extracted\nData', fillcolor='#c6f6d5', color='#2a9d8f', penwidth='2')

    # Edges
    dot.edge('client', 'website', label='HTTP Request', fontname='Inter', fontsize='10',
             penwidth='2', color='#1e3a5f')
    dot.edge('website', 'client', label='HTML Page', fontname='Inter', fontsize='10',
             penwidth='2', color='#e9c46a', style='dashed')
    dot.edge('client', 'extracted', label='Parse HTML', fontname='Inter', fontsize='10',
             penwidth='2', color='#4a5568')

    dot.render(os.path.join(OUTPUT_DIR, 'scraping_flow'), cleanup=True)
    print("Created: scraping_flow.png")


def create_restaurant_analogy():
    """Create the restaurant API analogy diagram (lines 232-244)."""
    dot = Digraph('restaurant_analogy', format='png')
    dot.attr(rankdir='TB', bgcolor='transparent', splines='ortho', dpi=DPI)
    dot.attr('node', shape='box', style='rounded,filled', fontname='Inter', fontsize='13')

    # Title
    dot.node('title', 'RESTAURANT', fillcolor='#1e3a5f', fontcolor='white',
             color='#1e3a5f', penwidth='2', fontsize='16')

    # Flow nodes
    dot.node('you', 'You\n(Client)', fillcolor='#dbeafe', color='#3b82f6', penwidth='2')
    dot.node('menu', 'Menu\n(API Docs)', fillcolor='#fffbeb', color='#e9c46a', penwidth='2')
    dot.node('order', 'Order\n(Request)', fillcolor='#fef3c7', color='#e9c46a', penwidth='2')
    dot.node('kitchen', 'Kitchen\n(Server)', fillcolor='#f0fff4', color='#2a9d8f', penwidth='2')
    dot.node('food', 'Food\n(Response)', fillcolor='#c6f6d5', color='#2a9d8f', penwidth='2')

    # Edges
    dot.edge('title', 'you', style='invis')
    dot.edge('you', 'menu', penwidth='2', color='#4a5568')
    dot.edge('menu', 'order', penwidth='2', color='#4a5568')
    dot.edge('order', 'kitchen', penwidth='2', color='#4a5568')
    dot.edge('kitchen', 'food', penwidth='2', color='#4a5568')
    dot.edge('food', 'you', penwidth='2', color='#2a9d8f', style='dashed', constraint='false')

    dot.render(os.path.join(OUTPUT_DIR, 'restaurant_analogy'), cleanup=True)
    print("Created: restaurant_analogy.png")


def create_http_flow():
    """Create the HTTP client-server diagram (lines 390-395)."""
    dot = Digraph('http_flow', format='png')
    dot.attr(rankdir='LR', bgcolor='transparent', dpi=DPI)
    dot.attr('node', shape='box', style='rounded,filled', fontname='Inter', fontsize='14')

    # Client
    dot.node('client', 'Client', fillcolor='#dbeafe', color='#3b82f6', penwidth='2')

    # Server
    dot.node('server', 'Server', fillcolor='#f0fff4', color='#2a9d8f', penwidth='2')

    # Edges with labels
    dot.edge('client', 'server', label='  HTTP Request  ', fontname='Inter', fontsize='11',
             penwidth='2', color='#1e3a5f')
    dot.edge('server', 'client', label='  HTTP Response  ', fontname='Inter', fontsize='11',
             penwidth='2', color='#2a9d8f', style='dashed')

    dot.render(os.path.join(OUTPUT_DIR, 'http_flow'), cleanup=True)
    print("Created: http_flow.png")


def create_data_pipeline():
    """Create the data collection pipeline diagram (lines 1808-1825)."""
    dot = Digraph('data_pipeline', format='png')
    dot.attr(rankdir='TB', bgcolor='transparent', nodesep='0.5', ranksep='0.6', dpi=DPI)
    dot.attr('node', shape='box', style='rounded,filled', fontname='Inter', fontsize='12')

    # Top row - API flow
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('omdb', 'OMDb API\n(requests)', fillcolor='#dbeafe', color='#3b82f6', penwidth='2')
        s.node('collect_meta', 'Collect\nMetadata', fillcolor='#e2e8f0', color='#4a5568', penwidth='2')
        s.node('store_json', 'Store\nas JSON', fillcolor='#f0fff4', color='#2a9d8f', penwidth='2')

    # Middle row - Scraping flow
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('imdb', 'IMDb Page\n(BeautifulSoup)', fillcolor='#fffbeb', color='#e9c46a', penwidth='2')
        s.node('scrape', 'Scrape\nReviews', fillcolor='#e2e8f0', color='#4a5568', penwidth='2')
        s.node('merge', 'Merge\nData', fillcolor='#f0fff4', color='#2a9d8f', penwidth='2')

    # Final output
    dot.node('csv', 'Final CSV\nfor ML', fillcolor='#c6f6d5', color='#2a9d8f', penwidth='2', fontsize='14')

    # Edges
    dot.edge('omdb', 'collect_meta', penwidth='2', color='#4a5568')
    dot.edge('collect_meta', 'store_json', penwidth='2', color='#4a5568')
    dot.edge('omdb', 'imdb', penwidth='2', color='#4a5568', style='dashed')
    dot.edge('imdb', 'scrape', penwidth='2', color='#4a5568')
    dot.edge('scrape', 'merge', penwidth='2', color='#4a5568')
    dot.edge('store_json', 'merge', penwidth='2', color='#4a5568', constraint='false')
    dot.edge('merge', 'csv', penwidth='2', color='#2a9d8f')

    dot.render(os.path.join(OUTPUT_DIR, 'data_collection_pipeline'), cleanup=True)
    print("Created: data_collection_pipeline.png")


def create_data_pipeline_flow():
    """Create the ML pipeline reality diagram (referenced at line 98)."""
    dot = Digraph('data_pipeline_flow', format='png')
    dot.attr(rankdir='LR', bgcolor='transparent', nodesep='0.4', dpi=DPI)
    dot.attr('node', shape='box', style='rounded,filled', fontname='Inter', fontsize='12')

    # Pipeline stages
    dot.node('collect', 'Data\nCollection', fillcolor='#fef3c7', color='#e9c46a', penwidth='2')
    dot.node('clean', 'Data\nCleaning', fillcolor='#fef3c7', color='#e9c46a', penwidth='2')
    dot.node('explore', 'Exploratory\nAnalysis', fillcolor='#fef3c7', color='#e9c46a', penwidth='2')
    dot.node('feature', 'Feature\nEngineering', fillcolor='#fef3c7', color='#e9c46a', penwidth='2')
    dot.node('model', 'Model\nTraining', fillcolor='#c6f6d5', color='#2a9d8f', penwidth='2')
    dot.node('eval', 'Evaluation', fillcolor='#c6f6d5', color='#2a9d8f', penwidth='2')

    # Edges
    dot.edge('collect', 'clean', penwidth='2', color='#4a5568')
    dot.edge('clean', 'explore', penwidth='2', color='#4a5568')
    dot.edge('explore', 'feature', penwidth='2', color='#4a5568')
    dot.edge('feature', 'model', penwidth='2', color='#4a5568')
    dot.edge('model', 'eval', penwidth='2', color='#4a5568')

    # Add percentage annotations
    dot.node('pct80', '80% of work', shape='none', fontname='Inter', fontsize='11', fontcolor='#e85a4f')
    dot.node('pct20', '20%', shape='none', fontname='Inter', fontsize='11', fontcolor='#2a9d8f')

    dot.edge('pct80', 'clean', style='invis')
    dot.edge('pct20', 'model', style='invis')

    dot.render(os.path.join(OUTPUT_DIR, 'data_pipeline_flow'), cleanup=True)
    print("Created: data_pipeline_flow.png")


def create_http_request_sequence():
    """Create HTTP request sequence diagram (referenced at line 407)."""
    dot = Digraph('http_request_sequence', format='png')
    dot.attr(rankdir='TB', bgcolor='transparent', dpi=DPI)
    dot.attr('node', shape='box', style='rounded,filled', fontname='Inter', fontsize='12')

    # Client and Server
    dot.node('client', 'Client', fillcolor='#dbeafe', color='#3b82f6', penwidth='2')
    dot.node('server', 'Server', fillcolor='#f0fff4', color='#2a9d8f', penwidth='2')

    # Steps
    dot.node('s1', '1. Initiate Connection', fillcolor='#e2e8f0', color='#4a5568')
    dot.node('s2', '2. Send Request', fillcolor='#e2e8f0', color='#4a5568')
    dot.node('s3', '3. Process Request', fillcolor='#e2e8f0', color='#4a5568')
    dot.node('s4', '4. Send Response', fillcolor='#e2e8f0', color='#4a5568')
    dot.node('s5', '5. Connection Closes', fillcolor='#e2e8f0', color='#4a5568')

    # Layout
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('client')
        s.node('server')

    dot.edge('client', 's1', style='invis')
    dot.edge('s1', 's2', penwidth='2', color='#3b82f6')
    dot.edge('s2', 's3', penwidth='2', color='#4a5568')
    dot.edge('s3', 's4', penwidth='2', color='#2a9d8f')
    dot.edge('s4', 's5', penwidth='2', color='#4a5568')

    dot.render(os.path.join(OUTPUT_DIR, 'http_request_sequence'), cleanup=True)
    print("Created: http_request_sequence.png")


if __name__ == '__main__':
    print("Generating Week 01 diagrams...")
    create_ml_model_flow()
    create_three_data_options()
    create_api_client_server()
    create_scraping_flow()
    create_restaurant_analogy()
    create_http_flow()
    create_data_pipeline()
    create_data_pipeline_flow()
    create_http_request_sequence()
    print("\nAll diagrams generated successfully!")
