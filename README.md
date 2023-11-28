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

main.py: the entrypoint that grabs data from google sheet and start the sorting

rag.ipynb: redis example for the github details fetching

candiate.py: Class that holds data for candidate and will hold comparator

parser.py: uses Mathpix api to turn resume into markdown

```bash
wget https://hackgtstoragebucket.s3.amazonaws.com/service_creds.json && wget https://hackgtstoragebucket.s3.amazonaws.com/.env

```
