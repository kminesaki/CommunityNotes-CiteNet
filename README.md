# CommunityNotes-CiteNet
This repository contains the code in the following paper.

Minesaki, K.: Characterizing Cited Media in Community Notes: Fact-Checking Factuality, Partisan Bias, and Co-Citation Network Analysis.

## Research Question
### In what contect specific media are likely to be cited in Community Notes on X?
This paper consists of the three following analysis.

1.	Assessing and analysis of factuality of each source media based on the ratings of each Community Notes

2.	Assessing and analysis of biases of each source media based on the labels provided by natural language processing

3.	Analysis of the citation network of source media considering factuality and biases

## Material 
- [Community Notes data](https://communitynotes.x.com/guide/en/under-the-hood/download-data)

**Notes**
|Field|Description|Response values|
|---|---|---|
|summary|User-entered text, in response to the note writing prompt “Please explain the evidence behind your choices, to help others who see this tweet understand why it is not misleading”|User entered text explanation, with some characters escaped (e.g. tabs converted to spaces).|
|currentStatus|The current status of the note.|"NEEDS_MORE_RATINGS", "CURRENTLY_RATED_HELPFUL", "CURRENTLY_RATED_NOT_HELPFUL"|
|createdAtMillis|Time the note was created, in milliseconds since epoch (UTC).|——|

Reference: X Community Notes. (n.d.). Downloading data. https://communitynotes.x.com/guide/en/under-the-hood/download-data

**Filters**
|Field|Filters|
|---|---|
|createdAtMillis|Notes created between January 1st and December 31st in 2024|
|summary|Notes containing "Trump", "Biden", "Kamala" or "Harris"|
|currentStatus|Notes rated as "CURRENTLY_RATED_HELPFUL" or "CURRENTLY_RATED_NOT_HELPFUL"|

## File Description
