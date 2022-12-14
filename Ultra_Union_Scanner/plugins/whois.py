from telethon.tl.functions.users import GetFullUserRequest
from Ultra_Union_Scanner import System, system_cmd


@System.on(system_cmd(pattern=r"whois"))
async def whois(event):
    try:
        to_get = event.pattern_match.group(1)
    except Exception:
        if event.reply:
            replied = await event.get_reply_message()
            to_get = int(replied.sender.id)
        else:
            return
    try:
        to_get = int(to_get)
    except Exception:
        pass
    try:
        data = await System(GetFullUserRequest(to_get))
    except Exception:
        await event.reply("Failed to get data of the user")
        return
    await System.send_message(
        event.chat_id,
        f"╒═══「 **Appraisal results:** 」\n**"
        f"**> First Name:** `{data.user.first_name}`\n"
        f"**> Last Name:** `{data.user.last_name}`\n"
        f"**> Username:** @{data.user.username}\n"
        f"**> Userlink:** [{data.user.first_name}](tg://user?id={data.user.id})\n"
        f"**> User ID:** `{data.user.id}`\n"
        f"**> About:** `{data.about}`")


help_plus = """ Here is Help for **Whois** -
• `whois` - get data of the user.
• `uid` - get User ID.
**Notes:**
`/` `?` `.` `!` are supported prefixes.
**Example:** `/addenf` or `?addenf` or `.addenf`
"""
__plugin_name__ = "whois"
