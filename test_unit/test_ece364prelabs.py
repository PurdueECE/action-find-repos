import os
from main import main
from unittest import mock

@mock.patch.dict(os.environ, {
    "INPUT_ORG": "PurdueECE364",
    "INPUT_PATTERN": '^prelabs-.*$',
    "INPUT_CREATED_AFTER": "2022-01-01T00:00:00",
    "INPUT_CREATED_BEFORE": "2022-06-01T00:00:00"
    })
def test_ece364sp22prelabs():
    main()