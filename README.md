\# 🛒 Real-Time Retail Analytics Platform



\### End-to-End Data Engineering \& Analytics Project



\*\*Apache Kafka → Apache Spark Structured Streaming → PostgreSQL → dbt → Streamlit\*\*



\---



\## 📌 Project Overview



The Real-Time Retail Analytics Platform is an end-to-end streaming analytics solution that simulates retail transactions, processes them in real time, stores them in a centralized data warehouse, transforms them into analytical datasets, and presents actionable business insights through an interactive dashboard.



The project demonstrates modern data engineering concepts including real-time ingestion, stream processing, data warehousing, analytical modeling, query optimization, data quality validation, security implementation, and business intelligence reporting.



\---



\## 🎯 Project Objectives



\* Build a real-time streaming data pipeline.

\* Store and manage transactional data in a warehouse.

\* Transform raw data into analytics-ready datasets.

\* Monitor business KPIs through dashboards.

\* Implement data quality validation.

\* Demonstrate database security controls.

\* Optimize analytical query performance.



\---



\## 🏗️ System Architecture



```text

Retail Transaction Producer

&#x20;           │

&#x20;           ▼

&#x20;     Apache Kafka

&#x20;           │

&#x20;           ▼

&#x20;Apache Spark Streaming

&#x20;           │

&#x20;           ▼

&#x20;      PostgreSQL

&#x20;     Data Warehouse

&#x20;           │

&#x20;           ▼

&#x20;           dbt

&#x20;    Transformation Layer

&#x20;           │

&#x20;           ▼

&#x20;   Streamlit Dashboard

```



\---



\## ⚙️ Technology Stack



| Component                 | Technology                        |

| ------------------------- | --------------------------------- |

| Programming Language      | Python                            |

| Message Broker            | Apache Kafka                      |

| Stream Processing         | Apache Spark Structured Streaming |

| Data Warehouse            | PostgreSQL                        |

| Data Transformation       | dbt                               |

| Dashboard \& Visualization | Streamlit                         |

| Data Validation           | Custom Quality Checks             |

| Query Optimization        | PostgreSQL Indexing               |

| Version Control           | Git \& GitHub                      |



\---



\## 🚀 Key Features



\### Real-Time Streaming Pipeline



\* Retail transaction generator using Python.

\* Kafka producer for event streaming.

\* Spark Structured Streaming consumer.

\* Near real-time ingestion into PostgreSQL.



\### Data Warehouse



\* Centralized PostgreSQL warehouse.

\* Historical transaction storage.

\* Structured schema for analytical workloads.



\### dbt Transformation Layer



The project implements a layered transformation architecture:



\#### Silver Layer



\* `stg\_transactions`



\#### Gold Layer



\* `product\_sales`

\* `daily\_sales`

\* `product\_performance`



\### Business Intelligence Dashboard



Interactive Streamlit dashboard featuring:



\* Live KPI monitoring

\* Revenue tracking

\* Product performance analytics

\* Revenue trend analysis

\* Product-wise sales analysis

\* Live transaction feed



\### Data Quality Validation



Automated checks include:



\* Transaction ID not null

\* Customer ID not null

\* Quantity greater than zero

\* Price greater than zero

\* Valid product values



\### Query Optimization



Performance improvements using:



\* Product-based indexing

\* Time-based indexing

\* EXPLAIN ANALYZE benchmarking

\* Execution plan comparison



\### Security Demonstration



Role-based access control implementation:



\* Regional Manager access

\* National Manager access

\* Controlled warehouse visibility



\---



\# 📸 Project Evidence



\## dbt DAG



Location:



```text

docs/screenshots/dbt\_dag.png

```



\---



\## Data Models



\### Staging Model



```text

docs/screenshots/stg\_transactions\_model.png

```



\### Product Sales Model



```text

docs/screenshots/product\_sales\_model.png

```



\### Daily Sales Model



```text

docs/screenshots/daily\_sales\_model.png

```



\### Product Performance Model



```text

docs/screenshots/product\_performance\_model.png

```



\---



\## Dashboard Screenshots



\### Dashboard Overview



```text

docs/screenshots/dashboard\_overview.png

```



\### Product Analytics



```text

docs/screenshots/dashboard\_product\_analytics.png

```



\### Live Transaction Feed



```text

docs/screenshots/dashboard\_live\_feed.png

```



\---



\## Query Optimization Evidence



\### Product Query (Before Optimization)



```text

docs/screenshots/query\_optimization\_product\_before.png

```



\### Product Query (After Optimization)



```text

docs/screenshots/query\_optimization\_product\_after.png

```



\### Time-Based Query Optimization



```text

docs/screenshots/query\_optimization\_product\_time.png

```



\### Recent Transactions Query



```text

docs/screenshots/query\_optimization\_recent\_transactions.png

```



\### Revenue Aggregation Query



```text

docs/screenshots/query\_optimization\_revenue.png

```



\---



\# 📂 Deliverables



The following internship deliverables have been completed:



| Deliverable                  | Status |

| ---------------------------- | ------ |

| Real-Time Streaming Pipeline | ✅      |

| PostgreSQL Data Warehouse    | ✅      |

| dbt Transformation Layer     | ✅      |

| Data Quality Validation      | ✅      |

| Query Optimization Report    | ✅      |

| Security Demonstration       | ✅      |

| Interactive Dashboard        | ✅      |

| Project Documentation        | ✅      |



\---



\# 📊 Data Quality Report



Location:



```text

docs/deliverables/data\_quality/data\_quality\_report.csv

```



Checks performed:



\* transaction\_id\_not\_null

\* customer\_id\_not\_null

\* quantity\_positive

\* price\_positive

\* valid\_products



\---



\# ⚡ Performance Optimization Report



Location:



```text

docs/deliverables/performance\_report/query\_optimization\_report.md

```



Includes:



\* Baseline query performance

\* Index implementation

\* Execution plan comparison

\* Performance improvement analysis



\---



\# 🔒 Security Demonstration



Location:



```text

docs/deliverables/security\_demo/

```



Includes:



\* Regional Manager access screenshots

\* National Manager access screenshots

\* Security demonstration report



\---



\# ▶️ Running the Project



\## 1. Start PostgreSQL



```bash

docker start retail-postgres

```



\## 2. Start Zookeeper



```bash

zookeeper-server-start.bat config/zookeeper.properties

```



\## 3. Start Kafka



```bash

kafka-server-start.bat config/server.properties

```



\## 4. Start Producer



```bash

python producer/producer.py

```



\## 5. Start Spark Consumer



```bash

python spark\_jobs/stream\_consumer.py

```



\## 6. Run dbt Models



```bash

dbt run

```



\## 7. Launch Dashboard



```bash

streamlit run streamlit\_app/app.py

```



\---



\# 📁 Repository Structure



```text

real\_time\_retail\_platform

│

├── producer

├── spark\_jobs

├── streamlit\_app

├── retail\_dbt

├── quality\_checks

├── docs

│   ├── screenshots

│   └── deliverables

└── README.md

```



\---



\# 👨‍💻 Author



\*\*Shabbir Rajgarh Wala\*\*



Bachelor of Computer Applications (BCA)



Shri Vaishnav Institute of Management \& Science (SVIMS), Indore



Data Analytics Internship Project



2026



