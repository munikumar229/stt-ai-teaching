.PHONY: all clean help html pdf list

# Find all .qmd files (excluding index.qmd)
SLIDES := $(filter-out index.qmd, $(wildcard *.qmd))
HTML_FILES := $(SLIDES:.qmd=.html)
PDF_FILES := $(SLIDES:.qmd=.pdf)

# Default target
all: html pdf index
	@echo "✓ All slides built successfully"

# Build all HTML slides
html: $(HTML_FILES)
	@echo "✓ HTML slides built"

# Generate index page
index:
	@./generate-index.sh

# Build all PDF documents
pdf: $(PDF_FILES)
	@echo "✓ PDF documents built"

# Pattern rule for HTML
%.html: %.qmd
	@echo "Building $< -> $@"
	@quarto render $< --to revealjs

# Pattern rule for PDF
%.pdf: %.qmd
	@echo "Building $< -> $@"
	@quarto render $< --to pdf

# Build specific slide by name (without extension)
%: %.qmd
	@echo "Building $<"
	@quarto render $< --to revealjs
	@quarto render $< --to pdf
	@echo "✓ Built $< (HTML + PDF)"

# List all available slides
list:
	@echo "Available slides:"
	@for file in $(SLIDES); do \
		echo "  - $${file%.qmd}"; \
	done
	@echo ""
	@echo "Usage:"
	@echo "  make all                  # Build all HTML and PDF"
	@echo "  make html                 # Build all HTML slides"
	@echo "  make pdf                  # Build all PDF documents"
	@echo "  make <name>               # Build specific slide (e.g., make data-collection-labeling)"
	@echo "  make clean                # Remove generated files"

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	@rm -f $(HTML_FILES) $(PDF_FILES) index.html
	@rm -rf *_files/
	@rm -f *.tex *.log *.aux
	@rm -rf .quarto/
	@echo "✓ Clean complete"

# Help
help: list
