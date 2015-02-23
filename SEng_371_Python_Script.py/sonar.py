from jira.client import JIRA

from datetime import datetime
from datetime import timedelta

# Server hosting the Jira repo and the JQL search query
server = 'https://issues.apache.org/jira/'

project = raw_input("Enter a project: ").upper()
filter_query = "project = " + project + ' AND issuetype = "New Feature" AND priority = Major AND status = Closed'
# project = PF AND issuetype = "New Feature" AND priority = Major AND status = Closed ORDER BY summary ASC
# project = AND issuetype = "New Feature" AND priority = Major AND status = Closed'


def main():
    print "Connecting to the server..."

    options = {
        'server': server
    }
    jira = JIRA(options)

    features_in_proj = jira.search_issues(filter_query, maxResults=None)

    # Store the issue information
    all_dates = []
    average_dates_per_feature = timedelta(0)
    length = 0

    # create two date time events, one with 30 minutes and one with 1 year = 365 days
    bottom_limit = timedelta(0, 0, 0, 0, 30)
    top_limit = timedelta(365)

    print bottom_limit
    print top_limit

    # Create a list of all difference in times and an average of all those times for each feature
    for issue in features_in_proj:
        current_datetime = get_date_difference(issue)
        if current_datetime >= bottom_limit and current_datetime <= top_limit:
            all_dates.append(current_datetime)
            average_dates_per_feature += current_datetime
            length += 1
            print current_datetime

    print str(length) + " Out of: " + str(len(features_in_proj))
    print "Average development time " + str(average_dates_per_feature/length)


# Format Expected: 2014-04-22T05:06:50.714-0500
def get_date_difference(issue):

    # Not accounting for any time smaller than seconds
    start_date_string = issue.fields.created.split(".")[0]
    end_date_string = issue.fields.resolutiondate.split(".")[0]

    date_format = "%Y-%m-%dT%H:%M:%S"

    # Create the datetime objects for easy subtraction
    start_date_time = datetime.strptime(start_date_string, date_format)
    end_date_time = datetime.strptime(end_date_string, date_format)

    return end_date_time - start_date_time


if __name__ == '__main__':
    main()