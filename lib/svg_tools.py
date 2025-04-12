import svgwrite
import subprocess
import os
import xml.etree.ElementTree as ET

def create_name(dwg, Name, x, y, stroke="red", fill="none", element_id=None, text_size = 85, bold = None, font = "Ariel"):
        text = dwg.text(
            Name,
            insert=(f"{x}", f"{y}"),
            fill=fill,
            font_size=f"{text_size}px",
            stroke=stroke,
            stroke_width="0.1px",
            font_family=font,

        )
        
        if bold:
            text['font-weight'] = "bold"

        text['text-anchor'] = "middle"
        text['dominant-baseline'] = 'middle'
        
        if element_id:
            text['id'] = element_id

        return text

def create_rectangle(dwg,x, y, width,height,stroke="red", fill="none", element_id=None):

    regtangle = dwg.rect(insert=(f"{x}", f"{y}"), 
                            size=(f"{width}", f"{height}"),
                            stroke=stroke,
                            stroke_width="0.1px",
                            fill=fill
                            )
    
    if element_id:
        regtangle['id'] = element_id
    
    return regtangle

def inkscape_command(filename, select, action):

    # firstNameTop union
    # 3. Combine paths for firstNameTop

    cmd = [
        "inkscape", filename,
        f"--select={select}",
        f"--actions={action}",
        "--export-overwrite"
    ]

    subprocess.run(cmd, check=True)

def create_svg(first_name, last_name, OUTPUT_DIR, width, height):

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Construct filename based on guest name
    filename = f"{OUTPUT_DIR}/{first_name}_{last_name}.svg"

    # Create the SVG drawing
    dwg = svgwrite.Drawing(filename, size=(f"{width}", f"{height}"))

    return filename, dwg

def create_horizontal_line(dwg, x, y, length, stroke="black", stroke_width="1px", element_id=None):
    # Draws a horizontal line from (x, y) to (x + length, y)
    line = dwg.line(start=(x, y), end=(x + length, y), stroke=stroke, stroke_width=stroke_width)
    if element_id:
        line['id'] = element_id
    return line

import xml.etree.ElementTree as ET

def update_svg_styles(filename, element_id, fill, stroke, stroke_width):
    # Parse the SVG file
    tree = ET.parse(filename)
    root = tree.getroot()
    
    # Define the SVG namespace (adjust if your file uses a different one)
    ns = {'svg': 'http://www.w3.org/2000/svg'}
    
    # Find the element by its ID
    element = root.find(f".//*[@id='{element_id}']", ns)
    if element is not None:
        # Update the fill, stroke, and stroke-width attributes
        element.attrib['fill'] = fill
        element.attrib['stroke'] = stroke
        element.attrib['stroke-width'] = stroke_width
        
        # Update the style attribute as well if it exists
        style = element.attrib.get('style', '')
        styles = {}
        if style:
            for part in style.split(';'):
                if ':' in part:
                    key, value = part.split(':', 1)
                    styles[key.strip()] = value.strip()
        styles['fill'] = fill
        styles['stroke'] = stroke
        styles['stroke-width'] = stroke_width
        
        # Rebuild the style attribute
        element.attrib['style'] = ';'.join(f"{k}:{v}" for k, v in styles.items())
        
        # Write the updated SVG back to file
        tree.write(filename)
        print(f"Updated element '{element_id}' in {filename}")
    else:
        print(f"Element with id '{element_id}' not found in {filename}")


import svgutils.transform as sg

# def parse_size(size_str):
#     # Remove "px" or any non-digit characters
#     return float(size_str.replace("px", ""))

def combine_svgs(main_svg_filename, imported_svg_filename, output_filename="combined.svg"):
    # Load both SVG files.
    main_svg = sg.fromfile(main_svg_filename)
    imported_svg = sg.fromfile(imported_svg_filename)
    
    # Get the root elements for both.
    main_root = main_svg.getroot()
    imported_root = imported_svg.getroot()

    # # Get the size of the main SVG and parse it
    # width_str, height_str = main_svg.get_size()

    # width = parse_size(width_str)
    # height = parse_size(height_str)
    
    # Optionally reposition the imported SVG.
    # Here we move it to coordinates (width/2, height). Adjust as needed.
    # imported_root.moveto(width/2, height * 0.90)

    main_svg.append(imported_root)
    main_svg.append(main_root)
    
    # Append both SVG roots to the figure.
    # fig.append([main_root, imported_root])
    
    # Save the combined SVG to the specified file.
    # fig.save(output_filename)

    main_svg.save(output_filename)