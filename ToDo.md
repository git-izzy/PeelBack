# PeelBack goals:

__Note:__ For a goal to be accomplished its functionality must be implemented in a .py file NOT a .ipynb file. Also code should be documented before it is considered complete

## Scananagrams (Phase 1):

Next up: 
- Implement stub for rendering boards
- Sort trainModel.ipynb into modules
- CNN 


### Step 1:
__Images -> Spatial + Character Data__
- Train CNN to recognize bananagrams letters (8)
- Create `TileInfo` class with attributes: (2)
  - letter
  - box
  - center
  - neighbors (private class: dict {up, down, left, right})
- Create pipeline with these steps: (5-8)
  - Read image, identify tiles 
  - for each tile:
    - Crop tile
    - Use CNN to identify letter in cropped tile 
    - create a `TileInfo` object and store it in an array 
- Set up tests for: (3)
  - CNN
  - TileInfo
  - Pipeline
- Clean up repo

### Step 2
__Spatial + Character Data -> Python Classes__
Letter/Word object structure is not set in stone
- create a `Letter` class with attributes: (2)
  - id?
  - letter val - char
  - words - dict {wordId:index}
  - floating - bool
- create a `Word` class with attributes: (2)
  - id?
  - word - str
  - horiz - bool
  - letters - Letter[]
- create a `Board` class: (2)
  - iter - int 
  - words - word[]
  - width?
  - len?
- Create a `findWords` method
  - Uses spatial + character data to traverse tile tree
  - As tiles are iterated over they are turned into `Letter` objects 

## Step 3
__Video analysis__
- Option 1:
  - Train (seperate?) model to recognize hands
  - Skip frames with hands in image
- Option 2: 
  - Pick n of every x frames to analyze
  - if tile count less than expected - skip
- Option 3: 
- Create `Game` class

### Step 4
__Publish__
- Ensure proper documentation
- Research how to publish models 

## Beyond The Camera - Phase 1.5
__Upgrade dev environment__
- Research how I will realistically deploy my architecture
- Set up necessary accounts and environments

## Flask + Database - Pahase 2