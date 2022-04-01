FLAGS = --verbose
ACT = act $(FLAGS)

test_ece364prelabs:
	$(ACT) -W test_integration/test_ece364prelabs.yml

test_firebase:
	$(ACT) -W test_integration/test_firebase.yml

test: test_ece364prelabs test_firebase