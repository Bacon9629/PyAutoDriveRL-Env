# PyAutoDriveRL-Env

**PyAutoDriveRL-Env** is a Python-based reinforcement learning (RL) framework designed for training and simulating autonomous driving in a Unity3D environment. The project integrates RL techniques using libraries like Stable Baselines3, and leverages Unity3D for realistic car simulation environments.


https://github.com/user-attachments/assets/675499d5-02cc-4880-8242-0b1c4333c3d2


## Features
- **Reinforcement Learning**: Uses algorithms like PPO and SAC to train autonomous driving models.
- **Unity3D Integration**: Communicates with Unity3D to simulate car environments.
- **Custom CNN Feature Extractor**: Handles camera input from the car simulation.
- **Car Simulation Control**: Provides throttle, steering, and reset triggers based on RL models.

## Additional Information
- Unity3D executable will be provided, and in future releases, the Unity project files to allow for custom environment editing will also be provided.
- This project features an environment wrapped using the Gym interface, allowing users to train models with Stable Baselines.
- A [Stable Baselines training example script](train_stable_baseline.py) is provided to help you get started quickly.
- A more flexible [training template script](train_my.py) is also available for users who want to modify the training logic or customize the environment further.

## File Structure
- **`CarDataService.py`**: Handles communication between the car simulation and Python. Manages car telemetry, including speed, position, and camera images.
- **`CarRLEnvironment.py`**: Defines the GYM-compatible RL environment, using car data for observations and rewards.
- **`train_stable_baseline.py`**: Main training script using Stable Baselines3 (PPO/SAC) for RL training.
- **`train_my.py`**: Custom RL training loop with reward computation and action selection.
- **`inference_template.py`**: Example script for performing inference using the trained RL model.

## Getting Started
1. **Requirements**:
    - OS: `windows`
    - Python version: 3.10
    - Libraries: `numpy==1.26.3`, `opencv-python==4.6.0.66`, `stable-baselines3==2.3.2`, `gymnasium==0.29.1`, `torch==2.1.2`

3. **Install dependencies**:
    ```bash
    conda create -n autodrive_rl python=3.10
    conda activate autodrive_rl
    pip install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/cu118
    pip install gymnasium==0.29.1
    pip install stable-baselines3==2.3.2
    pip install opencv-python==4.6.0.66
    pip install “python-socketio<4.3” “python-engineio<3.9”
    pip install eventlet
    pip install flask
    ```
    * CPU version
    ```bash
    conda create -n autodrive_rl python=3.10
    conda activate autodrive_rl
    pip install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/cpu
    pip install gymnasium==0.29.1
    pip install stable-baselines3==2.3.2
    pip install opencv-python==4.6.0.66
    pip install “python-socketio<4.3” “python-engineio<3.9”
    pip install eventlet
    pip install flask
    ```

5. **Run Training**:
    ```bash
    conda activate autodrive_rl
    python train_stable_baseline.py
    ```

6. **Inference**:
    After training, you can perform inference using:
    ```bash
    conda activate autodrive_rl
    python inference_template.py
    ```

## Customization
- Modify the **`CarRLEnvironment.py`** to adjust observation space or reward functions.
- Implement your custom RL algorithms in **`train_my.py`** if you prefer not to use Stable Baselines3.

## Enviroment Observation
[ObservationDetail.md](doc/ObservationDetail.md)

## Gym-like enviroment detail
[Gym-likeEnviromentDetail.md](doc/Gym-likeEnviromentDetail.md)

## Acknowledgments
This project is built using:
- **Stable Baselines3** for RL algorithms.
- **Unity3D** for car simulation.
