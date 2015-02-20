from jira.client import JIRA

from datetime import datetime
from datetime import timedelta


def main():
    options = {
        'server': 'https://jira.codehaus.org/'
    }
    jira = JIRA(options)

    features_in_proj = jira.search_issues('project = SONAR AND issuetype = "New Feature" AND status = Closed')

    all_dates = []
    average_dates_per_feature = timedelta(0)

    # Create a list of all difference in times and an average of all those times for each feature
    for issue in features_in_proj:
        all_dates.append(get_date_difference(issue))
        average_dates_per_feature += get_date_difference(issue)

    print average_dates_per_feature/len(features_in_proj)


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