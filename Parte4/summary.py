from torchsummary import summary
from model import CNN

model = CNN()
summary(model, input_size=(1, 28, 28))