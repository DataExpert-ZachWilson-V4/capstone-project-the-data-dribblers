Project Proposal: Data Engineering Pipeline for FIFA Ultimate Team Database using FUTDB 


[https://github.com/orgs/DataExpert-ZachWilson-V4/teams/the-data-dribblers]

Project members : 

Aleem Rahil - aleemrahil
Hariom Nayani - hariomnayani
Sanchit Burkule - sanchitburkule

#1. Introduction
Project Title: Building a Data Engineering Pipeline for FIFA Ultimate Team Database using FUTDB
Objective: To design and implement a robust data engineering pipeline that ingests, processes, and analyzes FIFA Ultimate Team data from the FUTDB API to derive insights and support decision-making.
Scope: This project will cover data extraction from FUTDB, transformation, loading (ETL), data warehousing, and basic analytics.

#2. Background
FIFA Ultimate Team (FUT): A mode in FIFA video games that allows players to build their own squad of football players. It involves player statistics, team building, match results, and market transactions.
Data Source: FUTDB API, which provides comprehensive data on players, teams, leagues, and matches in FIFA Ultimate Team.

#3. Objectives and Goals
Primary Objective: Develop an end-to-end data pipeline to process FUTDB data.
Specific Goals:
Data Ingestion: Collect raw data from the FUTDB API.
Data Cleaning and Transformation: Normalize and transform data to ensure consistency and quality.
Data Storage: Store processed data in a scalable data warehouse.
Data Analysis: Perform basic analytics to derive insights (e.g., player performance, market trends).
Visualization: Create dashboards and reports to visualize key metrics and insights.

#4. Project Phases

##Phase 1: Data Collection and Ingestion
Tasks:
Accessing FUTDB API: Obtain API key and set up authentication.
Data Extraction: Write scripts to extract data from FUTDB endpoints (players, teams, leagues, matches).
Scheduling: Automate data extraction using scheduling tools like Apache Airflow.
Deliverables:
Data ingestion scripts and workflows.
Documentation of API endpoints and data extraction processes.

##Phase 2: Data Cleaning and Transformation
Tasks:
Data Cleaning: Handle missing values, duplicates, and inconsistencies in the extracted data.
Data Transformation: Convert data into a structured format suitable for analysis (e.g., normalization, denormalization).
Tools: Use Pandas or PySpark for data cleaning and transformation tasks.
Deliverables:
Cleaned and transformed datasets.
Data transformation scripts and documentation.

##Phase 3: Data Storage
Tasks:
Schema Design: Design a data schema for the data warehouse.
Implementation: Implement the data warehouse using platforms like Amazon Redshift, Google BigQuery (Tentative)
ETL Process: Develop ETL scripts to load transformed data into the data warehouse.
Deliverables:
Data warehouse schema.
ETL scripts and workflows.

##Phase 4: Data Analysis
Tasks:
Exploratory Data Analysis (EDA): Understand data distributions and patterns.
Analytical Queries: Develop queries to extract insights (e.g., top players, market trends).
Tools: Use SQL and Python (Pandas, Matplotlib) for analysis.
Deliverables:
EDA reports and visualizations.
Analytical queries and results.

##Phase 5: Visualization and Reporting
Tasks:
Dashboard Creation: Create dashboards to visualize data insights using tools like Tableau, Power BI, or Looker.
Reporting: Generate reports to summarize key findings and insights.
Feedback: Share dashboards and reports with stakeholders and gather feedback.
Deliverables:
Interactive dashboards.
Final project report with key findings and insights.

#6. Tools and Technologies
Data Ingestion: Custom Python scripts, Apache Airflow.
Data Cleaning and Transformation: Pandas, PySpark.
Data Storage: Amazon Redshift, Google BigQuery, Snowflake.
Data Analysis: SQL, Python (Pandas, Matplotlib).
Visualization: Tableau, Power BI, Looker.

#8. Timeline
Week 1-2: Project planning and requirements gathering, Data collection and ingestion from FUTDB API.
Week 3: Data cleaning and transformation, Data storage setup and ETL processes.
Week 4: Data analysis and EDA. Visualization, reporting, and project finalization.

#10. Expected Outcomes
A fully functional data engineering pipeline for FUTDB data.
Cleaned and structured datasets ready for analysis.
Insightful analytics and visualizations to support decision-making.
Comprehensive documentation of the entire process and methodologies used.

#12. Challenges and Risks
Data Quality: Ensuring the accuracy and completeness of the ingested data.
API Limitations: Managing API rate limits and handling large volumes of data.
Scalability: Designing a pipeline that can handle increasing data volumes efficiently.
Technical Complexity: Managing different tools and technologies for each phase of the pipeline.

#14. Conclusion
This project will provide hands-on experience with real-world data engineering tasks, including data ingestion, transformation, storage, and analysis. The insights derived from FUTDB data can be valuable for game strategy, player performance evaluation, and market analysis.
This outline serves as a foundation for your project proposal. You can expand each section with more detailed information and specific implementation plans as needed.

Architecture Diagram:
![image](https://github.com/DataExpert-ZachWilson-V4/capstone-project-the-data-dribblers/assets/47569156/d4a6072f-aadf-4172-a82a-314e57e0e61c)

