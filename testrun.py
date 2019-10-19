import gym
import pybulletgym
import numpy as np

# Hill Climbing initialize weights randomly, utilize memory
# save food weights

def run_episode(env, parameters):
    observation = env.reset()
    totalreward = 0
    # for 200 timesteps
    for _ in range(200):
        env.render()
        # initialize random weights
        action = 0 if np.matmul(parameters, observation)<0 else 1
        observation, reward, done, info = env.step(action)
        totalreward +=  reward
        if done:
            break
    return totalreward

def train(submit):
    env = gym.make('CartPole-v0')

    episodes_per_update = 5
    noise_scaling = 0.1
    parameters = np.random.rand(4) * 2 -1
    bestreward = 0

    # 2000 episodes
    for _ in range(2000):
        newparams = parameters + (np.random.rand(4) *2 -1) * noise_scaling
        reward = run_episode(env, newparams)
        print("Reward "+ str(reward) +' best ' + str(bestreward))
        if reward > bestreward:
            bestreward = reward
            parameters = newparams
            if reward == 200:
                break
    return bestreward
    
r = train(submit=False)
print(r)