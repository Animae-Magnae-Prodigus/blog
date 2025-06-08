:let ln= getcurpos()[1]
:let tx=getline(ln)
:let mtx = system(["python", "/data/data/com.termux/files/home/gitdir/reading-journal/blog/prettifyStenograph.py", tx])
:call setline(ln, mtx)

