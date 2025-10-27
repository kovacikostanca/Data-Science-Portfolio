
# Email Spam Classifier using Bayes' Theorem

A machine learning project that classifies emails as spam or not spam based on the presence of three keywords: **WIN**, **FREE**, and **OFFER**.

## Overview

This project implements a Naive Bayes classifier from scratch to identify spam emails. The classifier uses Bayes' Theorem and assumes that the occurrence of keywords are independent events.

### Mathematical Foundation

The classifier is based on the principle that for independent events A and B:

```
P(A ∩ B) = P(A) × P(B)
```

For example:
```
P(WIN ∩ FREE | Spam) = P(WIN | Spam) × P(FREE | Spam)
```

## Dataset

The project uses a dataset of 18 emails with the following features:
- Email text content
- Presence of keyword "WIN" (Yes/No)
- Presence of keyword "FREE" (Yes/No)
- Presence of keyword "OFFER" (Yes/No)
- Classification (Spam/Not Spam)

### Dataset Statistics

- **Total emails**: 18
- **Spam emails**: 8 (44%)
- **Not Spam emails**: 10 (56%)

## Requirements

```
pandas
openpyxl (for reading Excel files)
jupyter notebook (for running the notebook)
```

Install dependencies:
```bash
pip install pandas openpyxl jupyter
```

## Project Structure

```
.
├── Email_Spam_Classifier.ipynb    # Main Jupyter notebook
├── email_spam_nospam.xlsx         # Dataset file
└── README.md                       # This file
```

## Usage

1. **Clone or download the project files**

2. **Ensure the dataset file `email_spam_nospam.xlsx` is in the same directory**

3. **Open the Jupyter notebook**:
   ```bash
   jupyter notebook Email_Spam_Classifier.ipynb
   ```

4. **Run all cells sequentially**

## How It Works

### 1. Data Preprocessing
- Load the dataset from Excel
- Convert categorical values (Yes/No, Spam/Not Spam) to binary (1/0)

### 2. Calculate Prior Probabilities
```python
P(Spam) = 0.44
P(Not Spam) = 0.56
```

### 3. Calculate Conditional Probabilities

| Keyword | P(Keyword \| Spam) | P(Keyword \| Not Spam) |
|---------|-------------------|----------------------|
| WIN     | 0.50              | 0.20                 |
| FREE    | 0.88              | 0.20                 |
| OFFER   | 0.25              | 0.70                 |

### 4. Apply Bayes' Theorem

For a new email with features (WIN, FREE, OFFER):

```
P(Spam | Features) = P(Features | Spam) × P(Spam) / P(Features)
```

Where:
```
P(Features | Spam) = P(WIN | Spam) × P(FREE | Spam) × P(OFFER | Spam)
```

The email is classified as **Spam** if `P(Spam | Features) ≥ 0.5`

## Example Results

| Email | WIN | FREE | OFFER | Prediction | P(Spam) |
|-------|-----|------|-------|------------|---------|
| WIN a FREE trip! | 1 | 1 | 0 | Spam | 0.96 |
| Exclusive OFFER for you! | 0 | 0 | 1 | Not Spam | 0.03 |
| WIN big with this special OFFER! | 1 | 0 | 1 | Not Spam | 0.10 |
| Get your FREE OFFER now! | 0 | 1 | 1 | Not Spam | 0.44 |
| WIN a FREE prize with our OFFER! | 1 | 1 | 1 | Spam | 0.76 |

## Key Findings

- Emails containing both **WIN** and **FREE** are highly likely to be spam (96% probability)
- Emails with only **OFFER** are usually not spam (97% not spam)
- The combination of all three keywords still indicates spam (76% probability)

## Functions

### `conditional_prob(word, spam)`
Calculates the conditional probability of a word appearing in spam or not spam emails.

### `bayes_classifier(win, free, offer)`
Classifies an email as spam or not spam based on the presence of keywords.

**Parameters:**
- `win` (int): 1 if WIN is present, 0 otherwise
- `free` (int): 1 if FREE is present, 0 otherwise
- `offer` (int): 1 if OFFER is present, 0 otherwise

**Returns:**
- Classification label ("Spam" or "Not Spam")
- Probability of being spam

## Limitations

- Assumes keyword independence (which may not always be true in practice)
- Limited to three keywords
- Small dataset (18 emails)
- Does not account for context or word combinations

## Future Improvements

- Expand keyword list
- Increase dataset size
- Implement Laplace smoothing to handle zero probabilities
- Add cross-validation
- Consider word frequency instead of just presence/absence
- Implement n-gram analysis

## License

This project is for educational purposes.

## Author

Machine Learning and Probability Classification Project

## Acknowledgments

- Based on Naive Bayes classification algorithm
- Implements Bayes' Theorem for probabilistic classification
