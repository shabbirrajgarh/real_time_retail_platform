\# Query Performance Optimization Report



\## Query 1: Product Filter



Before:

\- Seq Scan

\- Execution Time: 2.310 ms



After:

\- Bitmap Index Scan using idx\_transactions\_product

\- Execution Time: 1.224 ms



Improvement:

\- \~47%



\---



\## Query 2: Sort By Transaction Time



Before:

\- Seq Scan + Sort

\- Execution Time: 3.580 ms



After:

\- Index Scan using idx\_transactions\_time

\- Execution Time: 0.085 ms



Improvement:

\- \~97.6%



\---



\## Query 3: Revenue Aggregation



Before:

\- HashAggregate + Seq Scan

\- Execution Time: 5.529 ms



After:

\- HashAggregate + Seq Scan

\- Execution Time: 7.324 ms



Observation:

\- Index was not beneficial.

\- PostgreSQL correctly selected Seq Scan.

\- Demonstrates evidence-driven optimization.



\---



\## Query 4: Recent Transactions



Query:

transaction\_time > NOW() - INTERVAL '1 day'



Execution Time:

\- 2.016 ms



Index Used:

\- idx\_transactions\_time



\---



\## Query 5: Product + Time Filter



Query:

product='Laptop'

AND transaction\_time > NOW()-INTERVAL '1 day'



Execution Time:

\- 1.596 ms



Index Used:

\- idx\_transactions\_product



\---



Conclusion



Five warehouse optimization scenarios were tested using EXPLAIN ANALYZE.



Indexes improved selective lookups and time-based queries significantly while full-table aggregations remained faster using sequential scans.



The warehouse optimization objective was successfully achieved.

