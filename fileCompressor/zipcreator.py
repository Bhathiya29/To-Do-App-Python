import zipfile
import pathlib

def make_archive(filePaths, destDir):
    dest=pathlib.path(destDir,'compressed.zip')
    with zipfile.ZipFile(dest,'w') as archive:
        for filepath in filePaths:
            archive.write(filepath)



if __name__ == '__main__':
    make_archive(filePaths=['files/doc.txt','files/test.txt','weather.txt'],destDir='dest')