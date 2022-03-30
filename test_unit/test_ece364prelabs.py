import os
from main import main


def test_ece364sp22prelabs():
    main(
        ['PurdueECE364', '--name_filter', '^prelabs-.*$',
        '--pat', os.environ['GITHUB_TOKEN'],
        '--created_after', '2022-01-01T00:00:00', '--created_before', '2022-06-01T00:00:00'
        ]
    )