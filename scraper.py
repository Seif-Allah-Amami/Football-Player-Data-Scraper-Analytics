import csv
import json
import re

import requests
from bs4 import BeautifulSoup

CANDIDATES = [
    {"player": "Kylian Mbappé", "url": "https://www.footmercato.net/joueur/kylian-mbappe/statistique"},
    {"player": "Vinicius Junior", "url": "https://www.footmercato.net/joueur/vinicius-jr/statistique"},
    {"player": "Jude Bellingham", "url": "https://www.footmercato.net/joueur/jude-bellingham/statistique"},
    {"player": "Harry Kane", "url": "https://www.footmercato.net/joueur/harry-kane/statistique"},
    {"player": "Rodri", "url": "https://www.footmercato.net/joueur/rodri/statistique"},
    {"player": "Erling Haaland", "url": "https://www.footmercato.net/joueur/erling-haland/statistique"},
    {"player": "Lautaro Martínez", "url": "https://www.footmercato.net/joueur/lautaro-martinez/statistique"},
    {"player": "Bukayo Saka", "url": "https://www.footmercato.net/joueur/bukayo-saka/statistique"},
    {"player": "Phil Foden", "url": "https://www.footmercato.net/joueur/phil-foden/statistique"},
    {"player": "Lamine Yamal", "url": "https://www.footmercato.net/joueur/lamine-yamal-nasraoui-ebana/statistique"},
    {"player": "Mohamed Salah", "url": "https://www.footmercato.net/joueur/mohamed-salah-1/statistique"},
    {"player": "Robert Lewandowski", "url": "https://www.footmercato.net/joueur/robert-lewandowski/statistique"},
    {"player": "Federico Valverde", "url": "https://www.footmercato.net/joueur/federico-valverde/statistique"},
    {"player": "Martin Ødegaard", "url": "https://www.footmercato.net/joueur/martin-odegaard/statistique"},
    {"player": "Rúben Dias", "url": "https://www.footmercato.net/joueur/ruben-dias/statistique"},
    {"player": "Lionel Messi", "url": "https://www.footmercato.net/joueur/lionel-messi/statistique"},
    {"player": "Michael Olise", "url": "https://www.footmercato.net/joueur/michael-olise/statistique"},
    {"player": "Ousmane Dembélé", "url": "https://www.footmercato.net/joueur/ousmane-dembele/statistique"},
]

CSV_PATH = "ballon_dor_2025_26_ml_ready.csv"
BASE_FIELDS = [
    "player",
    "season",
    "matches",
    "starts",
    "sub_in",
    "sub_out",
    "goals",
    "assists",
    "yellow_cards",
    "red_cards",
    "status",
    "source_url",
    "competition_rows",
    "position_rows",
    "goal_details",
    "trophies_2025_26",
]


def clean_text(value):
    if value is None:
        return ""
    return " ".join(str(value).replace("\xa0", " ").split())


def normalize_label(value):
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = value.strip("_")
    return value


def season_label(raw_value):
    if not raw_value:
        return "2025/26"
    match = re.search(r"(\d{4})", raw_value)
    if not match:
        return "2025/26"
    year = int(match.group(1))
    return f"{year}/{str(year + 1)[-2:]}"


def get_rows_for_block(block):
    rows = []
    for row in block.select("tr"):
        cells = [clean_text(cell.get_text(" ", strip=True)) for cell in row.select("td, th")]
        cells = [cell for cell in cells if cell]
        if not cells:
            continue
        text = " | ".join(cells)
        rows.append(text)
    return rows


def parse_number(value):
    match = re.search(r"-?\d+(?:[.,]\d+)?", value)
    if not match:
        return value
    number = match.group(0).replace(",", ".")
    return float(number) if "." in number else int(number)


def extract_table_stats(table, row_label):
    if row_label == "competition":
        fields = ["matches", "goals", "assists", "sub_in", "sub_out", "yellow_cards", "red_cards"]
    else:
        fields = ["matches", "starts", "goals", "assists", "yellow_cards", "red_cards"]

    records = []
    for row in table.select("tr")[1:]:
        cells = [clean_text(cell.get_text(" ", strip=True)) for cell in row.select("td")]
        cells = [cell for cell in cells if cell]
        if len(cells) != len(fields) + 1:
            continue
        record = {row_label: cells[0]}
        record.update({field: parse_number(value) for field, value in zip(fields, cells[1:])})
        records.append(record)
    return records


def extract_goal_details(block):
    details = []
    for item in block.select(".goalsStatsByType .horizontalPercentageBar"):
        label = item.select_one(".horizontalPercentageBar__legend")
        percent = item.select_one(".horizontalPercentageBar__percent")
        value = item.select_one(".horizontalPercentageBar__value")
        if label and percent and value:
            details.append(
                {
                    "type": clean_text(label.get_text(" ", strip=True)),
                    "percentage": parse_number(percent.get_text(" ", strip=True)),
                    "goals": parse_number(value.get_text(" ", strip=True)),
                }
            )
    return details


def extract_trophies_2025_26(soup):
    trophies = []
    for item in soup.select(".tournamentAward"):
        competition = item.select_one(".tournamentAward__competition")
        seasons = item.select_one(".tournamentAward__seasons")
        if not competition or not seasons:
            continue
        season_values = [clean_text(value) for value in seasons.get_text(" ", strip=True).split(",")]
        if "2025/2026" in season_values or "2025" in season_values or "2026" in season_values:
            trophies.append({"competition": clean_text(competition.get_text(" ", strip=True)), "season": "2025/26"})
    return trophies


def extract_current_season_data(soup):
    blocks = soup.select("div.wrapper.playerStats")
    if not blocks:
        return {"season": "2025/26", "stats": {}, "status": "not_found", "competition_stats": [], "position_stats": [], "goal_details": []}

    block = None
    for item in blocks:
        season_attr = item.get("data-season-club", "")
        if season_label(season_attr) == "2025/26":
            block = item
            break

    if block is None:
        block = blocks[0]

    season_attr = block.get("data-season-club", "")
    season = season_label(season_attr)

    stats = {}
    for item in block.select(".globalStatItem"):
        label_tag = item.select_one(".globalStatItem__label")
        value_tag = item.select_one(".globalStatItem__value")
        if label_tag and value_tag:
            label = clean_text(label_tag.get_text(" ", strip=True))
            val = clean_text(value_tag.get_text(" ", strip=True))
            if label and val:
                stats[label] = val

    tables = block.select("table.complexTable")
    competition_stats = extract_table_stats(tables[0], "competition") if tables else []
    position_stats = extract_table_stats(tables[1], "position") if len(tables) > 1 else []

    return {
        "season": season,
        "stats": stats,
        "status": "ok" if stats else "empty",
        "competition_stats": competition_stats,
        "position_stats": position_stats,
        "goal_details": extract_goal_details(block),
    }


def write_row(writer, player_name, season, stats, competition_stats, position_stats, goal_details, trophies, status, url):
    writer.writerow(
        {
            "player": player_name,
            "season": season,
            "matches": stats.get("Matchs joués", ""),
            "starts": stats.get("Titularisations", ""),
            "sub_in": stats.get("Entrées en jeu", ""),
            "sub_out": stats.get("Remplacements", ""),
            "goals": stats.get("Buts", ""),
            "assists": stats.get("Passes décisives", ""),
            "yellow_cards": stats.get("Cartons jaunes", ""),
            "red_cards": stats.get("Cartons rouges", ""),
            "status": status,
            "source_url": url,
            "competition_rows": json.dumps(competition_stats, ensure_ascii=False),
            "position_rows": json.dumps(position_stats, ensure_ascii=False),
            "goal_details": json.dumps(goal_details, ensure_ascii=False),
            "trophies_2025_26": json.dumps(trophies, ensure_ascii=False),
        }
    )


def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=BASE_FIELDS)
        writer.writeheader()

        for candidate in CANDIDATES:
            player = candidate["player"]
            url = candidate["url"]
            try:
                response = requests.get(url, headers=headers, timeout=20)
            except requests.RequestException:
                write_row(writer, player, "2025/26", {}, [], [], [], [], "request_error", url)
                continue

            if response.status_code != 200:
                write_row(writer, player, "2025/26", {}, [], [], [], [], f"status_{response.status_code}", url)
                continue

            soup = BeautifulSoup(response.text, "html.parser")
            data = extract_current_season_data(soup)
            try:
                palmares_response = requests.get(url.replace("/statistique", "/palmares"), headers=headers, timeout=20)
                trophies = extract_trophies_2025_26(BeautifulSoup(palmares_response.text, "html.parser")) if palmares_response.status_code == 200 else []
            except requests.RequestException:
                trophies = []
            write_row(
                writer,
                player,
                data["season"],
                data["stats"],
                data["competition_stats"],
                data["position_stats"],
                data["goal_details"],
                trophies,
                data["status"],
                url,
            )

    print(f"Saved {CSV_PATH}")
    print(f"Processed {len(CANDIDATES)} candidates")


if __name__ == "__main__":
    main()