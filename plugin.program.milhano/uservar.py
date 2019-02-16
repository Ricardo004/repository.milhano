import os, xbmc, xbmcaddon
import binascii
#########################################################
### User Edit Variables #################################
#########################################################
# Enable/Disable the text file caching with 'Yes' or 'No' and age being how often it rechecks in minutes
CACHETEXT      = 'Yes'
CACHEAGE       = 30

ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[B][COLOR yellow]Assistente Milhano[/COLOR][/B]'
BUILDERNAME    = 'Milhano Build'
#########################Make sure to change the repo to yours!!!!
EXCLUDES       = [ADDON_ID, 'repo.Milhano', 'My_Builds', 'backupdir']
BUILDFILE      = 'http://milhano.com.pt/wizard.menu.milhano/wizard.txt'
UPDATECHECK    = 0
APKFILE        = 'http://milhano.com.pt/wizard.apk/wizard.apk.txt'
YOUTUBETITLE   = 'http://'
YOUTUBEFILE    = 'http://'
ADDONFILE      = 'http://milhano.com.pt/wizard.menu.milhano/wizaddons.txt'
ADVANCEDFILE   = 'http://'
ROMPACK        = 'http://'
EMUAPKS        = 'http://'
ADDONPACK      = 'http://milhano.com.pt/wizard.menu.milhano/temas.txt'
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################

##Alway test to see the color combo!!

#### NEW GUI THEME ###################################
# Choose from the following 
# Only these colors avalable
# white , blue , orange , yellow , red , purple , pink , lime , cyan, green
#Button focus color
FOCUS_BUTTON_COLOR = 'yellow'
EXIT_BUTTON_COLOR = 'white'
#Highlight outline for lists
HIGHLIGHT_LIST = 'white'
##No TXT file Banner
NO_TXT_FILE = 'red'

############################################
############################################
### The full list of colors for below can found @ https://forum.kodi.tv/showthread.php?tid=210837

#Top Main buttons
MAIN_BUTTONS_TEXT = 'white'
#All other buttons
OTHER_BUTTONS_TEXT = 'yellow'
#all list text color
##FYI any color placed in the txt file will overide this
LIST_TEXT = 'yellow'


#Description text title color
DES_T_COLOR = 'yellow'
#Description color
DESCOLOR = 'white'

#Wizard title name and verion color
WIZTITLE = 'Milhano Wizard'
WIZTITLE_COLOR = 'yellow'
VERTITLE_COLOR = 'white'
VER_NUMBER_COLOR = 'yellow'
############################################################

## The colors and theme below is still used for the pop up dialogs
##Alway test to see the color combo
# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'blue'
COLOR2         = 'yellow'
COLOR3         = 'red'
COLOR4         = 'snow'
COLOR5         = 'lime'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR2+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR2+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
THEME6         = '[COLOR '+COLOR3+'][B]%s[/B][/COLOR]'



#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'https://8buszp.s.cld.pt'
ICONMAINT      = 'https://8buszp.s.cld.pt'
ICONAPK        = 'https://8buszp.s.cld.pt'
ICONADDONS     = 'https://8buszp.s.cld.pt'
ICONYOUTUBE    = 'https://8buszp.s.cld.pt'
ICONSAVE       = 'https://8buszp.s.cld.pt'
ICONTRAKT      = 'https://8buszp.s.cld.pt'
ICONREAL       = 'https://8buszp.s.cld.pt'
ICONLOGIN      = 'https://8buszp.s.cld.pt'
ICONCONTACT    = 'https://8buszp.s.cld.pt'
ICONSETTINGS   = 'https://8buszp.s.cld.pt'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '~'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Obrigado por usar o instalador Milhano.'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = os.path.join(ART, 'icon.png')
CONTACTFANART  = 'http://'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'Yes'
# Url to wizard version
WIZARDFILE     = 'http://milhano.com.pt/wizard.menu.milhano/wizard.txt'
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'http://'
# Url to folder zip is located in
REPOZIPURL     =  'http://'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'No'
# Url to notification file
NOTIFICATION   = 'http://'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
# Font size of header
FONTHEADER     = 'Font25'
HEADERMESSAGE  = 'Milhano Builds Wizard'
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Font for Notification Window
FONTSETTINGS   = 'Font12'
# Background for Notification Window
BACKGROUND     = 'http://'
############################    #############################