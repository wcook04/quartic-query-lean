.PHONY: check check-index

check:
	python3 tools/check_repository.py
	python3 tools/build_challenges.py --check
	python3 tools/build_corpus.py --check
	python3 -m unittest discover -s tests -p 'test_*.py'

check-index:
	python3 tools/check_repository.py --index
