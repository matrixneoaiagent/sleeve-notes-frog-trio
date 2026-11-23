# Sleeve Notes for the Frog Trio entry.
import os


def main():
    os.makedirs('/output', exist_ok=True)
    entry = """Live at the Cistern
Two sets, one mic, a lot of echo and no setlist. The piano is out of tune in a way that suits the material. They take requests and then play something else. When the crowd thins out they get better, which is either integrity or habit."""
    with open('/output/entry.txt', 'w', encoding='utf-8') as f:
        f.write(entry)


if __name__ == "__main__":
    main()
