# ⚽ Football Player Data Scraper & Analytics

A Python football data project that collects player statistics through web scraping, cleans and prepares the data, and performs exploratory analysis and visualization using **Pandas** and **Matplotlib**.

The project started as a web scraping exercise and evolved into a complete data workflow:

**Web Scraping → Data Cleaning → Data Preparation → Exploratory Data Analysis → Visualization**

The dataset focuses on football players and their performance statistics, with the goal of creating a solid foundation for future **football analytics and machine learning** projects.

---

## 🎯 Project Objectives

This project was built to practice and demonstrate several important data skills:

* Web scraping with Python
* Extracting structured information from HTML pages
* Cleaning and validating raw data
* Data manipulation with Pandas
* Exploratory Data Analysis (EDA)
* Data visualization with Matplotlib
* Preparing datasets for future machine learning models
* Building a complete data workflow from raw data to insights

---

## 🛠️ Tech Stack

* **Python** — Main programming language
* **Requests** — Sending HTTP requests
* **BeautifulSoup4** — HTML parsing and web scraping
* **Pandas** — Data cleaning, transformation and analysis
* **Matplotlib** — Data visualization
* **CSV** — Data storage

---

## 🔄 Project Workflow

```text
                    ┌─────────────────┐
                    │   Foot Mercato  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Web Scraping  │
                    │ Requests + BS4  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    Raw Data     │
                    │       CSV       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Data Cleaning  │
                    │     Pandas      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Clean Data    │
                    │       CSV       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │      EDA        │
                    │     Pandas      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Visualization   │
                    │    Matplotlib   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  ML-Ready Data  │
                    └─────────────────┘
```

---

## 🕷️ 1. Web Scraping

The first stage of the project consists of collecting football player statistics from **Foot Mercato**.

The scraper uses:

* `Requests` to send HTTP requests
* `BeautifulSoup4` to parse HTML
* Python to extract and structure player information
* CSV files to store the collected data

### Data collected

The dataset contains information such as:

* Player name
* Season
* Matches
* Starts
* Substitutions in
* Substitutions out
* Goals
* Assists
* Yellow cards
* Red cards
* Player status
* Source URL
* Competition statistics
* Position statistics
* Goal details
* Trophies

Some fields contain nested or structured information that requires additional processing during the cleaning stage.

---

## 🧹 2. Data Cleaning & Preparation

After scraping the data, the raw dataset is cleaned and transformed using **Pandas**.

The cleaning process includes tasks such as:

* Handling missing values
* Converting columns to appropriate data types
* Cleaning numerical statistics
* Removing inconsistent or unnecessary data
* Structuring scraped information
* Preparing the dataset for analysis
* Creating a machine-learning-ready dataset

The cleaned dataset is stored separately from the raw scraped data.

### Dataset versions

```text
ballon_dor_2025_26_clean.csv
ballon_dor_2025_26_ml_ready.csv
```

The separation between cleaned and ML-ready data makes it possible to keep the data-processing workflow organized and reproducible.

---

## 📊 3. Exploratory Data Analysis

The cleaned dataset is analyzed using **Pandas** to better understand player performance.

The analysis explores relationships between different football statistics, including:

* Goals
* Assists
* Matches
* Starts
* Cards
* Player positions
* Competition performance
* Trophies

The purpose of this stage is not simply to create charts, but to understand the structure and characteristics of the dataset before applying machine learning.

---

## 📈 4. Data Visualization

**Matplotlib** is used to transform the analyzed data into visual representations.

The visualizations help explore questions such as:

* Which players have the highest goal contributions?
* How are goals distributed among players?
* How does player performance vary?
* What relationships exist between different performance statistics?
* How do different player characteristics compare?

Example visualization types include:

* Bar charts
* Histograms
* Scatter plots
* Comparative charts

The visualization code is contained in:

```text
analyse.py
```

---

## 📁 Project Structure

```text
football-player-data-scraper/
│
├── scraper.py
├── analyse.py
│
├── ballon_dor_2025_26_clean.csv
├── ballon_dor_2025_26_ml_ready.csv
│
├── requirements.txt
├── .gitignore
└── README.md
```

### Main files

| File                              | Description                                 |
| --------------------------------- | ------------------------------------------- |
| `scraper.py`                      | Collects football player data               |
| `analyse.py`                      | Cleans, analyzes and visualizes the dataset |
| `ballon_dor_2025_26_clean.csv`    | Cleaned dataset                             |
| `ballon_dor_2025_26_ml_ready.csv` | Dataset prepared for future ML work         |
| `requirements.txt`                | Python dependencies                         |
| `.gitignore`                      | Files excluded from Git                     |

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Seif-Allah-Amami/football-player-data-scraper.git
cd football-player-data-scraper
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Run the scraper

```bash
python scraper.py
```

### Run the analysis

```bash
python analyse.py
```

The analysis script processes the cleaned dataset and generates visualizations using Pandas and Matplotlib.

---

## 🧠 What I Learned

This project helped me move beyond basic Python programming and work through a complete data workflow.

### Data Collection

* HTTP requests
* HTML parsing
* Web scraping
* Handling HTTP errors
* Extracting structured information

### Data Processing

* Pandas DataFrames
* Data cleaning
* Missing-value handling
* Data transformation
* Feature preparation

### Data Analysis

* Exploratory Data Analysis
* Statistical exploration
* Comparing player performance
* Finding relationships between variables

### Data Visualization

* Matplotlib
* Creating meaningful charts
* Visualizing distributions
* Comparing football statistics

---

## 🔮 Future Improvements

This project is also the foundation for a larger football analytics and machine learning project.

Future improvements could include:

* Add more players and competitions
* Improve scraping reliability
* Automate data collection
* Expand the dataset across multiple seasons
* Store the data in PostgreSQL
* Build an ETL pipeline
* Add more advanced football analytics
* Engineer features for machine learning
* Train a machine learning model for player analysis
* Build an interactive football analytics dashboard

---

## 📌 Project Direction

The long-term goal is to transform this project from a simple scraper into a complete football data pipeline:

```text
Web Scraping
      ↓
Raw Data
      ↓
Data Cleaning
      ↓
Data Transformation
      ↓
Exploratory Data Analysis
      ↓
Data Visualization
      ↓
Feature Engineering
      ↓
Machine Learning
      ↓
Football Analytics
```

This makes the project a practical bridge between **Python, data analysis, data engineering and machine learning**.

---

## 📚 Data Source

Player statistics are collected from **Foot Mercato**.

This project is intended for educational and portfolio purposes. When running or extending the scraper, respect the website's terms of service, robots.txt, rate limits and access restrictions.

---

## 👨‍💻 Author

**Seif Allah Amami**

GitHub: https://github.com/Seif-Allah-Amami
