" ============================================================================
" File:        Cmdpalette.vim
" Description:
" Author:      WuHong <wuhong40@gmail.com>
" Website:     https://github.com/wuhong40
" Note:
" License:     Apache License, Version 2.0
" ============================================================================

if leaderf#versionCheck() == 0
    finish
endif

exec g:Lf_py "import vim, sys, os.path"
exec g:Lf_py "cwd = vim.eval('expand(\"<sfile>:p:h\")')"
exec g:Lf_py "sys.path.insert(0, os.path.join(cwd, 'python'))"
exec g:Lf_py "from cmdpaletteExpl import *"

function! leaderf#Cmdpalette#Maps()
    nmapclear <buffer>
    nnoremap <buffer> <silent> q    :exec g:Lf_py "cmdpaletteExplManager.quit()"<CR>
    nnoremap <buffer> <silent> i    :exec g:Lf_py "cmdpaletteExplManager.input()"<CR>
    nnoremap <buffer> <silent> <F1> :exec g:Lf_py "cmdpaletteExplManager.toggleHelp()"<CR>
endfunction

function! leaderf#Cmdpalette#Exec(cmd)
    exec "nnoremap <buffer> _exe :" . a:cmd
    exec _exe
endfunction

function! leaderf#Cmdpalette#startExpl(win_pos, ...)
    call leaderf#LfPy("cmdpaletteExplManager.startExplorer('".a:win_pos."')")
endfunction

function! leaderf#Cmdpalette#startExplPattern(win_pos, pattern)
    call leaderf#LfPy("cmdpaletteExplManager.startExplorer('".a:win_pos."', pattern='".a:pattern."')") 
endfunction

