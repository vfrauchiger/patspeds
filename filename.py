import win32gui, win32con, os

filter='Acrobat files\0*.pdf\0'
customfilter='Other file types\0*.*'
fname, customfilter, flags=win32gui.GetOpenFileNameW(
    InitialDir=os.environ['temp'],
    Flags=win32con.OFN_ALLOWMULTISELECT|win32con.OFN_EXPLORER,
    File='somefilename', DefExt='py',
    Title='GetOpenFileNameW',
    Filter=filter,
    CustomFilter=customfilter,
    FilterIndex=0)


print(fname)
print('rolf')

