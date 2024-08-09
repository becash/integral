SHELL := /bin/bash
NO_COLOR=$(shell echo -e "\033[0m")
OK_COLOR=$(shell echo -e "\033[32;01m")
ERROR_COLOR=$(shell echo -e "\033[31;01m")
WARN_COLOR=$(shell echo -e "\033[33;01m")
format:
	@echo "$(OK_COLOR)==> Formatting$(NO_COLOR)"
	@black -l 120 ./

static-check:
	@echo "$(OK_COLOR)==> Running static check$(NO_COLOR)"
	@pyright ./

lint:
	@echo "$(OK_COLOR)==> Linting$(NO_COLOR)"
	@black --check  -l 120 ./
