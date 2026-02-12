START_DATE=2026-02-11

update:
	@echo "Generating README..."

	@DAY=$$(expr $$(($$(date +%s) - $$(date -d $(START_DATE) +%s))) / 86400 + 1); \
	DATE=$$(date +%m/%d/%Y); \
	sed -e "s/{{DAY}}/$$DAY/g" \
	    -e "s/{{DATE}}/$$DATE/g" \
	    -e "s/{{STREAK}}/Active/g" \
	    README.template.md > README.md

	@echo "README updated."
