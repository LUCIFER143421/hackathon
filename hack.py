# satguru_ai_bot.py - MVP Code for SatGuru AI Bot (Fully Sandbox-Compatible)

# This version avoids openai/langchain/fitz/neo4j and uses local in-memory graph structure.
# Prerequisites (Install via pip if not already installed)
# pip install beautifulsoup4 pandas geopandas
#first change
import os
from bs4 import BeautifulSoup
import geopandas as gpd
import pandas as pd

# ----------------------
# DATA INGESTION
# ----------------------

def extract_text_from_txt(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        return f.read()

def extract_text_from_html(html_path):
    with open(html_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    return soup.get_text()

# ----------------------
# QA BOT FUNCTION (Simulated)
# ----------------------

def ask_local_bot(question, context):
    """
    Simulated QA function since LLMs are not available.
    Returns canned answers based on keyword matches.
    """
    q = question.lower()
    if "insat" in q:
        return "INSAT-3D provides rainfall and cloud cover data."
    elif "scatsat" in q:
        return "SCATSAT-1 provides ocean wind and scatterometer data."
    elif "risat" in q:
        return "RISAT-1A provides SAR imagery and vegetation index data."
    else:
        return "I couldn't find an exact answer based on current data."

# ----------------------
# IN-MEMORY KNOWLEDGE GRAPH STRUCTURE
# ----------------------

knowledge_graph = {
    "INSAT-3D": ["Cloud Cover", "Rainfall", "Wind Speed"],
    "SCATSAT-1": ["Ocean Wind", "Scatterometer", "Sea Surface Temp"],
    "RISAT-1A": ["SAR Imagery", "Soil Moisture", "Vegetation Index"]
}

def query_kg(entity):
    for satellite, products in knowledge_graph.items():
        if entity.lower() in satellite.lower():
            return {"Satellite": satellite, "Products": products}
    return None

# ----------------------
# MAIN FUNCTION / DEMO
# ----------------------

def main():
    print("\nWelcome to SatGuru AI Help Bot (Local Memory Version)")

    print("\nQuerying In-Memory Knowledge Graph for SCATSAT")
    result = query_kg("SCATSAT")
    if result:
        print(f"Satellite: {result['Satellite']}")
        print("Products:", ", ".join(result['Products']))
    else:
        print("No matching satellite found.")

    print("\nRunning Simulated QA")
    context = "INSAT-3D provides rainfall and cloud cover data."
    question = "What does INSAT-3D provide?"
    answer = ask_local_bot(question, context)
    print("QA Test - Question:", question)
    print("Answer:", answer)

if __name__ == "__main__":
    main()
