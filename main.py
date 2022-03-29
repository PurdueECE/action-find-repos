from datetime import datetime
import os
import re

from github import Github


def main(org = None, pat = None, name_filter = None, created_after = '1970-01-01T00:00:00',
    created_before = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')):
    if org == None: org = os.environ["ORG"]
    if pat == None: pat=os.environ["GITHUB_TOKEN"]
    if name_filter == None: name_filter=os.environ["PATTERN"]
    created_after = datetime.strptime(created_after, '%Y-%m-%dT%H:%M:%S')
    created_before = datetime.strptime(created_before, '%Y-%m-%dT%H:%M:%S')
    os.system(f"echo '::set-output name=TOKEN::${pat}'")
    g = Github(pat)
    all_repos = g.get_organization(org).get_repos()
    remaining = all_repos.totalCount; page_num = 0
    repos = []
    while remaining > 0:
        # get next page
        page_results = all_repos.get_page(page_num)
        # check each repo in page
        for repo in page_results:
            print(f"Checking repo '{repo.name}'")
            if re.match(name_filter, repo.name) != None:
                if repo.created_at > created_after and repo.created_at < created_before:
                    repos.append(repo.name)
        # update indeces
        remaining -= len(page_results)
        page_num += 1
    os.system(f"echo '::set-output name=REPOS::{','.join(repos)}'")

if __name__ == "__main__":
    main()
