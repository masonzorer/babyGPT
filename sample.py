# sample from a trained model
import model
from dataclasses import dataclass
import torch
import tiktoken

# Transformer decoder model components
@dataclass
class Config:
    vocab_size: int = 50304
    block_size: int = 512
    n_layer: int = 6
    n_head: int = 8
    n_embd: int = 256
    dropout: float = 0.0

def main():
    # load the model
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    config = Config()
    decoder = model.Decoder(config).to(device)
    decoder.load_state_dict(torch.load("decoder.pth"))
    decoder.eval()
    print("Model loaded.")
    
    # generate a sample
    x = torch.zeros((1, 1), dtype=torch.long)
    x = torch.randint(0, 50304, (1, 1))
    sample = decoder.generate_sample(x, 200)
    print("Sample generated.")
    
    # decode the sample
    enc = tiktoken.get_encoding("gpt2")
    print(enc.decode(sample[0].tolist()))

if __name__ == "__main__":
    main()