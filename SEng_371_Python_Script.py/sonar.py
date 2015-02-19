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
    get_date_difference(issue)


# Format Expected: 2014-04-22T05:06:50.714-0500
def get_date_difference(issue):

    # Not accounting for any time smaller than seconds
    start_date_string = issue.fields.created.split(".")[0]
    end_date_string = issue.fields.resolutiondate.split(".")[0]

    date_format = "%Y-%m-%dT%H:%M:%S"

    # Create the datetime objects for easy subtraction
    start_date_time = datetime.strptime(start_date_string, date_format)
    end_date_time = datetime.strptime(end_date_string, date_format)

    print end_date_time - start_date_time


if __name__ == '__main__':
    main()