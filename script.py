from lxml import html

def extract_image_data(html_content):
    # Parse the HTML content
    tree = html.fromstring(html_content)

    # Extract all image URLs (the href attribute of the <a> tags)
    image_links = tree.xpath('//div[@id="images"]/a/@href')
    
    # Extract and clean the names of the images (text inside <a> tags)
    image_names = tree.xpath('//div[@id="images"]/a/text()[1]')
    

    # Extract the thumbnail URLs (the src attribute of the <img> tags)
    thumbnail_links = tree.xpath('//div[@id="images"]/a/img/@src')
    
    return image_links, image_names, thumbnail_links

if __name__ == "__main__":
    # Sample HTML content
    html_content = '''
    <!DOCTYPE html>
    <html>
      <head>
        <base href='http://example.com/' />
        <title>Example website</title>
      </head>
      <body>
        <div id='images'>
          <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' alt='image1'/></a>
          <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' alt='image2'/></a>
          <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' alt='image3'/></a>
          <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' alt='image4'/></a>
          <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' alt='image5'/></a>
        </div>
      </body>
    </html>
    '''

    # Extract image data
    image_links, image_names, thumbnail_links = extract_image_data(html_content)
    
    # Print the extracted data
    print("Image Links:", image_links)
    print("Image Names:", image_names)
    print("Thumbnail Links:", thumbnail_links)
