import discord
from discord import app_commands
from discord.ext import commands

# Setting up intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

class RiyadhAirBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user.name} (ID: {self.user.id})')
        print('------')
        try:
            # This syncs your slash commands globally so they appear on Discord
            synced = await self.tree.sync()
            print(f"Synced {len(synced)} command(s) successfully!")
        except Exception as e:
            print(f"Failed to sync commands: {e}")

bot = RiyadhAirBot()

# --- SLASH COMMANDS ---

@bot.tree.command(name="book", description="Book a virtual flight with Riyadh Air!")
@app_commands.describe(destination="Where are you flying to?", flight_number="Enter your flight number (e.g., RX101)")
async def book(interaction: discord.Interaction, destination: str, flight_number: str):
    username = interaction.user.display_name
    embed = discord.Embed(
        title="✈️ Riyadh Air - Flight Booking Confirmed",
        description=f"Passenger **{username}** has successfully booked a flight!",
        color=discord.Color.from_rgb(74, 20, 140) # Luxury Riyadh Air Purple
    )
    embed.add_field(name="Flight Number", value=f"`{flight_number.upper()}`", inline=True)
    embed.add_field(name="Destination", value=f"📌 {destination.title()}", inline=True)
    embed.add_field(name="Status", value="🟢 Boarding Pass Generated", inline=False)
    embed.set_footer(text="Thank you for choosing Riyadh Air | Virtual Airline")
    
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="flightstatus", description="Check the status of a specific flight.")
@app_commands.describe(flight_number="Enter the flight number")
async def flightstatus(interaction: discord.Interaction, flight_number: str):
    embed = discord.Embed(
        title=f"📋 Flight Status: {flight_number.upper()}",
        color=discord.Color.blue()
    )
    embed.add_field(name="Departure", value="Riyadh (RUH)", inline=True)
    embed.add_field(name="Status", value="🕒 On Time", inline=True)
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="helpdesk", description="Get info on how to join the crew or log flights.")
async def helpdesk(interaction: discord.Interaction):
    embed = discord.Embed(
        title="ℹ️ Riyadh Air Help Desk",
        description="Welcome to the support center. Here are our quick resources:",
        color=discord.Color.light_grey()
    )
    embed.add_field(name="Trainee Pilot Guide", value="Check out the server channels to learn how to pass your checkride.", inline=False)
    embed.add_field(name="Flight Logging", value="Use `/book` to log your flight records for promotions.", inline=False)
    await interaction.response.send_message(embed=embed, ephemeral=True)


# --- YOUR CHAT TOKEN PLUGGED IN BELOW ---         
jclient.run(os.environ['DISCORD_TOKEN'])
