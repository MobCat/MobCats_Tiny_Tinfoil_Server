# MobCat's Tiny Tinfoil Server
Makes setting up a private LAN tinfoil server easy.

----

## What is this ##
This is a "simple" python3 script that adds switch packages to a index.htm file that can be used with tinfoil.

**Why?**<br>
Well Installing games off the SD card at the very least requires you to have double the space out side of the fat32 issues.<br>
Installing games over direct USB works but only for windows and not for all switch files as far as I know.<br>
Installing games from USB C OTG is ok but you first have to copy the file to a USB drive then install off the drive.<br>
Using a public server like HBG is fine however, very slow and you are beholden to their rules and what they host.<br>
So setting up your own local LAN tinfoil server is not as fast as installing from USB or SD card however it's way faster then a public server and you can host whatever you want, whenever you want, from whatever computer you want providing it can host a basic HTML website. So any computer including a raspberry pi if you have a big enough SD card to hold your games but I would still recommend a computer connected to ethernet for your server but if you only have a pi on WiFi then sure why not I guess.<br>
I'm not saying this method of installing switch games is the best, just it works best for me.<br>

## What is Tinfoil
Tinfoil is a free shop installer for the switch that lets you install switch NSP, NSZ, XCI and XCZ files onto your switch with ease... With ease after you set it up that is.<br>
You can find more about tinfoil [here](https://tinfoil.io/Download#download).

## Requirements ##
Tinfoil installed on your switch.<br>
Python 3.8 or higher.<br>
If your not using the windows pre pack, then a HTML web server like apache or windows IIS

## Noob friendly windows setup ##
1. Download the [WindowsPrePack.BetaRC1.zip](https://github.com/MobCat/MobCat-s-Tiny-Tinfoil-Server/releases/download/BetaRC1/WindowsPrePack.BetaRC1.zip) from the Releases page.<br>
2. Unpack the hole `_Tinfoil` folder to the root of one of your drives. So you have a file path like<br>
`C:\_Tinfoil\Apache_start.bat` or `E:\_Tinfoil\Apache_start.bat`<br>
`C:\_Tinfoil\htdocs\files\` or `E:\_Tinfoil\htdocs\files\`<br>
Which drive doesn't matter, as long as the `_Tinfoil` folder is in the root of that drive.
3. Copy any switch packages you want to install into the `_Tinfoil\htdocs\files\` folder.<br>
How the files are placed in this folder doesn't matter. They can be loose files or folders inside folders for days and the script will just work it out and add the full directory path to the index regardless of where it is, as long as it's in the `_Tinfoil\htdocs\files\` folder somewhere.<br>
Also you don't have to worry about other non switch related files being in these folders like .txt, .lnk, etc as the scrip is only looking for files with the switch package file extension and only adding them, nothing else.
4. Run the `UpdateHTML.bat` from the `_Tinfoil` folder. The script will tell you how many files where added to the index and what your server IP is, we need that IP for later, so you can just leave this window open for now.
5. Run the `Apache_start.bat` from the `_Tinfoil` folder.
6. Make sure your switch is connected to the same WiFi and network you are hosting the Tinfoil server on then launch Tinfoil on your switch.
7. Now goto File Browser then press - button to add a new server.
8. In this new window we want to set the Protocol to http by pressing A then arrowing down then press B when you find it.<br>
Next you want to set your Host to the IP address the `UpdateHTML.bat` told you.<br>
Now you can press X to save and Tinfoil will refresh its listings.
9. Now you have a new server in the File Browser labeled like http://192.168.1.x(or your server IP)<br>
If you open that new server with your server IP a message will show, welcoming you to the tiny tinfoil server and telling you how many files are on it.<br>
Dismissing this message, you will now see a list of all the packages on your server you can install.<br>
From here you can install the packages like you would from any other server.<br><br>
You can also press any key on the `UpdateHTML.bat` window that's still open as we don't need that any more.<br>
We only need to keep the `Apache_start.bat` open for the server to work.<br>
If you are finished with the server and want to shut it down then run `Apache_stop.bat` and this will auto shutdown the server.

# Updating the windows server with new switch packages#
If you want to add, edit, delete, etc any file on the server simply, make the changes to the files in the `_Tinfoil\htdocs\files\` folder, then run the `UpdateHTML.bat` again to update the index.htm file. Then press any key to close it as we already know our server IP.<br>
This can be done while apache is still running, it doesn't matter. As long as your not trying to install files at the same time you are trying to update the index.htm.

## Pro setup ##
1. Download the `UpdateHTML.py` from this github and place it in your `htdocs` or `www` folder depending on the type of server you are using.
2. Make a new `files` folder in your `htdocs` or `www` folder and copy all your switch package files into there.
3. If your running https then you want to edit `urlHead` on line 13 in `UpdateHTML.py`
4. If you are using an exturnal IP address for your server, edit `urlHead` on line 13 of `UpdateHTML.py` to something like<br>
`urlHead  = 'https://13.237.44.5/'` or `urlHead  = 'http://mykickassshop.com/'` 
6. If you want to edit the MotD then you can do that on line 74 of `UpdateHTML.py`
7. Once you have made all the edits you want, run the `UpdateHTML.py` to generate your index.htm for the server, then goto step 6. in the Noob friendly windows setup guide above this to setup your switch with the server you just made.

## Extra notes ##
The python scrip is a dumpster fire, it needs to be remade but for now "it just works".<br>
I may have to do more URL encoding to work with more web server setups. For now it works but If it doesn't then ill have to import a library to do URL encoding. I hate librarys but yeah...<br>
**If you are running the windows pre pack !DO NOT CONNECT IT TO THE INTERNET OR ANY NETWORK OUTSIDE OF YOUR PRIVATE LAN! I'm using a very old version of Apache for this pre pack, It was built to be as simple and noob friendly as possible. Not secure or upto date, just simple to use and setup.
