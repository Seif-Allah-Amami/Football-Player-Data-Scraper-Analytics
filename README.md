# Football Player Data Scraper

A Python web scraping project that collects football player statistics from Foot Mercato and stores the data in a structured CSV dataset.

The project was built as a practical step toward larger football analytics and data engineering projects.

## Project Goal

The goal of this project is to learn and apply the fundamentals of web scraping and data collection:

- Send HTTP requests to web pages
- Parse HTML with BeautifulSoup
- Extract structured player statistics
- Handle HTTP errors and request headers
- Store scraped data in CSV format
- Prepare data for analysis with pandas

The collected dataset can later be used for football analytics, feature engineering, visualization, and machine learning.

## Tech Stack

- **Python**
- **Requests** — HTTP requests
- **BeautifulSoup4** — HTML parsing and data extraction
- **Pandas** — data handling and analysis
- **CSV** — data storage

## Project Structure

```text
football-player-data-scraper/
│
├── scraper.py
├── data/
│   └── players.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## Data Collected

The scraper collects information such as:

- Player name
- Season
- Matches
- Starts
- Substitutions in/out
- Goals
- Assists
- Yellow cards
- Red cards
- Source URL
- Competition statistics
- Position statistics
- Goal details
- Trophies

Some detailed fields are stored as JSON-like data inside the CSV so they can be processed further during the data-cleaning phase.

## Example

A simplified player record looks like:

```text
Player              Matches    Goals    Assists
Kylian Mbappé       43         42       6
Vinicius Junior     51         21       10
Jude Bellingham     38         8        5
```

## How It Works

```text
Foot Mercato
     │
     ▼
HTTP Request
     │
     ▼
HTML Response
     │
     ▼
BeautifulSoup
     │
     ▼
Extract Player Data
     │
     ▼
Structured Dataset
     │
     ▼
CSV
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Seif-Allah-Amami/football-player-data-scraper.git
cd football-player-data-scraper
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the Scraper

```bash
python scraper.py
```

The scraped data is stored in the project's `data/` directory.

## Future Improvements

This project is intentionally the first stage of a larger football data pipeline.

Planned improvements include:

- Improve scraping reliability
- Add more players and competitions
- Automate data collection
- Clean and validate the scraped dataset
- Transform nested competition and position data into separate tables
- Add data visualization with pandas and Matplotlib
- Store the data in PostgreSQL
- Build an ETL pipeline
- Combine data from multiple football sources
- Develop football analytics features
- Explore machine learning for player analysis

## Data Source

Player statistics are collected from **Foot Mercato**.

This project is intended for educational and portfolio purposes. Please respect the website's terms of service, robots.txt, rate limits, and access restrictions when running or extending the scraper.

## Learning Outcome

This project helped me move from Python fundamentals toward practical data engineering by working through a complete data collection workflow:

**Web → Scraping → Structured Data → CSV → Data Cleaning → Analytics**

It is also a foundation for a future football analytics project focused on comparing player performance using data.

## Author

**Seif Allah Amami**

GitHub: https://github.com/Seif-Allah-Amami
