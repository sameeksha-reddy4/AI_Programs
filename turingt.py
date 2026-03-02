import random

#chatbot responses
responses = {
    "hello": ["Hi! How are you?", "Hello! Nice to meet you.", "Hey there!"],
    "how are you": ["I'm doing well, thanks for asking!", 
                    "Pretty good today. How about you?", 
                    "All good here!"],
    "name": ["I'm Alex, nice to meet you.", 
             "You can call me Sam.", 
             "I don't really have a fixed name."],
    "ai": ["AI is fascinating, isn't it?", 
           "Yes, artificial intelligence is everywhere now.", 
           "AI can do many interesting things."],
    "default": [
        "That's interesting.",
        "Tell me more about that.",
        "I see. Go on.",
        "Why do you say that?"
    ]
}

def chatbot_reply(user_input):
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return random.choice(responses["default"])


generic_phrases = [
    "that's interesting",
    "tell me more",
    "i see",
    "why do you say that"
]

def evaluate_human_like(reply, previous_replies):
    score = 0
    r = reply.lower()

    if any(p in r for p in generic_phrases):
        score -= 2
    else:
        score += 2

    if reply in previous_replies:
        score -= 2
    else:
        score += 1

    if 4 <= len(reply.split()) <= 15:
        score += 1

    if " i " in f" {r} " or "my" in r:
        score += 1

    return score


print("Turing Test Simulation — Chat for 5 messages\n")

previous_replies = []
total_score = 0

for i in range(5):
    user = input("Judge: ")
    reply = chatbot_reply(user)
    print("Entity:", reply)

    total_score += evaluate_human_like(reply, previous_replies)
    previous_replies.append(reply)


if total_score >= 6:
    print("\nResult: Entity appears HUMAN")
else:
    print("\nResult: Entity appears MACHINE")