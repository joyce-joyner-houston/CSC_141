def sent_messages(messages):
    sent_messages = []
    for message in messages:
        print(message)
        sent_messages.append(message)
    return sent_messages

messages = ["Hey, how's it going?",
            "What are you doing right now?",
            "That's great, can't wait to see you",
            "See ya later"
            ]

messages_copy = messages.copy()

sent_messages = sent_messages(messages_copy)

print("\nOriginal Messages:")
print(messages)
print("\nSent Messages:")
print(sent_messages)

