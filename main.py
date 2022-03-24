import os
import re
from github import Github


def main():
    g = Github(os.environ["GITHUB_TOKEN"])
    repos = g.get_organization(os.environ["ORG"]).get_repos()
    remaining = repos.totalCount; idx = 0
    while remaining > 0:
        # get next page
        page_results = repos.get_page(idx)
        for repo in page_results:
            print(re.match(pattern=os.environ["PATTERN"]))
    os.environ["REPOS"] = "empty"

if __name__ == "__main__":
    main()
