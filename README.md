# log-file-analyzer
Final project - Log File Analyzer for Intrusion Detection
#  Log File Analyzer for Intrusion Detection

A simple Python-based tool to detect suspicious activities from Apache and SSH logs. This project identifies potential brute-force attacks, DoS patterns, and scanning behavior. Ideal for SOC analysts, cybersecurity learners, and system administrators.

---

## Features

- Parse Apache (`access.log`) and SSH (`auth.log`) log files
- Detect:
  - Brute-force login attempts
  - Excessive traffic (DoS)
  - Scanning of multiple endpoints
- Cross-reference with public IP blacklists
- Generate CSV reports and visual charts

---

##  Tools & Technologies

- Python 3
- Regular Expressions (Regex)
- Pandas
- Matplotlib

---

##  Folder Structure

