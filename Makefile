.PHONY: me laugh help

me: ## Main task for running the game
	@python3 ./

laugh: ## Cleans all artifacts
	@rm -rf __pycache__/

help: ## Show this help
	@grep -Eh '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
