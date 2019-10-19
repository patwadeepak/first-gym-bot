import gym
import pybulletgym

env = gym.make('CartPole-v0')
env.reset()
for i_episode in range(20):
    observation = env.render()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)

        if done:
            print("episode finished after {} timesteps".format(t))
            break
