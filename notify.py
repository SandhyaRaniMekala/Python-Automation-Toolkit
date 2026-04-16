import os
title = "Hey! Cutie, Health Alert!"
message = "Drink a glass of water now. Stay hydrated while coding!"
os.system(f"osascript -e 'display notification \"{message}\"with title\"{title}\"'")