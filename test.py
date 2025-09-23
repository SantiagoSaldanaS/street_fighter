import gym, retro
import os
import sys
import time

print("gym:", gym.__version__)    # should print 0.21.0
print("retro:", retro.__version__) # should print 0.8.0 (or whatever gym-retro version)
print("Dir retro:", dir(retro))
print("Retro romfile:", retro.get_romfile_system)


print(f"Python version: {sys.version}")
print(f"Retro version: {retro.__version__ if hasattr(retro, '__version__') else 'Unknown'}\n")

print(retro.data.list_games())





env = retro.make(game='StreetFighterIISpecialChampionEdition-Genesis')


obs = env.reset()
print("Observation shape:", getattr(obs, "shape", obs))

step = 0

while step < 200:
    time.sleep(0.1)  # Slow down for visibility
    env.render()
    step += 1

env.close()