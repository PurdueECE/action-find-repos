from argparse import ArgumentParser
from datetime import datetime
import os
import re

from github import Github


def main(args):
    parser = ArgumentParser(
        'repo finder',
        description='Find repos that match a set of filters.'
    )
    parser.add_argument(
        'org',
        help="GitHub organization to search in.",
        type=str,
    )
    parser.add_argument(
        '--name_filter',
        required=False,
        help="Regular expression filter for repo name.",
        type=str,
        default=".*"
    )
    parser.add_argument(
        '--pat',
        required=False,
        help="Personal access token.",
        type=str,
    )
    parser.add_argument(
        '--created_after',
        required=False,
        help="Earliest creation date of repo. Defaults to Jan 1, 1970",
        type=str,
        default='1970-01-01T00:00:00',
    )
    parser.add_argument(
        '--created_before',
        required=False,
        help="Latest creation date of repo. Defaults to current time.",
        type=str,
        default=datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
    )
    args = parser.parse_args(args)

    # datetime parsing
    args.created_after = datetime.strptime(args.created_after, '%Y-%m-%dT%H:%M:%S')
    args.created_before = datetime.strptime(args.created_before, '%Y-%m-%dT%H:%M:%S')
    if args.created_after >= args.created_before: raise Exception('created_after must come before created_before.')

    # repo search
    g = Github(args.pat)
    repos = g.get_organization(args.org).get_repos()
    remaining = repos.totalCount; page_num = 0
    matched = []
    while remaining > 0:
        # get next page
        page_results = repos.get_page(page_num)
        # check each repo in page
        for repo in page_results:
            print(f"Checking repo '{repo.name}'")
            if re.match(args.name_filter, repo.name) != None:
                if repo.created_at >= args.created_after and repo.created_at <= args.created_before:
                    matched.append(repo.name)
        # update indeces
        remaining -= len(page_results)
        page_num += 1
    # set output
    os.system(f"echo '::set-output name=REPOS::{','.join(matched)}'")

if __name__ == "__main__":
    main()
