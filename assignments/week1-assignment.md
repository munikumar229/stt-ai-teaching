# Week 1 Assignment: Movie Recommendation Dataset Builder

**CS 203: Software Tools and Techniques for AI**
**Due**: End of Week 2
**Points**: 100

---

## Overview

You will build a comprehensive movie dataset collection system that gathers data from multiple sources, handles errors gracefully, and produces a clean dataset ready for machine learning. This assignment tests your ability to work with HTTP APIs, handle real-world data collection challenges, and write production-quality code.

---

## Learning Objectives

By completing this assignment, you will:
- Master HTTP APIs and web data collection
- Implement robust error handling and retry logic
- Work with multiple data sources and merge datasets
- Practice data cleaning and validation
- Write well-documented, maintainable code
- Create reproducible data pipelines

---

## Problem Statement

Netflix needs a dataset of movies to build a recommendation system. Your task is to collect comprehensive information about at least 200 movies from various sources, clean the data, and produce a high-quality dataset with the following features:

**Required Features** (minimum):
- Title
- Year of release
- Genre(s)
- IMDb rating
- Director
- Main actors (top 3)
- Plot summary
- Runtime
- Box office revenue (if available)

**Bonus Features** (for extra credit):
- Rotten Tomatoes score
- Production budget
- Awards won/nominated
- Number of user reviews
- Release date
- MPAA rating
- Language
- Country of production

---

## Part 1: Data Collection (60 points)

### Task 1.1: Single Source Collection (20 points)

Implement a movie data collector using the OMDb API.

**Requirements**:
- Use environment variables for API keys (never hardcode!)
- Implement proper error handling (network errors, invalid responses)
- Add request timeouts (10 seconds recommended)
- Handle rate limiting gracefully (exponential backoff)
- Collect data for at least 200 movies
- Save raw API responses for debugging

**Deliverables**:
- `collectors/omdb_collector.py` - Main collection script
- `.env.example` - Template for environment variables
- `data/raw/omdb_responses.json` - Raw API responses

**Grading Criteria**:
- Correct API usage (5 points)
- Proper error handling (5 points)
- Rate limit handling (5 points)
- Code quality and documentation (5 points)

---

### Task 1.2: Multi-Source Collection (25 points)

Extend your collector to gather data from at least TWO additional sources.

**Suggested Sources**:
1. **TMDb API** (The Movie Database)
   - More detailed movie information
   - Poster images, backdrops
   - User ratings and vote counts

2. **News API**
   - Recent news articles mentioning the movie
   - Can measure "buzz" for newer films

3. **Web Scraping** (IMDb or Rotten Tomatoes)
   - Practice web scraping techniques
   - Get data not available via API

**Requirements**:
- Implement separate collectors for each source
- Match movies across sources (use IMDb ID as key)
- Merge data intelligently (handle conflicts)
- Document which fields come from which source

**Deliverables**:
- `collectors/tmdb_collector.py` (or other sources)
- `collectors/data_merger.py` - Merge data from multiple sources
- `data/raw/` - Raw data from each source

**Grading Criteria**:
- Multiple source implementation (10 points)
- Correct data merging logic (8 points)
- Conflict resolution strategy (7 points)

---

### Task 1.3: Async Collection (15 points - Bonus)

Speed up data collection using asynchronous requests.

**Requirements**:
- Use `httpx` or `aiohttp` for async HTTP requests
- Collect data for 200 movies in under 60 seconds
- Maintain same error handling as synchronous version
- Document performance improvement

**Deliverables**:
- `collectors/async_collector.py`
- Performance comparison report in README

**Grading Criteria**:
- Correct async implementation (8 points)
- Performance improvement (4 points)
- Maintained error handling (3 points)

---

## Part 2: Data Processing (25 points)

### Task 2.1: Data Cleaning (15 points)

Clean and normalize the collected data.

**Requirements**:
- Handle missing values (document your strategy)
- Normalize inconsistent formats:
  - Dates (convert to YYYY-MM-DD)
  - Numbers (remove $ and commas from revenue)
  - Genres (split comma-separated into lists)
- Remove duplicate movies
- Validate data types (year should be integer, rating should be float)
- Handle "N/A" and null values appropriately

**Deliverables**:
- `processors/data_cleaner.py`
- Documentation of cleaning decisions

**Grading Criteria**:
- Handling missing values (5 points)
- Format normalization (5 points)
- Duplicate detection (5 points)

---

### Task 2.2: Data Validation (10 points)

Implement validation rules to ensure data quality.

**Validation Rules**:
- Year: between 1900 and current year
- Rating: between 0 and 10 (IMDb scale)
- Runtime: positive integer
- Genre: non-empty list
- Budget/Revenue: positive numbers or null

**Requirements**:
- Create validation functions for each field
- Generate a validation report:
  - Number of invalid records
  - Types of validation failures
  - Percentage of valid records
- Decide whether to fix, flag, or remove invalid data

**Deliverables**:
- `processors/data_validator.py`
- `reports/validation_report.txt`

**Grading Criteria**:
- Validation rules implementation (5 points)
- Validation report (3 points)
- Handling invalid data (2 points)

---

## Part 3: Analysis and Documentation (15 points)

### Task 3.1: Exploratory Data Analysis (10 points)

Analyze the collected dataset and generate insights.

**Required Visualizations**:
1. Distribution of genres (bar chart)
2. Rating distribution (histogram)
3. Movies per year (line chart)
4. Top 10 directors by movie count
5. Box office distribution (log scale recommended)

**Required Statistics**:
- Total movies collected
- Average rating
- Most common genre
- Year range
- Percentage of complete records (all features present)

**Deliverables**:
- `analysis/eda.py` - Analysis script
- `reports/eda_report.pdf` - Generated report with visualizations

**Grading Criteria**:
- Visualizations quality (5 points)
- Statistical summary (3 points)
- Insights and interpretation (2 points)

---

### Task 3.2: Documentation (5 points)

Write comprehensive documentation.

**README.md must include**:
- Project overview and goals
- Installation instructions
- How to obtain API keys
- How to run the collectors
- How to reproduce the dataset
- Data schema (field descriptions)
- Data sources and attribution
- Known limitations
- Future improvements

**Code Documentation**:
- Docstrings for all functions
- Inline comments for complex logic
- Type hints for function parameters

**Deliverables**:
- `README.md`
- Well-documented code

**Grading Criteria**:
- README completeness (3 points)
- Code documentation (2 points)

---

## Project Structure

Your submission should follow this structure:

```
week1-assignment/
├── README.md
├── .env.example
├── .gitignore
├── requirements.txt
├── collectors/
│   ├── __init__.py
│   ├── omdb_collector.py
│   ├── tmdb_collector.py
│   └── data_merger.py
├── processors/
│   ├── __init__.py
│   ├── data_cleaner.py
│   └── data_validator.py
├── analysis/
│   ├── __init__.py
│   └── eda.py
├── data/
│   ├── raw/                    # Raw API responses
│   ├── processed/              # Cleaned data
│   └── final/                  # Final dataset
│       └── movies.csv
├── reports/
│   ├── validation_report.txt
│   └── eda_report.pdf
└── tests/                      # Optional but recommended
    ├── test_collectors.py
    └── test_processors.py
```

---

## Submission Guidelines

### What to Submit

1. **Code**: ZIP file or GitHub repository link
2. **Data**: Final `movies.csv` (at least 200 movies)
3. **Reports**: Validation and EDA reports
4. **README**: Complete documentation

### Submission Checklist

- [ ] All required files included
- [ ] Code runs without errors
- [ ] API keys NOT in code (use .env)
- [ ] .env added to .gitignore
- [ ] requirements.txt includes all dependencies
- [ ] README has clear installation/run instructions
- [ ] At least 200 movies in final dataset
- [ ] Data validation report generated
- [ ] EDA report with visualizations
- [ ] Code is well-documented

### How to Submit

Upload to Moodle as:
- **Option 1**: ZIP file (< 50MB, exclude data/raw if too large)
- **Option 2**: GitHub repository link (make sure it's public or add instructor as collaborator)

### Late Submission Policy

- -10% per day late
- Maximum 3 days late accepted
- After 3 days: 0 points

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| **Single Source Collection** | 20 | API usage, error handling, rate limits |
| **Multi-Source Collection** | 25 | Multiple sources, merging, conflicts |
| **Data Cleaning** | 15 | Missing values, normalization, duplicates |
| **Data Validation** | 10 | Rules, report, invalid data handling |
| **EDA** | 10 | Visualizations, statistics, insights |
| **Documentation** | 5 | README, code docs |
| **Code Quality** | 10 | Style, structure, best practices |
| **Dataset Quality** | 5 | Completeness, accuracy |
| **Total** | 100 | |
| **Bonus (Async)** | +15 | Optional extra credit |

---

## Code Quality Standards

Your code will be evaluated on:

**Functionality** (40%)
- Meets all requirements
- Handles edge cases
- Produces correct output

**Code Organization** (20%)
- Logical file/folder structure
- Modular functions
- Separation of concerns

**Error Handling** (15%)
- Try-except blocks where appropriate
- Meaningful error messages
- Graceful degradation

**Documentation** (15%)
- Clear docstrings
- Helpful comments
- Complete README

**Style** (10%)
- PEP 8 compliance
- Consistent naming
- Readable code

---

## Common Pitfalls to Avoid

1. **Hardcoded API Keys**: Always use environment variables
2. **No Error Handling**: Network requests can fail - handle it!
3. **Ignoring Rate Limits**: Respect API limits or you'll be blocked
4. **Poor Documentation**: Others (including future you) need to understand your code
5. **Not Testing Edge Cases**: What if API returns unexpected data?
6. **Committing Large Files**: Don't commit raw data to Git
7. **Incomplete Data**: Missing critical fields reduces dataset quality
8. **No Data Validation**: Garbage in = garbage out

---

## Tips for Success

**Start Early**
- Data collection takes time
- API rate limits may slow you down
- Debugging network issues is time-consuming

**Test Incrementally**
- Start with 5-10 movies
- Scale up after confirming code works
- Don't wait until the end to test

**Handle Failures Gracefully**
- Not every movie will have all fields
- Some API calls will fail
- Design for failure, not just success

**Keep Raw Data**
- Save raw API responses
- You can reprocess without re-fetching
- Helps debugging

**Version Control**
- Commit frequently
- Write meaningful commit messages
- Use .gitignore properly

**Ask for Help**
- Post on discussion forum
- Attend TA office hours
- Form study groups

---

## Resources

**APIs**:
- OMDb: http://www.omdbapi.com/
- TMDb: https://www.themoviedb.org/documentation/api
- News API: https://newsapi.org/

**Documentation**:
- requests: https://requests.readthedocs.io/
- httpx: https://www.python-httpx.org/
- pandas: https://pandas.pydata.org/
- python-dotenv: https://pypi.org/project/python-dotenv/

**Tools**:
- curl: Test APIs from command line
- jq: Format JSON output
- Postman: API testing GUI

**Python Style**:
- PEP 8: https://pep8.org/
- Google Python Style Guide: https://google.github.io/styleguide/pyguide.html

---

## Academic Integrity

- You may discuss approaches with classmates
- You may use online resources and documentation
- You must write your own code
- You must cite any code snippets from external sources
- Sharing complete solutions is prohibited
- Using someone else's code is plagiarism

**Plagiarism will result in zero points and academic misconduct report.**

---

## Getting Help

**Discussion Forum**: Post questions (no code answers!)
**Office Hours**: TAs available (schedule on Moodle)
**Email**: For private/urgent questions only

**Good questions**:
- "My API call returns 401, what does this mean?"
- "How should I handle movies with no box office data?"
- "Is it okay to skip movies if the API returns an error?"

**Bad questions**:
- "Can you write the error handling code for me?"
- "What's wrong with my code?" (without showing effort to debug)

---

## Extension Ideas (Optional)

If you finish early and want to go further:

1. **Add more data sources** (Wikipedia, fan sites)
2. **Collect poster images** (computer vision features)
3. **Build a simple web interface** (Flask/FastAPI)
4. **Add caching** (avoid redundant API calls)
5. **Implement resume capability** (continue from where you left off)
6. **Add logging** (track collection progress)
7. **Create unit tests** (pytest)
8. **Build a data pipeline** (automated collection)

---

## FAQ

**Q: How do I choose which 200 movies?**
A: Use IMDb's Top 250, or recent releases, or a specific genre. Document your selection criteria.

**Q: What if an API is down?**
A: Implement retry logic and fallbacks. If persistent, contact instructor.

**Q: Can I use web scraping instead of APIs?**
A: APIs are preferred. Scraping is allowed as additional source only.

**Q: How do I handle movies in the dataset with different titles?**
A: Use IMDb ID as the primary key for matching across sources.

**Q: What if I can't get 200 movies due to API limits?**
A: Use free tier limits wisely, or email instructor for higher limit key.

**Q: Can I work in pairs?**
A: No, this is an individual assignment.

**Q: Can I use ChatGPT/Claude?**
A: You may use AI for understanding concepts and debugging. You must understand and be able to explain all code you submit.

---

**Good luck! Remember: Real data science is messy. Embrace the challenge!**
