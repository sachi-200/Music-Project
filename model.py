import torch.nn as nn
import torch.nn.functional as F

def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

#basic conv block
def conv_block(n_input, n_output, stride=1, kernel_size=80):
    layers = []
    if stride ==1:
        layers.append(nn.Conv1d(n_input, n_output, kernel_size=kernel_size, stride=stride, padding='same')) #Conv
    else:
        layers.append(nn.Conv1d(n_input, n_output, kernel_size=kernel_size, stride=stride)) #Conv
    layers.append(nn.BatchNorm1d(n_output))
    layers.append(nn.ReLU())
    return nn.Sequential(*layers)

class BaseRagaClassifier(nn.Module):
    def __init__(self, params):
        super().__init__()
        n_input = params.n_input
        n_channel = params.n_channel
        stride = params.stride
        self.conv_blocks = []
        
        self.conv_block1 = conv_block(n_input, n_channel, stride=stride, kernel_size=80)
        self.conv_block2 = conv_block(n_channel, n_channel, stride=1, kernel_size=3)
        self.conv_block3 = conv_block(n_channel, 2*n_channel, stride=1, kernel_size=3)
        self.conv_block4 = conv_block(2*n_channel, 2*n_channel, stride=1, kernel_size=3)
        self.fc1 = nn.Linear(2 * n_channel, params.num_classes)

    def forward(self, x):
        x = self.conv_block1(x)
        x = F.max_pool1d(x, 4)
        x = self.conv_block2(x)
        x = F.max_pool1d(x, 4)
        x = self.conv_block3(x)
        x = F.max_pool1d(x, 4)
        x = self.conv_block4(x)
        x = F.avg_pool1d(x, x.shape[-1])
        x = x.permute(0, 2, 1)
        x = self.fc1(x)
        x = F.log_softmax(x, dim=-1)
        return x