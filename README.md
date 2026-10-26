# Garmin Run Singapore 2026 – 21km (Shortened to 10km) result card

A static web page: type a bib number (and optionally a name) and it draws the result card. Try out the link here [link](https://krispynoodles.github.io/garmin-run-sg-2026-10km-results/)

## Motivation Behind This Repository

The main motivation behind creating this repository was that the official results for Garmin Run Singapore 2026, published through Sporthive, display runners' positions based solely on **gun time**, rather than **chip time**. Since runners started in different waves, those who crossed the starting line later could receive lower rankings despite having faster chip times. This repo aims to provide runners with an alternative way to view their results by displaying rankings based on **both gun time and chip time**, allowing them to better understand how their actual running performance compares with other participants.

**Note:** The chip-time rankings are independently calculated using the cleaned dataset and may differ from the official results.

## Files

| File | What it is |
|---|---|
| `index.html` | The page (form + card drawing). |
| `data.json` | Every runner's results, positions and averages. The page only reads this file. |
| `export_data.py` | Rebuilds `data.json` from the notebook and the spreadsheet (only needed if the data changes). |
| `data/garmin_run_10km_results_final.xlsx` | Dataset containing the race results extracted from the Sporthive website, after data cleaning and preprocessing. |
| `scripts/crawler.py` | Python web scraping script used to retrieve individual runners' details from Sporthive. |
| `scripts/data_viz.ipynb` | Original Jupyter Notebook used for data analysis, ranking calculations, and generating individual result cards. This notebook subsequently served as the reference for Claude to develop the web application in this repository. |


## Data Preprocessing Steps

Before calculating the rankings and generating the result cards, the dataset underwent the following preprocessing steps:

1. **Name Anonymisation:** Masked all participants' names as `XXX` to maintain anonymity.
2. **Anomalous Timing Records:** For participants with unrealistic timing records (e.g., completing 5KM in 5–10 minutes), replaced their chip times with their gun times.
3. **DNS/DNF Removal:** Removed participants marked as DNS (Did Not Start) or DNF (Did Not Finish) who had no recorded finishing times.
4. **Missing 5KM Splits:** For participants without a recorded 5KM split time, estimated their split by dividing their chip time by 2, assuming they maintained a constant pace throughout the entire 10KM race.

**Note:** These adjustments were made to facilitate the analysis. Some timing values are estimated or substituted and may not reflect the participants' actual performances.

---

## Explanation of Positional Rankings
### Timing Methods

- **Gun Time:** The time elapsed from the official race start until the runner crosses the finish line.
- **Chip Time:** The actual time taken by the runner, measured from crossing the starting line to crossing the finish line.

This repo calculates rankings independently using both timing methods.

### Ranking Categories
1. **Overall Position:** Includes all runners, regardless of gender or race category.
2. **Gender Position:** Includes all runners of the same gender, regardless of race category.
3. **Category Position:** Includes only runners belonging to the same race category **and gender**.

**Observation:** Sporthive appears to calculate category positions separately by gender but displays the total number of participants across both genders within that category. This results in a mismatch between the population used for the ranking and the population represented by the total.

For this repo, category positions and their corresponding totals are calculated using the same category-and-gender grouping.

### Ranking Calculation

Rankings are calculated using two methods:

- **Gun-Time Ranking:** Runners are primarily sorted by gun time, with chip time used as the tiebreaker.
- **Chip-Time Ranking:** Runners are primarily sorted by chip time, with gun time used as the tiebreaker.

### Tie-Breaking Rules

To ensure every runner receives a unique position:

- **For chip-time rankings:** If two runners have identical chip times, the runner with the faster gun time receives the better ranking.
- **For gun-time rankings:** If two runners have identical gun times, the runner with the faster chip time receives the better ranking.
- **If both times are identical:** The original dataset order is used to assign unique positions.

All rankings start from position 1, with faster finishing times receiving better rankings.

**Note:** Rankings are calculated using the available, cleaned dataset. As some records may be missing or adjusted during preprocessing, the calculated positions may differ slightly from those published by Sporthive.

## Development & AI Disclosure

This project was vibe-coded with the assistance of generative AI, which was used to develop the Python scripts, data visualisations, and web interface. My involvement primarily focused on extracting and cleaning the race results, understanding and defining the ranking methodology, and validating the calculated rankings. For the original Jupyter Notebook (data_viz.ipynb), I went through the code line by line to understand how the calculations and visualisations worked. I also manually cross-checked selected gun-time rankings against the official Sporthive results to verify their accuracy.

My background is primarily in Data Science, Data Analytics, Artificial Intelligence (AI), and Machine Learning (ML), rather than Software Engineering or Web Development. As I have limited experience building websites, I threw into Claude to help turn my analysis into an accessible web application that other runners could use.

Once I was satisfied with the notebook, I passed it to Claude to develop the web application, including generating data.json and index.html, which form the basis of this repository.

While the implementation was largely AI-generated, I was responsible for the data preprocessing, analytical decisions, understanding and reviewing the notebook's logic, and guiding the overall project direction.

Disclaimer: Although I have cross-checked selected rankings against Sporthive, I have not individually verified every participant's result or every component of the AI-generated web application. The calculated rankings are unofficial and may differ from the organiser's published results.
