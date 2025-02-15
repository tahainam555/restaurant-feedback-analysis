# OpenTable Restaurant Review Scraper & Analysis

## 📌 Project Overview
This project involves scraping restaurant reviews from OpenTable, analyzing the extracted data using prompt engineering, developing a GUI dashboard, and performing a competitor analysis. The goal is to structure and categorize customer reviews efficiently while allowing users to explore insights through an interactive interface.

---

## 📂 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## 🚀 Features
### Part 1: Web Scraping
- Scrapes reviews for a selected restaurant from OpenTable.
- Extracts the following data:
  - Restaurant name
  - Review content
  - Ratings
  - Review date
- Handles pagination to scrape all available reviews.
- Saves extracted data in JSON or CSV format.

### Part 2: Prompt Engineering
- Uses an LLM-based approach to analyze and extract:
  - Comments about food quality.
  - Comments about staff/service.
- Ensures data relevance and prevents hallucinations.
- Excludes personal information (PI) of reviewers.
- Saves structured data as `categorized_reviews.json`.

### Part 3: GUI Development
- Provides an interactive dashboard using **Streamlit** or **Flask**.
- Enables users to search for food and staff-related comments.
- Displays all reviews in a structured format similar to OpenTable.
- Highlights food and staff comments in different colors for better readability.

### Part 4: Competitor Analysis
- Extends scraping functionality to collect ratings over time for a selected restaurant and a competitor.
- Enables users to input a competitor restaurant link in the dashboard.
- Scrapes historical ratings data.
- Visualizes rating trends over time in a **time-series graph**.

---

## 🛠 Installation
### Prerequisites
Ensure you have Python installed. You may also need to install a web driver (such as **ChromeDriver**) for Selenium.

### Setup Steps
```bash
# Clone the repository
git clone https://github.com/your-repo/OpenTableScraper.git
cd OpenTableScraper

# Install dependencies
pip install -r requirements.txt

# Run the scraper
python scraper.py

# Run the GUI (if using Streamlit)
streamlit run app.py
```

---

## 📌 Usage
1. Scrape reviews from OpenTable.
2. Process and categorize reviews using LLM.
3. Launch the GUI to explore and filter reviews.
4. Perform competitor analysis by adding a competitor restaurant.

---

## 📁 Project Structure
```
OpenTableScraper/
│── data/
│   ├── reviews.json
│   ├── categorized_reviews.json
│── src/
│   ├── scraper.py
│   ├── prompt_engineering.py
│   ├── gui.py
│   ├── competitor_analysis.py
│── templates/
│   ├── index.html
│── static/
│── README.md
│── requirements.txt
```

---

## 🛠 Technologies Used
- **Python 3.8+**
- **BeautifulSoup** (Web Scraping)
- **Selenium** (Automated Browsing)
- **Pandas** (Data Processing)
- **OpenAI API** (Prompt Engineering)
- **Flask/Streamlit** (GUI Development)
- **Matplotlib, Seaborn, Plotly** (Visualization)

---

## 🚀 Future Improvements
- Improve prompt engineering for better review classification.
- Add **sentiment analysis** to reviews.
- Include **more competitor analysis** features.
- Enhance GUI with additional filters and user interactions.

---

## 📜 License
This project is licensed under the **MIT License**. See the LICENSE file for more details.

---

## ⭐ Contributing
Feel free to contribute! Open an issue or submit a pull request.

---

## 📧 Contact
For any inquiries, reach out to **your.email@example.com** or create an issue in the repository.

---

