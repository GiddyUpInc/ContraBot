# Connecting to discord
import yaml
import random
import discord
from discord.ext import commands
from discord import message
from text_contradiction.text_contradiction import TextContradiction

def main():
    # Read yaml files
    with open("discord.yaml", 'r') as yaml_file:
        yaml_dict = yaml.safe_load(yaml_file)
        credentials = yaml_dict["credentials"]

    TOKEN = credentials["Token"]

    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    model = TextContradiction()
    model.load_tokenizer()

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to discord")
        for member in client.get_all_members():
            print(member)
        
        for channel in client.get_all_channels():
            print(channel.name)
            if channel is discord.TextChannel:
                print(channel.history(limit=10))


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content == 'cont?':
            # Loading message
            response = "Checking Contradictions"
            await message.channel.send(response)
            # Gather messages
            user_messages = ""
            async for msg in message.channel.history(limit=20):
                if msg.author != client.user or msg.content != "cont?":
                    user_messages += msg.content
                    user_messages += ", "
            # Calculate contradiction
            prob_contradiction, prob_no_contradiction, prob_neutral = model.analyse_text(user_messages)

            # Make prediction about contradiction
            if prob_neutral > prob_contradiction and prob_neutral > prob_no_contradiction:
                answer = f"Sentences are unrelated with a probability: {prob_neutral}"
                print(answer)
                await message.channel.send(answer)
            else:
                if prob_contradiction > prob_no_contradiction:
                    answer = f"Contradiction Detected with a probability of: {prob_contradiction}"
                    print(answer)
                    await message.channel.send(answer)
                else:
                    answer = f"No Contradiction Detected with a probability of: {prob_no_contradiction}"
                    print(answer)
                    await message.channel.send(answer)

    client.run(TOKEN)


if __name__ == "__main__":
    main()