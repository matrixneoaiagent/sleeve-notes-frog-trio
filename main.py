# Sleeve Notes — Wexler Street reissue hedge.
import os

# Content from ENTRY.txt
text = """The Wexler Street Sessions, 1961
The tapes sat in a garage for thirty years. What survives is rough: one channel drops on the third tune, the leader's mute is cracked, and the drummer counts in from somewhere off-mic. The label fixed the speed, left the mistakes. First time on vinyl since the original run of two hundred."""

output_dir = "/output"
output_path = os.path.join(output_dir, "entry.txt")

os.makedirs(output_dir, exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)
