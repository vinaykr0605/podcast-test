import yaml
import xml.etree.ElementTree as ET

# Load YAML data
with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

# Create root RSS element with namespaces
rss_element = ET.Element(
    'rss',
    attrib={
        'version': '2.0',
        'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
        'xmlns:content': 'http://purl.org/rss/1.0/modules/content/',
    }
)

# Add <channel> element
channel = ET.SubElement(rss_element, 'channel')

# Example of populating channel data from YAML
# Assuming YAML contains keys like 'title', 'link', 'description'
if 'title' in yaml_data:
    ET.SubElement(channel, 'title').text = yaml_data['title']

if 'link' in yaml_data:
    ET.SubElement(channel, 'link').text = yaml_data['link']

if 'description' in yaml_data:
    ET.SubElement(channel, 'description').text = yaml_data['description']

# Convert to string or write to file
tree = ET.ElementTree(rss_element)
tree.write('feed.xml', encoding='utf-8', xml_declaration=True)
