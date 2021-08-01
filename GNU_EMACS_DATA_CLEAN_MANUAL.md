# Gnu Emacs Data Clean Manual

### C- means CONTROL KEY
### M- means ALT KEY

start emacs
```console
emacs
```
start emacs with file
```console
emacs filename
```
start shell
```console
M-x shell
```
undo
```console
C-x u
```
quit emacs
```console
C-x C-c
```
quit input session
```console
C-]
```
save as
```console
C-x C-w
```
kill buffer
```console
C-x k
```
close window
```console
C-0
```
close tab
```console
C-0 t
```
copy
```console
M-w
```
cut
```console
C-w
```
paste
```console
C-y
```
delete word
```console
M-backspace
```
delete line
```console
C-k
```
select all
```console
C-x h
```
start selecting
```console
C-space key
arrow keys
enter key
```
search
```console
C-s type word
C-s next occurrence
C-r previous occurrence
C-g quit search at beginning
enter key quit search at cursor
```
find replace
```console
M-x query-replace
y replace this one
n skip to next
! replace all
C-g quit
M-x replace-string
enter key to replace all
```
find replace regexp
```console
M-x query-replace-regexp
y replace this one
n skip to next
! replace all
C-g quit
M-x replace-regexp
enter to replace all
```
replace rectangle
```console
select rectangle
C-xrt
enter key
```
delete rectangle
```console
select rectangle
C-xrk
enter key
```
paste rectangle
```console
select rectangle
C-xry
enter key
```
edit files dired
```console
find file
C-x C-f
/bin
/opt
~
open emacs in folder
M-x shell
ls or ll
C-x d
m mark
u unmark
U unmark
C copy
R rename
D delete
+ create dir
! run selected
Q find replace regexp
Z compress/decompress selected
g refresh
^ go parent dir
> next sub dir
< previous sub dir
q quit window
```
preferred locations to save init.el file
```console
~/.emacs
~/.emacs.el
HERE-> ~/.emacs.d/init.el
HERE-> ~/.config/emacs/init.el
```
show emacs init path and value
```console
M-x user-emacs-directory
M-x describe-variable
```
start emacs without init.el
```console
emacs -q
```
evaluate init.el
```console
restart emacs
Alt+x eval-buffer
Alt+x load-file
```
emacs data cleaning delimiter = ";"
```elisp
(defun clean()
  (interactive)
  (let ($begin $end)
    (if (use-region-p)
        (setq $begin (region-beginning) $end (region-end))
      (setq $begin (point-min) $end (point-max)))
    (save-excursion
      (save-restriction
        (narrow-to-region $begin $end)
        (progn
          (goto-char (point-min))
          (while (re-search-forward "\t+" nil "move")
            (replace-match ";")))
        (progn
          (goto-char (point-min))
          (while (re-search-forward "\W+" nil "move")
            (replace-match ";")))
        (progn
          (goto-char (point-min))
          (while (re-search-forward "\s+" nil "move")
            (replace-match ";")))
        (progn
          (goto-char (point-min))
          (while (re-search-forward "\n+" nil "move")
            (replace-match ";")))
        (progn
          (goto-char (point-min))
          (while (re-search-forward "\Cg" nil move")
            (replace-match ";")))
        (progn
          (goto-char (point-min))
          (while (re-search-forward "\Ca+" nil move")
            (replace-match ";")))
        (progn
          (goto-char (point-min))
          (while (re-search-forward "" nil move")
            (replace-match ";")))
        (progn
          (goto-char (point-min))
          (while (re-search-forward "]|-^" nil move")
            (replace-match ";")))
        (progn
          (goto-char (point-min))
          (while (re-search-forward "[!"#$%&\'()*+,./:;<=>?@[\_`{|}~0-9]+" nil move")
            (replace-match ";")))
        (progn
          (goto-char (point-min))
          (while (re-search-forward ";+" nil move")
            (replace-match ";")))
        (progn
          (goto-char (point-max))
          (while (equal (char-before) 32)
            (delete-char -1))))
      (message "!!! FINISHED !!!"))))
```
emacs remove stop words delimiter = ";"
```elisp

```
