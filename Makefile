.PHONY: check check-layout check-generated check-tests check-index

check:
	$(MAKE) check-layout
	$(MAKE) check-generated
	$(MAKE) check-tests

check-layout:
	python3 tools/check_repository.py

check-generated:
	python3 tools/build_challenges.py --check
	python3 tools/build_corpus.py --check
	python3 tools/build_comparator_map.py --check
	python3 tools/build_lean_links.py --check

check-tests:
	python3 -m unittest discover -s tests -p 'test_*.py'

check-index:
	python3 tools/check_repository.py --index
