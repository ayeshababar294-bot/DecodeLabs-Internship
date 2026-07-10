# AI Recommendation System

items = {
    "Python Programming": ["programming", "python", "coding", "technology"],
    "Machine Learning": ["ai", "machine learning", "technology", "data"],
    "Web Development": ["html", "css", "javascript", "web"],
    "Graphic Design": ["design", "photoshop", "art"],
    "Photography": ["camera", "editing", "art"],
    "Football": ["sports", "football", "fitness"],
    "Cricket": ["sports", "cricket", "fitness"],
    "Cooking": ["food", "cooking", "recipe"],
    "Music": ["music", "songs", "instruments"],
    "Gaming": ["games", "gaming", "technology"]
}

print("=" * 45)
print("      AI Recommendation System")
print("=" * 45)

user_input = input("Enter your interests (comma separated): ").lower()

user_interests = [interest.strip() for interest in user_input.split(",")]

recommendations = []

for item, tags in items.items():
    score = 0
    for interest in user_interests:
        if interest in tags:
            score += 1

    if score > 0:
        recommendations.append((item, score))

recommendations.sort(key=lambda x: x[1], reverse=True)

print("\nRecommended Items:\n")

if recommendations:
    for item, score in recommendations:
        print(f"{item}  --> Similarity Score: {score}")
else:
    print("No recommendations found.")