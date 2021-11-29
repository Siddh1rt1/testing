import argparse
import torch
import numpy as np
from torch import nn, optim
from torch.utils.data import DataLoader
from model import Model
from dataset import Dataset


global xp 
print('13')

#text = 'Eil: Lindner'

#def train(dataset, model, args):
 #   model.train()
#
#    dataloader = DataLoader(dataset, batch_size=args.batch_size)
#    criterion = nn.CrossEntropyLoss()
 #   optimizer = optim.Adam(model.parameters(), lr=0.001)
#    
 #   od = open("input.txt", "r")
 #   text = od.read()
 #   od.close()
#    xp = ''
#    for epoch in range(args.max_epochs):
#        state_h, state_c = model.init_state(args.sequence_length)
#
#        for batch, (x, y) in enumerate(dataloader):
#            optimizer.zero_grad()
#
#            y_pred, (state_h, state_c) = model(x, (state_h, state_c))
#           loss = criterion(y_pred.transpose(1, 2), y)
#
#           state_h = state_h.detach()
#           state_c = state_c.detach()
#
#            loss.backward()
#            optimizer.step()
#            xp = xp + str({ 'epoch': epoch, 'batch': batch, 'loss': loss.item() })+"\n"
#            print({ 'epoch': epoch, 'batch': batch, 'loss': loss.item() })
#            print('47')
#            import app as baz
#            baz.updatetext("heyho")
 #           print({'epoch': epoch})
 #           print(predict(dataset, model, text='Eil: Lindner'))
#        animani= str(predict(dataset, model, text))
#        print(  animani)
       
#        with open ('end.txt', 'a') as endcsv :
#            xpz=0
#            endcsv.write(str(xp))
#            endcsv.write(str(xpz)+ '.: ' + animani + "\n")
#            xpz+=1
def predict(option,dataset, model, text, next_words=9):
    model.eval()

    
    words = text.split(' ')
    state_h, state_c = model.init_state(len(words))
   # from app import option
    #global option
    global classic_var
    classic_var=0
    for i in range(0, next_words):
        x = torch.tensor([[dataset.word_to_index[w] for w in words[i:]]])
        y_pred, (state_h, state_c) = model(x, (state_h, state_c))

        last_word_logits = y_pred[0][-1]
        p = torch.nn.functional.softmax(last_word_logits, dim=0).detach().numpy()
        word_index = np.random.choice(len(last_word_logits), p=p)
        words.append(dataset.index_to_word[word_index])
        word_main=str(dataset.index_to_word[word_index])

        if (str(option) in "Aggro")and ( "!" in str(words)):
            break
        else:
            print("no")


        if (str(option) in "Oneliner")and ("."in str(words) or "!" in str(words) or "?" in str(words)):
            break
        else:
            print("no")

        print(classic_var)

        if (str(option) in "Klassisch") and ("."in str(word_main) or "!" in str(word_main) or "?" in str(word_main)):
            classic_var=classic_var+1
        else:
            print("no")

        if classic_var>=2:
            break
        else:
            print("no")

        
    print('71')
    return ' '.join(words)
print("vor parser ")
#parser = argparse.ArgumentParser()
print("vor parser 2")
#parser.add_argument('--max-epochs', type=int, default=2)
#parser.add_argument('--batch-size', type=int, default=256)
#parser.add_argument('--sequence-length', type=int, default=1)
print("errorlog")
#args, unknown = parser.parse_known_args()
#print(args)
dataset = Dataset(2)
model = Model(dataset)

#train(dataset, model, args)
#print(predict(dataset, model, text='Eil: Lindner'))
