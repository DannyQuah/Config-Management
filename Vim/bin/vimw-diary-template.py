#!/usr/bin/env python
# @(#) gen-vimw-diary-template.py 
# Last-edited: Mon 2021.01.04.0745 -- Danny Quah (me@DannyQuah.com)
# ----------------------------------------------------------------
# Revision History:
#  % Sat 2020.09.26.0659 -- Danny Quah (me@DannyQuah.com)
#    First draft: Template for Vimwiki diary
#    Original from http://frostyx.cz/posts/vimwiki-diary-template
#    In frostyx.cz the vimscript call has '%' at the end for the 
#    buffer name. But I'm not going to use that (below) so I also
#    removed the '%' in my .vimrc call to this script.
# ----------------------------------------------------------------
import sys
import datetime

# ----------------------------------------------------------------
myTemplate = """# {theLocalDate}

## Log

({theDayDateTime})

## Daily.Checklist
- [ ] Lisoril, Gluocasamine, Vitamin C
- [ ] Temperature.AM
- [ ] Temperature.PM

## ToDo
- [ ] 

## Notes
({theDayDateTime}) Run WCP.  KV abs, core // top // 56.7  
{theSsDate}	08:02	06.12	'00:37:45	'00:06:10
({theDayDateTime}) Run CW.  KV abs, core // top // 57.3  
{theSsDate}	07:42	6.03	'00:39:41	'00:06:34
({theDayDateTime}) KV abs, core // top // 57.3  
{theSsDate}	06:21		'00:32:30
"""

# ----------------------------------------------------------------

# Date, my way
# This snippet immediately below, from the original source,
# activates on the second branch when called by vimwiki,
# and therefore fails when I seek to reformat the date
# x = (datetime.date.today() if len(sys.argv) < 2
#      # Expecting filename in YYYY-MM-DD.something format
#        else sys.argv[1].rsplit(".", 1)[0]) 
# Instead I do:
myNow = datetime.datetime.now()

myDiaryDict = {
        "theLocalDate": myNow.strftime("%a %d %b %Y"),
        "theDateTime": myNow.strftime("%Y.%m.%d.%H%M"),
        "theDayDateTime": myNow.strftime("%a %Y.%m.%d.%H%M"),
        "theSsDate": myNow.strftime("%d/%m/%Y") 
 
}                   

# Spread out the dictionary using Python's counterpart 
# to the splat operator
print(myTemplate.format(**myDiaryDict))

# eof gen-vimw-diary-template.py
