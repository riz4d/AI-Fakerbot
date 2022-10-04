#Queries @riz4d on telegram

import requests
import time
from pyrogram import *
import os
from Config import *
from faker import Faker



@bot.on_message(filters.command('start'))
async def start_message(client,message):
    await message.reply('__Hey '+str(message.from_user.first_name)+" 👻__")
    await message.reply("__Hope you're fine.__")
    await message.reply("__can i show you AI generated photo of a fictional person,that person doesn't exist's in the real world__")
    await message.reply("__- sent /person\n- for bulk purpose /bulkpersons \n- For source code /source\n- connect developer /dev__")
@bot.on_message(filters.command('about'))
async def help_message(client,message):
    await message.reply("__I can generate different person's face each time the people being shown are not real. Instead, each of these fake yet strangely familiar faces are generated through the use of a special kind of artificial intelligence algorithm called generative adversarial networks (GANs)__")

@bot.on_message(filters.command('source'))
async def help_message(client,message):
    await message.reply('Here is the Git Repo\n[AI-Fakerbot](https://github.com/riz4d/AI-Fakerbot)')
    
 
@bot.on_message(filters.command('dev'))
async def help_message(client,message):
    await message.reply('@riz4d')
    
@bot.on_message(filters.command('person'))
async def gen(client,message):
     r = requests.get(url, allow_redirects=True)
     pic=r.content
     file=open(f"person.png", "wb").write(pic)
     fake=Faker()
     name=fake.profile()['name']
     job=fake.profile()['job']
     residence=fake.profile()['residence']
     ssn=fake.profile()['ssn']
     company=fake.profile()['company']
     address=fake.profile()['address']
     blood=fake.profile()['blood_group']
     mail=fake.profile()['mail']
     pc = fake.chrome()
     cc = fake.credit_card_full()
     ip = fake.ipv4_private()
     android = fake.android_platform_token()
     fake_res='__Name__ : `'+name+'`\n\n__Job__ : `'+job+'`\n\n__Residence__ : `'+residence+'`\n\n__SSN__ : `'+ssn+'`\n\n__Blood Group__ : `'+blood+'`\n\n__Company__ : `'+company+'`\n\n__Address__ : `'+address+'`\n\n__Mail__ : `'+mail+'`\n\n__PC__ : `'+pc+'`\n\n__Credit Card__ : `'+cc+'`__IPV4__ : `'+ip+'`\n\n__PlatForm__ : `'+android+'`'
     await message.reply_photo('person.png',caption=fake_res)
     os.remove('person.png')
@bot.on_message(filters.command('bulkpersons'))
async def bulkgen(client,message):
    await message.reply('__How many fake persons you want??__')
    if message.text=='/bulkpersons':
        @bot.on_message(filters.text)
        async def bulkgen(client,messsage):
            howmany=messsage.text
            picno=0
            for i in range(int(howmany)):
                fake=Faker()
                name=fake.profile()['name']
                job=fake.profile()['job']
                residence=fake.profile()['residence']
                ssn=fake.profile()['ssn']
                company=fake.profile()['company']
                address=fake.profile()['address']
                blood=fake.profile()['blood_group']
                mail=fake.profile()['mail']
                pc = fake.chrome()
                cc = fake.credit_card_full()
                ip = fake.ipv4_private()
                android = fake.android_platform_token()     
                fake_res='__Name__ : `'+name+'`\n\n__Job__ : `'+job+'`\n\n__Residence__ : `'+residence+'`\n\n__SSN__ : `'+ssn+'`\n\n__Blood Group__ : `'+blood+'`\n\n__Company__ : `'+company+'`\n\n__Address__ : `'+address+'`\n\n__Mail__ : `'+mail+'`\n\n__PC__ : `'+pc+'`\n\n__Credit Card__ : `'+cc+'`__IPV4__ : `'+ip+'`\n\n__PlatForm__ : `'+android+'`'           
                picno+=1
                await messsage.reply('`uploading` '+str(picno)+'/'+str(howmany))
                r = requests.get(url, allow_redirects=True)
                pic=r.content
                file=open(f"pic.png", "wb").write(pic)
                await messsage.reply_photo('pic.png',caption=fake_res)
                os.remove('pic.png')
                time.sleep(2)
        



bot.run()
#Queries @riz4d on telegram
