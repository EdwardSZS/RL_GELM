from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
import gymnasium as gym
from huggingface_sb3 import load_from_hub
import streamlit as st
import cv2
import time
# Set up the Car Racing environment with rendering
st.title("Car Racing PPO Model")

env = gym.make("CarRacing-v2", render_mode="rgb_array", lap_complete_percent=0.95, domain_randomize=False, continuous=False)
checkpoint = load_from_hub(
    repo_id="rudder-tejas-dive/ppo-CarRacing-v2",  # Repo ID on Hugging Face Hub
    filename="CarRacing-v2.zip"  # Name of the model file
)

# Load the PPO model with the checkpoint


model = PPO.load(checkpoint)
# Evaluate the model
obs, _ = env.reset()
done = False
frame_placeholder = st.empty()
if st.button('Start'):
    while not done:
        action, _states = model.predict(obs, deterministic=True)
        obs, rewards, done,truncated, info = env.step(action)
        frame=env.render()
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame_placeholder.image(frame_bgr)
        time.sleep(0.01)
    # Close the environment
    env.close()

if st.button('Reset Simulation'):
    obs, _ = env.reset()
    done = False