
from PIL import Image, ImageDraw, ImageFont

image = Image.open("https://github.com/uroojfatima18/Python/blob/main/output_id_card%20(2).png?raw=true")

draw = ImageDraw.Draw(image)
font = ImageFont.load_default()


draw.text((10, 10), "ID Card", fill="black", font=font)

image.save("final_id_card.png")


from PIL import Image, ImageDraw, ImageFont

# Load your assets (font and logo)
logo = Image.open('/content/logo.png')  # Change the path to your logo
font = ImageFont.truetype('/content/Arial.ttf', 30)  # Change the path to your Arial.ttf

# Set ID card size (3.375 x 2.125 inches at 300 DPI)
width, height = int(3.375 * 300), int(2.125 * 300)
image = Image.new('RGB', (width, height), (255, 255, 255))  # White background

# Create a drawing context
draw = ImageDraw.Draw(image)

# Drawing the colored boxes (green and red on the bottom left)
draw.rectangle([(0, height - 110), (120, height - 60)], fill=(0, 255, 0))  # Green box
draw.rectangle([(120, height - 110), (240, height - 60)], fill=(255, 0, 0))  # Red box

# Add text to the colored boxes
font_small = ImageFont.truetype('/content/Arial.ttf', 20)
draw.text((10, height - 100), "WMD", font=font_small, fill=(255, 255, 255))  # Green box
draw.text((130, height - 100), "Q1", font=font_small, fill=(255, 255, 255))  # Red box

# Resize the logo and handle transparency
logo = logo.resize((400, 400), Image.LANCZOS)
if logo.mode != 'RGBA':
    logo = logo.convert("RGBA")

# Modify the alpha channel for transparency (95% transparent)
data = logo.getdata()
new_data = [(item[0], item[1], item[2], int(item[3] * 0.05)) for item in data]  # 5% opacity
logo.putdata(new_data)

# Paste the logo
image.paste(logo, (int((width - logo.width) / 2), 50), logo)  # Center logo at the top

# Add text on the card
draw.text((20, 20), "ID CARD", font=font, fill=(0, 128, 0))  # Title

# Define text variables and positions
text_variables = [
    ("Name:", "Urooj Fatima"),
    ("Roll No:", "PIAIC/C24777"),
    ("City:", "Karachi"),
    ("Center:", "Bahria Auditorium"),
    ("Campus:", "Karsaz"),
    ("Days/Time:", "Sunday - 09:00 AM to 01:00 PM"),
    ("Batch:", "61"),
]

# Set initial Y position for text
y_position = 100
for var, value in text_variables:
    draw.text((20, y_position), var, font=font, fill=(0, 0, 0))  # Variable name in black
    draw.text((200, y_position), value, font=font, fill=(0, 128, 0))  # Value in green
    y_position += 60  # Increment Y position

# Add photo on the right side (assuming you've uploaded the photo)
photo = Image.open('/content/downlaod anime pic.png')  # Change to your photo path
photo = photo.resize((200, 250))  # Resize the photo
image.paste(photo, (width - 220, 100))  # Paste photo on the right side

# Add "Authorized Signature" text at the bottom right
signature_x_position = width - 210  # Adjusted X position for signature
signature_y_position = height - 70  # Y position for signature at the bottom
draw.text((signature_x_position, signature_y_position), "Authorized Signature", font=font_small, fill=(0, 0, 0))

# Draw a black line above the "Authorized Signature"
draw.line([(signature_x_position - 10, signature_y_position - 10), 
            (signature_x_position + 200, signature_y_position - 10)], fill=(0, 0, 0), width=2)

# Save the final image
image.save('/content/output_id_card.png')  # Save your card

# Display the final image
image.show()


