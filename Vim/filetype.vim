" @(#) filetype.vim
" Last-edited: Sat 2020.07.18.1753 -- Danny Quah (me@DannyQuah.com)
" ----------------------------------------------------------------
" Revision History:
"  % Sat 2020.06.06.1522h -- Danny Quah (dq@pbook)
"    First draft https://vimhelp.org/vim_faq.txt.html#faq-26.8
" ----------------------------------------------------------------
"
if exists("did_load_filetypes")
   finish
endif

augroup filetypedetect
  autocmd!
"  autocmd BufRead,BufNewFile *.tex     setfiletype tex
"  autocmd BufEnter *.md setlocal filetype=markdown
  autocmd BufRead,BufNewFile *.md      setfiletype markdown
  autocmd BufRead,BufNewFile *.txt     setfiletype text
  autocmd BufRead,BufNewFile Vimrc     setfiletype vim
augroup END

" eof db/machines/Editors/Vim/filetype.vim
