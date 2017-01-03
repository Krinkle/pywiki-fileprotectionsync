# -*- coding: utf-8  -*-
# Production configuration file for fileprotectionsync.py

editsummary = 'Update [[Commons:Auto-protected files|auto-protection]] (r25)'
wikitext_start = '{{Auto-protected files gallery}}<gallery widths="80" heights="80">\n'
wikitext_end = '</gallery>'
wikis = [
    {
        'sourcewiki': 'de.wikipedia.org',
        'sourcepages': ['Wikipedia:Hauptseite', 'Wikipedia:Hauptseite/morgen'],
        'targetpage': 'Commons:Auto-protected files/wikipedia/de'
    },
    {
        'sourcewiki': 'en.wikipedia.org',
        'sourcepages': ['Main Page', 'Wikipedia:Main Page/Tomorrow'],
        'targetpage': 'Commons:Auto-protected files/wikipedia/en',
    },
    {
        'sourcewiki': 'en.wikinews.org',
        'sourcepages': ['Main_Page'],
        'targetpage': 'Commons:Auto-protected files/wikinews/en',
    },
    {
        'sourcewiki': 'en.wiktionary.org',
        'sourcepages': ['Main Page'],
        'targetpage': 'Commons:Auto-protected files/wiktionary/en',
    },
    {
        'sourcewiki': 'fr.wikipedia.org',
        'sourcepages': ['Wikipédia:Accueil principal'],
        'targetpage': 'Commons:Auto-protected files/wikipedia/fr',
    },
    {
        'sourcewiki': 'pl.wikipedia.org',
        'sourcepages': ['Strona główna'],
        'targetpage': 'Commons:Auto-protected files/wikipedia/pl',
    },
    {
        'sourcewiki': 'zh.wikipedia.org',
        'sourcepages': ['Wikipedia:首页/全部', 'Wikipedia:首页/明天'],
        'targetpage': 'Commons:Auto-protected files/wikipedia/zh',
    },
    {
        'sourcewiki': 'bn.wikipedia.org',
        'sourcepages': ['প্রধান পাতা'],
        'targetpage': 'Commons:Auto-protected files/wikipedia/bn',
    },
]
