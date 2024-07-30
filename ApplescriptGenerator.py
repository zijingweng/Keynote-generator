import re
import applescript

def splitOnEmptyLines(s):
    # match 2 or more empty-lines (can contain spaces)
    blank_line_regex = r'\r?\n\s*\n'
    return re.split(blank_line_regex, s.strip())

def generate(filename, songs):
    script = '''
        tell application "Keynote"
            activate
            set thisDocument to make new document with properties {document theme:theme "Worship", width:1920, height:1080}

            tell front document
    '''

    for song in songs:
        title = song[1]
        lyrics = splitOnEmptyLines(song[2])
        script += '''
                set currentSlide to make new slide with properties {base layout:slide layout "Title - Lyrics"}
                tell currentSlide
                    set the object text of the default title item to "%s"
                    set the object text of the default body item to "%s"
                end tell
        ''' % (title, lyrics[0])

        for section in lyrics[1:]:
            script += '''
                set currentSlide to make new slide with properties {base layout:slide layout "Lyrics"}
                tell currentSlide
                    set the object text of the default body item to "%s"
                end tell
            ''' % section
    
    script += '''
                move the first slide to before first slide
                delete first slide
            end tell
            save thisDocument in file (((path to desktop folder) as string) & "%s" & ".key")
        end tell
    ''' % filename
    # the move before delete is to let Keynote focus on the first slide

    # print(script)
    applescript.run(script)
