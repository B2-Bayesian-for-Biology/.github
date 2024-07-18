import requests
import matplotlib.pyplot as plt

# Replace 'B2-Bayesian' with your organization name
org_name = 'B2-Bayesian'

# GitHub API to fetch repositories
repos_url = f'https://api.github.com/orgs/B2-Bayesian-for-Biology/repos'
repos = requests.get(repos_url).json()

# Initialize a dictionary to store language usage
language_usage = {}

# Fetch language stats for each repository
for repo in repos:
    languages_url = repo['languages_url']
    languages = requests.get(languages_url).json()
    for language, bytes_of_code in languages.items():
        if language in language_usage:
            language_usage[language] += bytes_of_code
        else:
            language_usage[language] = bytes_of_code

# Plotting the pie chart
labels = language_usage.keys()
sizes = language_usage.values()

plt.figure(figsize=(10, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Programming Language Usage in B2-Bayesian for Biology')
plt.savefig('language_stats.png')
