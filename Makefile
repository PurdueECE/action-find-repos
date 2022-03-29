FLAGS = -r --secret-file .env
ACT = act $(FLAGS)

test_ece364prelabs:
	$(ACT) -W test_integration/test_ece364prelabs.yml

test: test_ece364prelabs