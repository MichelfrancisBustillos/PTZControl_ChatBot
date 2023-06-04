import pytchat

videoID = ""
message = ""

chat = pytchat.create(video_id=videoID)
while chat.is_alive():
    try:
        for c in chat.get().sync_items():
            print(f"{c.datetime} [{c.author.name}]- {c.message}")
            message = c.message
    except AttributeError:
        print("Error occurred. Restarting...")
        chat = pytchat.create(video_id=videoID)
    