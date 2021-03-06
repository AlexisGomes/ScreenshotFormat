# ScreenshotFormat
Python package to help create screenshot to upload on stores

### Instantiate the helper with your screenshot, and the desired store image size
```
from ScreenshotFormat import ScreenshotFormat, StoreSizeName, BackgroundType, Position

# 1. your screenshot
# - pass the path of your screenshot with "screenshot_path"
# - Or directly a PIL image with "screenshot_img"

2. screenshot size
# - By using the Enum StoreSizeName in "store_size_name" param
# - Or by passing a tuple (with, height) in "store_size"
helper = ScreenshotFormat(
                screenshot_path=PATH_SCREENSHOT, 
                store_size_name=StoreSizeName.iphone_6_5)
```

### Retrieve sizes
```
# get your screenshot size with :
width, height = helper.screenshot_size

# get your store size with :
width, height = helper.store_size
```

### Crop your screenshot
```
helper.crop_screenshot(left=None, top=100, right=None, bottom=None)
```

### Resize your screenshot
A ratio will multply width & height to keep
```  
helper.resize_screenshot(zoom_ratio=1.3)
```
Pass the desired size
```  
helper.resize_screenshot(size=(1080, 1920))
```

### Create a background
the image created will have the size of the store you pass the constructor.
All the background types are inside the Enum "BackgroundType":
- plain : A background with only one color
- vertical_gradient : A gradient from top to bottom
- horizontal_gradient : A gradient from left to right
- diagonal_gradient_right : A gradient from the top right corner to the bottom left corner
- diagonal_gradient_left : A gradient from the top left corner to the bottom right corner

You can pass as many color as you want in the "color_palette" argument
```
background = helper.create_background(type_=BackgroundType.diagonal_gradient_right, color_palette=[
    (255, 0, 0),
    (255, 255, 0),
    (255, 255, 255),
])
```

### Adding text
```
text_position = (Position.center, 150)
text = "My Caption"
background = helper.add_text_with_halo(background,
                                       text=text,
                                       position=text_position,
                                       color=(0, 0, 0),
                                       halo_col=(255, 255, 255),
                                       font_path=PATH_TO_YOUR_FONT,
                                       font_size=120)
```

### Pasting the screenshot on the background
```
position = (Position.center, helper.store_height - helper.screenshot_height - 100)
final_image = helper.apply_screenshot_on_background(background, position)
```

### Save image
```
ScreenshotFormat.save(img=final_image, path=OUTPUT_PATH, file_name="MyScreenshot.jpg")
```
