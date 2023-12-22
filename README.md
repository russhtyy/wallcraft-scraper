# wallcraft-scraper
This Python script utilizes the WallpaperCraft API to fetch 15 (or more) top-rated wallpapers with any themed query, tailored for a screen resolution of any pixels.

# WallpaperCraft API Wrapper

This Python script serves as a simple wrapper for the WallpaperCraft API, allowing you to retrieve wallpapers based on various parameters.

## Base API URL
- https://api-uc.wallpaperscraft.com/images
## Parameters

- **cost_variant** (optional)
- : Specify the cost variant, e.g., `'ios_cost_2'`.
- **lang** (optional): Language code, e.g., `'en'` for English.
- **limit** (required): Number of wallpapers to retrieve (default is 15 in this script).
- **offset** (optional): Offset for paginating through results.
- **query** (required): Search query for specific wallpapers.
- **screen[height]** (required): Height of the screen in pixels.
- **screen[width]** (required): Width of the screen in pixels.
- **sort** (required): Sorting order, e.g., `'rating'`.
- **types** (optional): Wallpaper types, can include `'free'`, `'private'`, etc.
- **uploader_types** (optional): Uploader types, e.g., `'wlc'`, `'user'`, `'wlc_ai_art'`.

## Example Usage

```python
import requests

base_url = 'https://api-uc.wallpaperscraft.com/images'
params = {
    'cost_variant': 'ios_cost_2',
    'lang': 'en',
    'limit': 15,
    'offset': 0,
    'query': 'landscape',
    'screen[height]': 2556,
    'screen[width]': 1179,
    'sort': 'rating',
    'types': ['free', 'private'],
    'uploader_types': ['wlc', 'user', 'wlc_ai_art']
}

response = requests.get(base_url, params=params).json()
print(response)
