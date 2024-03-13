CODE_DIRS=core users

format:
	isort $(CODE_DIRS)
	black $(CODE_DIRS)