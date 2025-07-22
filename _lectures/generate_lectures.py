import pandas


df = pandas.read_csv("lectures.csv")

for i, row in df.iterrows():
    base = f"""---
type: lecture
date: {row['date']}
title: "{row['lecture']}"
lecture_type: {row['lecture_type']}
thumbnail: /static_files/presentations/lec.jpg
"""

    base += "links:\n"
    if isinstance(row["slides"], str):
        base += f"- url: {row['slides']}\n  name: slides\n"

    if isinstance(row["notebooks"], str):
        base += f"- url: {row['notebooks']}\n  name: notebook\n"

    # need a newline
    base += "hide_from_announcments: true\n---"
    
    if isinstance(row["notes"], str):
        base += f"\n\n{row['notes']}"
    
    with open(f"{i}_lecture.md", "w") as log:
        log.write(base)
