# Sonos Marketing

A small Python script that tracks news coverage of Sonos and its competitors and uses Claude to classify the public sentiment of each headline. This was practice for version control and API calling with python. This project used AI as a tool for learning but was coded by me. Parts of this project I would copy from documentation online or from AI debugging a certain part. The parser for google news was becoming difficult but I pulled knowledge form my SEO build. That one used AI as the coder. This project I was the coder.

## What it does

1. Searches Google News (via RSS) for each search term and can be changed to fit for audio specific reviews.
2. Collects the top 5 articles per term (title, source, publish date, link).
3. Sends each headline to Claude (`claude-haiku-5-5`), which labels it `ok`, `good`, or `bad` based on the public opinion it suggests about the company.
4. Writes the results to `coverage.txt` and prints them.

## Setup

Requires Python 3 and an [Anthropic API key](https://console.anthropic.com/).

```bash
python -m venv venv
source venv/bin/activate
pip install anthropic requests beautifulsoup4 lxml
export ANTHROPIC_API_KEY="your-key-here"
```

(`lxml` is needed for BeautifulSoup's XML parser.)

## Usage

```bash
python sonos.py
```

Output is saved to `coverage.txt` (git-ignored), in this format:

```
1 sonos. <headline>
   Source:    <publication>
   Published: <date>
   Link:      <url>

   AI Model Response: good
```

## Customizing

Edit `search_terms` in the `__main__` block of [sonos.py](sonos.py) to track different companies or topics, or change `max_items` in `fetch_google_news` to get more articles per term.

## Future Plans

Create a simple GUI that allows different models to be picked out and a search query to look through different audio/tech companies.

## Versions
-Version 1 published November 4