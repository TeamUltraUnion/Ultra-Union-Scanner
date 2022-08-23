from Ultra_Union_Scanner import System, system_cmd
import os
import sys
import subprocess


@System.on(system_cmd(pattern=r"uus gitpull"))
async def gitpull(event):
    subprocess.Popen("git pull", stdout=subprocess.PIPE, shell=True)
    await event.reply("Git pulled probably.")
    os.system("restart.bat")
    os.execv("start.bat", sys.argv)


@System.on(system_cmd(pattern=r"uus restart"))
async def reboot(event):
    if event.fwd_from:
        return
    await event.reply("Restarting.....")
    await System.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    sys.exit()


@System.on(system_cmd(pattern=r"uus shutdown"))
async def shutdown(event):
    if event.fwd_from:
        return
    await event.reply("Shutting Down...")
    await System.disconnect()
