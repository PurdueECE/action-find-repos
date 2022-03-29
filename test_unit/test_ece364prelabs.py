from main import main


def test_ece364sp22prelabs():
    main(org='PurdueECE364', name_filter='^prelabs-.*$', created_after= '2022-01-01T00:00:00', created_before= '2022-06-01T00:00:00')