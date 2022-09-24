#Import Libraries
import summarize
from parrot import Parrot
import torch
import warnings
warnings.filterwarnings('ignore')

#For reproducibility
def random_state(seed):
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

random_state=(1234)


#Init models
parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)

#Test phrase
phrases = ["What's the most delicious papayas?"]

#Testing Output
for phrase in phrases:
  print("-"*100)
  print("Input_phrase: ", phrase)
  print("-"*100)
  para_phrases = parrot.augment(input_phrase=phrase)
  for para_phrase in para_phrases:
   print(para_phrase)




