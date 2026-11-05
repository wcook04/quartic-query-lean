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
	python3 tools/build_reading_api.py --check

check-tests:
	python3 -m unittest discover -s tests -p 'test_*.py'

check-index:
	python3 tools/check_repository.py --index

.PHONY: reading-api
reading-api: check-generated
	python3 tools/build_reading_api.py --output build/reading-api/v1

.PHONY: reading-web
reading-web: check-generated
	python3 tools/build_reading_api.py --web-manuscripts --output build/reading-api/v1
