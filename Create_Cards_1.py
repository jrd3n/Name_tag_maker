from lib.svg_tools import create_name, create_rectangle, create_svg, create_horizontal_line, inkscape_command, update_svg_styles, combine_svgs
import os
import svgwrite

OUTPUT_DIR = "output_cards"

width = 321.260
height = 377.953

def create_name_tag_mid(first_name, last_name, first_name_font, last_name_font, first_name_text_size, last_name_text_size, draft=False):
    
    svg_filename, dwg = create_svg(first_name, last_name, OUTPUT_DIR , width, height)

    # Add first name and mask to only show top half

    name_top = create_name(dwg, first_name, width/2, height/2, stroke="red",fill="red", element_id="1_union",text_size=first_name_text_size, font=first_name_font, bold=True)

    group_1 = dwg.g(id="2_flatten")

    regtangle_mask = create_rectangle(dwg,0,height/2,width,height/2,stroke="none",fill="white",element_id="top_mask")

    group_1.add(name_top)

    stroke_width = "1"

    if draft == False:
        group_1.add(regtangle_mask)
        stroke_width = "0.1"

    # Add fist name and mask to only show bottom half

    name_bottom = create_name(dwg, first_name, width/2, height/2, stroke="blue",fill="blue", element_id="3_union",text_size=first_name_text_size, font=first_name_font, bold=True)

    group_2 = dwg.g(id="4_flatten")

    regtangle_mask = create_rectangle(dwg,0,0,width,height/2,stroke="none",fill="white",element_id="bottom_mask")

    group_2.add(name_bottom)
    group_2.add(regtangle_mask)

    # Add last name

    last_name = create_name(dwg, last_name, width/2, height/1.33, stroke="blue",fill="blue", element_id="5_union",text_size=last_name_text_size, font=last_name_font)

    # Add thin line in middle and mask with first name

    name_mask = create_name(dwg, first_name, width/2, height/2, stroke="white",fill="white", element_id="Name_Mask",text_size=first_name_text_size, font=first_name_font, bold=True)

    fold_line = create_horizontal_line(dwg, 0, height/2, width,stroke="blue",element_id="fold_line",stroke_width=0.1)

    group_3 = dwg.g(id="6_flatten")

    group_3.add(fold_line)
    group_3.add(name_mask)

    # Add outline cut to image

    regtangle_outline = create_rectangle(dwg,0,0,width,height,stroke="red",fill="white",element_id="outline")

    # Add elements in the correct order

    # dwg.add(raw_element)
    dwg.add(regtangle_outline)
    dwg.add(group_3)
    dwg.add(last_name)
    dwg.add(group_2)
    dwg.add(group_1)
    dwg.save()

    # Do the inkscape commands

    inkscape_command(svg_filename,"1_union","path-union") # or path-union or path-difference

    update_svg_styles(svg_filename, "1_union","none","red",stroke_width=stroke_width)

    #

    inkscape_command(svg_filename,"3_union","path-union") # or path-union or path-difference

    update_svg_styles(svg_filename, "3_union","none","blue",stroke_width=stroke_width)

    #

    inkscape_command(svg_filename,"5_union","path-union") # or path-union or path-difference

    update_svg_styles(svg_filename, "5_union","none","blue",stroke_width=stroke_width)

    # 

    inkscape_command(svg_filename,"Name_Mask","path-union") # or path-union or path-difference

    update_svg_styles(svg_filename, "Name_Mask","white","white",stroke_width=stroke_width)

def create_name_tag_top(first_name, last_name, first_name_font, last_name_font, first_name_text_size, last_name_text_size, draft=False):
    
    svg_filename, dwg = create_svg(first_name, last_name, OUTPUT_DIR , width, height)

    first_name_y = height/2 - first_name_text_size / 6

    # Add first name and mask to only show top half

    name_top = create_name(dwg, first_name, width/2, first_name_y, stroke="red",fill="red", element_id="1_union",text_size=first_name_text_size, font=first_name_font, bold=True)

    group_1 = dwg.g(id="2_flatten")

    regtangle_mask = create_rectangle(dwg,0,height/2,width,height/2,stroke="none",fill="white",element_id="top_mask")

    group_1.add(name_top)

    stroke_width = "1"

    if draft == False:
        group_1.add(regtangle_mask)
        stroke_width = "0.01"

    # Add fist name and mask to only show bottom half

    name_bottom = create_name(dwg, first_name, width/2, first_name_y, stroke="blue",fill="blue", element_id="3_union",text_size=first_name_text_size, font=first_name_font, bold=True)

    group_2 = dwg.g(id="4_flatten")

    regtangle_mask = create_rectangle(dwg,0,0,width,first_name_y,stroke="none",fill="white",element_id="bottom_mask")

    group_2.add(name_bottom)
    group_2.add(regtangle_mask)

    # Add last name

    last_name = create_name(dwg, last_name, width/2, height/2 + last_name_text_size/1.3, stroke="blue",fill="blue", element_id="5_union",text_size=last_name_text_size, font=last_name_font)

    # Add thin line in middle and mask with first name

    name_mask = create_name(dwg, first_name, width/2, first_name_y, stroke="white",fill="white", element_id="Name_Mask",text_size=first_name_text_size, font=first_name_font, bold=True)

    fold_line = create_horizontal_line(dwg, 0, height/2, width,stroke="blue",element_id="fold_line",stroke_width=0.1)

    group_3 = dwg.g(id="6_flatten")

    group_3.add(fold_line)
    group_3.add(name_mask)

    # Add outline cut to image

    regtangle_outline = create_rectangle(dwg,0,0,width,height,stroke="red",fill="white",element_id="outline")

    # Add elements in the correct order

    # dwg.add(raw_element)
    dwg.add(regtangle_outline)
    dwg.add(group_3)
    dwg.add(last_name)
    # dwg.add(group_2)
    dwg.add(group_1)

    dwg.save()

    # Do the inkscape commands

    inkscape_command(svg_filename,"1_union","path-union") # or path-union or path-difference

    update_svg_styles(svg_filename, "1_union","none","red",stroke_width=stroke_width)

    #

    inkscape_command(svg_filename,"3_union","path-union") # or path-union or path-difference

    update_svg_styles(svg_filename, "3_union","none","blue",stroke_width=stroke_width)

    #

    inkscape_command(svg_filename,"5_union","path-union") # or path-union or path-difference

    update_svg_styles(svg_filename, "5_union","none","blue",stroke_width=stroke_width)

    # 

    inkscape_command(svg_filename,"Name_Mask","path-union") # or path-union or path-difference

    update_svg_styles(svg_filename, "Name_Mask","white","white",stroke_width=stroke_width)


    combine_svgs(svg_filename,"kids flowers.svg",svg_filename)

import pandas as pd

if __name__ == "__main__":

    first_name = "Robert"
    last_name = "Smith"

    print(f"processing {first_name}, {last_name}")

    try:
    
        # first_name_font = "Sunday Best"
        first_name_font = "Archer"
        last_name_font = "shine in valentine"

        first_name_sizes = [130, 120, 110, 100,85, 70,65,55,50,45,40,38]

        last_name_sizes = [75, 70, 65, 65,65, 65,65,65,65,65,65,60,60,58,55,50]

        first_name_text_size = first_name_sizes[len(first_name)-1]
        last_name_text_size = last_name_sizes[len(last_name)-1]

        # create_name_tag_mid(first_name.upper(),last_name, first_name_font, last_name_font, first_name_text_size, last_name_text_size, draft=True)

        create_name_tag_top(first_name.upper(),last_name, first_name_font, last_name_font, first_name_text_size, last_name_text_size, draft=False)
        
        print(f"Processed card for {first_name} {last_name}")

    except:
        print(f"ERROR {first_name} {last_name}")

    # Usage example:
