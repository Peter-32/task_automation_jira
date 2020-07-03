from jira import JIRA
from pandas import DataFrame

user = 'peter___@gmail.com'
apikey = '...'
password = 'pass123'
server = 'https://___.atlassian.net/'

jira = JIRA(basic_auth=(user, apikey), options={'server': server})

# Find issues with attachments:
query = jira.search_issues(jql_str="""(project = DS or project = MIDS)
AND created > -1d AND created <= 0d
 """, json_result=True, fields="key, description, summary", maxResults=100)

rows = []
# And remove attachments one by one
for issue in query['issues']:
    row = {}
    row['key'] = issue['key']
    row['title'] = issue['fields']['summary']
    row['description'] = issue['fields']['description']
    rows.append(row)
df = DataFrame(rows)
