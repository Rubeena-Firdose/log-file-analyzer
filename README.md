# log-file-analyzer
Final project - Log File Analyzer for Intrusion Detection
# Log File Analyzer for Intrusion Detection

A Python-based tool designed to analyze Apache and SSH logs for signs of intrusion such as brute-force attacks, DoS patterns, and scanning activity. Built to support SOC analysts, cybersecurity learners, and system administrators.

## Features

- Analyze Apache (`access.log`) and SSH (`auth.log`) files
- Detect:
  - Brute-force login attempts
  - Denial-of-Service (DoS) patterns
  - Endpoint scanning behavior
- Cross-reference with IP blacklist
- Export incident reports in CSV
- Generate charts for failed logins and access frequency

## Tools & Technologies

- Python 3
- Regex – for log pattern matching
- Pandas – for data analysis
- Matplotlib – for visualizations

## Folder Structure

log-file-analyzer/
├── logs/                # Contains sample Apache and SSH logs
├── analyzer.py          # Script to parse logs and detect suspicious IPs
├── visualizer.py        # Script to visualize failed logins/access frequency
├── blacklist.txt        # IPs flagged from known sources
├── report.csv           # Output report with flagged entries
└── README.md            # Project instructions and usage

## How to Use

1. Clone the repository:
   git clone https://github.com/your-username/log-file-analyzer.git
   cd log-file-analyzer

2. Place logs inside the `logs/` folder. Use real or sample logs from Apache (`access.log`) or SSH (`auth.log`).

3. Run the analyzer script:
   python analyzer.py

4. Optional – Generate visualizations:
   python visualizer.py

5. Review the results:
   - Check `report.csv` for suspicious activity
   - View graphs for login attempts or traffic spikes

## Sample Output

Example:
192.168.1.100 - Brute-force (20 failed logins)
192.168.1.101 - DoS (500+ requests in 10 mins)

Charts:
- Bar chart showing failed login attempts per IP
- Line graph of access over time

## License

This project is licensed under the MIT License – see the LICENSE file for details.

## Contributing

Feel free to fork the repo, open issues, or submit pull requests to improve detection accuracy or add more log types.

## Acknowledgments

- Inspired by real-world SOC practices
- Sample logs and detection patterns based on OWASP guidance
