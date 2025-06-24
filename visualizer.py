# visualizer.py - placeholder for matplotlib visualizations

import matplotlib.pyplot as plt

# Sample data for plotting
ips = ['192.168.1.1', '192.168.1.2', '192.168.1.3']
counts = [25, 18, 9]

plt.bar(ips, counts)
plt.title("Failed Login Attempts by IP")
plt.xlabel("IP Address")
plt.ylabel("Attempts")
plt.savefig("failed_logins.png")
plt.show()
