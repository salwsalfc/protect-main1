from pyrogram import Client, filters

api_id = 9157919
api_hash = "b90c282e584222babde5f68b5b63ee3b"

BOT_TOKEN = ""  
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=BOT_TOKEN)

ahmed = {}
tom_max = 3

@app.on_message(filters.command("انذار", ""))
async def tom(client, message):
    me = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    if chat_id not in ahmed:
        ahmed[chat_id] = {}
    if user_id not in ahmed[chat_id]:
        ahmed[chat_id][user_id] = 1
    else:
        ahmed[chat_id][user_id] += 1
    await message.reply_text(f"{ahmed[chat_id][user_id]}")
    if ahmed[chat_id][user_id] >= tom_max:
        try:
        	del ahmed[chat_id][user_id]
        	await client.ban_chat_member(chat_id, user_id)
        	await message.reply("تم تم طردة وركعة ميت قندرة 👞")   	
        except:
        	await message.reply("ميصير اطردة ")
        
        

app.run()