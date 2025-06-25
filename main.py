from scraper import fetch_chapter
from ai_writer import spin_text
from chroma_store import save_version

original = fetch_chapter()
spun = spin_text(original)

# Optionally print and allow human input
print("Spun Text:\n", spun)

save_version(spun, "chapter1_v1")
print("Version saved successfully!")
