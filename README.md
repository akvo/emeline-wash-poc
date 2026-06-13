# 💧 Water Projects — Streamlit App

A multi-page Streamlit app showcasing WASH (Water, Sanitation & Hygiene) research, tools, and project tracking built with Akvo.

---

## Pages

| Page | Description |
|------|-------------|
| Data for WASH · Theory of Change and Maturity Index | Interactive HTML framework |
| Country Opportunity | WASH explorer map |
| Investment in data infrastructure for WASH cascading effect | External Claude artifact |
| Akvo · Theory of Change & Assumptions | Theory of change visual |
| Why Akvo's Work Matters | Mindmap |
| WASH · Maturity Framework | Framework (French) |
| WaterConnect · Demo | WaterConnect demo mock |
| Project Tracker | Built-in tracker |
| Project Dashboard | Built-in dashboard |

---

## Requirements

- Python 3.8+
- Streamlit
- Folium

Install dependencies:

```bash
pip install streamlit folium
```

---

## Run the app

```bash
cd /Users/emelinebereziat/streamlit-app/streamlit-app
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## Project structure

```
streamlit-app/
├── app.py                          # Main app — page routing & sidebar
├── project_tracker.py              # Built-in project tracker page
├── dashboard.py                    # Built-in dashboard page
├── requirements.txt
├── data_for_wash_complete_v4_1.html
├── wash_explorer_map_v3.html
├── akvo_toc_with_assumptions.html
├── akvo_mindmap_v3_html.html
├── wash_maturity_framework_fr.html
├── WaterConnect_Demo_Mock.html
└── country-page-poc6.html
```

---

## Adding a new page

Open `app.py` and add an entry to the `PAGES` dictionary:

```python
# For a local HTML file:
"My New Page": {"file": "my_page.html"},

# For an external URL:
"My External Page": {"url": "https://example.com"},
```

Then place the HTML file in the same folder as `app.py`.

---

## Managing the app with Claude Code

[Claude Code](https://docs.anthropic.com/en/docs/claude-code) can manage this app from the terminal — installing packages, editing files, and running commands via plain English instructions.

```bash
cd /Users/emelinebereziat/streamlit-app/streamlit-app
claude
```
