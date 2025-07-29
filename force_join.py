from pyrogram.errors import UserNotParticipant
from pyrogram.types import Message

# Set your channel's numeric ID and public join link here
CHANNEL_ID = -1001789156562  # Replace with your channel's ID
CHANNEL_JOIN_LINK = "https://t.me/YourChannelUsername"  # Replace with your channel's public link

async def is_user_in_channel(bot, user_id):
    """
    Check if a user is a member of your channel.
    """
    try:
        member = await bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ("member", "administrator", "creator")
    except UserNotParticipant:
        return False
    except Exception:
        return False

async def enforce_channel_join(bot, message: Message) -> bool:
    """
    Checks if the user is in the channel. If not, sends a join message and returns False.
    Use at the START of your command handlers.
    """
    user_id = message.from_user.id if message.from_user else None
    if user_id is not None:
        in_channel = await is_user_in_channel(bot, user_id)
        if not in_channel:
            await message.reply(
                f"To use this command, you must join our channel first!\n\n"
                f"➡️ [Join Channel]({CHANNEL_JOIN_LINK})",
                disable_web_page_preview=True
            )
            return False
    return True
