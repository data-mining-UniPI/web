import pandas


df = pandas.read_csv("events.csv")

for i, row in df.iterrows():
    base = f"""---
type: {row['event_type']}
date: {row['date']}
description: "{row['name']}"
"""

    base += "links:\n"
    if isinstance(row["link"], str):
        base += f"- url: {row['link']}\n  name: folder\n"

    # need a newline
    base += f"hide_from_announcments: {'true' if row["hide"] else 'false'}\n---"

    
    if isinstance(row["notes"], str):
        base += f"\n\n{row['notes']}"
    
    with open(f"{i}_event.md", "w") as log:
        log.write(base)
