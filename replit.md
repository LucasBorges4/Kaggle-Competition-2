# Lucas Borges - Data Scientist Portfolio

## Overview
A static portfolio website built with Quarto, showcasing data science projects including a Kaggle competition on advanced market prediction.

## Project Structure
- `docs/` — Pre-built static HTML site (served directly)
  - `index.html` — Main portfolio page
  - `about.html` — About page
  - `Kaggle_Competition_2.html` — Kaggle competition project page
  - `site_libs/` — Quarto-generated JS/CSS assets
- `Kaggle_Competition_2.ipynb` — Source Jupyter notebook
- `requirements.txt` — Python data science dependencies (for development/notebook work)
- `serve.py` — Simple Python HTTP server for local development

## Running the App
The app is served via a Python HTTP server (`serve.py`) on port 5000, serving files from the `docs/` directory.

## Deployment
Configured as a **static** deployment with `publicDir: "docs"`.
