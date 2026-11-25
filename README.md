# Student-Feedback
# 😊 Student Feedback Sentiment Scoring System

## 📌 Project Overview

The **Student Feedback Sentiment Scoring System** is a Python-based application designed to analyse multiple student feedback sentences using predefined positive and negative keywords.

The system counts positive and negative indicators, calculates sentiment scores, and classifies feedback into three categories: Positive, Negative, and Neutral.

It also generates an overall sentiment summary to understand students' opinions and satisfaction levels.

## 🎯 Objectives

- Analyse multiple student feedback sentences.
- Identify positive sentiment keywords.
- Identify negative sentiment keywords.
- Count positive and negative indicators.
- Calculate sentiment scores.
- Classify feedback into sentiment categories.
- Calculate overall feedback sentiment.
- Generate a final sentiment analysis report.

## 📋 Sentiment Keyword Lists

### Positive Keywords

- Good
- Excellent
- Great
- Amazing
- Helpful
- Wonderful
- Satisfied
- Best
- Clear
- Interesting

### Negative Keywords

- Bad
- Poor
- Worst
- Boring
- Difficult
- Useless
- Confusing
- Disappointed
- Unsatisfied
- Slow

## 🧮 Sentiment Scoring Rules

The sentiment score is calculated using the following formula:

```text
Sentiment Score =
Positive Count - Negative Count
```

### Classification Thresholds

| Sentiment Score | Classification |
|---|---|
| Score ≥ 2 | Positive |
| Score between -1 and 1 | Neutral |
| Score ≤ -2 | Negative |

## 🚀 Features

1. Multiple feedback sentence input.
2. Positive keyword identification.
3. Negative keyword identification.
4. Positive indicator counting.
5. Negative indicator counting.
6. Automatic sentiment score calculation.
7. Positive, Negative, and Neutral classification.
8. Overall sentiment calculation.
9. Feedback summary generation.

## 💻 Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub

## 🐍 Python Concepts Used

- Variables and Data Types
- Strings
- Lists
- Dictionaries
- Conditional Statements
- For Loops
- While Loops
- Functions
- String Methods
- Arithmetic Operators
- User Input and Output

## 📁 Project Structure

```text
Student-Feedback-Sentiment-Scoring/
│
├── sentiment_scoring.py
├── README.md
├── problem_statement.txt
├── objectives.txt
├── assumptions.txt
├── algorithm.txt
├── pseudocode.txt
├── flowchart.png
├── test_cases.txt
│
└── output_screenshots/
    ├── output1.png
    ├── output2.png
    └── output3.png
```

## ▶️ How to Run the Project

**Step 1:** Install Python 3 on your computer.

**Step 2:** Download or clone the GitHub repository.

**Step 3:** Open the project folder in Visual Studio Code.

**Step 4:** Open the terminal.

**Step 5:** Run the following command:

```bash
python sentiment_scoring.py
```

**Step 6:** Enter the number of feedback sentences.

**Step 7:** Enter the student feedback sentences.

**Step 8:** View individual sentiment reports and the overall summary.

## 🧪 Test Cases

| Test Case | Feedback | Expected Result |
|---|---|---|
| TC01 | The teaching is excellent and helpful | Positive |
| TC02 | The class is bad and boring | Negative |
| TC03 | The classroom is available | Neutral |
| TC04 | The explanation is good and clear | Positive |
| TC05 | The lecture is confusing and difficult | Negative |
| TC06 | The teacher is amazing and wonderful | Positive |
| TC07 | The subject is interesting but difficult | Neutral |

## 📊 Expected Output

The program displays:

- Original feedback sentence.
- Identified positive keywords.
- Identified negative keywords.
- Positive keyword count.
- Negative keyword count.
- Individual sentiment score.
- Sentiment classification.
- Total positive indicators.
- Total negative indicators.
- Overall sentiment score.
- Overall sentiment classification.
- Number of positive, negative, and neutral feedback sentences.

## ⚠️ Limitations

- The system uses predefined keywords.
- It does not understand the full meaning or context of sentences.
- It does not automatically detect negation, sarcasm, or complex expressions.
- New keywords must be manually added to the keyword lists.

## 📝 Conclusion

The Student Feedback Sentiment Scoring System provides a simple method for analysing student feedback using Python.

It identifies positive and negative indicators, calculates sentiment scores, and classifies feedback into Positive, Negative, and Neutral categories.

The project demonstrates the practical application of Python lists, dictionaries, functions, loops, conditional statements, and string operations in a real-world feedback analysis system.

---

**Project Name:** Student Feedback Sentiment Scoring System

**Subject:** Python Activity-Based Learning

**Programming Language:** Python 3

**Project Type:** Case Study
name:sree hasini
section:5 
