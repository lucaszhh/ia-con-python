import gymnasium as gym
import numpy as np
from random import random
from tqdm import trange


def frozen(episodios, entrenar=True, render=False, greedy=True):
    problema = gym.make(
        "FrozenLake-v1",
        map_name="4x4",
        is_slippery=True,
        render_mode="human" if render == True else None,
    )

    alpha = 0.9  # tasa de aprendizaje
    gamma = 0.9  # factor de descuento
    epsilon = 1  # probabilidad de exploración
    epsilon_dec = 0.0001  # factor de decaimiento de epsilon

    if entrenar == True:
        q = np.zeros((problema.observation_space.n, problema.action_space.n))
    else:
        q = np.load("qf.npy")

    for episodio in trange(episodios):
        terminacion, truncamiento = False, False
        estado_actual = problema.reset()[0]
        while not terminacion or not truncamiento:
            if greedy:
                accion = np.argmax(q[estado_actual, :])
            else:
                if entrenar == True and random() < epsilon:
                    accion = problema.np_random.integers(0, 4)  # accion aleatoria
                else:
                    accion = np.argmax(q[estado_actual, :])  # la mejor accion
            estado_nuevo, recompensa, terminacion, truncamiento, info = problema.step(accion)  # ejecutamos la accion y obtenemos un nuevo estado
            if entrenar:
                q[estado_actual, accion] = q[estado_actual, accion] + alpha * (recompensa + gamma * np.max(q[estado_nuevo, :]) - q[estado_actual, accion])
            estado_actual = estado_nuevo
        epsilon = max(epsilon - epsilon_dec, 0)
    problema.close()
    np.save("qf", q)


if __name__ == "__main__":
    frozen(10000, entrenar=True, render=False, greedy=False)  # Entrenar
    # frozen(10, entrenar=True, render=True) # Testear y renderizar