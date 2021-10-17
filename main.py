import os
from telethon import TelegramClient

import asyncio

your_api_id=XXXXXX
your_api_hash="XXXXXXXXXXXXXXXXXXX"
from keep_alive import keep_alive

client = TelegramClient('anything_unique', your_api_id, your_api_hash )



print("Working!")


async def main():
  try:
    i = 1
    
        
    while True:
      msg = await client.send_message(-1001598581778, str(i))#send the message
      i=i+1 #increment of i
      await asyncio.sleep(1)#wait for a sec
      await client.delete_messages(-1001598581778, msg.id)#then delete
      await asyncio.sleep(1)     #again wait for a sec
      #wait is necessary for the removal of flooding
  except Exception as e:
    print(e)
    
		
keep_alive()#this is imported in the 8th line and used to run 24*7
client.start()
client.loop.run_until_complete(main())
# client.run_until_disconnected()
