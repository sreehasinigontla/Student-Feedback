
# Student Feedback Sentiment Scoring System

# Predefined positive keywords
positive_words = [
    "good", "excellent", "great", "amazing",
    "helpful", "wonderful", "satisfied",
    "best", "clear", "interesting"
]

# Predefined negative keywords
negative_words = [
    "bad", "poor", "worst", "boring",
    "difficult", "useless", "confusing",
    "disappointed", "unsatisfied", "slow"
]


# Function to classify sentiment
def classify_sentiment(score):

    if score >= 2:
        return "Positive"

    elif score <= -2:
        return "Negative"

    else:
        return "Neutral"


# Function to analyse feedback
def analyse_feedback(feedback):

    words = feedback.lower().split()

    positive_count = 0
    negative_count = 0

    positive_found = []
    negative_found = []

    for word in words:

        # Remove common punctuation
        word = word.strip(".,!?;:()[]{}\"'")

        if word in positive_words:
            positive_count += 1
            positive_found.append(word)

        elif word in negative_words:
            negative_count += 1
            negative_found.append(word)

    # Calculate sentiment score
    score = positive_count - negative_count

    # Determine sentiment
    sentiment = classify_sentiment(score)

    return (
        positive_count,
        negative_count,
        score,
        sentiment,
        positive_found,
        negative_found
    )


# Main Program
print("==========================================")
print("   STUDENT FEEDBACK SENTIMENT SCORING")
print("==========================================")

# Get number of feedback sentences
while True:

    try:
        n = int(input("\nEnter number of feedback sentences: "))

        if n > 0:
            break

        print("Enter at least one feedback sentence.")

    except ValueError:
        print("Please enter a valid whole number.")


feedback_list = []

total_positive = 0
total_negative = 0
total_score = 0

# Accept and analyse feedback
for i in range(n):

    print("\nEnter Feedback", i + 1, ":")

    feedback = input()

    result = analyse_feedback(feedback)

    positive_count = result[0]
    negative_count = result[1]
    score = result[2]
    sentiment = result[3]
    positive_found = result[4]
    negative_found = result[5]

    # Store feedback details
    feedback_data = {
        "feedback": feedback,
        "positive": positive_count,
        "negative": negative_count,
        "score": score,
        "sentiment": sentiment,
        "positive_words": positive_found,
        "negative_words": negative_found
    }

    feedback_list.append(feedback_data)

    total_positive += positive_count
    total_negative += negative_count
    total_score += score


# Display individual feedback reports
print("\n==========================================")
print("         INDIVIDUAL FEEDBACK REPORT")
print("==========================================")

for i in range(len(feedback_list)):

    data = feedback_list[i]

    print("\nFeedback", i + 1)
    print("Sentence:", data["feedback"])

    print("Positive Keywords:", data["positive_words"])
    print("Negative Keywords:", data["negative_words"])

    print("Positive Count:", data["positive"])
    print("Negative Count:", data["negative"])

    print("Sentiment Score:", data["score"])
    print("Classification:", data["sentiment"])


# Calculate overall sentiment
overall_sentiment = classify_sentiment(total_score)


# Display final summary
print("\n==========================================")
print("             FINAL SUMMARY")
print("==========================================")

print("Total Feedback:", n)
print("Total Positive Indicators:", total_positive)
print("Total Negative Indicators:", total_negative)
print("Overall Sentiment Score:", total_score)
print("Overall Classification:", overall_sentiment)

# Count sentiment categories
positive_feedback = 0
negative_feedback = 0
neutral_feedback = 0

for data in feedback_list:

    if data["sentiment"] == "Positive":
        positive_feedback += 1

    elif data["sentiment"] == "Negative":
        negative_feedback += 1

    else:
        neutral_feedback += 1


print("\nPositive Feedback:", positive_feedback)
print("Negative Feedback:", negative_feedback)
print("Neutral Feedback:", neutral_feedback)

print("\nFeedback Analysis Completed!")
