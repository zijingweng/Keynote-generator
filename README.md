# Keynote-generator
[Chinese Version 中文版](https://github.com/jimmywengzj/Keynote-generator-Chinese)

Store, view, edit lyrics and generate slides for Sunday worship using Python, AppleScript and Apple Keynote

<p align="center">
  <img src="https://github.com/user-attachments/assets/53fadb64-55e6-4a54-8342-2bc6c36d9a64">
  <img src="https://github.com/user-attachments/assets/bd5a9b66-c1ab-45d1-b2d7-8a41e85a64d4" width="480">
</p>

## Usage
### Install dependencies
First make sure that you have `Python` and `pip` installed. 
```
pip install PySide6 applescript
```

### Keynote theme
This generator creates the slides from a Keynote theme. 
Double click on `Worship.kth` and add the theme to Keynote theme selector, make sure to keep its original name `Worship`. 
Feel free to customize the theme, by changing the background, textbox sizes, font, etc.

### Extract lyrics from existing Keynote files (Optional)
If you have existing Keynotes lyrics presentations, copy them to `~/Desktop/slides` folder. 
Double click and run the AppleScript `parser.scpt`, and it should write all the lyrics to `out.txt` located on `Desktop`. 
Check the content of this file manually, each song should start with `#Title` followed by its title, and `#Page` for each Keynote slide. 

When you are done, `cd` to the folder and run
```
python database-init.py
```
and your lyrics should appear when you launch the program.

### Generate the slides!
```
python GUI.py
```
Use the buttons below the middle section to permenantely modify the songs in the datase. 
Search and double click on the results or select the song then press the `→` button to add them to the queue. 
After choosing the filename, click on `Generate Keynote` and the Keynote presentation will be generated and saved on `Desktop`!
