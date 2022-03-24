# pylint Action

This action will run pylint in the specified directory.

# Usage
```yaml
- uses: PurdueECE/action-pylint@v1.2
  with:
    # Path to be linted
    # Default: .
    path: ''
```

# Testing
Test cases are contained in the `test/` directory.
To test, you must install the [`act`](https://github.com/nektos/act) command line tool.
After install, run `make test`.