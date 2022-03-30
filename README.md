# Find Repos Action

This action will search an organization for repos that match a provided RegEx pattern.

# Usage
```yaml
- uses: PurdueECE/action-find-repos@v1.0
  id: get_repos
  with:
    # Org to search in
    org: PurdueECE364
    # Personal access token
    pat: ${{ secrets.GITHUB_TOKEN }}
    # Pattern to match against
    pattern: ^prelabs-.*$
    # Earliest creation date
    created_after: 2022-01-01T00:00:00
    # Latest creation date
    created_before: 2022-06-01T00:00:00
# Prints results - output parameters is 'repos'
- run: "echo results: ${{ steps.get_repos.outputs.repos }}"
```

# Testing
## Unit
Unit tests are in the `test-unit/` directory. They can be run with `pytest`.
## Integration
Integration test cases are in the `test-integration/` directory.
To test, you must install the [`act`](https://github.com/nektos/act) command line tool.
After install, run `make test`.