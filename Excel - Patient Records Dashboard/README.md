<p align="center">
  <h1>Healthcare Data Analysis Excel Dashboard</h1>
</p>

<p align="center">
  <img src="Healthcare_Data_Analysis_Dashboard.png" alt="Dashboard Preview" width="600">
</p>

This project focuses on analyzing healthcare clinical and operational data using Microsoft Excel.  
The objective of the dashboard is to help clinicians and administrators **monitor patient outcomes, common diagnoses, departmental workload, and improvement trends** in a clear, interactive format.

---

## Project Overview

The dataset includes patient visits with fields such as:

| Field | Description |
|------|-------------|
| Patient_ID | Unique identifier for each patient |
| Visit_Date | Date of the clinical visit |
| Diagnosis | Primary diagnosis assigned at visit |
| Treatment | Treatment or intervention provided |
| Outcome | Final patient status: Improved / Stable / Worsened |
| Department | Clinical department responsible for the visit |
| Age | Patient age (optional) |

The data was cleaned, structured, and converted into an **Excel Table** to allow dynamic analysis and automatic updates.

---

## Key Performance Indicators (KPIs)

The dashboard highlights the following metrics:

- **Total number of patients**
- **Total number of visits**
- **Percentage of improved outcomes**
- **Most frequent diagnoses**
- **Patient distribution by department**
- **Monthly visit trends**

These KPIs update automatically when new data is added.

---

## Dashboard Visualizations

The dashboard includes the following charts:

| Visualization | Chart Type | Purpose |
|--------------|------------|---------|
| Diagnosis Frequency | Horizontal Bar Chart | Shows the most common diagnoses |
| Outcome by Diagnosis | Stacked Column Chart | Highlights treatment effectiveness by condition |
| Patients by Department | Donut / Bar Chart | Displays clinical workload distribution |
| Outcome by Department | Grouped Column Chart | Compares performance across departments |
| Monthly Visit Trend | Line Chart + Slicer | Tracks visit volume over time |

Interactive **slicers** allow users to filter the entire dashboard by:
- **Department**
- **Visit Year**

---

## Tools & Techniques Used

| Skill / Feature | Description |
|-----------------|-------------|
| Excel Tables | Created a dynamic dataset (`tbl_Healthcare`) |
| Data Validation | Ensured clean and consistent data entry |
| Helper Columns | Extracted Visit Year and Visit Month automatically |
| PivotTables & PivotCharts | Used for dynamic charting and aggregation |
| Slicers / Report Connections | Enabled interactive filtering across dashboards |
| Conditional Formatting | Highlighted key KPIs for quick interpretation |

---

## How to Use

1. Open **Healthcare_Dashboard.xlsx**
2. Use slicers (Department & Visit Year) to explore data interactively
3. Enter new patient visit records in the **Raw_Data** sheet — all charts update automatically

---

## What I Learned

- Designing healthcare performance dashboards for clinical use
- Using PivotTables and slicers for interactive reporting
- Applying COUNTIFS, AVERAGEIFS, and dynamic formulas for KPI calculations
- Structuring datasets to support automated analytics workflows

---

## Future Enhancements

- Integrate Power Query for automated data refresh
- Add trending alerts using advanced conditional formatting
- Publish dashboard to Power BI for broader accessibility
