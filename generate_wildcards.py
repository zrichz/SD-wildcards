import json
import os

out_dir = "wildcards"
pantry_file = "nsp_pantry.json"


def check_dir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)


def write_to_file(filename, text, o):
    if o:
        filename = os.path.join(out_dir, filename)
    else:
        filename = filename
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    f.close()


def main():
    check_dir(out_dir)

    with open(pantry_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    data = {k: v for k, v in sorted(data.items(), key=lambda item: len(item[1]), reverse=True)}

    status_text = ""
    print("Generating text files...")
    for key in data:
        status_text += f"{key}: {len(data[key])} items\n"

        key_text = ""
        for item in data[key]:
            key_text += f"{item}\n"

        write_to_file(f"{key}.txt", key_text, True)

    write_to_file("status.txt", status_text, False)


if __name__ == "__main__":
    main()
