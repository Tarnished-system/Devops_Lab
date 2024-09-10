print("Find sem 4 gpa")
subjects = ["Math", "DBMS", "IIME", "ADA", "FinMgmt", "UHV", "Minipro", "Adalab"]

scores = []

print("Please enter the scores for the following subjects:")

for subject in subjects:
    score = float(input(f"{subject}: "))
    scores.append(score)

average_score = sum(scores) / len(scores)

print("\nScores entered:")
for subject, score in zip(subjects, scores):
    print(f"{subject}: {score}")

print(f"\nAverage Score: {average_score:.2f}")
scores[0] *= 3
scores[1] *= 4
scores[2] *= 4
scores[3] *= 3
scores[4] *= 3
scores[5] *= 1
scores[6] *= 1 
scores[7] *= 1

sgpa = float(sum(scores)/20)
