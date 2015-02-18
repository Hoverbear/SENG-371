from jira.client import JIRA

from datetime import datetime


def main():
    options = {
        'server': 'https://jira.codehaus.org/'
    }
    jira = JIRA(options)

    # Get all projects viewable by anonymous users.
    projects = jira.projects()

    # Sort available project keys, then return the second, third, and fourth keys.
    keys = sorted([project.key for project in projects])[2:5]

    # Get an issue.
    issue = jira.issue('SONAR-5132')

    # print issue.raw

    print issue.fields.created
    start_time = issue.fields.created

    print issue.fields.resolutiondate
    end_time = issue.fields.resolutiondate


# Format Expected: 2014-04-22T05:06:50.714-0500
"""def create_date(date_string):

    date_time_array = date_string.split("T")
    dates_array = date_time_array[0].split("-")
    time_array = date_time_array[1].split(";")

    # Create a readable array of all dates
    dates = {
        "year": dates_array[0],
        "month": dates_array[1],
        "day": dates_array[2]
    }

    # Create a readable array of all times up to seconds
    times = {
        "hour": time_array[0],
        "minute":
    }"""


if __name__ == '__main__':
    main()