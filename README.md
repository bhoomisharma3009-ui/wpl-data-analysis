# WPL Data Analysis (2023–2025)

A complete data analytics project analyzing Women's Premier League (WPL) cricket
matches using **SQL**, **Excel**, and **Python (Pandas/Seaborn)** — covering data
cleaning, EDA, visualizations, and insights across all three tools recruiters
typically look for in a data analyst project.

## ⚠️ About the Data
`dataset.csv` is a **sample dataset** built with the exact same column structure
as the real Kaggle WPL dataset. The 2023, 2024, and 2025 **finals are real**
(Mumbai Indians won 2023 & 2025, RCB won 2024), but individual league-stage match
results are randomly generated so the project works end-to-end out of the box.

**Before submitting this as a resume project**, download the real dataset and
replace `dataset.csv` with it (same headers, so nothing else in the project needs
to change):
🔗 https://www.kaggle.com/datasets/sahiltailor/womens-premier-league-2023-2024-ball-by-ball
(use `matches.csv`, rename to `dataset.csv`)

Then re-run `build_database.py` and `build_excel.py` to refresh the SQL database
and Excel dashboard with real numbers.

## Project Components

| Tool | File | What it shows |
|---|---|---|
| **Python/Jupyter** | `notebook.ipynb` | Data cleaning, EDA, 6+ charts, insights, optional ML |
| **SQL (SQLite)** | `wpl_database.db`, `wpl_analysis.sql` | 11 analytical queries: wins, win %, toss impact, venues, champions |
| **Excel** | `WPL_Dashboard.xlsx` | 5-sheet dashboard with live formulas + 5 native charts |

## Folder Structure
```
project/
├── notebook.ipynb          # Main Python EDA notebook
├── dataset.csv              # WPL matches data
├── wpl_database.db          # SQLite database (matches table)
├── wpl_analysis.sql         # SQL analysis queries
├── WPL_Dashboard.xlsx       # Excel dashboard with formulas & charts
├── generate_data.py         # (optional) regenerates dataset.csv
├── build_database.py        # (optional) rebuilds wpl_database.db from dataset.csv
├── build_excel.py           # (optional) rebuilds WPL_Dashboard.xlsx from dataset.csv
├── README.md
└── requirements.txt
```
> The three `build_*.py` / `generate_*.py` scripts are one-time setup scripts.
> You only need to re-run them if you replace `dataset.csv` with new data.

## Tools & Libraries
- Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter
- SQLite (via Python's built-in `sqlite3`)
- Excel / openpyxl (formulas: `COUNTIF`, `SUMPRODUCT`, `IFERROR`; native bar & pie charts)
- (Optional) Scikit-learn for a small bonus prediction demo

## What Each Part Covers

**`notebook.ipynb`** — data cleaning → EDA → 6 visualizations (season trend, team
wins, toss impact, toss decision split, venue distribution, win-margin histograms)
→ written key insights → conclusions → optional logistic regression bonus.

**`wpl_analysis.sql`** — matches per season, total wins & win % per team, toss
impact %, toss decision counts, venue match counts, average win margins, season
champions, top Player-of-the-Match awardees.

**`WPL_Dashboard.xlsx`** — 5 sheets: *Raw Data*, *Team Summary* (bar chart), *Toss
Analysis* (pie + bar chart), *Season Trend* (bar chart), *Venue Summary* (bar
chart), plus a *Notes* sheet documenting the data-source assumption. All numbers
are live formulas referencing Raw Data, not hardcoded — edit a row on Raw Data
and every chart updates.

## Key Findings
- Toss winning provides only a marginal advantage in match outcomes.
- A few franchises show early dominance in win counts.
- Fielding first after winning the toss is the more common strategic choice.
- Win margins are generally competitive rather than one-sided.
- Matches are concentrated at a small number of venues so far.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Open `notebook.ipynb` in Jupyter and run all cells.
3. Open `WPL_Dashboard.xlsx` in Excel to explore the dashboard and charts.
4. Explore SQL queries — easiest way is [DB Browser for SQLite](https://sqlitebrowser.org/)
   (free tool): open `wpl_database.db`, paste any query from `wpl_analysis.sql` into
   the "Execute SQL" tab, and run it. Command-line alternative (if `sqlite3` CLI is
   installed):
   ```bash
   sqlite3 wpl_database.db
   sqlite> SELECT winner, COUNT(*) FROM matches GROUP BY winner ORDER BY 2 DESC;
   ```

## Author
[Bhoomi Sharma] — 3rd Year B.Tech CSE Student
