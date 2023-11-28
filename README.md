# cs3300-project-2

## Release Notes

**Version 1.1**  
_Release Date: 28 November_

### New Software Features for this Release

- Automated data retrieval from Google Sheets for efficient candidate data management.
- Resume parsing using Mathpix API for detailed candidate evaluation.
- GitHub profile analysis to assess candidates' coding contributions.
- Candidate comparison and ranking using advanced AI algorithms.
- Integration of sorting results back into Google Sheets for streamlined review.

# cs3300-project-2 README

## Bug Fixes Made Since the Last Release

- **API Key Exposure Fix**: Removed hardcoded API keys from the script, ensuring secure and environment-based key management.
- **Error Handling in API Calls**: Enhanced error handling in API requests to prevent crashes due to network issues or invalid responses.
- **Improved XML Parsing**: Fixed bugs in XML parsing logic to handle unexpected or malformed content more gracefully.
- **Function Call Handling**: Resolved issues in the function call mechanism within the `openai.ChatCompletion.create` method, ensuring proper execution of custom functions.
- **Retries Logic Optimization**: Optimized the retry logic in `compare_resumes` to handle exceptions more effectively and reduce unnecessary retries.
- **Scoring System Adjustment**: Corrected the scoring algorithm in `compute_scores` to accurately reflect comparative results between candidates.
- **File Reading Error**: Fixed an issue where the system would fail to read the `rubric.txt` file due to incorrect file path handling.

## Known Bugs and Defects

- **Inconsistent Response Parsing**: Occasional issues in parsing responses from the LLM, leading to inconsistent candidate comparisons.
- **Latency in Data Retrieval**: Slower performance observed when fetching large amounts of data from Google Sheets.
- **Rubric Flexibility**: The current rubric implementation lacks flexibility and may not cater to varied evaluation criteria.
- **Limited Error Reporting**: Insufficient error reporting and debugging information for failed API requests.
- **UI Integration Incomplete**: The backend logic for candidate evaluation is not fully integrated with a front-end interface for user interaction.

## Missing Functionality

- **Real-time Updates**: The system does not currently support real-time updates from Google Sheets, requiring manual triggering of data retrieval.
- **Automated Testing Integration**: Automated unit and integration tests for the system are yet to be implemented.


## Install Guide

### Pre-requisites

- Operating System: Windows 10 or newer, MacOS, Linux.
- Python version 3.11 or newer.
- Access to Google Sheets API and Mathpix API.

main.py: the entrypoint that grabs data from google sheet and start the sorting

rag.ipynb: redis example for the github details fetching

candiate.py: Class that holds data for candidate and will hold comparator

parser.py: uses Mathpix api to turn resume into markdown

```bash
wget https://hackgtstoragebucket.s3.amazonaws.com/service_creds.json && wget https://hackgtstoragebucket.s3.amazonaws.com/.env

```
