Bash Utils (miscellaneous small utils for the Bash shell)
=========================================================

**New (Jan 9, 2017)!** All scripts were updated to Python 3. The original Python 2 version (which is not maintained anymore) is tagged as "v0.1". You can find that
under the "release" link.

Here I collect some small command-line utils.

* Author:  Laszlo Szathmary, 2011-2017 (jabba.laci@gmail.com)
* Github:  https://github.com/jabbalaci/Bash-Utils

dictionary/meaning.py
---------------------
* Look up the meaning of a word.
* Usage: `meaning pen`
* Meaning: what does the word `pen` mean?

dropbox/dropbox_permissions.py
------------------------------
* Set directory/file permissions in your Dropbox folder in an intelligent way.
* Intended audience: Linux users who also use Windows sometimes.
* Usage: put the script in the root of your Dropbox folder and launch it.
* [blog post](https://ubuntuincident.wordpress.com/2011/05/08/setting-file-permissions-in-your-dropbox-folder-recursively/)

dropbox/get_public_link.py
--------------------------
* Show the public Dropbox link(s) of one (or several) file(s).
* Dropbox made some changes in 2017, so it doesn't work anymore.
* Usage: `get_public_link [<file> | -a]`
* [blog post](https://ubuntuincident.wordpress.com/2011/06/01/get-the-public-dropbox-links-of-several-files/)

firefox/export_firefox_cookies.py
---------------------------------
* This script extracts cookies from Firefox's `cookies.sqlite`  that are specific to a given host. The exported cookies are saved in `cookies.txt`. New! It also exports session cookies from Firefox's `recovery.js` file.
The exported cookies are saved to `session_cookies.txt`.
* The original script was [written by Dirk Sohler](https://old.0x7be.de/2008/06/19/firefox-3-und-cookiestxt/).
* Usage: `export_firefox_cookies.py <host>`
* [blog post](https://ubuntuincident.wordpress.com/2011/09/05/download-pages-with-wget-that-are-protected-by-cookies/)

mouse/mousepos_gui.py
---------------------
* Monitor the mouse position in real-time.
* It only worked for me under Python 2!
* I made it to facilitate the usage of autopy (http://www.autopy.org). Autopy has a [Python 3 port here](https://github.com/Riamse/autopy3).
* Usage: `mousepos_gui.py`
* [blog post](https://ubuntuincident.wordpress.com/2011/09/11/gui-to-monitor-mouse/)

radio/radio.py
--------------
* A minimalistic radio player.
* Available stations: Slay Radio, goa, trance, chillout, etc.
* Usage: `radio.py`

replace_accents/replace_latex_accents.pl
----------------------------------------
* This script allows you to write special Hungarian and French characters in a simple way
(using the ISO-8859-1 (Latin-1) charset), then convert them to their LaTeX-equivalents.
* Example: La'szlo'  =>  L\'{a}szl\'{o}
* [blog post]( https://ubuntuincident.wordpress.com/2011/07/01/replace-accents-for-latex/)

replace_accents/replace_french_accents_to_latex.pl
--------------------------------------------------
* This script converts a French accented text to LaTeX replacing the funny characters with their LaTeX equivalents.
* Example: é  =>  \'{e}
* [blog post]( https://ubuntuincident.wordpress.com/2011/07/01/replace-accents-for-latex/)

alarm.py
--------
* A simple alarm script that plays a list of MP3s at a given time.
Very useful if you leave your computer switched on during the night.
* Usage:
```
$ alarm -p
    Play music first to adjust volume.
$ alarm -t 7h5
    Set alarm time (5 past 7 in this example).
```
* [blog post]( https://ubuntuincident.wordpress.com/2011/04/17/alarm-script/)

cb.py
-----
* Print the content of the clipboard to the standard output.
* Usage: `cb.py`

fftabs.py
---------
* A command line program for manipulating Firefox tabs.
* Requirements: Firefox + MozRepl add-on.
* Help: `fftabs -h`

from_base64.py
--------------
* Ask a base64 string and convert it back to a normal string (decode).
* Usage: `from_base64`

get_alap.py
-----------
* An interactive program to generate a skeleton source code.
* Supported languages: Python, Go, Java, C, D.
* Usage: `get_alap.py`

get_images.py
-------------
* Extract image links from a web page.
* Usage: `get_images URL [URL]... [-l]`

get_links.py
------------
* Extract all links from a web page.
* Usage: `get_links.py <URL>`
* [blog post](https://pythonadventures.wordpress.com/2011/03/10/extract-all-links-from-a-web-page/)

github_user_email.py
--------------------
* An interactive program that figures out the email address of a GitHub user.
* Usage: `github_user_email.py`

here.py and here.sh
-------------------
* Print just the name of the current directory. For instance, if you are in `/home/students/solo`, then this script will print just `solo`.
* `here.sh` simply prints the output, while `here.py`, in addition, copies the output to the clipboards.
* Usage: `here`

img_to_base64.py
----------------
* Take an image file and encode it with BASE64. Put the encoded data in an "img" HTML tag.
* Usage: `img_to_base64 <image_file>`
* [blog post](https://ubuntuincident.wordpress.com/2011/04/17/embed-images-in-html-pages/)

inout.py
--------
* An interactive script for 1) compressing a folder to another directory, and
  2) uncompressing an archive file to a destination directory.
* Rationale: I always forget the order of parameters...
* Usage: `inout`

is_net_back.py
--------------
* Play a sound when the Internet connection is back.
* Usage: `is_net_back`

myip.py
-------
* My external IP address.
* Usage: `myip`

ocr.py
------
* A wrapper script around the [Tesseract](https://github.com/tesseract-ocr/tesseract) OCR engine. Convert an image to string.
* Usage: `ocr <image_file>`

open_in_tabs.py
---------------
* Read URLs from the standard input and open them in separated browser tabs.
* Usage: `cat url_list.txt | open_in_tabs`
* [blog post](https://ubuntuincident.wordpress.com/2011/03/09/open-urls-in-browser-tabs-simultaneously/)

prettify.py
-----------
* Prettify an HTML page, i.e. pretty print its HTML source.
* The script prints the HTML source that is built by BeautifulSoup (BS). Idea: if you want to manipulate a page with BS, analyze the prettified source instead of the original because this is how BS stores it.
* Usage: `prettify <URL>`
* [blog post](https://pythonadventures.wordpress.com/2011/04/03/prettify-html-with-beautifulsoup/)

prettyjson.py
-------------
* Prettify a JSON file.
* Usage: `prettyjson ugly.json`

py2rtf.py
---------
* Transform a python source file to RTF.
* Usage: `py2rtf [-f] hello.py`
* Meaning: the output is written to `hello.rtf`
* [blog post](http://ubuntuincident.wordpress.com/2012/08/07/insert-syntax-highlighted-source-in-powerpoint/)

redirect_to.py
--------------
* This script tells you where a webpage redirects.
* Usage: `redirect_to.py <URL>`
* [blog post](http://pythonadventures.wordpress.com/2010/12/21/where-does-a-page-redirect-to/)

rep.py
------
* Repeat a bash command several times.
* Usage: `rep <rep> <cmd>`
* Example: `rep 3 echo hello`
* Meaning: print the text "hello" three times.

slogan.py
------
* Generate some slogans from a keyword.
* Usage: `slogan <keyword>`

sp.py
-----
* Print the absolute path of a file. If no parameter is passed, show the current path. The name stands for "show path".
* This is one of my most useful scripts :) I use it every day.
* Usage: `sp [<filename>]`
* [blog post](https://ubuntuincident.wordpress.com/2011/03/17/show-the-absolute-path-of-a-file/)

to_base64.py
------------
* Ask a string and convert it to a base64 string (encode).
* Usage: `to_base64`

to_md5.py
---------
* This scripts reads a text *interactively* and prints its
md5-encoded version. The output is a 32-character long
hexa string.
* Usage: `to_md5`

to_utf8.py
----------
* Convert a text file to an UTF-8-encoded text. The output is printed to the screen.
* Usage: `to_utf8 input.txt`

tocb.py
-------
* Copy the text from the standard input to ALL clipboards. Thus, you can use any paste method to insert your text (middle mouse button or Shift+Insert). The name stands for "to clipboard(s)".
* Usage: `cat file.txt | tocb`
* Options: with `-t` you can trim the text first (remove whitespaces from both ends of the text).
* [blog post](https://pythonadventures.wordpress.com/2011/03/05/copy-string-to-x-clipboards/)

top10.py
--------
* Show the top 10 largest files in the current directory. Filesizes can be shown in a human-readable format with the `-h` option.
* Usage: `top10 [-h]`

twitch2mp3.py
-------------
* Grab a twitch video in mp3.
* Usage: `twitch2mp3 TWITCH_VIDEO_URL`

userpass.py
-----------
* Username and password generator.
* Usage: `userpass`

us.py
-----
* Change spaces to underscores. Pass a string as a parameter OR pass it
on the standard input.
* Example #1: `us "How to Think Like a Computer Scientist.pdf"`
* Result #1: `How_to_Think_Like_a_Computer_Scientist.pdf`
* Example #2: `echo "he he" | us`
* Result #2: `he_he`

xml2json.py
-----------
* Convert an XML file to JSON.
* This is a wrapper around the excellent [xmltodict](https://github.com/martinblech/xmltodict) library.
* Usage: `xml2json <input.xml>`
