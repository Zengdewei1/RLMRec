python encoder/train_encoder.py --model lightgcn --dataset amazon --cuda 0
python encoder/train_encoder.py --model lightgcn_plus --dataset amazon --cuda 1
python encoder/train_encoder.py --model lightgcn_gene --dataset amazon --cuda 0

python encoder/train_encoder.py --model lightgcn_plus --dataset amazon --cuda 1 & python encoder/train_encoder.py --model lightgcn_gene --dataset amazon --cuda 0

python encoder/train_encoder.py --model lightgcn --dataset amazon --cuda 0 & python encoder/train_encoder.py --model gccf_plus --dataset amazon --cuda 1

python encoder/train_encoder.py --model lightgcn_plus --dataset amazon --cuda 0 & python encoder/train_encoder.py --model gccf --dataset amazon --cuda 1

# plus + plus
python encoder/train_encoder.py --model lightgcn_plus --dataset amazon --cuda 0 & python encoder/train_encoder.py --model gccf_plus --dataset amazon --cuda 1


srun -p q3090 --gres=gpu:rtx3090:2 --cpus-per-task=8 --pty --mail-type=ALL bash