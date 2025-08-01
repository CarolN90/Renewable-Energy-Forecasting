
<h1 align="center">Towards a Resilient Grid: Strategies for Variable Renewable Energy in Kenya</h1>

<h2 align="center"><i>Data-Driven Solutions for a Reliable and Green Energy Future</i></h2>

![Gemini_Generated_Image_adcgg3adcgg3adcg](https://github.com/user-attachments/assets/c408eaa8-ac4c-459c-a339-bf2a192294c7)

---
Live Webapp: https://energyconsumptionapp.streamlit.app/ 
>*This architecture supports scalability and modularity, making it easy to incorporate more data sources or integrate into real-time systems like Streamlit or PowerBI dashboards.*
---
##  Project Overview

Kenya is a global leader in renewable electricity generation, with over 80% of its power coming from sustainable sources like geothermal, wind, and solar. However, as the country accelerates toward its ambitious 100% renewable energy goal by 2050, critical challenges emerge—especially around variability, grid reliability, and equitable access.

This project explores **data-driven strategies** to enhance grid stability and optimize renewable energy integration, leveraging machine learning and exploratory data analysis (EDA) on datasets sourced from Kenya's national energy agencies.

---

## Objectives
This analysis seeks to answer the following key questions:

1.  How have electricity consumption trends and grid connectivity evolved over time in Kenya?
    
2.  How does energy generation by source evolve over time, and what trends emerge in the mix of renewables vs non-renewables?
    
3.  How can we visualize Kenya’s energy landscape using interactive and static plots to reveal key insights?
    
4.  What patterns and insights can be uncovered to inform future energy planning and improve grid resilience?

---
##  Project Architecture & Data Flow

The project follows a structured pipeline from data acquisition to deployment and feedback, enabling robust analysis and insights for Kenya’s energy resilience:

```
Data Extraction → Data Processing → Modeling & Analysis → Visualization & Reporting → Feedback Loop
     ↓                  ↓                   ↓                        ↓                        ↓
  EPRA Excel       →  Cleaning        →  EDA & Stats         →  Jupyter Charts        →  Strategic Insights
  Datasets         →  Merging         →  Trend Analysis      →  Grid Maps             →  Policy Feedback
  Sector Data      →  Feature Eng     →  Scenario Testing    →  Dashboards            →  Planning Review
```
---

##  Methods and Tools

###  Technologies
- Python 3.x (3.11+ in your case)
- Data manipulation: Pandas, NumPy
- Visualization: Matplotlib, Seaborn, Plotly (often via Streamlit dashboards)
- Time‑series statistical modeling: SARIMAX (from statsmodels)
- Deep learning: LSTM (e.g. via TensorFlow or PyTorch)
- Interactive app frameworks: Streamlit, integrated with Plotly
- Notebooks: Jupyter Notebook

###  Data Sources
- [Energy and Petroleum Regulatory Authority (EPRA)](https://www.epra.go.ke)
- National energy statistics from Excel datasets

| **#** | **Dataset Name**                               | **Time Range**                | **Key Features**                                                                                       |
| ----- | ---------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------ |
| 1     | **Electricity Generation by Technology**       | Jan 2019 – Apr 2025 (Monthly) | Generation (GWh) by source:<br>Hydro, Thermal, Wind, Geothermal, Bagasse/Biogas, Imports, Solar, Total |
| 2     | **Installed Renewable Capacity**               | 2024 (Annual Snapshot)        | Installed capacity (MW) by:<br>Hydro, Geothermal, Wind, Biomass, Solar                                 |
| 3     | **Transmission & Distribution Infrastructure** | FY 2019/20 – Apr 2025         | Circuit length (km) by voltage:<br>HV (500–66kV), MV (33kV, 11kV), LV (415/240V)                       |
| 4     | **Grid Connectivity**                          | Jul 2019 – Apr 2025 (Monthly) | Monthly new connections & cumulative customer totals                                                   |
| 5     | **Electricity Consumption**                    | Jul 2019 – Apr 2025 (Monthly) | Electricity sales to end-users (GWh)                                                                   |


---

##  Key Insights

- **Demand-Supply Mismatch**:
<img width="2214" height="927" alt="image" src="https://github.com/user-attachments/assets/6deafa4a-b6e0-4ea9-aa01-03cb85c07486" />

**Insights:**
  
Electricity demand is steadily rising with seasonal peaks, and while grid capacity is expanding, it may lag behind, causing bottlenecks that highlight the need for proactive upgrades to ensure stability, reduce outages, and guide strategic investment decisions.
- **Tariff Variability**:
<img width="1760" height="1238" alt="image" src="https://github.com/user-attachments/assets/a4df0273-93de-4239-abaa-3ee6a66eba8b" />

**Insights:**
  
  DC3 (Small Commercial) leads in electricity consumption, exceeding 100K GWh, followed by CI1 (Commercial Industrial), reflecting strong industrial demand, while SC3 also shows high usage just below DC3; in contrast, residential categories (DC1, DC2) have lower consumption, Bulk Supply (SC3 1000pe) indicates moderate demand, and higher-tier CI and SC classes (CI4–CI6, SC7) consume the least.
- **Technology Trends**: Wind and solar have seasonal patterns affecting their contribution to the grid.
<img width="2214" height="1085" alt="image" src="https://github.com/user-attachments/assets/b8eb9931-56e2-4895-89bb-1c12936c560f" />

**Insights**:

Electricity demand in Kenya is rising with seasonal peaks, while stable geothermal supply contrasts with variable hydro, solar, and wind generation, leading to reliance on costly thermal power to fill gaps and exposing grid bottlenecks and storage challenges.

---

##  Impact

This work provides a foundation for:
- Policymakers to assess current grid resilience and future investment needs.
- Grid operators to plan for load balancing amidst variable generation.
- Stakeholders to visualize clean energy transition trajectories.

---

##  How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/CarolN90/Renewable-Energy-Forecasting
cd Renewable-Energy-Forecasting
```

2. Set up a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Launch the notebook:

```bash
jupyter notebook Capstone_phase5.ipynb
```

---

##  Requirements

Generate with:

```bash
pip freeze > requirements.txt
```

Content:

```
pandas
numpy
matplotlib
seaborn
openpyxl
```
---
##  Contributors

- [Naomi Ngigi](https://github.com/Naomi-N-w)
- [Elvis Tile](https://github.com/elvis07jr)
- [Janine Makorre](https://github.com/Uxer-Janine)  
- [Trevor Maina](https://github.com/trevormaina2)  
- [Caroline Wachira](https://github.com/CarolN90)  

---

##  Project Structure

```bash
.
Renewable-Energy-Forecasting/
├── app/
│   ├── data/
│   │   └── merged1_energy_data.csv
│   ├── models/
│   │   ├── LSTM Model - 1.ipynb
│   │   └── sarimax_results.pkl
│   ├── pages/
│   │   ├── Forecasting_Tool.py
│   │   ├── Generation_Mix.py
│   │   ├── Grid_Connectivity.py
│   │   ├── Overview.py
│   │   └── Scenario_Explorer.py
│   └── utils/
│       ├── data_loader.py
│       └── plots.py
├── epra_data/
│   ├── Average_Retail_Prices.xlsx
│   ├── Electricity_Consumption.xlsx
│   ├── Electricity_Generation_By_Technology.xlsx
│   ├── Energy_consumption_by_region_and_consumer_class_as_at_dec2022.xlsx
│   ├── Grid_Connectivity.xlsx
│   ├── Installed_Capacity_Renewables.xlsx
│   ├── Transmission_and_Distribution_Infrastructure.xlsx
│   ├── final_processed_energy_dataset.csv
│   ├── merged_energy_dataset.csv
│   └── model_merged.csv
│   └── models/
│       └── epra_lstm_model.h5
├── models/
│   ├── LSTM Model - 1.ipynb
│   └── sarimax_results.pkl
├── .gitignore
├── best_model_LinearRegression.joblib
├── Capstone_phase5.ipynb
├── Capstone_PowerConsumption.pbix
└── README.md
```
---
##  License

This project is open-source and available under the [MIT License](LICENSE).

---
