import torch
print(torch.__version__)            # should show 2.6.0+cu124
print(torch.cuda.is_available())     # should print True
print(torch.cuda.get_device_name(0)) # should print your GPU name
