# wallcraft-scraper
This Python script utilizes the WallpaperCraft API to fetch 15 (or more) top-rated wallpapers with any themed query, tailored for a screen resolution of any pixels.

## Base API URL
- URL: https://api-uc.wallpaperscraft.com/images
## Parameters
- **cost_variant** (optional): Specify the cost variant, e.g., `'ios_cost_2'`.
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
    'limit': 1,
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

## Example Response
```python
{
  "count": 572,
  "items": [
    {
      "author": "Kostya Basorin",
      "category_id": 65,
      "colors": [
        [
          15,
          24,
          47
        ],
        [
          102,
          79,
          115
        ],
        [
          217,
          158,
          109
        ]
      ],
      "content_type": "private",
      "cost": 11,
      "description": "river, valley, mountains, clouds, landscape, art",
      "downloads": 15830,
      "favorites": 837,
      "for_adult_only": false,
      "id": 941839,
      "license": "WallpapersCraft License",
      "min_cost_ends_at": "2023-05-26T12:44:41Z",
      "nft_links": [],
      "rating": 25,
      "source_link": "",
      "tags": [
        "river",
        "valley",
        "mountains",
        "clouds",
        "landscape",
        "art"
      ],
      "theme_color": [],
      "uploaded_at": "2023-05-25T15:44:41+0300",
      "uploader_type": "wlc",
      "user_id": 0,
      "user_pseudo_id": "",
      "variations": {
        "adapted": {
          "resolution": {
            "height": 3045,
            "width": 1407
          },
          "size": 622764,
          "url": "https://images.wallpaperscraft.com/image/single/941839_1407x3045.jpg"
        },
        "adapted_landscape": {
          "resolution": {
            "height": 2560,
            "width": 2560
          },
          "size": 998048,
          "url": "https://images.wallpaperscraft.com/image/single/941839_2560x2560.jpg"
        },
        "original": {
          "resolution": {
            "height": 5760,
            "width": 3240
          },
          "size": 14297873,
          "url": "https://images.wallpaperscraft.com/image/single/941839_3240x5760.jpg"
        },
        "preview_small": {
          "resolution": {
            "height": 1015,
            "width": 469
          },
          "size": 102218,
          "url": "https://images.wallpaperscraft.com/image/single/941839_469x1015.jpg"
        }
      }
    }
  ],
  "response_time": "2023-12-25T00:25:13Z"
}
