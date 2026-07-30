import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SOURCES_DIR = os.path.join(BASE_DIR, "sources")

DATA_DIR = os.path.join(BASE_DIR, "data")

OUTPUT_DIR = os.path.join(BASE_DIR, "output")


if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)