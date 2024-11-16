import feedparser
import requests
import xml.etree.ElementTree as ET
from datetime import datetime


# RSS feed URL
rss_url = "https://any.run/cybersecurity-blog/category/malware-analysis/feed/"

# Fetch and parse the RSS feed
feed = feedparser.parse(rss_url)
entries = feed.entries  # list of feed entries


def create_rss_xml(feed, filename="app_any_feed.xml"):
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")

    # Add channel information
    link = "https://any.run/" + feed.feed.link
    ET.SubElement(channel, "title").text = feed.feed.title
    ET.SubElement(channel, "link").text = feed.feed.link
    ET.SubElement(channel, "description").text = feed.feed.description

    # Add entries
    for entry in entries:
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = entry.title
        ET.SubElement(item, "link").text = entry.link
        ET.SubElement(item, "description").text = entry.description
        ET.SubElement(item, "pubDate").text = entry.published

        # Fetch and include categories
        if hasattr(entry, 'tags'):
            for tag in entry.tags:
                category = ET.SubElement(item, "category")
                category.text = tag.term

    # Write to file
    tree = ET.ElementTree(rss)
    tree.write(filename, encoding="utf-8", xml_declaration=True)
    print(f"RSS feed saved to {filename}")

create_rss_xml(feed)
