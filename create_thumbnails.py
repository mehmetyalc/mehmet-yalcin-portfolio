"""
Create simple, professional thumbnail images for ML projects
"""
from PIL import Image, ImageDraw, ImageFont
import os

# Create images directory
os.makedirs('images', exist_ok=True)

# Project data
projects = [
    {
        'name': 'transfer_success',
        'title': 'Transfer Success\nPrediction',
        'subtitle': 'Football Analytics',
        'color': '#10b981',  # green
        'icon': 'R²: 0.94'
    },
    {
        'name': 'transfer_efficiency',
        'title': 'Transfer Economic\nEfficiency',
        'subtitle': 'Value Analysis',
        'color': '#3b82f6',  # blue
        'icon': '238 Transfers'
    },
    {
        'name': 'f1_prediction',
        'title': 'F1 Race Position\nPrediction',
        'subtitle': 'Formula 1 Analytics',
        'color': '#ef4444',  # red
        'icon': 'R²: 0.63'
    },
    {
        'name': 'super_lig',
        'title': 'Turkish Super Lig\nMatch Prediction',
        'subtitle': 'Football Forecasting',
        'color': '#f59e0b',  # amber
        'icon': '51.3% Acc'
    }
]

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_thumbnail(project):
    """Create a simple, professional thumbnail"""
    # Image dimensions
    width, height = 800, 600
    
    # Create image with white background
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw colored header bar
    color_rgb = hex_to_rgb(project['color'])
    draw.rectangle([(0, 0), (width, 120)], fill=color_rgb)
    
    # Draw subtle gradient effect (darker bottom)
    for i in range(120, height):
        alpha = int(255 * (1 - (i - 120) / (height - 120) * 0.05))
        draw.rectangle([(0, i), (width, i+1)], fill=(245, 245, 245))
    
    # Try to use a nice font, fallback to default
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
        icon_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        icon_font = ImageFont.load_default()
    
    # Draw title (white text on colored background)
    title_lines = project['title'].split('\n')
    y_offset = 20
    for line in title_lines:
        bbox = draw.textbbox((0, 0), line, font=title_font)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) // 2
        draw.text((x, y_offset), line, fill='white', font=title_font)
        y_offset += 50
    
    # Draw subtitle
    bbox = draw.textbbox((0, 0), project['subtitle'], font=subtitle_font)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) // 2
    draw.text((x, 200), project['subtitle'], fill=(100, 100, 100), font=subtitle_font)
    
    # Draw icon/metric in center
    bbox = draw.textbbox((0, 0), project['icon'], font=icon_font)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) // 2
    draw.text((x, 350), project['icon'], fill=color_rgb, font=icon_font)
    
    # Draw decorative elements
    # Top left corner accent
    draw.rectangle([(0, 0), (10, 120)], fill='white')
    # Bottom right corner accent
    draw.rectangle([(width-10, height-80), (width, height)], fill=color_rgb)
    
    # Draw "ML Project" badge
    badge_text = "ML PROJECT"
    bbox = draw.textbbox((0, 0), badge_text, font=subtitle_font)
    badge_width = bbox[2] - bbox[0] + 40
    badge_height = 50
    badge_x = (width - badge_width) // 2
    badge_y = 480
    
    # Badge background
    draw.rounded_rectangle(
        [(badge_x, badge_y), (badge_x + badge_width, badge_y + badge_height)],
        radius=25,
        fill=color_rgb
    )
    
    # Badge text
    text_bbox = draw.textbbox((0, 0), badge_text, font=subtitle_font)
    text_width = text_bbox[2] - text_bbox[0]
    text_x = badge_x + (badge_width - text_width) // 2
    text_y = badge_y + 10
    draw.text((text_x, text_y), badge_text, fill='white', font=subtitle_font)
    
    # Save image
    output_path = f"images/{project['name']}.png"
    img.save(output_path, 'PNG', quality=95)
    print(f"Created: {output_path}")

# Create all thumbnails
for project in projects:
    create_thumbnail(project)

print("\nAll thumbnails created successfully!")
