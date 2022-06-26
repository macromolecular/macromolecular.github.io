import sys
import pathlib as pl
import pandas as pd

def known_author(author):

    author = author.lower()

    if 'pearce' in author:
        return True

    return False

template = """---
title: "{title}"
authors: "{authors}"
journal: "{journal}"
pub_date: "{pub_date}"
journal_link: ""
download_link: ""
---
"""

o_dir = pl.Path('citations')
if not o_dir.exists():
    o_dir.mkdir()

p_template = '{year}{letter}_{author}.markdown'

df = pd.read_csv(sys.argv[1])

for e in df.itertuples():

    print(e)

    f_authors = [
        '**'+a.strip()+'**'
        if known_author(a)
        else a.strip()
        for a in e.Authors.split(';')
    ]

    f = template.format(
        title = e.Title,
        authors = '; '.join(f_authors),
        journal = e.Publication,
        pub_date = e.Year,
        )

    f_author = e.Authors.split(';')[0].split(',')[0].replace('.','').replace(' ','-')

    for i in range(1,27):

        p_base = p_template.format(
            year = int(e.Year),
            author = f_author,
            letter = chr(ord('@')+i).lower(),
            )

        p = (o_dir / p_base)

        if not p.exists():
            break

    with open(str(p), 'w') as fh:
        fh.write(
            f
        )





