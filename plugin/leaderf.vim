" ============================================================================
" File:        leaderf.vim
" Description:
" Author:      Wu Hong <wuhong40@gmail.com>
" Website:     https://github.com/wuhong40
" Note:
" License:     Apache License, Version 2.0
" ============================================================================

command! -bar -nargs=0 LeaderfCmdpalette call leaderf#Cmdpalette#startExpl(g:Lf_WindowPosition)
command! -bar -nargs=0 LeaderfCmdpaletteCword call leaderf#Cmdpalette#startExplPattern(g:Lf_WindowPosition, expand('<cword>'))

call g:LfRegisterSelf("LeaderfCmdpalette", "navigate the cmdpalette")

