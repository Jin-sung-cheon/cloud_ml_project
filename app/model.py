import torch
import torch.nn as nn

class TinyTransformer(nn.Module):
    def __init__(self):
        super().__init__()
        self.embedding = nn.Embedding(128, 32)
        self.fc = nn.Linear(32, 1)

    def forward(self, x):
        x = self.embedding(x)
        x = torch.mean(x, dim=1)
        return torch.sigmoid(self.fc(x))

model = TinyTransformer()

def predict(text: str):
    tokens = [ord(c) % 128 for c in text]
    x = torch.tensor(tokens).unsqueeze(0)
    out = model(x)
    return float(out.item())
