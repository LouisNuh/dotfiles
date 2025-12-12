#!/usr/bin/env python3
"""
Generate preview images for the PowerPoint template.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_preview_image():
    """Create a preview image representing the first slide."""
    # Create a 16:9 image (1920x1080 for high quality)
    width, height = 1920, 1080
    img = Image.new('RGB', (width, height), color=(245, 247, 250))
    draw = ImageDraw.Draw(img)
    
    # Draw left accent bar (cyan-green)
    bar_width = 40
    draw.rectangle([(0, 0), (bar_width, height)], fill=(12, 170, 170))
    
    # Try to use a decent font, fallback to default
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 120)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 48)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
    
    # Draw title text
    title_text = "科技商业演示模板"
    title_y = 300
    draw.text((150, title_y), title_text, fill=(11, 59, 113), font=title_font)
    
    # Draw subtitle text
    subtitle_text = "Tech-Business Presentation Template"
    subtitle_y = 500
    draw.text((150, subtitle_y), subtitle_text, fill=(51, 51, 51), font=subtitle_font)
    
    # Save the preview
    preview_path = "preview.png"
    img.save(preview_path, 'PNG')
    print(f"✓ Preview image saved as: {preview_path}")
    
    return preview_path

def create_placeholder_screenshot():
    """Create a placeholder for the original screenshot."""
    width, height = 1920, 1080
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Draw border
    draw.rectangle([(10, 10), (width-10, height-10)], outline=(200, 200, 200), width=5)
    
    # Try to use a font
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
    except:
        font = ImageFont.load_default()
    
    # Draw placeholder text
    text = "原始截图占位符\nOriginal Screenshot Placeholder"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    draw.text((text_x, text_y), text, fill=(150, 150, 150), font=font)
    
    # Add note
    note = "注：实际截图由用户提供 | Note: Actual screenshot provided by user"
    try:
        note_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    except:
        note_font = ImageFont.load_default()
    
    note_bbox = draw.textbbox((0, 0), note, font=note_font)
    note_width = note_bbox[2] - note_bbox[0]
    note_x = (width - note_width) // 2
    draw.text((note_x, text_y + 100), note, fill=(180, 180, 180), font=note_font)
    
    # Save the placeholder
    screenshot_path = "original-screenshot.png"
    img.save(screenshot_path, 'PNG')
    print(f"✓ Placeholder screenshot saved as: {screenshot_path}")
    
    return screenshot_path

def main():
    """Generate all preview images."""
    print("Generating preview images...")
    create_preview_image()
    create_placeholder_screenshot()
    print("✓ All images generated successfully!")

if __name__ == "__main__":
    main()
