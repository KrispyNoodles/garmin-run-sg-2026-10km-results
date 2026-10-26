# Garmin Run Singapore 2026 – 10km result card

A static web page: type a bib number (and optionally a name) and it draws the result card.
Everything runs in the visitor's browser, so it works on free GitHub Pages.

## Files

| File | What it is |
|---|---|
| `index.html` | The page (form + card drawing). |
| `data.json` | Every runner's results, positions and averages. The page only reads this file. |
| `export_data.py` | Rebuilds `data.json` from the notebook and the spreadsheet (only needed if the data changes). |

## Put it online (GitHub Pages)

1. On github.com, click **New repository**. Name it (for example `garmin-run`), choose **Public**, click **Create repository**.
2. Click **uploading an existing file**, drag in `index.html` and `data.json` (and the other files if you like), then **Commit changes**.
3. Go to **Settings → Pages**. Under **Build and deployment**, set Source to **Deploy from a branch**, choose branch **main** and folder **/ (root)**, then **Save**.
4. Wait a minute or two. The link appears at the top of that page:
   `https://<your-username>.github.io/garmin-run/`

You can also share a pre-filled link: `https://<your-username>.github.io/garmin-run/?bib=22091&name=Joey`

## Changing the data

If the spreadsheet or the notebook's logic changes, rebuild `data.json` and upload it again:

    pip install pandas openpyxl matplotlib
    python export_data.py data_viz.ipynb garmin_run_10km_results_final.xlsx data.json

`export_data.py` runs the notebook's own calculation cells, so the positions, totals and averages always match the notebook.

## Notes

- Opening `index.html` by double-clicking won't work, because browsers block it from reading `data.json` from a folder. Use the GitHub Pages link, or run `python -m http.server` in the folder and open http://localhost:8000.
- The repository is public, so `data.json` is public too: bib numbers, times and masked names.
- The name box is only a label on the card. The page can't check that it matches the bib.


## Development & AI Disclosure

This project was vibe-coded with the assistance of generative AI, which was used to develop the Python scripts, data visualisations, and web interface.

### My Contributions

- Extracting the race results from Sporthive.
- Cleaning and preprocessing the dataset, including handling anomalous finishing times, missing 5KM splits, and DNS/DNF records.
- Defining the ranking methodology for gun-time and chip-time positions, including tiebreaking rules and category-specific rankings.
- Reviewing and validating the calculated rankings against the official Sporthive results.
- Iteratively refining the visualisations, functionality, and presentation of the result cards.

While AI assisted with the implementation, the **data preparation, analytical decisions, validation, and overall project direction were guided by me**.

### Disclaimer

> **This is an independent, unofficial project** and is not affiliated with Garmin, Sporthive, or the race organisers.
>
> Rankings are calculated using the cleaned dataset and may differ from the official published results.
