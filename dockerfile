# This dockerfile serves to let me know if my gpu is accessible from within a container
# The process for setting up NVIDIA Container Toolkit is more involved for Pop!_OS
# If I care enough, I found instructions here: https://gist.github.com/kuang-da/2796a792ced96deaf466fdfb7651aa2e

FROM nvidia/cuda:10.2-base
CMD nvidia-smi