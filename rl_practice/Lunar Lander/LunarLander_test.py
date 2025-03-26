import os
import gymnasium as gym
from sympy import false
from stable_baselines3 import PPO

"""
rl_practice-v2环境是一个经典的强化学习环境，任务是让一个小飞船在月球表面着陆。
在这个环境中，飞船有4个动作可以选择：向左、向右、向上、不动。
飞船的状态是一个8维的向量，包括飞船的位置、速度、角度等信息。
飞船的目标是在规定的时间内，以尽可能小的速度着陆在指定区域内。
"""

# 使用PPO算法训练LunarLander-v3环境
def PPO_lunar_lander_v3():
    # ppo_model_path = "LunarLanderV3_PPO_model"
    ppo_model_path = "LunarLander_PPO_model"

    # 创建环境实例，设置渲染模式为human（直接在窗口中渲染，适合人类观看）
    env = gym.make("rl_practice-v3", render_mode="human")
    # env = gym.make("rl_practice-v3", render_mode="rgb_array")

    # 如果模型不存在，则训练模型
    if not os.path.exists(ppo_model_path + '.zip'):
        # 创建PPO模型, 使用MlpPolicy作为神经网络结构，verbose=1表示打印训练过程
        model = PPO("MlpPolicy", env, verbose=2,device='cpu')

        # 训练模型
        model.learn(total_timesteps=500_000)
        # 保存模型
        model.save(ppo_model_path)

    # 加载模型
    model = PPO.load(ppo_model_path, env=env)

    for episode in range(1000):

        # 重置环境
        next_state, _ = env.reset()

        done = false
        reward = 0
        truncated = false
        info = None

        # 测试模型
        while not done:
            # 预测动作
            action, _states = model.predict(next_state)
            # 执行动作
            next_state, reward, done, truncated, info = env.step(action)

            if truncated:
                done = True

            # 渲染环境
            env.render()

    env.close()

def main():
    PPO_lunar_lander_v3()


if __name__ == "__main__":
    main()