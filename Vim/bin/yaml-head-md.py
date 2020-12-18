#!/usr/bin/env python
# @(#) gen-yaml-head-md.py
# Last-edited: Sat 2020.11.14.1236 -- Danny Quah (me@DannyQuah.com)
# ----------------------------------------------------------------
# $
# Revision History:
#  # Fri 2020.11.13.2248 -- Danny Quah (me@DannyQuah.com)
#    First draft: PURPOSE
# $
# $Log$
# ----------------------------------------------------------------
import sys
import datetime

# ----------------------------------------------------------------
myMdHeader = """---
fileName: TheTitle
# Last-edited: TIMESTAMP-- Danny Quah (me@DannyQuah.com)
Type: Event | Person | Notes | Publication | Log | Misc
Tags: China, US, LKYSPP, NUS, Hardware, Software, Talk, Write, Finance, COVID19
# Created: TIMESTAMP-- Danny Quah (me@DannyQuah.com)

output: pdf_document
title: DocTitle
## include DQ-latex-yaml.md, etc., as required here
---

<!---
   Invisible section // TheTitle
-->
"""

print(myMdHeader)

# eof gen-yaml-head-md.py

