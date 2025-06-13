# NYC Collisions Mini-Project

Learn to ingest data, clean, load to SQLite and make a simple interactive dashboard

## Description

This project ingests cleaned and sampled data from a longer NYC motor vehicle collisions dataset into a local SQLite database. It also runs core SQL analysis scripts, validates them using a Jupyter notebook and pytest, and uses Streamlit to dashboard with filters, charts, and a detailed heatmap over New York showing crashes.

**Deployed Live:** https://nyc-collisions-2020-2025.streamlit.app/


## Getting Started

### Dependencies

* Python 3.8 or higher  
* `pip` package manager  
* Virtual environment tool (e.g. `venv` or `conda`)  
* OS: any (tested on Windows 10, macOS, Linux)

### Installing

1. **Clone the repo**  
```bash
git clone https://github.com/yougijain/ds-fundamentals-ingest-clean
cd ds-fundamentals-ingest-clean
```
2. **Create & activate a virtualenv**  
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate.bat
# macOS/Linux
source .venv/bin/activate
```
3. **Install Python dependencies**  
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Executing program

1. **Load the data into SQLite**

```bash
python scripts/load_to_sqlite.py
```

2. **Validate SQL scripts in notebook**

* Open `notebooks/sql_queries.ipynb` in VS Code or Jupyter and run all cells.

3. **Run automated tests**

```bash
pytest -q
```

4. **Launch the dashboard**

```bash
streamlit run app/dashboard.py
```

## Help

* If you get a “unable to open database file” error, confirm you ran the loader script and that data/clean/data.db exists.

* To use the Mapbox dark basemap, copy .streamlit/secrets.toml.example → .streamlit/secrets.toml and insert your MAPBOX_API_KEY.

* For other issues, open an issue on the GitHub repo.

## Authors

Yougi Jain

## Version History

* 0.1
    * See [contribution history](https://github.com/yougijain/ds-fundamentals-ingest-clean/graphs/contributors)
    * Initial Release

## License

This project is licensed under the MIT License.

## Acknowledgements

#### Data Source

* Motor Vehicle Collisions – Crashes  
* NYC Open Data (CC0 1.0)  
* https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95

#### ReadMe Template

* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
